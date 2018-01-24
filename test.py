from cp.CpSysDib.MarketEye import get_marketeye
from cp.CpSysDib.StockChart import get_stockchart
from cp.CpDib.StockMst import get_stockmst
from cp.CpDib.StockMstM import get_stockmstm
from cp.CpDib.StockMst2 import get_stockmst2
from cp.CpDib.StockCur import get_stockcur

# r = get_marketeye(
# 	code='A003540', field=['현재가', 'PER', '최근분기년월', 'EPS', '결산년월', 'BPS'], 
# 	# contract='체결가비교*'
# )

# for row in r:
# 	print(row)


# r = get_stockchart(
# 	code = 'A003540',
# 	reqgb = '기간',
# 	start_date = '20161020',
# 	end_date = '20161031',
# 	count = 10,
# 	field = ['날짜', '시가', '고가', '저가', '종가', '거래량',],
# 	chart = '일',
# 	stockadj = '수정',
# 	extras = ['code', '상한가', '하한가']
# )

# for row in r:
# 	print(row)


# r = get_stockmst(
# 	code = 'A003540',
# 	fields = [
# 		'종목코드', '종목명', 'EPS', 'BPS', 'PER', '신고가', '기준가', '52주최고가', '52주최고일', '52주최저일',
# 		'액면가', '신용잔고비율', '외국인DATA일자', '외국인상장주식수', '외국인한도수량', '외국인한도비율',
# 	]
# )
# print(r)

# r = get_stockmstm(
# 	code= ['A003540','A000060','A000010'],
# 	fields = [
# 		'종목코드', '종목명', '대비', '대비구분코드', '현재가', '매도호가', '매수호가', '거래량', '장구분플래그',
# 		'예상체결가', '예상체결가전일대비', '예상체결수량'
# 	]
# )

# for row in r:
# 	print(row)
# r = get_stockcur(code='A000060')
# print(r)


r = get_stockmst2(code=['A003045'], fields=['종목코드', '종목명'])