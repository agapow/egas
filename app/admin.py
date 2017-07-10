"""
Administrative page.

"""

### IMPORTS

from flask_appbuilder import AppBuilder, expose, BaseView
from app import appbuilder


### CONSTS & DEFINES

### CODE ###


class AdminView (BaseView):
   route_base = "/admin"

   default_view = 'upload'

   @expose('/upload/')
   def upload (self):
      # do something with param1
      # and return it
      self.update_redirect()
      return self.render_template ('upload.html')



appbuilder.add_view (AdminView, "Upload", category='Admin')


### END ###
