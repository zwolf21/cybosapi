
DESCRIPTION = {
	'summary': '최장 10년 과거데이터 7026',
	'point': '''

	-StockCur가 당일시세인데 비해 10년 최장 과거제이터 제공. 
	-과거 다양한 정보주는  StockChart에 비해 차별화된 데이터는 없음.(StockChart 제공 기간확인 필요) 
	-StockChart도 외국인 보유수량을 제공하긴 하나 StockWeek의 외국인 관련 정보는 써볼필요 있음. 

통신종류 
	 Request/Reply
 	
StockWeek.SetInputValue(type,value)
	0 - (string) 종목 코드


value = StockWeek.GetHeaderValue(type)
	type: 데이터 종류

	0 - (string) 종목코드
	1 - (short) count
	2 - (long) 날짜

value = StockWeek.GetDataValue(Type,Index)

type에 해당하는 데이터를 반환합니다

type: 데이터 종류

0 - (long) 일자
7 - (long) 외인보유
8 - (long) 외인보유 전일대비
9 - (double) 외인비중




 ''',

'default': [
		'종목코드', '일자', '시가', '고가','저가','종가', '누적거래량'
		,'외인보유', '외인보유전일대비', '외인비중'
	]

    
	
}



