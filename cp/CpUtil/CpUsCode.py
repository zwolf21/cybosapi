import win32com.client

DESCRIPTION = {
	'summary': '해외종목 코드 조회',
	'point': '''
	- 해외종목에 직접 투자할 것이 아니지만 글로벌화로 각국 동일 업종 상승하락의 유사성은 있음 . 
  - 미국 시장 정도의 업종별 인덱스 값은 비교해 볼 필요 있음 
	
  Value =CpUtil.GetUsCodeList(USTYPE UsType)

		USTYPE_UPJONG : 업종 3  
        

'''    
   
}

MODULE_NAME = 'CpUtil.CpUsCode'

def get_us_code_list(type):
	interface = {
		'전종목': 1,
		'국가대표': 2,
		'업종': 3,
		'종목': 4,
		'예탁증서': 5,
		'상품선물': 6,
		'환율': 7,
		
	}
	if type not in interface.values():
		type = interface.get(type)

	cp = win32com.client.Dispatch(MODULE_NAME)
	return cp.GetUsCodeList(type)

def uscode2name(uscode):
	if isinstance(uscode, str):
		uscode = [uscode]
	cp = win32com.client.Dispatch(MODULE_NAME)
	pair = {}
	for cd in uscode:
		pair[cd] = cp.GetNameByUsCode(cd)
	return pair
