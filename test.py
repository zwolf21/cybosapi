import pandas as pd
from cp.CpSysDib.MarketEye import get_marketeye
from cp.CpSysDib.StockChart import get_stockchart
from cp.CpDib.StockMst import get_stockmst
from cp.CpDib.StockMstM import get_stockmstm
from cp.CpDib.StockMst2 import get_stockmst2
from cp.CpDib.StockCur import get_stockcur
from cp.CpDib.StockJpBid import get_stockjpbid
from cp.CpDib.StockBid import get_stockbid
from cp.CpDib.StockWeek import get_stockweek
from cp.CpDib.CpSvr7819C import get_cpsvr7819c
from cp.CpDib.StockIndexIR import get_stockindexir
from cp.CpUtil.CpCodeMgr import CpCodeManager, get_stocklist_by_market
from cp.CpUtil.CpUsCode import get_us_code_list, uscode2name
from cp.CpUtil.CpStockCode import CpStockCode, get_code_table, get_count
from cp.CpSysDib.CpMarketWatch import get_stockmarket_watch
from cp.CpDib.CpSvr8300 import get_cpsvr8300
from cp.CpDib.CpSvr8561 import get_cpsvr8561 #테마 리스트
from cp.CpDib.CpSvr8562 import get_cpsvr8562 #테마코드 종목별 매핑
from cp.CpDib.CpSvr8561T import get_cpsvr8561t #테마코드별 종목 조회

# r = get_marketeye(
# 	code='A003540', field=['현재가', 'PER', '최근분기년월', 'EPS', '결산년월', 'BPS', '시간', '당일*'], 
# 	contract='호가비교방식'
# )

# print(pd.DataFrame(r))

# r = get_marketeye(
# 	code='A003540', field=['현재가', 'PER', 'EPS', '최근분기년*'], 
# 	contract='체결가비교방식'
# )

# print(pd.DataFrame(r))


# for row in r:
# 	print(row)


# r = get_stockchart(
# 	code = 'A003540',
# 	reqgb = '기간',
# 	start_date = '20161020',
# 	end_date = '20161031',
# 	count = 10,
# 	field = ['날짜', '시가', '*가', '거래량',],
# 	chart = '일',
# 	stockadj = '수정',
# 	extras = ['code', '*한가']
# )

# print(pd.DataFrame(r))


# r = get_stockmst(
# 	code = 'A003540',
# 	fields = [
# 		'종목코드', '종목명', 'EPS', 'BPS', 'PER', '신고가', '기준가', '52주최고가', '52주최고일', '52주최저일',
# 		'액면가', '신용잔고비율', '외국인DATA일자', '외국인*'
# 	]
# )
# print(r)

# r = get_stockmstm(
# 	code= ['A003540','A000060','A000010'],
# 	fields = [
# 		'종목코드', '종목명', '대비', '대비구분코드', '현재가', '매도호가', '매수호가', '거래량', '장구분플래그', '예상*'
# 	]
# )
# for row in r:
# 	print(row)

# print('='*50)
# r = get_stockcur(code='A003540')
# print(r)


# import pythoncom
# import time
# while 1:
# 	pythoncom.PumpWaitingMessages()
# 	time.sleep(0.1)
# 	print('wating...')
# r = get_stockmst2(code=['A003045'], fields=['종목코드', '종목명', '시간'])

# for row in r:
# 	print(row)

# r = get_stockjpbid2(
# 	code='A000060',
# 	fields = ['종목코드', '시간', '거래량', '총매도잔량']
# )

# print(r)

# r = get_stockbid(
# 	code = 'A000060',
# 	types = ['*'],
# 	count = 10,
# 	fields = ['*'],
# )
# for row in r:
# 	print(row)

# r = get_stockweek(
# 	code= 'A00060',
# 	fields = ['*'],
# 	extras=['날짜','*']
# )
# for row in r:
# 	print(row)

# 안됨
# r = get_cpsvr7819c(kind='미수금잔고', period='1년', fields=['*'])
# for row in r:
# 	print(row)

# r = get_stockindexir(fields=['*'], ucode='U005')

# for row in r:
# 	print(row)

# r = get_stocklist_by_market(type='코스닥')
# print(r)

# r = get_codemap(type='거래소')
# print(r)

# cpm = CpCodeManager('A011070')
# print(cpm.name)
# print(cpm.industry_name)
# print(cpm.stock_market_kind)
# print(cpm.stock_control_kind)
# print(cpm.stock_kospi200_kind)
# print(cpm.stock_section_kind)
# print(cpm.market_start_time)
# print(cpm.market_end_time)
# print(cpm.stock_meme_min)
# print(cpm.stock_industry_code)
# print(cpm.stock_capital)
# print(cpm.stock_group_code)
# print(cpm.stock_lac_kind)
# print(cpm.stock_listed_date)
# print(cpm.is_stock_credit_enable)
# print(cpm.stock_parprice_change_type)

# r = get_stock_elw_basket_comp_list('Q590001')
# print(r)


# r = get_us_code_list('전종목')
# print(r)

# r = uscode2name(r)
# print(r)

# ctk = CpStockCode('Q590001')
# print(ctk.code2name())
# print(ctk.code2index())
# print(get_count())

# print(get_code_table())
# r = get_stockmarket_watch(code='*', field=['종목뉴스', '공시정보'])
# for row in r:
# 	print(row)

# r = get_cpsvr8300(code='BHI', fields=['*'], period='월', count=5)
# df = pd.DataFrame(r)
# print(df)



# r = get_stockindexir(ucode='006', fields=['*'])
# for row in r:
# 	print(row)

# r = get_cpsvr8561()
# for row in r:
# 	print(row)

# r = get_cpsvr8561t(tcode=346)
# for row in r:
# 	print(row)


r = get_stocklist_by_market(type='거래소'
)
print(r)