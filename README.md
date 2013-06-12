# Magic the Gathering TCG Price Checking API

This repository contains my REST API for checking current prices on Magic TCG singles.


Changelog:

* Fixed and made TCGPlayer scraping more accurate and reliable
* Added caching via memcache to save data and reduce load times

## API Documentation

### Card Images (/api/images/imageurl.json)

| Parameter     | Description                                   |
| ------------- | --------------------------------------------- |
| cardname      | The name of the card to retrieve an image for. |
| cardset(optional)       | The set we want to retrieve the image from, as listed on [magiccards.info](http://magiccards.info/sitemap.html)    |

### TCGPlayer Prices (/api/tcgplayer/price.json)

| Parameter     | Description                                   |
| ------------- | --------------------------------------------- |
| cardname      | The name of the card to retrieve TCGPlayer pricing on. |
| cardset(optional)        | The set we want to retrieve TCGPlayer prices from as listed on [TCGPlayer](http://magic.tcgplayer.com/all_magic_sets.asp)    |

### Lowest Ebay Buy It Now Price (/api/ebay/price.json)

| Parameter     | Description                                   |
| ------------- | --------------------------------------------- |
| cardname      | The name of the card to retrieve Ebay pricing on. |
| cardset(optional)        | The set we want to retrieve the Ebay price from in any format    |

### Channel Fireball (/api/cfb/price.json)

| Parameter     | Description                                   |
| ------------- | --------------------------------------------- |
| cardname      | The name of the card to retrieve Channel Fireball pricing on. |
| cardset(optional)        | The set we want to retrieve the Channel Fireball price from in any format    |

## API Examples

These examples demonstrate the proper URLs and return values for these APIs.

### [Card Image](http://magictcgprices.appspot.com/api/images/imageurl.json?cardname=Pillar%20of%20Flame&cardset=fnmp)

URL:

 ```
 http://magictcgprices.appspot.com/api/images/imageurl.json?cardname=Pillar%20of%20Flame&cardset=fnmp
 ```

Result:

 ```
 ["http://magiccards.info/scans/en/fnmp/150.jpg"]
 ```

### [TCGPlayer Prices](http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=Tarmogoyf&cardset=Modern%20Masters)

URL:

 ```
 http://magictcgprices.appspot.com/api/tcgplayer/price.json?cardname=Tarmogoyf&cardset=Modern%20Masters
 ```

Result:

 ```
 ["$97.25", "$115.20", "$149.98"]
 ```

### [Lowest Ebay Buy It Now Price](http://magictcgprices.appspot.com/api/ebay/price.json?cardname=Restoration%20Angel&cardset=promo)

URL:

 ```
 http://magictcgprices.appspot.com/api/ebay/price.json?cardname=Restoration%20Angel&cardset=promo
 ```

Result:

 ```
 ["$11.99"]
 ```

### [Channel Fireball Price](http://magictcgprices.appspot.com/api/cfb/price.json?cardname=Dark%20Confidant&setname=ravnica)

URL:

 ```
 http://magictcgprices.appspot.com/api/cfb/price.json?cardname=Dark%20Confidant&setname=ravnica
 ```

Result:

 ```
 ["$59.99"]
 ```

## Apps

To test this API, I write a simple Android app which will be released in the Google Play Store.  After it shows up in the market, I will post the link here, as well as potentially uploading the source code for that app.