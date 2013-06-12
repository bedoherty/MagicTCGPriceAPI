#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import json
import urllib
from scraper import *
from ndbmodels import *
from google.appengine.api import memcache
from google.appengine.ext import ndb
import logging

#
#   URL Handlers
#
class GetImageURLHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        cardSet = self.request.get('cardset')
        retVal = None
        if not cardSet:
            retVal = memcache.get('Image '  + cardName)
        else:
            retVal = memcache.get('Image ' + cardName + " " + cardSet)
        if retVal is None:
            retVal = getCardImageURL(cardName, cardSet)
            if not cardSet:
                memcache.add('Image '  + cardName, retVal, 300)
            else:
                memcache.add('Image ' + cardName + " " + cardSet, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class CFBPriceCheckHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        cardSet = self.request.get('cardset')
        retVal = None
        if not cardSet:
            retVal = memcache.get('CFB '  + cardName)
        else:
            retVal = memcache.get('CFB ' + cardName + " " + cardSet)
        if retVal is None:
            retVal = getCFBPrice(cardName, cardSet)
            if not cardSet:
                memcache.add('CFB '  + cardName, retVal, 300)
            else:
                memcache.add('CFB ' + cardName + " " + cardSet, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class TCGPriceCheckHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        cardSet = self.request.get('cardset')
        retVal = None
        if not cardSet:
            retVal = memcache.get('TCG '  + cardName)
        else:
            retVal = memcache.get('TCG ' + cardName + " " + cardSet)
        if retVal is None:
            retVal = getTCGPlayerPrices(cardName, cardSet)
            if not cardSet:
                memcache.add('TCG '  + cardName, retVal, 300)
            else:
                memcache.add('TCG ' + cardName + " " + cardSet, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class EbayPriceCheckHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        cardSet = self.request.get('cardset')
        retVal = None
        if not cardSet:
            retVal = memcache.get('Ebay '  + cardName)
        else:
            retVal = memcache.get('Ebay ' + cardName + " " + cardSet)
        if retVal is None:
            retVal = getEbayPrice(cardName, cardSet)
            if not cardSet:
                memcache.add('Ebay '  + cardName, retVal, 300)
            else:
                memcache.add('Ebay ' + cardName + " " + cardSet, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello world")

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/api/tcgplayer/price.json', TCGPriceCheckHandler), ('/api/ebay/price.json', EbayPriceCheckHandler), 
    ('/api/cfb/price.json', CFBPriceCheckHandler), ('/api/images/imageurl.json', GetImageURLHandler)
], debug=True)