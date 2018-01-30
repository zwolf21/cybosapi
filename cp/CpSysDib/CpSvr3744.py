
DESCRIPTION = {
	'summary': '입력한 종목들의 지수를 산정 3744',
	'point': '''
	  - 입려한 종목들을 지수화한 값을 산출해 줌. 아주 중요한 기능임.  
    - 50여 종목까지 구성. 네이버 등에서 제공하는 종목군 또는 
       내가 만들어낸 팩터에 의한 종목군을 지수화하는데 필요. 

	통신종류 
 		Request/Reply
 
	CpSvr3744.SetInputValue(type,value)
	  0 - (string) 다수의 종목코드(ex: "A000660A003540" 연속적으로 최대 50종목까지 구성)

	value = CpSvr3744.GetHeaderValue(type)
       type: 데이터 종류
       0 - (short) count
       반환값: 데이터 종류에 해당하는 값

	value = CpSvr3744.GetDataValue(Type,Index)
      0 - (string) 일자
      1 - (float) 구성종목지수 
      2 - (float) 구성종목지수대비
      3 - (float) 구성종목지수등락률
      		
		 
''',    
    'default': [
		'일자', '구성종목지수', '구성종목지수대비', '구성종목지수등락률'
	]

}

