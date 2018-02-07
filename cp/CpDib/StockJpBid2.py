from ..core.cporm import Cporm


DESCRIPTION = {
    'summary': '10차 호가 7021',
    'point': '''
    -작성하지 않아도 되는 모듈로 생각됨. 
    -단순한 매수 매도 호가 각 10여개를 보여 줌.  
    -자동 실주문을 내기 위한 정보로 중요하지 않음.   
    
    통신종류 
        Request/Reply

    총매수호가잔량 총매도호가잔량
      -해당 정보는 경험상 cum_bid cum_ask 형태로 제공되는 데이터를 많이 써보았으나 
       허수 매수나 매도가 잡히는 경우가 많아 유용성이 떨어짐.  
'''    
 
}

MODULE_NAME = 'dscbo1.StockJpBid2'

METHODS_INTERFACES = {

    'SetInputValue': {
        'code': {
            'position': 0,
            'type': ['str'],
            'essential': True,
        },
    },
    'GetHeaderValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: "종목코드",
                1: "count",
                3: "시각",
                4: "총매도잔량",
                5: "총매도잔량대비",
                6: "총매수잔량",
                7: "총매수잔량대비",
                8: "시간외총매도잔량",
                9: "시간외총매도잔량대비",
                10: "시간외총매수잔량",
                11: "시간외총매수잔량대비",
            },
        },
    },
    'GetDataValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: "매도호가",
                1: "매수호가",
                2: "매도잔량",
                3: "매수잔량",
                4: "매도잔량대비",
                5: "매수잔량대비",
            },
        },
    },
}

def get_stockjpbid2(fields, addons=['종목코드'], **kwargs):
    '''주식 종목에 대해 매도, 매수에 관한 1차 ~ 10차 호가, 호가잔량
        record = get_stockjpbid2(
            code='A078070', # 종목코드
            addons=['종목코드', '시각', '총매도잔량*', '시간외*'],
            fields=['*호가', '*잔량', '*대비']
        )
    '''
    crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
    crm.set_inputvalues(**kwargs)
    crm.blockrequest()
    ext = crm.get_headervalues(addons)
    ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
    records = crm.get_datavalue_table(ordered_fields)
    for row in records:
        row.update(ext)
    return records

