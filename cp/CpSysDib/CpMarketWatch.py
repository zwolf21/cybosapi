from ..core.cporm import Cporm

DESCRIPTION = {
	'summary': '특정 주식 종목이나 주식 전 종목에 대한 특징주 포착 데이터 8092',
	'point': '''
    -궁극적 종목을 검색하는 것이 목표이나, 이미 정해놓은 종목 검색식 샘플에 해당. 
	-cci, stoc, sonar, 삼선, 일목 등 봉패턴에 의한 검색은 전부 무시하는게 좋음. 
	 과거의 패턴이 반복되지도 않으며, 주식은 굉장히 종목별로 일관성 없이 움직임. 
	-CpMaarketWatch와  CpMaarketWatchS 의 유일한 차이는 통신 방식임 

통신종류 
 	Request/Reply
 
		
CpMarketWatch.SetInputValue(0,value)
->0(string), 종목 코드. Default("*") - 전종목
  1 - 수신항목구분목록(string): 

	"12": 외국인 순매수: 리턴값이 여부인지 금액인지 확인 필요
	"13": 외국인 순매도: 리턴값이 여부인지 금액인지 확인 필요 
	"21": 전일 거래량 갱신 : 단순 갱신은 유용하지 않음. 
	"22": 최근5일 거래량최고 갱신 **(몇가지 조건식 결합 필요)
	"30": 최근5일 신저가 갱신: 패턴 검색으로 유용함 
	"42": 주가 5MA 하향 돌파
	"43": 거래량 5MA 상향 돌파
	"44": 주가 데드크로스(5MA < 20MA) :이평을 본다면 단순이평이 젤 유효 
	"45": 주가 골든크로스(5MA > 20MA)
	"81": 단기급락 후 5MA 상향돌파: 단기급락이 정의돼 있지 않아 유용하지 않으나 
	                          재정의시 아주 유용한 정보 줄 것으로 기대. 
	"82": 주가 이동평균밀집-5%이내: 방향성 생겨나기 이전으로 많이 봄
	"83": 눌림목 재 상승-20MA 지지: 눌림목이 정의왜 있지 않아 유용하지 않음. 81과 유사

value = CpMarketWatch.GetHeaderValue(type)
type: 데이터 종류
	0 - 수신항목구분목록(string)
	1 - 시작시간(short)
	2 - 수신개수(short)

value = CpMarketWatch.GetDataValue (Type,index)
	type: 데이터 종류
	0 - 시간(ushort)
	1 - 종목코드(string)
	2 - 종목명(string)
	3 - 항목구분(ushort)
	4 - 내용(string)

 ''',

'default': [
		'시간', '종목코드', '종목명', '내용', '외국인순매수', '최근5일거래량최고갱신', 
		'최근5일신저가갱신','주가5MA하향돌파', '주가데드크로스', '단기급락후5MA돌파', 
		'주가이동평균밀집','눌림목재상승'
	]

    
	
}

MODULE_NAME = 'CpSysDib.CpMarketWatch'

METHODS_INTERFACES = {

	'SetInputValue': {
		'code': {
			'position': 0,
			'type': ['str[]', 'str'],
			'essential': True,
		},
		'field': {
			'position': 1,
			'type': ['str'],
			'essential': True,
			'options': 	{
				"*": "모든항목",
				"1" : "종목뉴스",
				"2" : "공시정보",
				"10": "외국계증권사창구첫매수",
				"11": "외국계증권사창구첫매도",
				"12": "외국인순매수",
				"13": "외국인순매도",
				"21": "전일거래량갱신",
				"22": "최근5일거래량최고갱신",
				"23": "최근5일매물대돌파",
				"24": "최근60일매물대돌파",
				"28": "최근5일첫상한가",
				"29": "최근5일신고가갱신",
				"30": "최근5일신저가갱신",
				"31": "상한가직전",
				"32": "하한가직전",
				"41": "주가5MA상향돌파",
				"42": "주가5MA하향돌파",
				"43": "거래량5MA상향돌파",
				"44": "주가데드크로스(5MA<20MA)",
				"45": "주가골든크로스(5MA>20MA)",
				"46": "MACD매수-Signal(9)상향돌파",
				"47": "MACD매도-Signal(9)하향돌파",
				"48": "CCI매수-기준선(-100)상향돌파",
				"49": "CCI매도-기준선(100)하향돌파",
				"50": "Stochastic(10,5,5)매수-기준선상향돌파",
				"51": "Stochastic(10,5,5)매도-기준선하향돌파",
				"52": "Stochastic(10,5,5)매수-%K%D교차",
				"53": "Stochastic(10,5,5)매도-%K%D교차",
				"54": "Sonar매수-Signal(9)상향돌파",
				"55": "Sonar매도-Signal(9)하향돌파",
				"56": "Momentum매수-기준선(100)상향돌파",
				"57": "Momentum매도-기준선(100)하향돌파",
				"58": "RSI(14)매수-Signal(9)상향돌파",
				"59": "RSI(14)매도-Signal(9)하향돌파",
				"60": "VolumeOscillator매수-Signal(9)상향돌파",
				"61": "VolumeOscillator매도-Signal(9)하향돌파",
				"62": "Priceroc매수-Signal(9)상향돌파",
				"63": "Priceroc매도-Signal(9)하향돌파",
				"64": "일목균형표매수-전환선>기준선상향교차",
				"65": "일목균형표매도-전환선<기준선하향교차",
				"66": "일목균형표매수-주가가선행스팬상향돌파",
				"67": "일목균형표매도-주가가선행스팬하향돌파",
				"68": "삼선전환도-양전환",
				"69": "삼선전환도-음전환",
				"70": "캔들패턴-상승반전형",
				"71": "캔들패턴-하락반전형",
				"81": "단기급락후5MA상향돌파",
				"82": "주가이동평균밀집-5%이내",
				"83": "눌림목재상승-20MA지지",
			},
			'default': "*"
		},
		'start_time': {
			'position': 2,
			'type': ['long'],
			'essential': False,
			'options': {
				0: '처음부터',
			},
			'default': 0,
		},
	},
	'GetHeaderValue': {
		'type': {
			'position': 0,
			'type': ['long'],
			'essential': True,
			'options': {
				0: '수신항목구분목록',
				1: '시작시간',
				2: '수신개수',
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

def get_stockmarket_watch(**kwargs):
	crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
	args = crm.ip.gen_args('SetInputValue', **kwargs)
	for pos, arg in args:
		if pos == 1:
			arg = ','.join(arg)
		crm.cp.SetInputValue(pos, arg)
	crm.cp.blockrequest()
	ordered_fields = crm.get_ordered_fields('SetInputValue', **kwargs)
	records = crm.get_datavalue_table(ordered_fields)
	return records
