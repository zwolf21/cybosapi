
DESCRIPTION = {
	'summary': '입력한 종목 기관매매누적과 외인순매수',
	'point': '''
	  - CpSvrNew7216은 기관전체 누적과 외인전체 매수의 경향
	  - CpSvrNew7254는 세분화된 기관 의 매수경향을 보여줌.(ex 투신, 연기금...)   
      - 종목별로 기관 또는 외인의 순매수 누적 추이 정도는 확인할 필요가 있다. 

	통신종류 
 		Request/Reply
 
	CpSvrNew7216.SetInputValue(type,value)
	  0 - (string) 종목코드

	value = CpSvrNew7216.GetHeaderValue(type)
       type: 데이터 종류
		0 -(string) 종목코드
		1 -(short) 카운트 
		2 -(long) 조회일자

	value = CpSvrNew7216.GetDataValue(Type,Index)
        0-(long) 일자
		1- (long) 종가
		7- (long) 기관매매 누적
		8- (long) 외국인 순매매 <-- 누적값으로 전환 필요 		
		 
''',    
    'default': [
		'종목코드', '일자', '종가', '기관매매누적', '외국인순매매누적'
	]

}

