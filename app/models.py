

### IMPORTS

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Table, ForeignKey, Column, Integer, String, Enum, Float
from sqlalchemy.orm import relationship

#from sqlalchemy import UniqueConstraint

from . import consts


### CODE ###

## Linkintg table for assictaion sets
set_membership_table = Table ('set_membership', Model.metadata,
   Column ('id', Integer, primary_key=True),
   Column ('assoc_id', String(48), ForeignKey ('associations.id')),
   Column ('set_id', Integer, ForeignKey ('sets.id'))
)

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
   snp_locn_chr = Column (Enum (*consts.chromosomes), nullable=False)
   snp_locn_posn = Column (Integer, nullable=False)

   snp_base_wild = Column (String (1), nullable=False)
   snp_base_var = Column (String (1), nullable=False)

   cpg_id = Column (String (16), nullable=False)
   cpg_locn_chr = Column (Enum (*consts.chromosomes), nullable=False)
   cpg_locn_posn = Column (Integer, nullable=False)

   stat_beta = Column (Float)
   stat_stderr = Column (Float)
   stat_pval = Column (Float)

   sets = relationship ('AssocSet', secondary=set_membership_table, backref='association')

   def __repr__(self):
     return self.id



class AssocSet (AuditMixin, Model):
   """
   A group of associations.
   """

   __tablename__ = 'sets'

   ## Properties:
   id = Column (Integer, autoincrement=True, primary_key=True)

   title = Column (String (64), nullable=False)
   description = Column (String())

   def __repr__(self):
     return self.id


### END ###
