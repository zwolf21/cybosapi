import os, re, time
from urllib.parse import *

import requests
from bs4 import BeautifulSoup

HEADERS = {
	'Content-Type':'application/x-www-form-urlencoded',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}

domain = 'http://finance.naver.com/'

start_urls = [
	'http://finance.naver.com/sise/sise_group.nhn?type=upjong',
]

def collect_link():
	links = []
	link_regx = re.compile(r'/sise/sise_group_detail\.nhn\?type=upjong&no=\d+')
	for url in start_urls:
		r = requests.get(url, headers=HEADERS)
		soup = BeautifulSoup(r.content, 'html.parser')
		for a in soup('a', href=link_regx):
			links.append((a.text.strip(), urljoin(domain, a['href'])))
	return links


def parse_link(link):
	r = requests.get(link, headers=HEADERS)
	detail_regx = re.compile(r'/item/main\.nhn\?code=(?P<code>.+)')
	soup = BeautifulSoup(r.content, 'html.parser')
	items = []
	for a in soup('a', href=detail_regx):
		g = detail_regx.search(a['href'])
		code = g.group('code')
		name = a.text.strip()
		item = {
			'표준종목코드': code, '종목명': name
		}
		items.append(item)
	return items

def scrap(limit=None):
	records = []
	links = collect_link()
	if limit:
		links = links[:limit]
	for uname, link in links:
		items = parse_link(link)
		for item in items:
			item['업종명'] = uname
		records+=items
	return records







