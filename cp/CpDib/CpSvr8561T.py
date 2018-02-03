from ..core.cporm import Cporm

DESCRIPTION = {
    'summary': '',
    'point': '''
    ''',
    'default': ['종목*', '현재가', '대비*', '거래량', '전일동시간대비'],
}

MODULE_NAME = 'dscbo1.CpSvr8561T'

METHODS_INTERFACES = {
    
    'SetInputValue': {
        'tcode': {
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
                0: '테마코드',
                1: 'rows',
                2: 'comment',
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
                2: '현재가',
                3: '대비',
                4: '대비율',
                5: '거래량',
                6: '전일동시간대비',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr8561t(fields=DESCRIPTION['default'], **kwargs):
    '''테마별 종목 조회 데이터를 요청하고 수신합니다.
    '''
    crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
    crm.set_inputvalues(**kwargs)
    crm.blockrequest()
    ext = crm.get_headervalues(['테마코드', 'comment'])
    ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
    records = crm.get_datavalue_table(ordered_fields)
    for row in records:
        row.update(ext)
    return records


