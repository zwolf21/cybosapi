from ..core.cporm import Cporm


DESCRIPTION = {
	'summary': '코드 정보 및 코드리스트',
	'point': '''

	-CpCodeMgr은 거래 가능한 종목군 정도를 추출하는 용도로 쓰여야 함. 
  -1)거래소와 코스닥 종목인지, 2)주권인지 3)정상 종목인지.  
  -신용가능 종목인지 증거금등의 정보는 필효하지 않으므로 생략. 
  -관리종목 정도는 매매 가능하므로, 궂이 판단하지 않고 정상여부만  판단한다.   

value = object.CodeToName( code ) 
  code 에 해당하는 주식 종목명 반환
 
value = CpCodeMgr.GetStockMarketKind ( code ) 
  code 에 해당하는 소속부를 반환
  -> 1거래소 2 코스닥에 해당하는 값이어야 한다

value = CpCodeMgr.GetStockControlKind ( code ) 
  code에 해당하는 감리부문 값. 정상인지만 체크하면 된다.
  typedef enum { [helpstring("정상")].......}   

 value = CpCodeMgr.GetStockKospi200Kind ( code ) 
   code 에 해당하는KOSPI200 종목여부 반환
   바스켓 거래와 연동되는 종목인지 체크가능. 

 value =  CpCodeMgr.GetStockSectionKind ( code ) 
   code 에 해당하는 부 구분 코드를 반환.
   주권에 해당하는 1값 이외의 요소(0,2~15)들을 제거하기 위한 모듈로 사용. 
'''    

}


MODULE_NAME = 'CpUtil.CpCodeMgr'

METHOD_INTERFACE = {

    'GetStockListByMarket': {
        'type': {
            'position': 0,
            'type': ['long'],
            'essential': True,
            'options': {
                0: '구분없음',
                1: '거래소',
                2: '코스닥',
                3: '프리보드',
                4: 'KRX',
            },
            'default': 1,
        },
    },
    'CodeToName': {
        'code': {
            'position': 0,
            'type': ['str'],
            'essential': True,
        },
    },

}


def get_stocklist_by_market(**kwargs):
    '''시장구분에 따른 주식종목배열을 반환하다
    '''
    crm = Cporm(MODULE_NAME, METHOD_INTERFACE)
    args = crm.ip.gen_args('GetStockListByMarket', setposition=False, **kwargs)
    return crm.cp.GetStockListByMarket(*args)

def code2name(code):
    crm = Cporm(MODULE_NAME, METHOD_INTERFACE)
    if isinstance(code, str):
        return crm.cp.CodeToName(code)
    elif isinstance(code, (list, set, tuple)):
        return [crm.cp.CodeToName(cd) for cd in code]
    return code

def get_codemap(**kwargs):
    codelist = get_stocklist_by_market(**kwargs)
    return {cd: code2name(cd) for cd in codelist}

def get_stock_elw_basket_code_list(code):
    crm = Cporm(MODULE_NAME, METHOD_INTERFACE)
    return crm.cp.GetStockElwBasketCodeList(code)

def get_stock_elw_basket_comp_list(code):
    crm = Cporm(MODULE_NAME, METHOD_INTERFACE)
    return crm.cp.GetStockElwBasketCompList(code)



class CpCodeManager:

    def __init__(self, code, module_name=MODULE_NAME, interface=METHOD_INTERFACE):
        self.crm = Cporm(module_name, interface)
        self.code = code

    @property
    def name(self):
        '''code 에 해당하는 주식/선물/옵션 종목명 을 반환한다. 
           code : 주식/선물/옵션 코드
        '''
        return self.crm.cp.CodeToName(self.code)

    @property
    def industry_name(self):
        '''증권전산업종코드에 해당하는 증권전산업종명을 반환한다
        '''
        ucode = self.crm.cp.GetStockIndustryCode(self.code)
        if ucode:
            return self.crm.cp.GetIndustryName(ucode)

    @property
    def stock_margin_rate(self):
        '''code 에 해당하는 주식 매수 증거금율을 반환한다. 
        '''
        return self.crm.cp.GetStockMarginRate(self.code)

    @property
    def stock_meme_min(self):
        '''code 에 해당하는 주식 매매 거래단위주식수를 반환한다. 
           code : 주식코드
           반환값 : 주식 매매 거래단위 주식수
        '''
        return self.crm.cp.GetStockMemeMin(self.code)

    @property
    def stock_industry_code(self):
        '''code 에 해당하는 증권전산업종코드를 반환한다. 
        '''
        return self.crm.cp.GetStockIndustryCode (self.code)

    @property
    def stock_capital(self):
        '''code 에 해당하는 자본금규모구분 반환한다
        '''
        retmap = {
            0: '제외', 1: '대', 2: '중', 3:'소',
        }
        value = self.crm.cp.GetStockCapital(self.code)
        return retmap.get(value)

    @property
    def stock_fiscal_month(self):
        '''code 에 해당하는 결산기 반환한다.
        '''
        return self.crm.cp.GetStockFiscalMonth(self.code)

    @property
    def stock_group_code(self):
        '''code 에 해당하는 그룹(계열사)코드 반환한다. 
        '''
        return self.crm.cp.GetStockGroupCode(self.code)

    @property
    def stock_lac_kind(self):
        retmap = {
              0: "구분없음",
              1: "권리락",
              2: "배당락",
              3: "분배락",
              4: "권배락",
              5: "중간배당락",
              6: "권리중간배당락",
              99: "기타",
        }
        value = self.crm.cp.GetStockLacKind(self.code)
        return retmap.get(value)

    @property
    def stock_listed_date(self):
        '''code 에 해당하는 상장일을 반환한다
        '''
        return str(self.crm.cp.GetStockListedDate(self.code))

    @property
    def stock_max_price(self):
        return self.crm.cp.GetStockMaxPrice(self.code)

    @property
    def stock_min_price(self):
        return self.crm.cp.GetStockMinPrice(self.code)

    @property
    def stock_par_price(self):
        return self.crm.cp.GetStockParPrice(self.code)

    @property
    def stock_std_price(self):
        '''code 에 해당하는 권리락 등으로 인한 기준가를 반환한다
        '''
        return self.crm.cp.GetStockStdPrice(self.code)

    @property
    def is_stock_credit_enable(self):
        '''code 에 해당하는 신용가능종목 여부를 반환한다
        '''
        return bool(self.crm.cp.IsStockCreditEnable(self.code))

    @property
    def stock_parprice_change_type(self):
        '''code 에 해당하는 액면정보 코드를 반환한다
        '''
        retmap = {
            0: '해당없음',
            1: '액면분할',
            2: '액면병합',
            99: '기타',
        }
        value = self.crm.cp.GetStockParPriceChageType(self.code)
        return retmap.get(value)

    @property
    def stock_market_kind(self):
        '''code 에 해당하는 소속부를 반환한다
        '''
        retmap = {
            0: '구분업음',
            1: '거래소',
            2: '코스닥',
            3: '프리보드',
            4: 'KRX',
        }
        value = self.crm.cp.GetStockMarketKind(self.code)
        return retmap.get(value)

    @property
    def stock_control_kind(self):
        '''code 에 해당하는 감리구분을 반환한다.
        '''
        retmap = {
            0: '정상',
            1: '주의',
            2: '경고',
            3: '위험예고',
            4: '위험',
        }
        value = self.crm.cp.GetStockControlKind(self.code)
        return retmap.get(value)

    @property
    def stock_kospi200_kind(self):
        '''code 에 해당하는KOSPI200 종목여부 반환한다
        '''
        retmap = {
            0: '미채용',
            1: '제조업',
            2: '전기통신업',
            3: '건설업',
            4: '유통업',
            5: '금융업',
        }
        value = self.crm.cp.GetStockControlKind(self.code)
        return retmap.get(value)

    @property
    def stock_section_kind(self):
        '''code 에 해당하는 부 구분 코드를 반환한다.
        '''
        retmap = {
            0: "구분없음",
            1: "주권",
            2: "투자회사",
            3: "부동산투자회사",
            4: "선박투자회사",
            5: "사회간접자본투융자회사",
            6: "주식예탁증서",
            7: "신수인수권증권",
            8: "신주인수권증서",
            9: "주식워런트증권",
            10: "상장지수펀드",
            11: "수익증권",
            12: "해외ETF",
            13: "외국주권",
            14: "선물",
            15: "옵션",
        }
        value = self.crm.cp.GetStockControlKind(self.code)
        return retmap.get(value)

    @property
    def stock_supervision_kind(self):
        '''code 에 해당하는 관리구분 반환한다. 
        '''
        retmap = {
            0: '일반종목',
            1: '관리',
        }
        value = self.crm.cp.GetStockSupervisionKind(self.code)
        return retmap.get(value)

    @property
    def stock_status_kind(self):
        '''code 에 해당하는 주식상태를 반환한다
        '''
        retmap = {
            0: '정상',
            1: '거래정지',
            2: '거래중단',
        }
        value = self.crm.cp.GetStockStatusKind(self.code)
        return retmap.get(value)


    @property
    def market_start_time(self):
        '''장 시작 시각 얻기 (ex 9시일경우 리턴값 900)
        '''
        return self.crm.cp.GetMarketStartTime()

    @property
    def market_end_time(self):
        '''장 마감 시각 얻기 (ex오후 3시30분일경우 리턴값 1530)
        '''
        return self.crm.cp.GetMarketEndTime()



