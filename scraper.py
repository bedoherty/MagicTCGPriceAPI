#
#   Scraping Utilities
#

import urllib
import logging

#
#   Retrieves a URL to the card's image as represented by http://magiccards.info
#
def getCardImageURL(cardName, cardSet):
    magicInfoURL = "http://magiccards.info/query?q=" + urllib.quote(cardName)
    if cardSet:
        magicInfoURL += urllib.quote(" e:" + cardSet + "/en")
    htmlFile = urllib.urlopen(magicInfoURL)
    rawHTML = htmlFile.read()
    startURLIndex = rawHTML.find("http://magiccards.info/scans")
    endURLIndex = rawHTML.find("\"", startURLIndex)
    imageURL = rawHTML[startURLIndex:endURLIndex]
    return [imageURL]

#
#   Retrieves a cards current price on Channel Fireball
#
def getCFBPrice(cardName, cardSet):
    cfbURL = "http://store.channelfireball.com/products/search?q=" + urllib.quote(cardName)
    if cardSet:
        cfbURL += " " + urllib.quote(cardSet)
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
def getEbayPrice(cardName, cardSet):
    ebayURL = "http://www.ebay.com/sch/i.html?_sacat=0&_sop=15&LH_BIN=1&_nkw=" + urllib.quote(cardName)
    if cardSet:
        ebayURL += urllib.quote(" " + cardSet)
    ebayURL += urllib.quote( " mtg nm")
    logging.info(ebayURL)
    htmlFile = urllib.urlopen(ebayURL)
    rawHTML = htmlFile.read()
    startPriceIndex = rawHTML.find('itemprop="price">')
    startPriceIndex = rawHTML.find("$", startPriceIndex)
    endPriceIndex = rawHTML.find("<", startPriceIndex)
    lowestBIN = rawHTML[startPriceIndex:endPriceIndex]
    return [lowestBIN]

#
#   Retrieves the low, mid, and high prices of a card as shown on http://tcgplayer.com
#
def getTCGPlayerPrices(cardName, cardSet):
    #   Open the TCGPlayer URL
    tcgPlayerURL = "http://magic.tcgplayer.com/db/magic_single_card.asp?cn=" + urllib.quote(cardName)
    if cardSet:
       tcgPlayerURL += "&sn=" + urllib.quote(cardSet)
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
