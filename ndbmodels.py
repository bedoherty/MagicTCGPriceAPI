from google.appengine.ext import ndb

#
#   NDB Models
#

#
#	Model for the Card class used to track a cards values over time in the NDB
#
class Card(ndb.Model):
  cardName = ndb.StringProperty()
  cardSet = ndb.StringProperty()
  cardPrices = ndb.FloatProperty(repeated=True)
  cardPriceDates = ndb.DateTimeProperty(repeated=True)