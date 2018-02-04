from cp.core.cporm import Cporm

DESCRIPTION = {
    'summary': '종목 실시간 체결강도 8081',
    'point': '''
      8081, 8082,8083이 유사해서, 사용을 위해그 차이 정도를  숙지 
  - 8081 요청하는 종목 실시간 체결강도 데이티를 받아오는 것에 특화로 보임.  
    특이한 것은 최근 *일 간의 체결강도 순위와 *거래량 기준 단위별로 데이터를 요청가능.  
    그리고 유용해보이는 하락률 큰 순의 요청도 가능하다는 것이다.(하락율순이 가격인지 체결강도 자체의 감소인지 확인필요)
       
  
          통신방식        연속여부  특성
  - 8081 Request/Reply    o   종목별 (실시간) 체결강도 
    8082 Request/Reply    x   종목별/업종별 일별 체결강도 
    8083 Request/Reply    x   종목별/업종별 시간대별 체결강도 (최대 360분) 

    통신종류 
        Request/Reply
 
CpSvr8081.SetInputValue(type,value)
  type: 입력 데이터 종류
0 - (string)  종목/업종/선물 
1 - (char)  최근분수 구분 
  '0' 시장구분  1전체, 2거래소,3코스닥
  '1' 정렬구분 1.당일 2.5일 3.50(?확인필요), 4.60, 5.하락율큰순 
  '2' 거개량구분 1.전체, 2.1만, 3.5만, 4.10만, 5.50만, 6.100만(이상)
 
value = CpSvr8081.GetHeaderValue(type)
type: 데이터 종류
  0 - (short) 수신개수

value = CpSvr8081.GetDataValue (Type,index)
  type: 데이터 종류
0 - (string) 종목코드
1 - (string) 종목명
2 - (long) 전일대비
3 - (float) 전일대비율
4 - (long) 현재가
5 - (long) 거래량
6 - (float) 체결강도(%) 1일
7 - (float) 체결강도(%) 5일
8 - (float) 체결강도(%) 20일
9 - (float) 체결강도(%) 59일

''' ,

    'default': [
          '종목업종명', '일자', '1체결강도', '5체결강도', '20체결강도', '59체결강도', '현재가', '전일대비율','전일대비','거래량'
    ]

}

MODULE_NAME = 'dscbo1.CpSvr8081'


METHODS_INTERFACES = {

    'SetInputValue': {
        'market_kind': {
            'position': 0,
            'type': ['char'],
            'essential': True,
            'options': {
              ord('1'): '전체',
              ord('2'): '거래소',
              ord('3'): '코스닥',
              ord('4'): '관리',
            },
            'default': ord('1'),
        },
        'order_kind': {
            'position': 1,
            'type': ['char'],
            'essential': True,
            'options': {
              ord('1'): '금일큰순',
              ord('2'): '최근5일큰순',
              ord('3'): '최근50일큰순',
              ord('4'): '최근60일큰순',
              ord('5'): '하략율큰순',
            },
            'default': ord('1'),
        },
        'stock_amount_kind': {
            'position': 2,
            'type': ['char'],
            'essential': False,
            'options': {
              ord('1'): '전체',
              ord('2'): '10000주이상',
              ord('3'): '50000주이상',
              ord('4'): '10만주이상',
              ord('5'): '50만주이상',              
              ord('6'): '100만주이상',              
            },
            'default': ord('1')
        },
        
    },
    'GetHeaderValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '카운트',
            },
        },
    },
    'GetDataValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '종목코드',
                1: '종목명',
                2: '전일대비',
                3: '전일대비율',
                4: '현재가',
                5: '거래량',
                6: '체결강도(%)1일',
                7: '체결강도(%)5일',
                8: '체결강도(%)20일',
                9: '체결강도(%)59일',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr8081(fields, **kwargs):
    '''종목별 체결강도 데이터를 요청하고 수신한다.
      r = get_cpsvr8081(
      market_kind='코스닥', # 시장구분: ['전체', '거래소', '코스닥', '관리']
      order_kind='최근50일*', # 정렬구분: ['금일큰순', '최근5일큰순', '최근50일큰순', '최근60일큰순', '하락율큰순']
      stock_amount_kind='10만주*', # 거래량구분: ['전체', '1000주이상', 50000주, 10만주~, 50만주~, 100만주이상]
      fields=['종목코드', '종목명', '전일대비', '전일대비율', '현재가', '거래량', '체결강도*'],
    )
    '''
    crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
    crm.set_inputvalues(**kwargs)
    crm.blockrequest()
    ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
    records = crm.get_datavalue_table(ordered_fields)
    return records



