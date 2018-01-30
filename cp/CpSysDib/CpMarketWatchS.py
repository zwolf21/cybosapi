

DESCRIPTION = {
	'summary': '특정 주식 종목이나 주식 전 종목에 대한 특징주 포착 데이터 8092',
	'point': '''
    -궁극적 종목을 검색하는 것이 목표이나, 이미 정해놓은 종목 검색식 샘플에 해당. 
	-cci, stoc, sonar, 삼선, 일목 등 봉패턴에 의한 검색은 전부 무시하는게 좋음. 
	 과거의 패턴이 반복되지도 않으며, 주식은 굉장히 종목별로 일관성 없이 움직임. 
	-CpMaarketWatchS와  CpMaarketWatch 의 유일한 차이는 통신 방식임 

통신종류 
 	Subscribe/Publish
 
		
CpMarketWatchS.SetInputValue(0,value)
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

value = CpMarketWatchS.GetHeaderValue(type)
type: 데이터 종류
	0 - 수신항목구분목록(string)
	1 - 시작시간(short)
	2 - 수신개수(short)

value = CpMarketWatchS.GetDataValue (Type,index)
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

