# Magic the Gathering TCG Price Checking API

This repository contains my REST API for checking current prices on Magic TCG singles.


Changelog:

* Fixed and made TCGPlayer scraping more accurate and reliable
* Added caching via memcache to save data and reduce load times

## API Examples

These examples demonstrate the proper URLs and return values for these APIs.

* [Card Image](http://magictcgprices.appspot.com/api/images/imageurl.json?cardname=Emrakul,%20the%20Aeons%20Torn)
* [TCGPlayer Prices](http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=Emrakul,%20the%20Aeons%20Torn)
* [Lowest Ebay Buy It Now Price](http://magictcgprices.appspot.com/api/ebay/price.json?cardname=Emrakul,%20the%20Aeons%20Torn)
* [Channel Fireball Price](http://magictcgprices.appspot.com/api/cfb/price.json?cardname=Emrakul,%20the%20Aeons%20Torn)

## Apps

To test this API, I write a simple Android app which will be released in the Google Play Store.  After it shows up in the market, I will post the link here, as well as potentially uploading the source code for that app.