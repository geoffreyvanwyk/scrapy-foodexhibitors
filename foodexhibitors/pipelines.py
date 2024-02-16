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
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting.
#
# @copyright  2024 Geoffrey Bernardo van Wyk {@link https://geoffreyvanwyk.dev}
# @link       https://docs.scrapy.org/en/latest/topics/item-pipeline.html
##


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FoodexhibitorsPipeline:
    def process_item(self, item, spider):
        return item
