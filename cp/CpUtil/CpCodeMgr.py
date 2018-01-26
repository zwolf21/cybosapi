
DESCRIPTION = {
	'summary': '코드 정보 및 코드리스트',
	'point': '''

	-CpCodeMgr은 거래 가능한 종목군 정도를 추출하는 용도로 쓰여야 함. 
  -1)거래소와 코스닥 종목인지, 2)주권인지 3)정상 종목인지.  
  -신용가능 종목인지 증거금등의 정보는 필효하지 않으므로 생략. 
  -관리종목 정도는 매매 가능하므로, 궂이 판단하지 않고 정상여부만  판단한다.   

value = object.CodeToName( code ) 
  code 에 해당하는 주식 종목명 반환
 
value = CpCodeMgr.GetStockMarketKind ( code ) 
  code 에 해당하는 소속부를 반환
  -> 1거래소 2 코스닥에 해당하는 값이어야 한다

value = CpCodeMgr.GetStockControlKind ( code ) 
  code에 해당하는 감리부문 값. 정상인지만 체크하면 된다.
  typedef enum { [helpstring("정상")].......}   

 value = CpCodeMgr.GetStockKospi200Kind ( code ) 
   code 에 해당하는KOSPI200 종목여부 반환
   바스켓 거래와 연동되는 종목인지 체크가능. 

 value =  CpCodeMgr.GetStockSectionKind ( code ) 
   code 에 해당하는 부 구분 코드를 반환.
   주권에 해당하는 1값 이외의 요소(0,2~15)들을 제거하기 위한 모듈로 사용. 

'''    
    

}

