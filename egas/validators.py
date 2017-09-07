"""
Custom validators for the app.
"""

### IMPORTS

from wtforms import validators as wtfval

__all__ = (
	'NotEqualTo',
	'GreaterThan',
	'PositiveNumber',
)


### CONSTS & DEFINES

### CODE ###

class NotEqualTo (object):
	"""
	Compares the values of two fields.

	:param fieldname:
		The name of the other field to compare to.
	:param message:
		Error message to raise in case of a validation error.

   This is copied blantantly from the wtforms EqualTo example.

	"""
	def __init__(self, fieldname, message=None):
		self.fieldname = fieldname
		self.message = message

	def __call__(self, form, field):
		try:
			other = form[self.fieldname]
		except KeyError:
			raise wtfval.ValidationError (field.gettext
				("Invalid field name '%s'.") % self.fieldname)
		if field.data == other.data:
			d = {
				'other_label': hasattr(other, 'label') and
					other.label.text or self.fieldname,
				'other_name': self.fieldname
			}
			message = self.message
			if message is None:
				message = field.gettext (
					'Field must not be equal to %(other_name)s.')

			raise wtfval.ValidationError (message % d)


class GreaterThan (object):
	"""
	Check that a field is greater than a given value.

	:param lower_bound:
		The value to be greater than.
	:param message:
		Error message to raise in case of a validation error.

   Not necessarily just for numbers.

	"""
	def __init__(self, lower_bound, message=None):
		self.lower_bound = lower_bound
		self.message = message

	def __call__(self, form, field):
		data == field.data
		# XXX: how to handle None / no data, how's this combine
		# with the required?
		if (data is not None) and (self.lower_bound is not None):
			# we have the data to test
			if (data <= self.lower_bound):
				# there's a problem
				d = {
					'lower_bound': self.Lower_bound,
				}
				message = self.message
				if message is None:
					message = field.gettext (
						'Field must be greater than %(lower_bound)s.')
				raise wtfval.ValidationError (message % d)


class PositiveNumber (GreaterThan):
	"""
	Check that a field is a positive number.

	:param message:
		Error message to raise in case of a validation error.

   Just uses the GreaterThan machinery.

	"""
	def __init__(self, message=None):
		if not message:
			message = "Field should be a positive number"
		super (PositiveNumber, self).__init__(lower_bound=0,
			message=message)




### END ###
