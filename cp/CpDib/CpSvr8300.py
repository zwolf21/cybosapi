from ..core.cporm import Cporm

DESCRIPTION = {
	'summary': '해외지수코드에 대한 과거 데이터 8300',
	'point': '''
	- 해외데이터는 과거데이터 즉 전일 포함한 데이터로도 충분함. 

	- 해외 엄종지수를 가져올 수 있다면 최근 글로벌 증시의 종목군 추이파악 가능함. 
	  당일 현재 데이터도 이미 국내주가에 반영중이므로 따로 가져올 필요 없음.  
    - 8311의 해외 시간별 데이터, 8312 해외 현재가는 참조로 유용성 떨어짐. 
    - CpSysDib에  Subscribe/Publish 방식으로 있는 WorldCur 와 거의 동일 택일해서 사용. 


	통신종류 
 		Request/Reply
 
	CpSvr8300.SetInputValue(type,value)
	  0 - (string) 해외 지수코드
	  1 - (char) 일주월구분('D','W','M')
         
		UsType(USTYPE): 해외종목 종류
			USTYPE_ALL : 전종목 - 1
			USTYPE_CONTRY : 국가 대표 - 2
			USTYPE_UPJONG : 업종 3
			USTYPE_JONGMOK : 종목 - 4
			USTYPE_DR : 예탁증서 - 5
			USTYPE_RAW : 상품선물 - 6	
			USTYPE_EXCHANGE : 환율 - 7


	value = CpSvr8300.GetHeaderValue(type)
	 0 - (string) 해외지수코드 1 - (char) 일주월구분 2 - (long) 최근일 3 - (short) 수신데이터수

	value = CpSvr8300.GetDataValue(Type,Index)
		0 - (long) 날짜
		1 - (float) 시가
		2 - (float) 고가
		3 - (float) 저가
		4 - (float) 종가 
		5 - (ulong) 거래량 


''',    
    'default': [
		'해외지수명','해외업종명', '날짜', '종가', '거래량'
	]

}


MODULE_NAME = 'dscbo1.CpSvr8300'


METHODS_INTERFACES = {

    'SetInputValue': {
        'code': {
            'position': 0,
            'type': ['str'],
            'essential': True,
        },
        'period': {
            'position': 1,
            'type': ['char'],
            'essential': True,
            'options': {
            	ord('D'): '일',
            	ord('W'): '주',
            	ord('M'): '월',
            },
        },
        'count': {
            'position': 3,
            'type': ['long'],
            'essential': False,
        },
        
    },
    'GetHeaderValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '해외지수코드',
                1: '일주월구분 ',
                2: '최근일',
                3: '수신데이터수',
            },
        },
    },
    'GetDataValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '날짜',
                1: '시가',
                2: '고가',
                3: '저가',
                4: '종가',
                5: '거래량',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr8300(fields, **kwargs):
	crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
	crm.set_inputvalues(**kwargs)
	crm.blockrequest()
	addon = crm.get_headervalues(['최근일', '해외지수코드'])
	ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
	records = crm.get_datavalue_table(ordered_fields)
	for row in records:
		row.update(addon)
	return records

