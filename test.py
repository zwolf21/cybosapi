from cp.CpSysDib.MarketEye import get_marketeye
from cp.CpSysDib.StockChart import get_stockchart

r = get_marketeye(
	code='A003540', field=['현재가', 'PER', '최근분기년월', 'EPS', '결산년월', 'BPS'], 
	# contract='체결가비교*'
)

for row in r:
	print(row)


r = get_stockchart(
	code = 'A003540',
	reqgb = '기간',
	start_date = '20161020',
	end_date = '20161031',
	count = 10,
	field = ['날짜', '시가', '고가', '저가', '종가', '거래량',],
	chart = '일',
	stockadj = '수정',
	extras = ['code', '상한가', '하한가']
)

for row in r:
	print(row)