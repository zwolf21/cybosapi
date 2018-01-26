import win32com.client

from ..utils import *



DESCRIPTION = {
	'summary': '주식 현재가 관련데이터 7021',
	'point': '''

	-종목에 대한 가장 전반적인 정보를 담고 있는 화면으로.. 
	-해당 종목이 정상인지 관리나 위험 등의 종목인지 판단하고, 
		       몇 가지의 재무정보를 받기에 유용한 api로 생각됨.
		
StockMst.SetInputValue(0,value)
->0(string), 종목 코드

value = StockMst.GetHeaderValue(type)

type 설명

25.신용시장: 대략 개인들이 신용으로 전체시장에서 얼마나 돈을 빌려 거래했는지 파악. 
27.basis price: 보통 일반적인 기준가는 전일 종가를 의미함. 전일대비 파악용.
28.PER: 통상적인 중요 재무지표. 주가수익비율
31.상장주식수: 보통 유동주식수를 파악하기 위한 용도로 많이 씀. 
32.상장자본금: 재무비율을 구하기 위한 수단으로 사용. 
33~40 외국인 정보는 필요하지 않다고 봄. 
 실제 외국인 보유량이나 거래량이 아닌.. 시장에서 정한 외국인 소유한도량 데이터들임. 
 경험상 외국인 주식취득의 점진적 증가나 감소 추이 파악 정도만 유용.
43.매매수량단위: 가격대별 매매 수량단위 
44.~~ 정상 종목인지 여부만 판단하면 됨.  
53.KOSPI200 채용 여부는. 시장의 대형우량주 지수에 편입된 종목 파악. 
 기관중 연기금이나 투신의 상품팀, 외인들은 KOSPI200 종목들을 사서 
 그 포트폴리오가  KSOPI200을 추종하도록 하는 매매전략을 많이 구사. 
 따라서 KOSPI200을 구성하는 종목의 급격한 하락 이탈은 관찰되야 함. 저렴한 구매기회.  
54.액면가는 주식의 원래 발행가격으로 재무 비교 데이터로 사용. 
55~ 58. 예상 관련 데이터는 불필요. 
60~61 자사주 매수는  자기주식을 회사가 취득하는 것으로 신고사항임.
 시장에 긍정적임. 그러나 해당기간동안 다 사지 않고 기간연장도 많음. 
 자사주 매수 신청이  있는지. 그 금액이 아주큰지  참고만 하는게 좋음. 
62.63. 외국인 매수도 총합은 시장의 주포인 외국인들의 해당종목 참여 여부 판단.    
64.신용잔고비율. 보통 개인들이 얼마나 해당종목에 따라 붙었는지 판단하는 요소.
 신용 많으면 못 간다는 속설이 있지만 절대적 요소 아님. 가면 갈 뿐..  
 그러나 경험상, 신용이 0 근처로 떨어진 후 크게 상승했던 종목들 종종  많음.
 (이러한 현상을 개미들 다 털고 간다고 말하기도 함) 
65.CB는 서킷브레이크 발동 여부  
1단계 종합주가지수가 전일에 비해 8% 이상 하락한 경우 발동. 2,3단계는 생략. 
이런 일은 경험상 5년에 한 번 정도 일어날까 말까임.  
불난 집 장사 잘 되다는 속설처럼.. 개인적으로 시장의 장기적 안목에서는 호재로 봄.. 
66~68은 정상종목, 정상, 정상종목 이어야 하는 판단 자료로 활용. 
70.BPS***는 중요한 정보로 생각함. 주당 장부가치로 주가와 비교할 수 있음. 

 ''',

'default': [
		'종목코드', '종목명', '전일대비', '현재가', '시가', '고가', '누적거래량'
		,'누적거래량', '누적거래대금', 'EPS', '신용시장', '신용잔고비율','PER', '정상', 'KOSPI200'
		,'자사주 신청 수량','거래원 외국계매도총합', '거래원 외국계매수총합', 'BPS'
	]

    
	
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
	fields = expand_field_fnmatch(METHODS_INTERFACES, 'GetHeaderValue', fields)
	for colnm in fields:
		arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type=colnm)
		value = cp.GetHeaderValue(arg)
		ext[colnm] = value
	return ext
