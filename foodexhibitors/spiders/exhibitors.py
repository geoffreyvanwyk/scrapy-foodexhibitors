# This file is part of project scrapy-foodexhibitors.
#
# Project scrapy-foodexhibitors is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project scrapy-foodexhibitors is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# project scrapy-foodexhibitors. If not, see <https://www.gnu.org/licenses/>.

##
# Spider to collect exhibitor information.
#
# @copyright  2024 Geoffrey Bernardo van Wyk {@link https://geoffreyvanwyk.dev}
##

import scrapy


class ExhibitorsSpider(scrapy.Spider):
    name = "exhibitors"
    allowed_domains = ["www.gulfood.com", "gulfood.com"]

    def make_request(self, page_number):
        return scrapy.Request(
            f"https://www.gulfood.com/exhibitors?page={page_number}&searchgroup=D1CFEFEE-exhibitorslist-2024",
            callback=self.parse,
            cb_kwargs={"page_number": page_number + 1},
        )

    def start_requests(self):
        yield self.make_request(page_number=1)

    def parse(self, response, **kwargs):
        total_pages = response.xpath(
            "//li[@class='pagination__list__item']/a[@element='last']/@data-page"
        ).get("0")
        if kwargs["page_number"] <= int(total_pages):
            yield self.make_request(page_number=kwargs["page_number"])

        exhibitor_rows = response.xpath(
            "//li[@class='m-exhibitors-list__items__item m-exhibitors-list__items__item--status-mainexhibitor']"
        )
        self.logger.debug(
            f'Exhibitor count on page {kwargs["page_number"]}: {len(exhibitor_rows)}'
        )
        for exhibitor_row in exhibitor_rows:
            yield self.parse_exhibitor_row(exhibitor_row)

    def parse_exhibitor_row(self, exhibitor_row):
        exhibitor_page_url = self.exhibitor_page_url(exhibitor_row)

        exhibitor = {
            "company_name": exhibitor_row.xpath(
                ".//h2[@class='m-exhibitors-list__items__item__name']/a/text()"
            )
            .get("")
            .strip(),
            "sector": self.sector(
                exhibitor_row.xpath(
                    ".//*[@class='m-exhibitors-list__items__item__category']/img[@class='key-item__icon']/@src"
                ).get("")
            ),
            "country": exhibitor_row.xpath(
                ".//*[@class='m-exhibitors-list__items__item__location']/text()"
            )
            .get("")
            .strip(),
            "gulfood_page": exhibitor_page_url,
        }

        return scrapy.Request(
            exhibitor_page_url.replace(
                "https://gulfood.com", "https://www.gulfood.com"
            ),
            callback=self.parse_exhibitor,
            cb_kwargs={"exhibitor": exhibitor},
        )

    def parse_exhibitor(self, response, **kwargs):
        exhibitor = kwargs["exhibitor"]

        exhibitor["description"] = (
            response.xpath(
                "//*[@class='m-exhibitor-entry__item__body__description']/text()"
            )
            .get("")
            .strip()
        )

        exhibitor["specialities"] = " | ".join(
            filter(
                lambda v: v != "",
                map(
                    lambda v: v.replace("\t", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .replace("|", "")
                    .strip(),
                    response.xpath(
                        "//*[@class='m-exhibitor-entry__item__header__infos__categories__item']/text()"
                    ).getall(),
                ),
            )
        )

        address_list = list(
            filter(
                lambda v: v != "",
                map(
                    lambda v: v.replace("\t", "")
                    .replace("\r", "")
                    .replace("\n", "")
                    .strip(),
                    response.xpath(
                        "//*[@class='m-exhibitor-entry__item__body__contacts__address']/text()"
                    ).getall(),
                ),
            )
        )
        exhibitor["address"] = address_list[0] if address_list else ""

        exhibitor["website"] = response.xpath(
            "//*[@class='m-exhibitor-entry__item__body__contacts__additional__button__website']/a/@href"
        ).get("")

        return exhibitor

    def sector(self, icon):
        sectors_by_icon = {
            "https://cdn.asp.events/CLIENT_Dubai_Wo_4B15F265_5056_B739_54F3125D47F0BC95/sites/gulfood-2024/media/2021icons/worldfood.png": "World Food",
            "https://cdn.asp.events/CLIENT_Dubai_Wo_4B15F265_5056_B739_54F3125D47F0BC95/sites/gulfood-2024/media/2021icons/pulsesgrainscereals.png": "Pulses, Grains & Cereals",
            "https://cdn.asp.events/CLIENT_Dubai_Wo_4B15F265_5056_B739_54F3125D47F0BC95/sites/gulfood-2024/media/2021icons/beverages.png": "Beverages",
            "https://cdn.asp.events/CLIENT_Dubai_Wo_4B15F265_5056_B739_54F3125D47F0BC95/sites/gulfood-2024/media/2021icons/meatpoultry.png": "Meat & Poultry",
            "https://cdn.asp.events/CLIENT_Dubai_Wo_4B15F265_5056_B739_54F3125D47F0BC95/sites/gulfood-2024/media/2021icons/powerbrands.png": "Power Brands",
            "https://cdn.asp.events/CLIENT_Dubai_Wo_4B15F265_5056_B739_54F3125D47F0BC95/sites/gulfood-2024/media/2021icons/fatsoils.png": "Fats & Oils",
            "https://cdn.asp.events/CLIENT_Dubai_Wo_4B15F265_5056_B739_54F3125D47F0BC95/sites/gulfood-2024/media/2021icons/dairy.png": "Dairy",
        }

        if icon not in sectors_by_icon:
            return ""

        return sectors_by_icon[icon]

    def exhibitor_page_url(self, exhibitor_row):
        logo_href = exhibitor_row.xpath(
            ".//a[contains(@class, 'm-exhibitors-list__items__item__logo__link')]/@href"
        ).get("")

        return "https://gulfood.com/" + logo_href.removeprefix(
            "javascript:openRemoteModal("
        ).split(",")[0].strip("'")
