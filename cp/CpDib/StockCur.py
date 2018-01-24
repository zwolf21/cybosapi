import win32com.client

from ..utils import *


DESCRIPTION = {
	'summary': '현재가 시간대별 체결 7021,7024',
	'point': '''
	
	- 해당 종목들의 순간체결이나 매도체결누적체결량 매도누적체결량 파악이 핵심. 
      체결량을 현재가격의 상승 하락과 비교. 상승하락이 실제 체결에 의한 것인지
       그 강도가 어느정도인지 파악 가능.  
    -과거 지수선물 단타거래에는 가장 중요한 정보값 들임   
    - 주식, 업종만 필요. 예상체결 관련, 프리보드, ELW 데이터는 불필요. 
      따라서 19 이후와 LP관련 설명 생략.

	통신종류 
 		Subscribe/Publish

	StockCur.SetInputValue(type,value)
	  0 - (string) 종목코드

	value = StockCur.GetHeaderValue(type)
	   type에 해당하는 헤더 데이터를 반환합니다
       type: 데이터 종류
     

	type 설명 
		7.8 매도수호가 -> 최우선 1매도 1매수 호가 의미
		9.누적거래량***-종목 업종의 추이. 
		10.누적거래대*** - 거래대금은 개별종목의 바닥이나 꼭지 등 시장의 판도 파악에 유용합니다.
		15.누적 매도체결수량(체결가방식)**** - 사실상 다운틱 합으로 매수체결합보다 많을시 하락에 무게.
		16.누적 매수체결수량(체결가방식)**** - 업틱체결 합으로 상승 판단 요소. 
		  *27,28의 호가방식은 실제 체결이 아닌 사자와 팔자에 대기중인 수량으로
		   데이터에 왜곡이 있는 경우가 많아 잘 쓰질 않습니다.
		17.순간체결수량 -참조로만.

	''',
	    
    'default': [
		'종목코드', '종목명', '전일대비', '시간', '시가', '고가', '저가'
		,'매도호가', '매수호가', '누적거래량', '누적거래대금', '현재가', '체결상태', '누적매도체결수량',
		'누적매수체결수량', '순간체결수량',
	]

}

MODULE_NAME = 'dscbo1.StockCur'

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
				0  : "종목코드",
				1  : "종목명",
				2  : "전일대비",
				3  : "시간",
				4  : "시가",
				5  : "고가",
				6  : "저가",
				7  : "매도호가",
				8  : "매수호가",
				9  : "누적거래량",
				10 : "누적거래대금",
				13 : "현재가",
				14 : "체결상태",
				15 : "누적매도체결수량",
				16 : "누적매수체결수량",
				17 : "순간체결수량",
				18 : "시간",
				19 : "예상체결가구분플래그",
				20 : "장구분플래그",
				21 : "장전시간외거래량",
				22 : "대비부호",
				23 : "LP보유수량",
				24 : "LP보유수량대비",
				25 : "LP보유율",
				26 : "체결상태",
				27 : "누적매도체결수량",
				28 : "누적매수체결수량",
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

def get_stockcur(code, fields = DESCRIPTION.get('default')):
	setinputvalue_argset = encode_args(METHODS_INTERFACES, 'SetInputValue', code=code) 
	cp = win32com.client.Dispatch(MODULE_NAME)
	# cp = set_inputvalue(cp, setinputvalue_argset, blockrequest=False)
	cp.SetInputValue(0, code)
	ext = {}
	for colnm in fields:
		arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type=colnm)
		print('arg:', arg)
		value = cp.GetHeaderValue(arg)
		ext[colnm] = value
	return ext

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

