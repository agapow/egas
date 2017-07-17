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


from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm
from time import gmtime, strftime

def make_upload_set_name():
   current_dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
   return "Uploaded %s" % current_dt

class BulkUploadForm (DynamicForm):

   upload_file = FileField (('Association file'),
      description=('CSV file of association data in prescribed format'),
      validators = [DataRequired()],
   )
   makeset = BooleanField (('Create set'),
      description=('Assemble all uploaded data into '),
      default=True,
   )
   set_name = StringField (('Set name'),
      description=('Name for the set (if created)'),
      default=make_upload_set_name(),
   )
   overwrite = BooleanField (('Overwrite pre-existing associations'),
      description=('Association with the same SNP-methylation pair will be overwritten with the new data'),
      default=False,
   )
   dryrun = BooleanField (('Dry run'),
      description=("Don't create or commit new data, just check for errors"),
      default=True,
   )

### END ###
