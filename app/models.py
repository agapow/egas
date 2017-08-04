

### IMPORTS

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Table, ForeignKey, Column, Integer, String, Enum, Float
from sqlalchemy.orm import relationship

#from sqlalchemy import UniqueConstraint

from . import consts


### CODE ###

## Linking table between tags and associations
tag_membership_table = Table ('tag_membership', Model.metadata,
   Column ('assoc_id', String(48), ForeignKey ('associations.id')),
   Column ('tag_id', Integer, ForeignKey ('tags.id'))
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

   tags = relationship ('Tag', secondary=tag_membership_table, back_populates='associations')

   def __repr__(self):
     return self.id



class Tag (AuditMixin, Model):
   """
   A group of associations, implemented as tagging.
   """

   __tablename__ = 'tags'

   ## Properties:
   id = Column (Integer, autoincrement=True, primary_key=True)

   title = Column (String (64), nullable=False)
   description = Column (String())

   associations = relationship ('Association', secondary=tag_membership_table, back_populates='tags')

   def __repr__(self):
     return self.id


class News (AuditMixin, Model):
   """
   News items and updates for the website.
   """

   __tablename__ = 'news'

   ## Properties:
   id = Column (Integer, autoincrement=True, primary_key=True)
   title = Column (String (64), nullable=False)
   body = Column (String(), nullable=False)

   def __repr__(self):
     return self.id


### END ###
