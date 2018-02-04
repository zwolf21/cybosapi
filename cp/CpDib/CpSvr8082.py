from cp.core.cporm import Cporm

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


MODULE_NAME = 'dscbo1.CpSvr8082'


METHODS_INTERFACES = {

    'SetInputValue': {
        'code': {
            'position': 0,
            'type': ['str'],
            'essential': True,
        },
        'recent_days': {
            'position': 1,
            'type': ['char'],
            'essential': True,
            'options': {
              ord('1'): '20개의최근일수',
              ord('2'): '60개의최근일수',
              ord('3'): '120개의최근일수',
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
                0: '수신개수',
            },
        },
    },
    'GetDataValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '일자',
                1: '체결강도(%)1일',
                2: '체결강도(%)5일',
                3: '체결강도(%)20일',
                4: '체결강도(%)60일',
                5: '주가',
                6: '전일대비',
                7: '전일대비율',
                8: '거래량',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr8082(fields, **kwargs):
    '''종목/업종별 일별 체결강도 데이터를 요청하고 수신한다.
    r = get_cpsvr8082(
      code='A093640', # 종목코드 or 업종코드
      recent_days='60개*', # 최근일수 구분:[20*, 60*, 120*]
      fields = ['일자', '체결*', '주가', '전일*', '거래량']
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


