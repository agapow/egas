"""
Views for application models and pages.

"""

### IMPORTS

from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from wtforms import validators as wtfval

from app import appbuilder, db
from app import validators as appval

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

ASSOC_COLS = [
   'snp_id',
   'snp_locn_chr',
   'snp_locn_posn',
   'snp_base_wild',
   'snp_base_var',
   'cpg_id',
   'cpg_locn_chr',
   'cpg_locn_posn',
   'stat_beta',
   'stat_stderr',
   'stat_pval',
]

class AssociationModelView (ModelView):
   """
   A SNP-methylation association.
   """
   # TODO: ensure wild and variant bases are different

   datamodel = SQLAInterface (models.Association)

   # route to nicer url
   route_base = '/associations'

   # friendly name for columns
   label_columns = {
      'title': 'SNP id',
      'description': 'SNP chromosome',
      'snp_locn_posn': 'SNP position',
      'snp_base_wild': 'Wild base',
      'snp_base_var': 'Variant base',
      'cpg_id': 'CpG Id',
      'cpg_locn_chr': 'CpG chromosome',
      'cpg_locn_posn': 'CpG location',
      'stat_beta': 'Beta',
      'stat_stderr': 'Std error',
      'stat_pval': 'P-value',
   }

   ## Listing / showing
   # what columns appear in a table/list & the order
   list_columns = ASSOC_COLS
   base_order = ('snp_id','asc')

   # how columns are grouped in individual record view
   show_fieldsets = [
      ('SNP',
         {
            'fields':['snp_id','snp_locn_chr','snp_locn_posn',
               'snp_base_wild', 'snp_base_var']
         }
      ),
      ('Methylation',
         {
            'fields':['cpg_id','cpg_locn_chr', 'cpg_locn_posn'],
         }
      ),
      ('Statistical support',
         {
            'fields':['stat_beta','stat_stderr', 'stat_pval'],
         }
      ),
   ]

   ## Adding / editing
   # what columns are visible in add/edit
   add_columns = ASSOC_COLS
   edit_columns = ASSOC_COLS

   ## validation
   validators_columns = {
      'snp_base_wild': [
         appval.NotEqualTo ('snp_base_var',
            message='wild and variant bases cannot match'
         )
      ],

      'snp_locn_posn': [appval.PositiveNumber()],
      'cpg_locn_posn': [appval.PositiveNumber()],

      'stat_beta': [appval.PositiveNumber()],
      'stat_stderr': [appval.PositiveNumber()],
      'stat_pval': [appval.PositiveNumber()],

   }


## ASSOCIATION SETS

SET_COLS = [
   'title',
   'description',
]

class SetModelView (ModelView):
   """
   A group of associations.
   """
   # TODO: ensure wild and variant bases are different

   datamodel = SQLAInterface (models.AssocSet)

   # route to nicer url
   route_base = '/sets'

   # friendly name for columns
   label_columns = {
      'title': 'Title',
      'description': 'Description',
   }

   ## Listing / showing
   # what columns appear in a table/list & the order
   list_columns = ['title']
   base_order = ('created_on','asc')

   ## Adding / editing
   # what columns are visible in add/edit
   add_columns = SET_COLS
   edit_columns = SET_COLS



## ASSOCIATION SETS

SET_COLS = [
   'title',
   'description',
]

class NewsModelView (ModelView):
   """
   Newsitems & updates.
   """

   datamodel = SQLAInterface (models.News)

   # route to nicer url
   route_base = '/news'

   # friendly name for columns
   label_columns = {
      'title': 'Title',
      'description': 'Description',
   }

   ## Listing / showing
   # what columns appear in a table/list & the order
   list_columns = ['title']
   base_order = ('title','asc')

   ## Adding / editing
   # what columns are visible in add/edit
   #add_columns = SET_COLS
   #edit_columns = SET_COLS



## Registration and coordination
# create and register everything
db.create_all()

appbuilder.add_view (AssociationModelView, "Associations", icon="fa-file-o")
appbuilder.add_view (SetModelView, "Sets", icon="folder-open-o")
appbuilder.add_view (NewsModelView, "News", icon="newspaper-o")

# fa-exchange

### END ###
