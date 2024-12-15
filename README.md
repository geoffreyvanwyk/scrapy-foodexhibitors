![Repository Banner](https://upwork-usw2-prod-agora-file-storage.s3.us-west-2.amazonaws.com/profile/portfolio/thumbnail/5689ac7cc0368a61090daf895e93695c?response-content-disposition=inline;+filename=%22image_original%22;+filename*=utf-8%27%27image_original&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDfHO4IwXeai78VAQpML%2BRhoWuwy6utCpVt3NCMQWQKCwIgRFeW4/3wF5c5FzkcU8LAbVOaSGWzcDe9Si8Ma5%2Bxxx8qkAUIEBAAGgw3Mzk5MzkxNzM4MTkiDMqq2TJiZzWha379YyrtBKDiVzalenML/UEMrvxLnPue8%2Bw8arFmWMPJCl8cNWSW7hVCHM8jK5yucHzhfwxRW5kQCi3i8eOvBWPhiMQ5WhBmoC75kBrJZ8SP0sK5h4c6YPh/TX21p8Yo%2BcmR1M/vxZLCPPCm0/dHAH5kh/aIjcu9rh%2BOYnuJRpCnkGhZtzVAVTvNTTNy4aumm8N6CS4/NA7UxpFSgSW2y0%2ByEGOSmIFFdZkg/te4ybTHNKOcQhnEbwJWJ6YmKoIKUiXf%2BYTRPHKyDNMD0S4Z2Opmd67%2B0ehJxXSPoW75wjkPBY9aNORbu0yjhJmkdCWZ5u7mCBB4wHOaX20VI8hk54OSLtgjtv1IGY5sGRBupzkePiz1ZGRmskYdKklgv9l9W0MXpMD%2B6VUTJ9d3dx7VilyhOf6pNCJaMf/UuqAxeb7Srlr/jp4mR44YKABDBTw1MxE8v9X8H4PdiTgZNE/JdYm7ZgLkfSzVWvxMnXeeRYg0jRzPYAsSxMW8924nzRZ2hCbM0SLKZH1WknJ60j0a4waQA1YZAMsituKRIB80bmSCOpnVP4Ymp3pCsDSR/KUBC6hNsPGpzTCJeJFsDrkdZZwHI0wQxp26QmTgyrvnsUdF9hNC/6LtMdvEy0kyJ/f2syhH9z/dlo1Yn4vwwr1/NSslAuOtT2%2BxVc9%2BSXRautvLNJhuuuTYFLgHaH1N07kavM7M8VZqyRSbCajLFebxBQmz4GUIxMnMB5nxcC5v3e6RFv51NmtkSAcQ9jowPYk/Uv2Mw0HkwKWbUlm28cVAfbs3MxMdinhf/3ewfCvC36%2BatbE3BpRTGO9cg7QoQFmW/WPyhDDCgfq6BjqbAQdQttorNLGjo4teKSLsu6ceEjM6zNXvPIs/1Qrw5Pr3q3e3UpuEXH3DPEUHgh2F%2B7LiziLkBwFma45wkAAWkyJztYw3Feyl0LZE3d8z3OAx1YmXkeZ6I3PsmqJ8Tv/IrcXORHvYQ8SPqNWMIzRZFsrQq5XiUSB9vBR2JWqbOH%2BQrmrwP%2BS0DzyJDYjN0i84wxtbbVEEod%2Br2yqM&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241215T073854Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=ASIA2YR6PYW5WA5G3YBY/20241215/us-west-2/s3/aws4_request&X-Amz-Signature=c685ec391c14354552a67998157e2a336b09461d156f16852c21c81e72401125)

# Web Scraper for Exhibitors at Food Producers Conference

This is a web scraper written in Python using the Scrapy framework for
collecting information on all the exhibitors at a food producers conference.

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
_foodexhibitors/settings.py_ file.

## License

Copyright &copy; 2024 Geoffrey Bernardo van Wyk [https://geoffreyvanwyk.dev](https://geoffreyvanwyk.dev)

This file is part of project scrapy-foodexhibitors.

Project scrapy-foodexhibitors is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Project scrapy-foodexhibitors is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along with
project scrapy-foodexhibitors. If not, see <https://www.gnu.org/licenses/>.
