import win32com.client


DESCRIPTION = {

'summary': '연결상태',

'point': '''

-code와 fullcode간의 차이를 알 수 없으므로 code만 진행. 
-아래 3가지 정도의 메서드 정도만 필요할 듯. 

value = CpStockCode.CodeToName(code)

code에 해당하는 종목명을 반환


value = CpStockCode. NameToCode(name)

name에 해당하는 code를 반환


value = CpStockCode.GetCount()

종목 코드 개수를 반환

 '''

}


MODULE_NAME = 'CpUtil.CpStockCode'


def get_count(module_name=MODULE_NAME):
	cp = win32com.client.Dispatch(module_name)
	return cp.GetCount()


def get_code_table(module_name=MODULE_NAME):
	cp = win32com.client.Dispatch(module_name)
	nrows = get_count()
	colmap = {
		0: '종목코드',
		1: '종목명',
		2: 'FullCode',
	}
	table = []
	for r in range(nrows):
		row = {}
		for type, name in colmap.items():
			row[name] = cp.GetData(type, r)
		table.append(row)
	return table


class CpStockCode:

	def __init__(self, code=None, fullcode=None, many=False, module_name=MODULE_NAME):
		self.code = code or fullcode
		self.cp = win32com.client.Dispatch(module_name)
		self.many = many
		if code is None:
			raise ValueError("code 또는 fullcode 를 입력하여야 합니다")

		if many == True:
			if isinstance(self.code, str):
				self.code = self.code.split()

	def code2name(self):
		if self.many:
			pair = {}
			for cd in self.code:
				pair[cd] = self.cp.CodeToName(cd)
			return pair
		else:
			return self.cp.CodeToName(self.code)

	def name2code(self, name):
		return self.cp.NameToCode(name)

	def code2index(self):
		if self.many:
			pair = {}
			for cd in self.code:
				pair[cd] = self.cp.CodeToName(cd)
			return pair
		else:
			return self.cp.CodeToIndex(self.code)

	def get_price_unit(self, base_price, direction_up=True):
		''' 주식/ETF/ELW의 호가 단위를 구한다
			basePrice(long):기준가격
			directionUp(bool[default:true]]):상승의 단위인가의 여부
			반환값(long): 호가단위
		'''
		return self.cp.GetPriceUnit(self.code, base_price, direction_up)














