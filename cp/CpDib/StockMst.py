import win32com.client

from ..utils import *

DESCRIPTION = {
	'summary': '주식 현재가 관련데이터 7021',
	'point': '''
		
StockMst.SetInputValue(0,value)
->0(string), 종목 코드

value = StockMst.GetHeaderValue(type)

0 - (string) 종목 코드 *****

1 - (string) 종목 명 *****

2 - (string) 대신 업종코드 ***

3 - (string) 그룹 코드

4 - (short) 시간 **

5 - (string) 소속 구분(문자열) **

6 - (string) 대형,중형,소형

7 - 사용하지 않음

8 - (long) 상한가

9- (long) 하한가

10 - (long) 전일종가 *****

11 - (long) 현재가 *****

12 - (long) 전일대비***

13 - (long) 시가 *****

14 - (long) 고가 *****

15 - (long) 저가 *****

16 - (long) 매도호가 ***

17 - (long) 매수호가 ***

18 - (long) 누적거래량 [주의] 기준 단위를 확인하세요 *****

시장구분
 기준 단위
 
거래소,코스닥
 단주 1
 
거래소 지수
 천주 1000
 
코스닥 지수 
 단주 1
 

19 - (long) 누적거래대금 [주의] 기준 단위를 확인하세요

거래소
 만원 10000
 
코스닥
 천원 1000
 
거래소 지수, 코스닥 지수
 백만원 1000000
 
20 - (long) EPS 주당순익  ***

21 - (long) 신고가 **

22 - (long) 신고가일 **

23 - (long) 신저가 **

24 - (long) 신저가일 **

25 - (short) 신용시장(전체) *

26 - (short) 결산월

27 - (long) basis price (기준가) **

28 - (float) PER 주가수익비율 ***

31 - (decimal) 상장주식수 [주의] 기준 단위를 확인하세요  **

32 - (long) 상장자본금 **

33 - (long) 외국인 DATA 일자

34 - (short) 외국인 TIME 일자

35 - (decimal) 외국인 상장주식수

36 - (decimal) 외국인 주문주식수

37 - (long) 외국인 한도수량

38 - (float) 외국인 한도비율

39 - (decimal) 외국인 주문가능수량

40 - (float) 외국인 주문가능비율

42 - (string) 증권 전산 업종코드

43 - (short) 매매 수량 단위 **

44 - (char) 정상/이상급등/관리/거래 정지 등등 구분(코드) 

이 구분값 대신에 66, 67, 68번 구분값을 조합해서 사용하시기 바랍니다.


45 - (char) 소속 구분(코드)

코드
 내용 ---거래소와 코스닥만...
 
'1'
 거래소
 
'4'
 증권투자
 
'5'
 코스닥
 
'6'
 프리보드
 
'7'
 리츠
 

46 - (long) 전일 거래량

시장구분
 기준 단위
 
거래소,코스닥
 단주 1
 
거래소지수
 천주 1000
 
코스닥지수
 단주 1
 

47 - (long) 52주 최고가 **

48 - (long) 52주 최고일 **

49 - (long) 52주 최저가 **

50 - (long) 52주 최저일 **

51 - 지원하지 않음

52 - (string) 벤처기업 구분

코스닥
 일반기업/벤처기업
 

53 - (string) KOSPI200 채용 여부
 
거래소
 미채용/건설기계/조선운송/철강소재/에너지화학/정보통신/금융/필수소비재/자유소비재
 

54 - (short) 액면가 **

예상체결 관련 항목들  제외 
 

60 - (char) 자사주 신청여부 **

'1' 신청/ '0' 미신청
 

61 - (long) 자사주 신청 수량 *

62 - (long) 거래원 외국계매도총합 ***

63 - (long) 거래원 외국계매수총합 ***

64 - (float) 신용잔고비율 **

65 - (char) CB여부  - 전환사채  *
 
'0'
 초기
 
'1'
 CB발동
 
'2'
 CB해제
 

66 - (char) 관리구분 ***

'Y' 관리종목 / 'N' 정상종목
 

67 -(char)투자경고구분 ***

'1'  정상 / '2' 주의/ '3' 경고 '4' 위험예고/'5' 위험
 

68 -(char)거래정지구분 **
 
 'Y' 거래정지종목 /'N' 정상종목
 
69 -(char) 불성실 공시구분

 '0'  정상 / '1' 불성실 공시
 
70 - (long) BPS 주당순자산 ***

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
