"""
Read in and validate associations.
"""

### IMPORTS

import csv
import re


### CONSTANTS & DEFINES

FIRST_CAP_RE = re.compile ('(.)([A-Z][a-z]+)')
OTHER_CAP_RE = re.compile ('([a-z0-9])([A-Z])')
UNDERSCORE_RE = re.compile ('_+')

DATA_FLD_NAMES = (
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
)

### CODE ###


def camel_to_snakecase (name):
   s1 = FIRST_CAP_RE.sub (r'\1_\2', name)
   return OTHER_CAP_RE.sub (r'\1_\2', s1).lower()
    

class AssocReader (csv.DictReader):
   def __init__ (self, hndl):
      super().__init__ (hndl)
      # super(self.__class__, self).__init__()
      self.csv_rdr = csv.DictReader (hndl)

   @property
   def fieldnames (self):
      if self._fieldnames is None:
         try:
            tmp_fieldnames = next (self.reader)
            san_fieldnames = self.sanitize_fieldnames (tmp_fieldnames)
            self.check_fieldnames (san_fieldnames)
            self._fieldnames = san_fieldnames
         except StopIteration:
            pass
      self.line_num = self.reader.line_num
      return self._fieldnames
     
   def sanitize_fieldnames (self, fld_names):
      fld_names = [s.strip() for s in fld_names]
      fld_names = [s.replace (' ', '_') for s in fld_names]
      fld_names = [s.replace ('.', '_') for s in fld_names]
      # fld_names = [camel_to_snakecase (s) for s in fld_names]
      fld_names = [UNDERSCORE_RE.sub (r'_', s) for s in fld_names]
      fld_names = [s.lower() for s in fld_names]
      fld_names = [s.strip() for s in fld_names]
      return fld_names

   def check_fieldnames (self, fld_names):
      for f in DATA_FLD_NAMES:
         assert f in fld_names, \
            "required field '%s' missing from input fields" % f

   

### END ###
