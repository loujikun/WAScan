#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I

def grails(headers,content):
	_ = False
	for header in headers.items():
		_ |= search("grails",header[1]) is not None
		_ |= search("x-grails",header[0]) is not None
		_ |= search("x-grails-cached",header[0]) is not None
		if _ : break
	if _ : return "Grails - Java Framework"