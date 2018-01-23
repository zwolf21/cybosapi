import win32com.client

from ..utils import *

DESCRIPTION = {
	'summary': '',
	'point': '''
		
	'''
}


MODULE_NAME = 'dscbo1.StockMstM'

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



def get_stockmstm(code, fields):
	cp = win32com.client.Dispatch(MODULE_NAME)
	setinputvalue_argset = encode_args(METHODS_INTERFACES, 'SetInputValue', code=code)
	cp = set_inputvalue(cp, setinputvalue_argset)
	nrows_arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type='rows')
	nrows = cp.GetHeaderValue(nrows_arg)

	records = []
	for r in range(nrows):
		row = {}
		for colnm in fields:
			args = encode_args(METHODS_INTERFACES, 'GetDataValue', indexed=False, flated=True, type=colnm, index=r)
			data = cp.GetDataValue(*args)
			row[colnm] = data
		records.append(row)
	return records

