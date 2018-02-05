from ..core.cporm import Cporm

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

MODULE_NAME = 'dscbo1.CpSvr8561'

METHODS_INTERFACES = {

    'GetHeaderValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: 'rows',
            },
        },
    },
    'GetDataValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '테마코드',
                1: '테마순서',
                2: '테마명',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr8561(fields=['테마코드', '테마순서', '테마명']):
	'''테마별 테마코드,테마명을 요청하고 수신합니다
	'''
	crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
	crm.blockrequest()
	nrows = crm.cp.GetHeaderValue(0)
	records = crm.get_datavalue_table(fields)
	return records




