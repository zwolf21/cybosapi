from ..core.cporm import Cporm

DESCRIPTION = {
    'summary': '입력한 종목들의 지수를 산정 3744',
    'point': '''
      - 입려한 종목들을 지수화한 값을 산출해 줌. 아주 중요한 기능임.  
    - 50여 종목까지 구성. 네이버 등에서 제공하는 종목군 또는 
       내가 만들어낸 팩터에 의한 종목군을 지수화하는데 필요. 

    통신종류 
        Request/Reply
 
    CpSvr3744.SetInputValue(type,value)
      0 - (string) 다수의 종목코드(ex: "A000660A003540" 연속적으로 최대 50종목까지 구성)

    value = CpSvr3744.GetHeaderValue(type)
       type: 데이터 종류
       0 - (short) count
       반환값: 데이터 종류에 해당하는 값

    value = CpSvr3744.GetDataValue(Type,Index)
      0 - (string) 일자
      1 - (float) 구성종목지수 
      2 - (float) 구성종목지수대비
      3 - (float) 구성종목지수등락률
''',    
    'default': [
        '일자', '구성종목지수', '구성종목지수대비', '구성종목지수등락률'
    ]
}


MODULE_NAME = 'CpSysDib.CpSvr3744'

METHODS_INTERFACES = {

    'SetInputValue': {
        'code': {
            'position': 0,
            'type': ['str[]', 'str'],
            'essential': True,
        },
    },
    'GetHeaderValue': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '데이터개수',
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
                1: '구성종목지수',
                2: '구성종목지수대비',
                3: '구성종목지수등락률',
            },
        },
        'index': {
            'position': 1,
            'type': ['long'],
            'essential': True,
        },
    },  
}

def get_cpsvr3744(codes, fields):
    '''입력한 종목들의 지수를 산정 3744
        # r = get_cpsvr3744(
        #   codes = "A000660", # 종목코드 최대 50개
        #   fields = ['일자', '구성종목지수*']
        # )
    '''
    if not isinstance(codes, str):
        code = ''.join(codes)
    else:
        code = codes
    crm = Cporm(MODULE_NAME, METHODS_INTERFACES)
    crm.set_inputvalues(code=code)
    crm.blockrequest()
    ordered_fields = crm.get_ordered_fields('GetDataValue', option='type', fields=fields)
    records = crm.get_datavalue_table(ordered_fields)
    return records



