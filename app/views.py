"""
Views for application models and pages.

"""

### IMPORTS

from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db

from . import models


### CONSTS & DEFINES

### CODE ###

@appbuilder.app.errorhandler (404)
def page_not_found (e):
   """
   Application wide 404 error handler
   """
   return render_template (
         '404.html',
         base_template=appbuilder.base_template,
         appbuilder=appbuilder
      ), 404


class AssociationModelView (ModelView):
   """
   A SNP-methylation association.
   """
   datamodel = SQLAInterface (models.Association)

   label_columns = {}
   list_columns = ['stat_beta', 'stat_stderr']

   show_fieldsets = [
      ('SNP',
         {
            'fields':['snp_id','snp_locn_chr','snp_locn_posn']
         }
      ),
      ('Methylation',
         {
            'fields':['cpg_id','cpg_locn_chr'],
         }
      ),
      ('Statistical support',
         {
            'fields':['stat_beta','stat_stderr', 'stat_pval'],
         }
      ),
   ]


# create and register everything
db.create_all()

appbuilder.add_view (AssociationModelView, "Association", icon="fa-file-o")

# fa-exchange

### END ###
