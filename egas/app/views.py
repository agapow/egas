"""
Views for application models and pages.

"""

### IMPORTS

from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db

from . import models


### CONSTS & DEFINES

### CODE ###

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler (404)
def page_not_found(e):
   return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


class AssociationModelView (ModelView):
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
            'expanded':False
         }
      ),
   ]


# create and register everything
db.create_all()

appbuilder.add_view (AssociationModelView, "Association", icon="fa-folder-open-o")


### END ###
