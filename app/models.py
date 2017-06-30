"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

### IMPORTS

from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column, Integer, String, Enum, Float
from sqlalchemy import UniqueConstraint

from . import consts


### CODE ###

class Association (AuditMixin, Model):
   __tablename__ = 'associations'

   ## Properties:
   snp_id = Column (String (16), nullable=False, primary_key=True)
   
   snp_locn_chr = Column (Enum (consts.Chromosome), nullable=False)
   snp_locn_posn = Column (Integer, nullable=False)
   snp_base_wild = Column (String (1), nullable=False)
   snp_base_var = Column (String (1), nullable=False)

   cpg_id = Column (String (16), nullable=False, primary_key=True)
   cpg_locn_chr = Column (Enum (consts.Chromosome), nullable=False)
   cpg_locn_posn = Column (Integer, nullable=False)

   stat_beta = Column (Float)
   stat_stderr = Column (Float)
   stat_pval = Column (Float)

   __table_args__ = (
      UniqueConstraint ("snp_id", "cpg_id"),
   )

   def __repr__(self):
     return self.name


### END ###
