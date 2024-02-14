# This file is part of project scrapy-gulfoodexhibitors.
#
# Project scrapy-gulfoodexhibitors is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project scrapy-gulfoodexhibitors is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# project scrapy-gulfoodexhibitors. If not, see <https://www.gnu.org/licenses/>.

##
# Scrapy settings for gulfoodexhibitors project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation linked
# below.
#
# @copyright  2024 Geoffrey Bernardo van Wyk {@link https://geoffreyvanwyk.dev}
# @link       https://docs.scrapy.org/en/latest/topics/settings.html
# @link       https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# @link       https://docs.scrapy.org/en/latest/topics/spider-middleware.html
##

from datetime import datetime

import pytz
from scrapy.utils.misc import os

# ------ Context

today = datetime.now(pytz.timezone("Africa/Johannesburg"))
current_date = today.strftime("%Y-%m-%d")
current_time = today.strftime("%H-%M-%S%z")

# ------ Spiders

BOT_NAME = "gulfoodexhibitors"

SPIDER_MODULES = ["gulfoodexhibitors.spiders"]
NEWSPIDER_MODULE = "gulfoodexhibitors.spiders"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# ------ Responsible Scraping

ROBOTSTXT_OBEY = False

## ------------ Autothrottling

# Limit the rate at which requests are made so that the web server is not
# overloaded.
AUTOTHROTTLE_ENABLED = True

# The average number of requests Scrapy should be sending in parallel to
# each remote server.
AUTOTHROTTLE_TARGET_CONCURRENCY = 6.0

# ------ Downloader Middlewares

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "random_useragent.RandomUserAgentMiddleware": 400,
}

USER_AGENT_LIST = "user_agents.txt"

# ------ Pipelines

# ITEM_PIPELINES = {
#    "gulfoodexhibitors.pipelines.GulfoodexhibitorsPipeline": 300,
# }


# ------ Caching

# Cache responses received from the web server. This is especially useful
# during development, because the requests for which responses have been cached
# are not sent to the web server again, reducing the load on the web server and
# speeding up the development cycle.
HTTPCACHE_ENABLED = True

# ------ Feed Exports

FEED_EXPORT_ENCODING = "utf-8"
FEED_EXPORT_INDENT = 4

FEED_EXPORTERS = {
    "xlsx": "scrapy_xlsx.XlsxItemExporter",
}

FEEDS = {
    f"feeds/{current_date}/%(name)s-%(time)s.xlsx": {"format": "xlsx"},
    f"feeds/{current_date}/%(name)s-%(time)s.json": {"format": "json"},
}

# ------ Logging

LOG_ENABLED = True

# Create log file.
logs_directory = f"logs/{current_date}"
os.makedirs(logs_directory, exist_ok=True)
log_filename = f"gulfoodexhibitors-{current_date}T{current_time}.log"
log_file = "/".join([logs_directory, log_filename])
open(log_file, "a").close()

LOG_FILE = log_file
