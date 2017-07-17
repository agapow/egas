"""
Public pages.

"""

### IMPORTS

from flask_appbuilder import AppBuilder, expose, BaseView
from app import appbuilder


### CONSTS & DEFINES

### CODE ###


class AboutView (BaseView):
   route_base = "/about"

   default_view = 'about'

   @expose('/')
   def about (self):
      # just show an about page
      self.update_redirect()
      return self.render_template ('about.html')



appbuilder.add_view (AboutView, "About this site", category='About')


### END ###
