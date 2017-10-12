"""
Application-wide constants.

"""

### IMPORTS

import enum


### CONSTANTS & DEFINES

chromosomes = (
   "1",
   "2",
   "3",
   "4",
   "5",
   "6",
   "7",
   "8",
   "9",
   "10",
   "11",
   "12",
   "13",
   "14",
   "15",
   "16",
   "17",
   "18",
   "19",
   "20",
   "21",
   "22",
   "X",
   "Y",
)

bases = (
   'A',
   'C',
   'G',
   'T', # OR U?
   'R', # A or G
   'Y', # C or T
   'S', # G or C
   'W', # A or T
   'K', # G or T
   'M', # A or C
   'B', # C or G or T
   'D', # A or G or T
   'H', # A or C or T
   'V', # A or C or G
   # 'N',
)

INDATA_FLDS = (
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

### END ###
