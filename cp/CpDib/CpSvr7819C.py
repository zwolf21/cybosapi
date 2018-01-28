import win32com.client

from ..utils import *

DESCRIPTION = {
	'summary': '6개월, 1년 기간 종류별 증시 자금 동향 차트 데이터 7819 ',
	'point': '''

	-시장으로 유입 유출되는 자금의 동향으로 특정 업종이나 전체시장 상황 파악에 참조.

통신종류 
	 Request/Reply
 
CpSvr7819C.SetInputValue(type,value)

0 - (char)  종류

'1' 고객예탁금: 시장 전체적인 자금유입 파악에 가장 개괄적 정보임.  
'2' 신 용 융 자: 개인들의 신용공여 형태를 볼 수 있다.
'3' 미수금잔고: 미수거래
'4' 선물예수금 : 선물시장에 자금유입. 아주 금액이 크다면 관심. 
'5' 주식형 수익증권: 주식형 운용되는 상품에 자금유입 
'6' 혼합형 수익증권 : 주식채권 상품에 자금 유입 
'7' 채권형 수익증권: 채권형 사움으로 자금 유입 여부 
'8'  MMF :단기 이자형 상품 

1 - (char) 차트 데이터 기간 구분
	'1'  6개월/ '2'  1년
 

value = CpSvr7819C.GetHeaderValue(type)
	0 - (short) 데이터 개수


value = CpSvr7819C.GetDataValue (Type,index)

0 - (long) 일자
1 - (long) 수치 
2 - (long) 전일 대비

''',
'default': [
		'일자', '수치', '고객예탁금', '신용융자', '미수금잔고', '선물예수금', '주식형 수익증권'
		,'혼합형수익증권', '채권형 수익증권', 'MMF'
	]
}

MODULE_NAME = 'dscbo1.CpSvr7819C'

METHODS_INTERFACES = {

	'SetInputValue': {
		# 'type': {
		# 	'position': 0,
		# 	'type': ['char'],
		# 	'essential': True,
		# 	'options': {
		# 	}
		# },
		'kind': {
			'position': 0,
			'type': ['char'],
			'essential': True,
			'options': {
				ord('1'): '고객예탁금',
				ord('2'): '신용융자',
				ord('3'): '미수금잔고',
				ord('4'): '선물예수금',
				ord('5'): '주식형 수익증권',
				ord('6'): '혼합형수익증권',
				ord('7'): '채권형수익증권',
				ord('8'): 'MMF',			
			},
		},
		'period': {
			'position': 1,
			'type': ['char'],
			'essential': True,
			'options': {
				ord('1'): '6개월',
				ord('2'): '1년',
			},
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
				0: '일자',
				1: '수치',
				3: '전일대비',
			},
		},
		'index': {
			'position': 1,
			'type': ['long'],
			'essential': True,
		},
	},	
}

def get_svr7819c(type=['일자', '수치', '전일대비'], **kwargs):
	setinputvalue_argset = encode_args(METHODS_INTERFACES, 'SetInputValue', **kwargs)
	cp = win32com.client.Dispatch(MODULE_NAME)
	print('args:', setinputvalue_argset)
	cp = set_inputvalue(cp, setinputvalue_argset)
	nrow_arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', type='rows', indexed=False, flated=True)
	print('nrow_arg:', nrow_arg)
	nrow = cp.GetHeaderValue(nrow_arg)
	print('nrow:', nrow)
	records = []
	for r in range(nrow):
		row = {}
		for tp in type:
			arg = encode_args(METHODS_INTERFACES, 'GetDataValue', index=r, type=tp, flated=True, indexed=False)

			# row[tp] = cp.GetDataValue(arg)
		records.append(row)
	return records

