# Web Scraping for IP Addresses

This project utilizes web scraping techniques to fetch IP addresses from a specified website.

## Overview

The purpose of this project is to automate the process of collecting IP addresses from a website. It utilizes Selenium, a Python library for web automation, to navigate the website and extract relevant information.

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome WebDriver (or WebDriver for your preferred browser)

## Installation

```
import ProxyScraper
proxy_scraper = ProxyScraper()
ip_addresses = proxy_scraper.fetch_ip_addresses(10)
print(ip_addresses)
```
