#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
# author    heming.zhang
# 线上数据库读取层

import urllib   
import urllib2

def urlPost(url, data):   
    req = urllib2.Request(url)   
    data = urllib.urlencode(data)   
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())   
    response = opener.open(req, data)   
    
    return response.read()      

def urlGet(url):
    urlItem = urllib.urlopen(url)
    htmSource = urlItem.read()
    urlItem.close()
    
    return htmSource