import win32com.client

from ..utils import *


DESCRIPTION = {
	'com_type': 'Request/Reply',
	'summary': '주식 업종 차트데이터 수신 7400',
	'point': '''

-과거데이터를 수신하는 가장 일반적인 모듈. 틱, 일, 주 월, 년 단위. 수정주가로만..
 기본 가격 데이터 외에,  기관 외국인의 순매수는 그  추이를 파악하는 데 아주 중요 *****

통신종류 
 Request/Reply
 

StockChart.SetInputValue(type,value)

type

type5의 필드값 

13.시가총액: 적정 시총인지는 영업익 등과 비교할 수 있는 지표  
16.외국인 정보는 단순 거래소 규정 사항인지 실제 보유인지 확인 필요. 
18.수정주가일자: 주가의 보정이 발생한 날짜. 예를 들면 감자, 액면분할 등.
22.기관누적순매수: 추이는 매우 중요한 정보임
22.23 등락주선 등락비율 은.. 상승하락 종목수 비율등을 나타내지만 유용성 없음
24. 예탁금은 전체 시장 자금유입  상홤 보여줌
25.주식회전율: 종목들의 거래 활발함 나타냄. 대략 거래량을 상장주식로 나눠 비율화 

value = StockChart.GetHeaderValue(type) 
type값 정보 
기존 정형화된 가격정보 

	'''
	
	'default': [
		'날짜', '종목코드','종목상태','시가', '고가', '저가', '종가', '전일대비','대비부호','거래량','거래대금','거래대금','누적체결매도수량'
        ,'누적체결매수수량','시가총액',	'외국인현보유비율','기관누적순매수','기관순매수','주식회전율'
        

	]
}

MODULE_NAME = 'CpSysDib.StockChart'

METHODS_INTERFACES = {

	'SetInputValue': {
		'code': {
			'position': 0,
			'type': ['str'],
			'essential': True,
		},
		'reqgb': {
			'position':1,
			'type': ['char'],
			'essential': True,
			'options': {
				ord('1'): '기간',
				ord('2'): '개수',
			},
			'default': ord('2'),
		},
		'end_date': {
			'position': 2,
			'type': ['str'],
			'essential': False,
		},
		'start_date': {
			'position': 3,
			'type': ['str'],
			'essential': False,
		},
		'count': {
			'position': 4,
			'type': ['long'],
			'essential': True,
			'default': 10,
		},
		'field': {
			'position': 5,
			'type': ['long[]', 'long'],
			'essential': True,
			'options': 	{
					0: "날짜",
					1: "시간",
					2: "시가", # 필수 
					3: "고가",
					4: "저가",
					5: "종가",
					6: "전일대비",
					8: "거래량",
					9: "거래대금", 
					10: "누적체결매도수량",
					11: "누적체결매수수량",
					12: "상장주식수",
					13: "시가총액",
					14: "외국인주문한도수량",
					15: "외국인주문가능수량",
					16: "외국인현보유수량",
					17: "외국인현보유비율",
					18: "수정주가일자",
					19: "수정주가비율",
					20: "기관순매수",
					21: "기관누적순매수",
					22: "등락주선",
					23: "등락비율",
					24: "예탁금",
					25: "주식회전율",
					26: "거래성립률",
					37: "대비부호",
				},
			'default': (0, 2, 3, 4, 5, 8),
		},
		'chart': {
			'position': 6,
			'type': ['char'],
			'essential': True,
			'options': {
				ord('D'): '일',
				ord('W'): '주',
				ord('M'): '월',
				ord('m'): '분',
				ord('T'): '틱',
			},
			'default': ord('D')
		},
		'period': {
			'position': 7,
			'type': ['long'],
			'essential': False,
			'default': 1
		},
		'geprevision': {
			'position': 8,
			'type': ['char'],
			'essential': False,
			'options': {
				ord('0'): '갭무보정',
				ord('1'): '갭보정',
			},
			'default': ord('0')
		},
		'stockadj': {
			'position': 9,
			'type': ['char'],
			'essential': False,
			'options': {
				ord('0'): '무수정',
				ord('1'): '수정',
			},
			'default': ord('0'),
		},
		'stockamt': {
			'position': 10,
			'type': ['char'],
			'essential': False,
			'options': {
				ord('1'): '시간외거래량모두',
				ord('2'): '장종료시간외거래량만',
				ord('3'): '시간외거래량제외',
				ord('4'): '장전시간외거래량만',
			},
			'default': ord('1')
		},
	},
	'GetHeaderValue': {
		'type': {
			'position': 0,
			'type': ['long'],
			'essential': True,
			'options': {
				0: 'code',
				1: 'columns',
				2: 'fields',
				3: 'rows',
				4: 'last_bartick',
				5: 'recent',
				6: 'yesterday',
				7: 'current',
				8: 'signal',
				9: '대비',
				10: 'amount',
				11: '매도호가',
				12: '매수호가',
				13: '시가',
				14: '고가',
				15: '저가',
				16: '거래대금',
				17: '종목상태',
				18: '상장주식수',
				19: '자본금백만',
				20: '전일거래량',
				21: '최근갱신시간',
				22: '상한가',
				23: '하한가',
			}
		},
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


def get_stockchart(extras=None, **kwargs):
	setinputvalue_argset = encode_args(METHODS_INTERFACES, 'SetInputValue', **kwargs)
	cp = win32com.client.Dispatch(MODULE_NAME)
	cp = set_inputvalue(cp, setinputvalue_argset)
	records =  output_to_records(METHODS_INTERFACES, cp, setinputvalue_argset)
	if extras:
		ext = {}
		for colnm in extras:
			arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type=colnm)
			value = cp.GetHeaderValue(arg)
			ext[colnm] = value
		for row in records:
			row.update(ext)
	return records







