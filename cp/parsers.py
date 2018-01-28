import fnmatch, functools, re
from collections import OrderedDict
from itertools import zip_longest

from listorm import Listorm
from dateutil.parser import parse

METHODS_INTERFACES = {

	'SetInputValue': {
		'code': {
			'position': 0,
			'type': ['str'],
			'essential': True,
		},
	},
	'GetHeaderValue': {
		'type': {
			'position': 0,
			'type': ['long'],
			'essential': True,
			'options': {
				0: 'rows',
			},
		}
	},
	'GetDataValue': {
		'type': {
			'position': 0,
			'type': ['str'],
			'essential': True,
			'options': {
				0 : "종목코드",
				1 : "종목명",
				2 : "대비",
				3 : "대비구분코드",
				4 : "현재가",
				5 : "매도호가",
				6 : "매수호가",
				7 : "거래량",
				8 : "장구분플래그",
				9 : "예상체결가",
				10: "예상체결가전일대비",
				11: "예상체결수량",
			}
		},
		'index': {
			'position': 1,
			'type': ['long'],
			'essential': True,
		},
	},	
}


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
			return ord(str(value))
		elif 'str' in dtypes:
			return str(value)

	def _normalize_dtypes(self, dtypes, values):
		if any(t.endswith('[]') for t in dtypes):
			if not isinstance(value, (list, tuple, set)):
				values = [values]
			return tuple(self._norm_dtype(dtypes, v) for v in values)
		else:
			return self._norm_dtype(values)

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

	def encode_field_options(self, method, option='type', fields=None, indexing=False):
		fields_mapping = self._get_option_fields(method, option)
		fields = self._fnmatch_fields(fields_mapping, fields)
		ret = []
		for i, f in enumerate(fields):
			val = fields_mapping[f]
			if indexing == True:
				ret.append((i, val))
			else:
				ret.append(val)
		return tuple(ret)
			
	def decode_arg_options(self, method, options='type', args=None):
		args = args or []
		if isinstance(args, str):
			args = [args]
		m = self._get_option_fields(method, options)
		rev = {val: key for key, val in m.items()}
		fields = []
		for a in args:
			if isinstance(a, (list, tuple, set)) and len(a) == 2:
				a = a[1]
			f = rev[a]
			if f not in fields:
				fields.append(f)
		return fields


ip = InterfaceParser(METHODS_INTERFACES)

r = ip.encode_field_options('GetDataValue', 'type', ['종목명', '매*', '*코드'])
print(r)
d = ip.decode_arg_options('GetDataValue', args=r)
print(d)

