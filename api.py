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




from listorm import Listorm
from fnmatch import fnmatch
from collections import OrderedDict
from itertools import zip_longest
from win32com.client import Dispatch

class InterfaceParser:

	def __init__(self, module_name, interface):
		records = self._flatten_interface(interface)		
		self.lst = Listorm(records)
		self.cp = Dispatch(module_name)
		
	def _flatten_interface(self, interface, levelnames=['method', 'arg', 'prop', 'value', 'options']):
		from itertools import zip_longest
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
		return [dict(zip_longest(levelnames, r)) for r in dictraversal(interface)]

	def encode_fields(self, method, fields, arg='type'):
		context = self.lst.filter(lambda row: row.options and row.method==method and arg==arg)
		if not context:
			raise ValueError('No options fields in {} on {}'.format(arg, method))
		matches = []
		headers = []

		for pat in fields:
			for row in context:
				opt = row.options
				if opt in matches:
					continue
				if fnmatch(opt, pat):
					matches.append(row.value)
					headers.append(row.options)
		return matches

	def decode_fields(self, method, raw_fields, arg='type'):
		context = self.lst.filter(lambda row: row.options and row.method==method and arg==arg)
		if not context:
			raise ValueError('No options fields in {} on {}'.format(arg, method))
		columns = context.filter(lambda row: row.value in raw_fields).column_values('options')
		columns = []

		for raw in raw_fields:
			r = context.filterand(value=raw)
			if r:
				columns.append(r.first.options)
		return columns

	def assign_args(self, method, *args):
		func = getattr(self.cp, method)
		for arg in args:
			if isinstance(arg, (int, str, bytes)):
				arg = (arg, )
			func(*arg)
		return obj

	def retrieve_args(self, method, *args):
		func = getattr(self.cp, method)
		record = {}
		for arg in args:
			if isinstance(arg, (int, str, bytes)):
				arg = (arg, )
				ret = func(*arg)
				record[arg[0]] = ret
		return record

ip = InterfaceParser(METHODS_INTERFACES)

ip.assign_args('SetInputValue', 'A003540')
