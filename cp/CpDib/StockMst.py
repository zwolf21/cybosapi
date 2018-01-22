import win32com.client

from ..utils import *

DESCRIPTION = {
	'summary': '주식 현재가 관련데이터 7021',
	'point': '''
		
	'''
}


MODULE_NAME = 'dscbo1.StockMst'

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
				0: '종목코드',
				1: '종목명',
				2: '대신업종코드',
				3: '그룹코드',
				4: '시간',
				5: '소속구분',
				6: '대중소',
				8: '상한가',
				9: '하한가',
				10: '전일종가',
				11: '현재가',
				12: '전일대비',
				13: '시가',
				14: '고가',
				15: '저가',
				16: '매도호가',
				17: '매수호가',
				18: '누적거래량',
				19: '누적거래대금',
				20: "EPS",
				21: "신고가",
				22: "신고가일",
				23: "신저가",
				24: "신저가일",
				25: "신용시장",
				26: "결산월",
				27: "기준가",
				28: "PER",
				31: "상장주식수",
				32: "상장자본금",
				33: "외국인DATA일자",
				34: "외국인TIME일자",
				35: "외국인상장주식수",
				36: "외국인주문주식수",
				37: "외국인한도수량",
				38: "외국인한도비율",
				39: "외국인주문가능수량",
				40: "외국인주문가능비율",
				42: "증권전산업종코드",
				43: "매매수량단위 ",
				45: "소속구분",
				46: "전일거래량",
				47: "52주최고가",
				48: "52주최고일",
				49: "52주최저가",
				50: "52주최저일",
				52: "벤처기업구분",
				53: "KOSPI200채용여부",
				54: "액면가",
				55: "예상체결가",
				56: "예상체결가전일대비",
				57: "예상체결수량",
				58: "예상체결가구분플래그",
				59: "장구분플래그",
				60: "자사주신청여부",
				61: "자사주신청수량",
				62: "거래원외국계매도총합",
				63: "거래원외국계매수총합",
				64: "신용잔고비율",
				65: "CB여부",
				66: "관리구분",
				67: "투자경고구분",
				68: "거래정지구분",
				69: "불성실공시구분",
				70: "BPS",
			},
		}
	},
	'GetDataValue': {
		'type': {
			'position': 0,
			'type': ['long'],
			'essential': True,
		},
		'index': {
			'position': 1,
			'type': ['long'],
			'essential': True,
		},
	},	
}



def get_stockmst(code, fields):
	cp = win32com.client.Dispatch(MODULE_NAME)
	setinputvalue_argset = encode_args(METHODS_INTERFACES, 'SetInputValue', code=code)
	cp = set_inputvalue(cp, setinputvalue_argset)
	ext = {}
	for colnm in fields:
		arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type=colnm)
		value = cp.GetHeaderValue(arg)
		ext[colnm] = value
	return ext

