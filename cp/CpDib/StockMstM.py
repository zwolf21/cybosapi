from ..core.cporm import Cporm

DESCRIPTION = {

	'summary': '복수 종목 조회 7059',

	'point': '''
		주식 복수 종목에 대해 간단한 내용을 일괄 조회 요청하고 수신
	    Mst 모듈이  한종목의 다양한 정보라면, MstM은 복수종목의 간략정보

    통신종류 
		 Request/Reply
 
	MstM.SetInputValue(type,value)
		0 - (string) 다수의 종목코드
			ex) A003540A000060A000010 (MAX:110개)
	''',

	 'default': [
		'종목코드', '종목명', '대비', '현재가', '매도호가','매수호가'
	],
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
			'type': ['long'],
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


TRANTAB = {
	"대비구분코드": {
		1 : "상한",
		2 : "상승",
		3 : "보합",
		4 : "하한",
		5 : "하락",
		6 : "기세상한",
		7 : "기세상승",
		8 : "기세하한",
		9 : "기세하락",
	},
	"장구분플래그": {
		ord('0'): "동시호가와장중이외의시간",
		ord('1'): "동시호가시간",
		ord('2'): "장중",
	},

}

@Cporm.translate(TRANTAB)
def get_stockmstm(codes, fields=DESCRIPTION['default']):
	'''주식 복수 종목에 대해 간단한 내용을 일괄 조회
		records = get_stockmstm(
		    codes=['A003540','A000060','A000010'],
		    fields = [
		        '종목코드', '종목명', '대비', '대비구분코드', '현재가', '매도호가', '매수호가', '거래량', '장구분플래그', '예상*'
		    ]
		)
	'''
	if isinstance(codes, (list, tuple, set)):
		codes = ''.join(codes)
	crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
	crm.set_inputvalues(code=codes)
	crm.blockrequest()
	ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
	records = crm.get_datavalue_table(ordered_fields)
	return records