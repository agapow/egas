"""
Simple utilities.
"""

### IMPORTS

from werkzeug.contrib.cache import SimpleCache

from app import app, db
from . import models

#__all__ = (
#   'simple_repr',
#)

print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
### CONSTANTS & DEFINES

CACHE = SimpleCache()
CACHE_TIMEOUT = 5 * 60 # 5 minutes


### CODE ###

def simple_repr (obj, *fields):
   """
   Quick-and-dirty way of making repr strings for models.
   """
   field_strs = ['%s: %s' % (f, getattr (obj, f)) for f in fields]
   field_bdy = '(%s)' % ', '.join (field_strs)
   return '%s %s' % (obj.__class__.__name__, field_bdy)


@app.context_processor
def utility_processor():
   """
   All those function you want available in templates
   """

   def date_now(format="%d.m.%Y %H:%M:%S"):
      """ returns the formated datetime """
      return datetime.datetime.now().strftime (format)

   def get_total_associations():
      """
      For use in template, tracking number of records.
      """
      global CACHE
      val = CACHE.get ('total_associations')
      if val is None:
         val = db.session.query (models.Association).count()
         CACHE.set ('total_associations', val, timeout=CACHE_TIMEOUT)
      return val

   def get_latest_news():
      """
      Get the most recent news item.
      """
      global CACHE
      val = CACHE.get ('latest_news')
      if val is None:
         val = db.session.query (models.News).order_by (models.News.created_on.desc()).first()
         print (val)
         if val:
            val = {
               'id': val.id,
               'title': val.title,
               'created_on': val.created_on,
            }
         CACHE.set ('latest_news', val, timeout=CACHE_TIMEOUT)
      return val

   return dict (
      date_now=date_now,
      get_total_associations=get_total_associations,
      get_latest_news=get_latest_news,
   )



### END ###
