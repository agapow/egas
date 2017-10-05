"""
Administrative page.

"""

### IMPORTS

from flask_appbuilder import AppBuilder, expose, BaseView
from egas import appbuilder


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



#appbuilder.add_view (AdminView, "Upload", category='Admin')


from wtforms import Form, StringField, FileField, BooleanField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm
from time import gmtime, strftime

def make_upload_set_name():
   current_dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
   return "Uploaded %s" % current_dt


class BulkUploadForm (DynamicForm):
   """
   Form object / contents for bulk uploading of associations.
   """

   upload_file = FileField (('Association file'),
      description=('CSV file of association data in prescribed format'),
      validators = [DataRequired()],
   )

   set_name = StringField (('Set name'),
      description=('Name for the set'),
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

from flask import flash
from flask_appbuilder import SimpleFormView

class BulkUploadView (SimpleFormView):
    form = BulkUploadForm
    form_title = 'Bulk upoad of associations'
    message = 'My form was submitted'

    def form_get(self, form):
      pass
      # form.field1.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash (self.message, 'info')


import flask_appbuilder.security.views as sec_views

for cat in ['Admin']:
   appbuilder.add_view (BulkUploadView, "Bulk upload of associations",
      icon="fa-upload",
      category=cat,
      category_icon="fa-wrench",
   )

   appbuilder.menu.add_separator (cat)

   # appbuilder.add_view (appbuilder.sm.user_view, "List Users",
   #    icon="fa-user",
   #    label="List Users",
   #    category=cat,
   #    category_icon="fa-cogs",
   # )
   # appbuilder.add_view (sec_views.RoleModelView, "List Roles",
   #    icon="fa-group",
   #    label='List Roles',
   #    category=cat,
   #    category_icon="fa-cogs",
   # )
# role_view.related_views = [self.user_view.__class__]



### END ###
