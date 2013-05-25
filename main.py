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
from google.appengine.api import memcache

#
#   Scraping Utilities
#

#
#   Retrieves a URL to the card's image as represented by http://magiccards.info
#
def getCardImageURL(cardName):
    magicInfoURL = "http://magiccards.info/query?q=" + urllib.quote(cardName)
    htmlFile = urllib.urlopen(magicInfoURL)
    rawHTML = htmlFile.read()
    startURLIndex = rawHTML.find("http://magiccards.info/scans")
    endURLIndex = rawHTML.find("\"", startURLIndex)
    imageURL = rawHTML[startURLIndex:endURLIndex]
    return [imageURL]

#
#   Retrieves a cards current price on Channel Fireball
#
def getCFBPrice(cardName):
    cfbURL = "http://store.channelfireball.com/products/search?q=" + urllib.quote(cardName)
    htmlFile = urllib.urlopen(cfbURL)
    rawHTML = htmlFile.read()    
    tempIndex = rawHTML.find("grid-item-price")
    startPriceIndex = rawHTML.find("$", tempIndex)
    endPriceIndex = rawHTML.find("<", startPriceIndex)
    cfbPrice = rawHTML[startPriceIndex:endPriceIndex]
    return [cfbPrice]

#
#   Retrieves the lowest buy it now price for a card on ebay
#
def getEbayPrice(cardName):
    ebayURL = "http://www.ebay.com/sch/i.html?_sacat=0&_sop=15&LH_BIN=1&_nkw=" + urllib.quote(cardName + " mtg nm")
    htmlFile = urllib.urlopen(ebayURL)
    rawHTML = htmlFile.read()
    startPriceIndex = rawHTML.find("$")
    endPriceIndex = rawHTML.find("<", startPriceIndex)
    lowestBIN = rawHTML[startPriceIndex:endPriceIndex]
    return [lowestBIN]

#
#   Retrieves the low, mid, and high prices of a card as shown on http://tcgplayer.com
#
def getTCGPlayerPrices(cardName):
    #   Open the TCGPlayer URL
    tcgPlayerURL = "http://magic.tcgplayer.com/db/magic_single_card.asp?cn=" + urllib.quote(cardName)
    htmlFile = urllib.urlopen(tcgPlayerURL)
    rawHTML = htmlFile.read()

    #   Scrape for the low price
    tempIndex = rawHTML.find('>L:')
    startLowIndex = rawHTML.find("$", tempIndex)
    endLowIndex = rawHTML.find("<", startLowIndex)

    lowPrice = rawHTML[startLowIndex:endLowIndex]

    #   Scrape for the mid price
    tempIndex = rawHTML.find('>M:')
    startMidIndex = rawHTML.find("$", tempIndex)
    endMidIndex = rawHTML.find("<", startMidIndex)
    
    midPrice = rawHTML[startMidIndex:endMidIndex]

    #   Scrape for the high price
    tempIndex = rawHTML.find('>H:')
    startHighIndex = rawHTML.find("$", tempIndex)
    endHighIndex = rawHTML.find("<", startHighIndex)
    
    highPrice = rawHTML[startHighIndex:endHighIndex]

    return [lowPrice, midPrice, highPrice]

#
#   URL Handlers
#
class GetImageURLHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        retVal = memcache.get('Image'  + cardName)
        if retVal is None:
            retVal = getCardImageURL(cardName)
            memcache.add('Image ' + cardName, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class CFBPriceCheckHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        retVal = memcache.get('CFB ' + cardName)
        if retVal is None:
            retVal = getCFBPrice(cardName)
            memcache.add('CFB ' + cardName, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class TCGPriceCheckHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        retVal = memcache.get('TCG ' + cardName)
        if retVal is None:
            retVal = getTCGPlayerPrices(cardName)
            memcache.add('TCG ' + cardName, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class EbayPriceCheckHandler(webapp2.RequestHandler):
    def get(self):
        cardName = self.request.get('cardname')
        retVal = memcache.get('Ebay ' + cardName)
        if retVal is None:
            retVal = getEbayPrice(cardName)
            memcache.add('Ebay ' + cardName, retVal, 300)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(retVal))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Hello world")

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/api/tcgplayer/price.json', TCGPriceCheckHandler), ('/api/ebay/price.json', EbayPriceCheckHandler), 
    ('/api/cfb/price.json', CFBPriceCheckHandler), ('/api/images/imageurl.json', GetImageURLHandler)
], debug=True)