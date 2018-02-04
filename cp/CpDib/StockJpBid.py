import win32com.client

from ..utils import *


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

MODULE_NAME = 'dscbo1.StockjpBid2'

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
                1: "시간",
                2: "거래량",
                3: "1차매도호가",
                4: "1차매수호가",
                5: "1차매도잔량",
                6: "1차매수잔량",
                7: "2차매도호가",
                8: "2차매수호가",
                9: "2차매도잔량",
                10: "2차매수잔량",
                11: "3차매도호가",
                12: "3차매수호가",
                13: "3차매도잔량",
                14: "3차매수잔량",
                15: "4차매도호가",
                16: "4차매수호가",
                17: "4차매도잔량",
                18: "4차매수잔량",
                19: "5차매도호가",
                20: "5차매수호가",
                21: "5차매도잔량",
                22: "5차매수잔량",
                23: "총매도잔량",
                24: "총매수잔량",
                25: "시간외총매도잔량",
                26: "시간외총매수잔량",
                27: "6차매도호가",
                28: "6차매수호가",
                29: "6차매도잔량",
                30: "6차매수잔량",
                31: "7차매도호가",
                32: "7차매수호가",
                33: "7차매도잔량",
                34: "7차매수잔량",
                35: "8차매도호가",
                36: "8차매수호가",
                37: "8차매도잔량",
                38: "8차매수잔량",
                39: "9차매도호가",
                40: "9차매수호가",
                41: "9차매도잔량",
                42: "9차매수잔량",
                43: "10차매도호가",
                44: "10차매수호가",
                45: "10차매도잔량",
                46: "10차매도잔량",
                47: "1차LP매도잔량",
                48: "1차LP매수잔량",
                49: "2차LP매도잔량",
                50: "2차LP매수잔량",
                51: "3차LP매도잔량",
                52: "3차LP매수잔량",
                53: "4차LP매도잔량",
                54: "4차LP매수잔량",
                55: "5차LP매도잔량",
                56: "5차LP매수잔량",
                57: "6차LP매도잔량",
                58: "6차LP매수잔량",
                59: "7차LP매도잔량",
                60: "7차LP매수잔량",
                61: "8차LP매도잔량",
                62: "8차LP매수잔량",
                63: "9차LP매도잔량",
                64: "9차LP매수잔량",
                65: "10차LP매도잔량",
                66: "10차LP매수잔량",
                67: "LP매도잔량10차합",
                68: "LP매수잔량10차합",
            },
        }
    },
}



def get_stockjpbid(code, fields=None):
    fields = fields or []
    cp = win32com.client.Dispatch(MODULE_NAME)
    setinputvalue_argset = encode_args(METHODS_INTERFACES, 'SetInputValue', code=code)
    cp = set_inputvalue(cp, setinputvalue_argset)
    ext = {}
    fields = expand_field_fnmatch(METHODS_INTERFACES, 'GetHeaderValue', fields)
    for colnm in fields:
        arg = encode_args(METHODS_INTERFACES, 'GetHeaderValue', indexed=False, flated=True, type=colnm)
        value = cp.GetHeaderValue(arg)
        ext[colnm] = value

    return ext

