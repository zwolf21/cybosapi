import fnmatch
from collections import OrderedDict
from itertools import zip_longest

from listorm import Listorm

def _encode_options(method_info, method_name, argname, optionvals, many=True):
	optsets = method_info[method_name][argname].get('options')
	if optsets is None:
		return optionvals
	revoptsets = {v: k for k, v in optsets.items()}

	args = []
	if many == True:
		for val in optionvals:
			if val in optsets:
				args.append(val)
			elif val in revoptsets:
				trans = revoptsets[val]
				args.append(trans)
			else:
				args+=[
					idx for opname, idx in revoptsets.items()
					if fnmatch.fnmatch(opname, val)
				]
		args = tuple(sorted((OrderedDict.fromkeys(args))))
	else:
		if isinstance(optionvals, (list, tuple, set)):
			optionvals = optionvals[0]

		if optionvals in optsets:
			args = optionvals
		elif optionvals in revoptsets:
			args = revoptsets[optionvals]
		else:
			try:
				arg, *_ = sorted(
					idx for opname, idx in revoptsets.items()
					if fnmatch.fnmatch(opname, optionvals)  and isinstance(optionvals, str)
				)
			except:
				raise ValueError('Option name mating fault: {}'.format(optionvals))
			else:
				args = arg
	return args


def encode_args(method_info, method_name, indexed=True,  flated=False, **kwargs):
	arginfo = method_info[method_name]

	encoded_args = []
	for argname, info in arginfo.items():
		pos = info['position']
		tp = info['type']
		many = any(t.endswith('[]') for t in tp)
		single = any(not t.endswith('[]') for t in tp)
		essential = info['essential']
		options = info.get('options')
		default = info.get('default')

		if argname not in kwargs:
			if essential == True and default is None:
				raise ValueError('{} is required'.format(argname))
			else:
				continue

		argval = kwargs[argname]

		if argval is None:
			if default:
				argval = default
			else:
				if essential == True:
					raise ValueError('{} is required'.format(argname))
				else:
					continue
		argval = _encode_options(method_info, method_name, argname, argval, many)

		if isinstance(argval, (str, bytes, int)):
			argcount = 1
		else:
			argcount = len(argval)

		if many == False and isinstance(argval, (list, tuple, set)):
			raise ValueError('{} is single argument, might be not in containter'.format(argval))

		tosingle = False
		if many == True:
			if single == True:
				if argcount == 1:
					tosingle = True
		else:
			tosingle = True

		if tosingle:
			if isinstance(argval, (list, tuple, set)):
				argval = argval[0]
			if 'long' in tp:
				val = int(argval)
			else:
				val = argval
			if options:
				if val not in options:
					raise ValueError('{} is invalid options value for {}'.format(argval, argname))
		else:
			if 'long' in tp:
				val = tuple(map(int, argval))
			else:
				val = tuple(argval)
			if options:
				noexists = []
				for v in val:
					if v not in options:
						noexists.append(v)
				if noexists:
					noexists = map(str, noexists)
					noexists = ', '.join((noexists))
					raise ValueError('{} are(is) invalid options value for {}'.format(noexists, argname))
		encoded_args.append((pos, val))

	if indexed:
		if flated == True and len(encoded_args) == 1:
			return encoded_args[0]
		else:
			return tuple(sorted(encoded_args))
	else:
		if flated == True and len(encoded_args) == 1:
			return encoded_args[0][1]
		return tuple(e[1] for e in sorted(encoded_args))


def set_inputvalue(cp, argset, blockrequest=True):
	for idx, arg in argset:
		cp.SetInputValue(idx, arg)
	cp.BlockRequest()
	return cp


def _decode_options(method_info, method_name, argset):
	arginfo = method_info[method_name]

	kwargset = {}
	for pos, rawarg in argset:
		for argname, info in arginfo.items():
			idx = info['position']
			if pos == idx:
				optionmap = arginfo[argname].get('options')
				if optionmap:
					if isinstance(rawarg, (list, tuple, set)):
						kwargset[argname] = tuple(optionmap[e] for e in rawarg)
					else:
						kwargset[argname] = optionmap[rawarg]
				else:
					kwargset[argname] = rawarg
	return kwargset

def output_to_records(method_info, cp, argset):
	set_inputvalue_kwargs = _decode_options(method_info, 'SetInputValue', argset)
	header = set_inputvalue_kwargs['field']
	ncols_argset = encode_args(method_info, 'GetHeaderValue', flated=True, indexed=False, type='columns')
	nrows_argset = encode_args(method_info, 'GetHeaderValue', flated=True, indexed=False, type='rows')
	ncols = cp.GetHeaderValue(ncols_argset)
	nrows = cp.GetHeaderValue(nrows_argset)
	
	records = []
	for r in range(nrows):
		row = []
		for c in range(ncols):
			getdatavalue_argset = encode_args(method_info, 'GetDataValue', indexed=False, index=r, type=c)
			data = cp.GetDataValue(*getdatavalue_argset)
			row.append(data)
		records.append(dict(zip(header, row)))
	return records




class InterfaceParser:

	def __init__(self, interface):
		records = self._flatten_interface(interface)		
		self.lst = Listorm(records)

	def _flatten_interface(self, interface, levelnames=['method', 'arg', 'prop', 'val', 'opt']):
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