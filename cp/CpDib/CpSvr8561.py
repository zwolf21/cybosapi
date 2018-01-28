
DESCRIPTION = {
	'summary': '테마별종목조회 8561',
	'point': '''
	  - 특정 테마가 언제갈지 아는 것은 신의 영역임. 
      그러나 역으로 사고해보기 위해 사용. 향후, 
    1) CpSvr8563 상승하락률에 의한 테마 검색   
    2) CpSvr8561로 해당 테마별 종목을 받는다.  
    3) StokChart로 특정 종목 패턴 연구 

	통신종류 
 		Request/Reply
 
	value = CpSvr8561.GetHeaderValue(type)
	  0 - (short) 테마코드
    1 - (short) 테마순서
    2 - (string) 테마명
 

''',    
    'default': [ 	'테마명'
	]

}
