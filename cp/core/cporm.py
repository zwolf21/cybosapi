import win32com.client

from .apiparser import InterfaceParser

class Cporm:

	def __init__(self, module_name, interface):
		self.cp = win32com.client.Dispatch(module_name)
		self.ip = InterfaceParser(interface)

	def set_inputvalues(self, **kwargs):
		argset = self.ip.gen_args('SetInputValue', **kwargs)
		for args in argset:
			self.cp.SetInputValue(*args)

	def get_ordered_fields(self, method, option='field', **kwargs):
		fields = kwargs.get('fields') or kwargs.get('field')
		if fields:
			raw_fields = self.ip.encode_field_options(method, option=option, fields=fields)
			return self.ip.decode_arg_options(method, option=option, args=raw_fields)
		else:
			raise ValueError('fields or field argument needed')

	def get_headervalues(self, fields):
		args = self.ip.encode_field_options('GetHeaderValue', option='type', fields=fields, indexing=False)
		fields = self.ip.decode_arg_options('GetHeaderValue', option='type', args=args)
		ext = {}
		for arg, f in zip(args, fields):
			ext[f] = self.cp.GetHeaderValue(arg)
		return ext

	def get_rows_count(self):
		arg = self.ip.get_headervalue_nrow_arg()
		if arg is not None:
			return self.cp.GetHeaderValue(arg)

	def get_columns_count(self):
		arg = self.ip.get_headervalue_ncolumn_arg()
		if arg is not None:
			return self.cp.GetHeaderValue(arg)

	def get_datavalue_table(self, ordered_fields):
		nrows = self.get_rows_count()
		ncols = self.get_columns_count()
		records = []
		if ncols is None:
			coliter = self.ip.encode_field_options('GetDataValue',
				option='type', fields=ordered_fields, indexing=False
			)
		else:
			coliter = range(ncols)
		for r in range(nrows):
			values = []
			for c in coliter:
				value = self.cp.GetDataValue(c, r)
				values.append(value)
			row = dict(zip(ordered_fields, values))
			records.append(row)
		return records


	def blockrequest(self):
		self.cp.BlockRequest()

	def subscribe(self):
		self.cp.Subscribe()
