import win32com.client

from ..utils import *

DESCRIPTION = {
	'summary': '최장 10년 과거데이터 7026',
	'point': '''

	-StockCur가 당일시세인데 비해 10년 최장 과거제이터 제공. 
	-과거 다양한 정보주는  StockChart에 비해 차별화된 데이터는 없음.(StockChart 제공 기간확인 필요) 
	-StockChart도 외국인 보유수량을 제공하긴 하나 StockWeek의 외국인 관련 정보는 써볼필요 있음. 

통신종류 
	 Request/Reply
 	
StockWeek.SetInputValue(type,value)
	0 - (string) 종목 코드


value = StockWeek.GetHeaderValue(type)
	type: 데이터 종류

	0 - (string) 종목코드
	1 - (short) count
	2 - (long) 날짜

value = StockWeek.GetDataValue(Type,Index)

type에 해당하는 데이터를 반환합니다

type: 데이터 종류

0 - (long) 일자
7 - (long) 외인보유
8 - (long) 외인보유 전일대비
9 - (double) 외인비중




 ''',

'default': [
		'종목코드', '일자', '시가', '고가','저가','종가', '누적거래량'
		,'외인보유', '외인보유전일대비', '외인비중'
	]
}

MODULE_NAME = 'dscbo1.StockWeek'


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
                0: '종목코드',
                1: 'rows',
                2: '날짜',
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
                1: '시가',
                2: '고가',
                3: '저가',
                4: '종가',
                5: '전일대비',
                6: '누적거래량',
                7: '외인보유',
                8: '외인보유전일대비',
                9: '외인비중',
                10: '등락률',
                11: '대비부호',
                12: '기관순매수수량',
                13: "시간외단일가시가",
				14: "시간외단일가고가",
				15: "시간외단일가저가",
				16: "시간외단일가종가",
				17: "시간외단일가대비부호",
				18: "시간외단일가전일대비",
				19: "시간외단일가거래량",
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_stockweek(extras, fields=None,**kwargs):
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
