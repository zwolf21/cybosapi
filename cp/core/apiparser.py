import fnmatch, functools, re
from collections import OrderedDict
from itertools import zip_longest

from listorm import Listorm
from dateutil.parser import parse


class InterfaceParser:
	levelnames = 'method', 'arg', 'prop', 'val', 'opt',

	def __init__(self, interface):
		records = self._flatten_interface(interface)		
		self.lst = Listorm(records)

	def _flatten_interface(self, interface):
		def dictraversal(d, path=None):
			path = path or []
			visited = []
			for key, val in d.items():
				if isinstance(val, dict):
					visited += dictraversal(val, path+[key])
				else:
					subpath = path + [key, val]
					visited.append(subpath)
			return visited
		return [dict(zip_longest(self.levelnames, r)) for r in dictraversal(interface)]

	def _norm_dtype(self, dtypes, value):
		if 'float' in dtypes:
			exp = str(value)
			if exp.isdigit():
				return int(value)
			else:
				return float(value)
		elif 'long' in dtypes:
			return int(str(value))
		elif 'char' in dtypes:
			return value
		elif 'str' in dtypes:
			return str(value)

	def _normalize_dtypes(self, dtypes, values):
		if any(t.endswith('[]') for t in dtypes):
			if not isinstance(values, (list, tuple, set)):
				values = [values]
			norms = tuple(self._norm_dtype(dtypes, v) for v in values)
			if len(norms) == 1:
				return norms[0]
			return norms
		else:
			return self._norm_dtype(dtypes, values)

	def _fnmatch_fields(self, fields, fnmatch_expressions):
		if isinstance(fnmatch_expressions, str):
			fnmatch_expressions = [fnmatch_expressions]
		opts = []
		for pat in fnmatch_expressions:
			for f in fields:
				if f in opts:
					continue
				if fnmatch.fnmatch(f,pat):
					opts.append(f)
		return opts

	def _get_option_fields(self, method, options='type'):
		lst = self.lst.filterand(method=method, arg=options, prop='options')
		return {row.opt: row.val for row in lst}

	def _get_arg_dtype(self, method, arg):
		lst = self.lst.filterand(method=method, arg=arg, prop='type')
		return lst.first.val

	def _get_arg_position(self, method, arg):
		lst = self.lst.filterand(method=method, arg=arg, prop='position')
		return lst.first.val

	def _get_arg_default(self, method, arg):
		lst = self.lst.filterand(method=method, arg=arg, prop='default')
		if lst.exists:
			return lst.first.val

	def get_headervalue_nrow_arg(self):
		lst = self.lst.filterand(method='GetHeaderValue', arg='type', prop='options', opt='rows')
		if  lst.exists:
			return lst.first.val
			# raise ValueError("It needs 'rows' property in GetHeaderValue options")

	def get_headervalue_ncolumn_arg(self):
		lst = self.lst.filterand(method='GetHeaderValue', arg='type', prop='options', opt='columns')
		if lst.exists:
			return lst.first.val
			# raise ValueError("It needs 'columns' property in GetHeaderValue options")

	def encode_field_options(self, method, option='type', fields=None, indexing=False):
		fields_mapping = self._get_option_fields(method, option)
		fields = self._fnmatch_fields(fields_mapping, fields)
		dtypes = self._get_arg_dtype(method, option)
		ret = []
		for i, f in enumerate(fields):
			val = fields_mapping[f]
			val = self._normalize_dtypes(dtypes, val)
			if indexing == True:
				ret.append((i, val))
			else:
				ret.append(val)
		return tuple(ret) if len(ret) > 1 else ret[0]
			
	def decode_arg_options(self, method, option='type', args=None):
		args = args or []
		if isinstance(args, str):
			args = [args]

		m = self._get_option_fields(method, option)
		rev = {val: key for key, val in m.items()}
		
		fields = []
		for a in args:
			if isinstance(a, (list, tuple, set)) and len(a) == 2:
				a = a[1]

			f = rev[a]
			if f not in fields:
				fields.append(f)

		return fields

	def gen_args(self, method, setposition=True, **kwargs):
		lst = self.lst.filterand(method=method)
		argset = []
		for argnm, value in kwargs.items():
			arglst = lst.filterand(arg=argnm)

			if not arglst.exists:
				raise ValueError("{} is not a arg in {}".format(argnm, method))

			optlst = arglst.filter(where=lambda row: row.opt)
			pos = self._get_arg_position(method, argnm)
			default = self._get_arg_default(method, argnm)
			dtypes = self._get_arg_dtype(method, argnm)
			if optlst.exists:
				value = self.encode_field_options(method, option=argnm, fields=value)
			argset.append((pos, value))

		if setposition == True:
			return tuple(argset)
		return tuple(e[1] for e in argset)