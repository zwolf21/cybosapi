import win32com.client

from ..utils import *

DESCRIPTION = {
	'summary': '호가 잔량 7024',
	'point': '''
	  - 
    -StockCur와 상당히 유사하며 호가 위주의 단순 정보제공.  통신 방식은 다름. 
    -StockJpBid2는 생략함. 실주문을 위한 매수매도 10호가를 받아와 효용 떨어짐.  
    -통신 방식에 따른 차이가 존재하지 않는다면 StockCur사용하고 궂이 안써도 되는 모듈로 생각됨. 

	통신종류 
 		Subscribe/Publish

    -StockBid는 체결 비교 방식에 있어서 호가방식도 제시함. 
	   호가방식: 현재의 체결가와 매수,매도 호가와 비교하여 거래형을 판단
     체결가 방식 : 호가는 무시하고 직전 체결가만을 비교하여 거래형을 판단
    -대부분 증권사들 HTS에서  호가식으로 많이 보여주나 체결가 방식으로 가는 것이 오류가 적음. 


'''    
 
}


MODULE_NAME = 'dscbo1.StockBid'

METHODS_INTERFACES = {

    'SetInputValue': {
        'code': {
            'position': 0,
            'type': ['str'],
            'essential': True,
        },
        'count': {
            'position': 2,
            'type': ['long'],
            'essential': True,
        },
        'contract_type':{
            'position': 3,
            'type': ['char'],
            'essential': True,
            'options': {
                ord('C'): '체결가비교방식',
                ord('H'): '호가비교방식',
            },
            'default': ord('C')
        },
        'date': {
            'position': 4,
            'type': ['str'],
            'essential': False,
        }
        
    },
    'GetHeaderValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '종목코드',
                2: 'rows',
                3: '누적매도체결량',
                4: '누적매수체결량',
                5: '체결비교방식',
            }
        },
    },
    'GetDataValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '시각',
                1: '전일대비',
                2: '매도호가',
                3: '매수호가',
                4: '현재가',
                5: '거래량',
                6: '순간체결량',
                7: '체결상태',
                8: '체결강도',
                9: '시각(초)',
                10: '장구분플래그',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_stockbid(extras, fields=None,**kwargs):
    setinputvalue_argset = encode_args(METHODS_INTERFACES, 'SetInputValue', **kwargs)
    cp = win32com.client.Dispatch(MODULE_NAME)
    cp = set_inputvalue(cp, setinputvalue_argset)

    extras = expand_field_fnmatch(METHODS_INTERFACES, 'GetHeaderValue', extras)
    fields = expand_field_fnmatch(METHODS_INTERFACES, 'GetDataValue', fields)

    headerset = {}
    for h in extras:
        harg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type=h)
        headerset[h] = cp.GetHeaderValue(harg)

    nrow_arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type='rows')
    nrows = cp.GetHeaderValue(nrow_arg) 

    records = []
    for r in range(nrows):
        row = {}
        for f in fields:
            farg = encode_args(
                METHODS_INTERFACES, 'GetDataValue', indexed=False, type=f, index=r
            )
            value = cp.GetDataValue(*farg)
            row[f] = value
        row.update(headerset)
        records.append(row)
    return records
