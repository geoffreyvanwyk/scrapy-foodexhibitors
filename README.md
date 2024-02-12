# Web Scraper for Exhibitors at Gulfood Expo

This is a web scraper for collecting information on all the exhibitors at a
Gulfood expo from the web page https://gulfood.com/exhibitors.

## Installation

This webscraper was developed using Python 3.12 and Scrapy 2.11.

Install PIP, the Python package manager. For example, on Ubuntu:

```shell
sudo apt install python3-pip
```

Install the required Python packages as listed in the _requirements.txt_ file
in the project root directory.

```shell
pip install --requirement requirements.txt
```

## Usage

Run the webscraper as follows:

```shell
scrapy crawl exhibitors
```

The data will be collected in both Excel spreadsheet format and JSON in the
_feeds_ directory inside a subdirectory named according to the date. Each feed
file's name will also include the date and time.

The output of the crawl will not be output to stdout but to a log file in the
_logs_ directory with the same structure as the _feeds_ directory.

Caching is enabled, which means that for each request the response is stored
locally so that if a request is made again in a subsequent crawl, the request
will not be sent to the server again. This saves time during development. In
order to fetch new data, the caching must be disabled in the
_gulfoodexhibitors/settings.py_ file.

## License

Copyright &copy; 2024 Geoffrey Bernardo van Wyk [https://geoffreyvanwyk.dev](https://geoffreyvanwyk.dev)

This file is part of project scrapy-gulfoodexhibitors.

Project scrapy-gulfoodexhibitors is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Project scrapy-gulfoodexhibitors is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along with
project scrapy-gulfoodexhibitors. If not, see <https://www.gnu.org/licenses/>.
