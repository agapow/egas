"""
Some useful mixins.
"""

### IMPORTS

import datetime
import logging

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import sqlalchemy.types as types
from sqlalchemy.ext.declarative import declared_attr


### CONSTANTS & DEFINES

### CODE ###

class AuditMixin(object):
    """
    The supplied Audit mixin doesn't work
    """
    created_on = Column(DateTime, default=datetime.datetime.now, nullable=False)
    changed_on = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now, nullable=False)

### END ###
