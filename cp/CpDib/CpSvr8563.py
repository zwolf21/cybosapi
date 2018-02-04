from ..core.cporm import Cporm


DESCRIPTION = {
    'summary': '상승율로 상위테마 검색 8563',
    'point': '''
      - 특정 테마가 언제갈지 아는 것은 신의 영역임. 
      그러나 역으로 사고해보기 위해 사용. 향후, 
    1) CpSvr8563 상승하락률에 의한 테마 검색   
    2) CpSvr8561로 해당 테마별 종목을 받는다.  
    3) StokChart로 특정 종목 패턴 연구 

    통신종류 
        Request/Reply
 
    CpSvr8563.SetInputValue(type,value)
      0 -  (char)상승율 구분
    '1'  전일대비 상승율 상위순
    '2'  전일대비 상승율 하위순
    '3'  5일 대비 상승율 상위순
    '4'  5일 대비 상승율 하위순
    '5'  상승종목비율 상위
    '6'  상승종목비율 하위
 
    value = CpSvr8563.GetHeaderValue(type)
        0 - (short) 데이터건수
    
  value = CpSvr8563.GetDataValue(type)  
      0 - (short)테마 코드
      1 - (string)테마 명
      2 - (short)구성 종목수
      3 - (float)1일전 대비
      4 - (float)5일전 대비
      5 - (long)상승종목수
      6 - (long)하락종목수
      7 - (long)상승종목비율


''',    
    'default': [
        '테마명', '구성종목수', '1일전대비', '5일전대비', '상승종목비율'
    ]

}


MODULE_NAME = 'dscbo1.CpSvr8563'


METHODS_INTERFACES = {

    'SetInputValue': {
        'inc_kind': {
            'position': 0,
            'type': ['char'],
            'essential': True,
            'options': {
              ord('1'): '전일대비상승율상위순',
              ord('2'): '전일대비상승율하위순',
              ord('3'): '5일대비상승율상위순',
              ord('4'): '5일대비상승율하위순',
              ord('5'): '상승종목비율상위',
              ord('6'): '상승종목비율하위',
            },
            'default': ord('1'),
        },
    },
    'GetHeaderValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: 'data건수',
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
                1: '테마명',
                2: '구성종목수',
                3: '1일전대비',
                4: '5일전대비',
                5: '상승종목수',
                6: '하락종목수',
                7: '상승종목비율',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr8563(fields, **kwargs):
    '''상승율 구분을 두어 상승율 상위 테마 데이터를 요청하고 수신
        r = get_cpsvr8563(
            inc_kind='5일대비상승율상위순', # 상승율 구분:[전일대비상승율상위순, ~하위순, 5일대비~, 상승종목비율상위, ~하위]
            fields=[
                '테마코드', '테마명', '구성종목수', '*일전대비', '상승종목수', '하락종목수', '상승종목비율'
            ]
        )
    '''
    crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
    crm.set_inputvalues(**kwargs)
    crm.blockrequest()
    ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
    records = crm.get_datavalue_table(ordered_fields)
    for row in records:
        row['code'] = kwargs.get('code')
    return records

