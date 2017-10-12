"""
Administrative page.

"""

### IMPORTS

from time import gmtime, strftime
from io import StringIO

from flask_appbuilder import AppBuilder, expose, BaseView
from flask import flash, request
from flask_appbuilder import SimpleFormView
from flask_appbuilder.upload import FileUploadField
from wtforms import Form, StringField, FileField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

from egas import appbuilder

from .assocreader import AssocReader
from . import consts
from . import models


### CONSTS & DEFINES

### CODE ###

### Utils

def make_upload_set_name():
   current_dt = strftime("%Y-%m-%d %H:%M:%S", gmtime())
   return "Uploaded %s" % current_dt


### Upload associations

class BulkUploadForm (DynamicForm):
   """
   Form object / contents for bulk uploading of associations.
   """

   upload_file = FileUploadField (('Association file'),
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

def parse_upload_recs (recs):
   """
   Return records & parsing errors.
   """
   errors = []
   new_db_recs = []

   for i, r in enumerate (recs):
      curr_idx = i + 1
      try:
         # clean & check vals
         clean_rec = sanitize_upload_rec (r)
         # check creation
         new_row = models.Association (**clean_rec)
         new_db_recs.append (new_row)

      except Exception as err:
         print (err)
         prob_rec_id = "%s-%s" % (r['snp_id'], r['cpg_id'])
         msg = "Problem parsing row %s (%s): %s" % (curr_idx, prob_rec_id, err)

   return new_db_recs, errors


def sanitize_upload_rec (r):
   """
   Takes an upload record, cleans & checks it.
   """
   clean_rec = {}
   for f in consts.INDATA_FLDS:
      # clean up whitespace
      v = r[f].strip()
      # ids in lowercase, chromosomes & bases in uppercase
      if f in ('snp_id', 'cpg_id'):
         v = v.lower()
      else:
         v = v.upper()
      # convert & check numbers
      if f.endswith ('_posn'):
         v = int (v)
         assert 0 < v, "negative chromosoaml location '%s'" % v
      elif f.startswith ('stat_'):
         v = float (v)
      # check chromsome names
      if f.endswith ('_chr'):
         assert v in consts.chromosomes, "invalid chromosome '%s'" % v
      # finally, store it
      clean_rec[f] = v
   return clean_rec


def gen_association_uid (snp_id, cpg_id):
   return "%s.%s" % (snp_id, cpg_id)


class BulkUploadView (SimpleFormView):
   route_base = "/admin/upload"

   form = BulkUploadForm
   form_title = 'Upload associations'
   message = 'My form was submitted'

   def form_get (self, form):
      # preprocess form
      pass
      # form.field1.data = 'This was prefilled'

   def form_post (self, form):
      """
      Post process form.
      """
      # assume input validation has been done
      errors = []
      rec_cnt = None
      try:
         errors, rec_cnt = self.execute_upload (form)
         print (errors)
         print (rec_cnt)
      except Exception as err:
         errors.append = str (err)

      # didsplay results
      flash (self.message, 'info')

      # direct back to page
      widgets = self._get_edit_widget (form=form)
      return self.render_template (
         self.form_template,
         title=self.form_title,
         widgets=widgets,
         appbuilder=self.appbuilder
      )

   def execute_upload (self, form):
      # passed in form with:
      #    upload_file
      #    set_name
      #    overwrite
      #    dryrun

      # params
      set_name, overwrite, dryrun = form.set_name, form.overwrite, form.dryrun
      print (set_name, overwrite, dryrun)

      # grab file data
      # TODO: use 'save' feature of fileStorage as it buffers
      raw_data = request.files['upload_file'].stream.read()
      str_data = StringIO (raw_data.decode ("utf-8"))

      # produce records
      recs = [r for r in AssocReader (str_data)]
      rec_cnt = len (recs)

      # parse records
      new_db_recs, errors = parse_upload_recs (recs)

      # if there are records & no parse errors, proceed:
      if new_db_recs and not errors:

         # if not overwriting, check for collision
         overwrite_err = None
         if not overwrite:
            assoc_ids = [gen_association_uid (d.snp_id, d.cpg_id) for d in new_db_recs]
            all_db_ids = models.Association.query (models.Association.id)
            print (all_db_ids)
            matching_db_ids = [x for x in assoc_ids if x in all_db_ids]
            if matching_db_ids:
               overwrite_err = "Uploads match pre-existing associations (%s)" % ', '.join (matching_db_ids)
               errors.append (overwrite_err)

         # if actually storing & nothing gone wrong so far
         if not dryrun and not overwrite_err:
            # find or generate tag
            if set_name:
               curr_tag = models.Tag.query.get (set_name) or models.Tag (id=set_name)
               # attach tag to recs
               for r in new_db_recs:
                  if curr_tag not in r.tags:
                     r.tags.append (curr_tag)
            # actually persist recs

      ## Postconditions & return:
      return errors, rec_cnt




### Register views

# import flask_appbuilder.security.views as sec_views

for cat in ['Admin']:
   appbuilder.add_view (BulkUploadView, "Bulk upload of associations",
      icon="fa-upload",
      category=cat,
      category_icon="fa-wrench",
   )

   appbuilder.menu.add_separator (cat)

   # TODO: add security viuews?
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
