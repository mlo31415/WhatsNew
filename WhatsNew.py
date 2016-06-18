#!/usr/bin/python

import sys
from optparse import OptionParser
import wikidotapi

api = wikidotapi.connection("default")

site=api.get_site()
categories=api.get_categories()
fullname=api.page_exists("fapa")
name=api.get_username()

pages=api.get_pages()


print("Done")

