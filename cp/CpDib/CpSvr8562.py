from ..core.cporm import Cporm

DESCRIPTION = {
    'summary': '',
    'point': '''
    ''',
    'default': [],
}

MODULE_NAME = 'dscbo1.CpSvr8562'

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
                1: '테마명',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr8562(fields, **kwargs):
    '''종목별 테마 조회 데이터를 요청하고 수신합니다.
    '''
    crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
    crm.set_inputvalues(**kwargs)
    crm.blockrequest()
    records = crm.get_datavalue_table(fields)
    for row in records:
        row['종목코드'] = kwargs.get('code')
    return records


