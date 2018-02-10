from cp.core.cporm import Cporm


DESCRIPTION = {
	'summary': '복수 종목 일괄조회 7059',
	'point': '''
		StockMst 모듈이 하는 일을 복수종목에 한해서 수행한다. (최대,110종목)
		또 다른 점은 StockMst 모듈이 호출하는 type들에 비해 type이 제한적이다. 

	StockMst2.SetInputValue(0,value)
	->0(string), 종목 코드(구분자:',' , MAX: 110종목) 예) 

value = StockMst2.GetHeaderValue(type)

type 설명(StockMst에 없는 정보)

 18.외국인보유비율: StockMst없는 정보로 실제 매매로 인한 보유인지 확인 필요. 
            증감은 나름중요정보임.
 21.체결강도는 보통 (매수체결량 / 매도체결량) X 100 인데, 너무 올드한 방법임
   나름의 체결강도를 측정하는 것은 나름 중요한 시장정보라 오랫동안, 모든 시스템트레이딩
   집단이 각종 물리법칙을 동원해 심혈을 기울인 분야임.
   사이언스 테크놀러지는 HMM이론과 로켓사이언스로 이를 행했다고 알려짐. 
   과거에 스터디에서  이를 테스트해본 결과 2009년 임.
   당시로서는 이미 효율적이 되서 HMM 이나 로켓사이언스로는 시장에서 수익내기 어려웠음.    
   2010년경 국내 한 시스테머가 열역학을 이용한 체결강도로 큰 수익 내고 은퇴한다고 인증해서 인구에 회자됨. 

   ''',
	'default': [
		'종목코드', '종목명', '전일대비', '현재가', '시가', '고가', '거래량','거래대금'
		, '외국인보유비율','체결강도'
	]

}


MODULE_NAME = 'dscbo1.StockMst2'

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
				0: 'count',
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
				2 : "시간",
				3 : "현재가",
				4 : "전일대비",
				5 : "상태구분",
				6 : "시가",
				7 : "고가",
				8 : "저가",
				9 : "매도호가",
				10: "매수호가",
				11: "거래량단위1주",
				12: "거래대금단위천원",
				13: "총매도잔량",
				14: "총매수잔량",
				15: "매도잔량",
				16: "매수잔량",
				17: "상장주식수",
				18: "외국인보유비율%",
				19: "전일종가",
				20: "전일거래량",
				21: "체결강도",
				22: "순간체결량",
				23: "체결가비교Flag",
				24: "호가비교Flag",
				25: "동시호가구분",
				26: "예상체결가",
				27: "예상체결가전일대비",
				28: "예상체결가상태구분",
				29: "예상체결가거래량",
			}
		},
		'index': {
			'position': 1,
			'type': ['long'],
			'essential': True,
		},
	},	
}

TRAN_TAB = {
	"상태구분": {
		ord('1'): "상한",
		ord('2'): "상승",
		ord('3'): "보합",
		ord('4'): "하한",
		ord('5'): "하락",
		ord('6'): "기세상한",
		ord('7'): "기세상승",
		ord('8'): "기세하한",
		ord('9'): "기세하락",
	},
	"체결가비교Flag":{
		ord('O'): "매도",
		ord('B'): "매수",
	},
	"호가비교Flag": {
		ord('O'): "매도",
		ord('B'): "매수",		
	},
	"동시호가구분": {
		ord('1'): "동시호가",
		ord('2'): "장중",
	},
	"예상체결가상태구분": {
		ord('1'): "상한",
		ord('2'): "상승",
		ord('3'): "보합",
		ord('4'): "하한",
		ord('5'): "하락",
		ord('6'): "기세상한",
		ord('7'): "기세상승",
		ord('8'): "기세하한",
		ord('9'): "기세하락",		
	},
}


@Cporm.translate(TRAN_TAB)
def get_stockmst2(codes, fields):
	if not isinstance(codes, str):
		codes = ','.join(codes)
	crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
	crm.set_inputvalues(code=codes)
	crm.blockrequest()
	ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
	return crm.get_datavalue_table(ordered_fields)




