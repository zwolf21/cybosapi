
DESCRIPTION = {
	'summary': '종목 업종 일별 체결강도 8082',
	'point': '''
	  8081, 8082,8083이 유사해서, 사용을 위해그 차이 정도를  숙지 
  - 8082는 요청하는 종목 및  업종 포한한 일자별 체결강도 데이티를 받아오는 것에 특화. 
    CpSvr8082.SetInputValue는 20일 60일 120일 인데 반해, 
    CpSvr80832.GetDataValue가 뱉어내는 값은 1,5,20,60일이어서 확인 필요. 
   
  
          통신방식        연속여부  특성
    8081 Request/Reply    o   종목별 (실시간) 체결강도 
    8082 Request/Reply    x   종목별/업종별 일별 체결강도 
  - 8083 Request/Reply    x   종목별/업종별 시간대별 체결강도 (최대 360분) 

	통신종류 
 		Request/Reply
 
CpSvr8082.SetInputValue(type,value)
  type: 입력 데이터 종류
0 - (string)  종목/업종/선물 코드
1 - (char)  최근분수 구분 
  '1' 최근 20일/'2' 최근 60일/'3' 최근 120일
 
value = CpSvr8082.GetHeaderValue(type)
type: 데이터 종류
  0 - (short) 수신개수

value = CpSvr8082.GetDataValue (Type,index)
  type: 데이터 종류
0 - (long) 일자
1 - (float) 체결강도(%) 1일
2 - (float) 체결강도(%) 5일
3 - (float) 체결강도(%) 20일
4 - (float) 체결강도(%) 60일
5 - (long,float) 주가(종목 코드인 경우 long,업종 코드인 경우 float)
6 - (long,float) 전일대비(종목 코드인 경우 long,업종 코드인 경우 float)
7 - (float) 전일 대비율
8 - (long) 거래량
 

''' ,

    'default': [
		'종목업종명', '일자', '1체결강도', '5체결강도', '20체결강도', '60체결강도', '주가', '전일대비율','전일대비','거래량'
	]

}

