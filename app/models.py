

### IMPORTS

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column, Integer, String, Enum, Float
from sqlalchemy import UniqueConstraint

from . import consts


### CODE ###

def gen_assoc_id (context):
   return "%s.%s" % (context.current_parameters['snp_id'],
      context.current_parameters['cpg_id'])


class Association (AuditMixin, Model):
   """
   A SNP and methylation pairing with statistical support.
   """

   __tablename__ = 'associations'

   ## Properties:
   id = Column (String (48), primary_key=True, default=gen_assoc_id)

   snp_id = Column (String (16), nullable=False)
   snp_locn_chr = Column (Enum (consts.Chromosome), nullable=False)
   snp_locn_posn = Column (Integer, nullable=False)
   snp_base_wild = Column (String (1), nullable=False)
   snp_base_var = Column (String (1), nullable=False)

   cpg_id = Column (String (16), nullable=False)
   cpg_locn_chr = Column (Enum (consts.Chromosome), nullable=False)
   cpg_locn_posn = Column (Integer, nullable=False)

   stat_beta = Column (Float)
   stat_stderr = Column (Float)
   stat_pval = Column (Float)

   def __repr__(self):
     return self.id


### END ###
