import pandas as pd

from cp.CpDib.CpSvr8081 import get_cpsvr8081 # 종목 실시간 체결강도
from cp.CpDib.CpSvr8082 import get_cpsvr8082 # 종목/업종별 일별 체결강도
from cp.CpDib.CpSvr8083 import get_cpsvr8083 # 종목/업종 ,선물 시간대별 체결강도
from cp.CpDib.CpSvr8300 import get_cpsvr8300 # 해외지수코드에 대한 과거 데이터
from cp.CpDib.CpSvr8561 import get_cpsvr8561 # 테마테이블
from cp.CpDib.CpSvr8561T import get_cpsvr8561t # 테마별 종목 조회 데이터
from cp.CpDib.CpSvr8562 import get_cpsvr8562 # 종목별 테마 조회
from cp.CpDib.CpSvr8563 import get_cpsvr8563 # 상승율 구분을 두어 상승율 상위 테마 데이터
from cp.CpDib.StockBid import get_stockbid # 주식 종목의 시간대별 체결값
from cp.CpDib.StockIndexIR import get_stockindexir # 업종 코드에 관한 데이터(지수,업종명,거래량,거래 대금)을 1분 간격
from cp.CpDib.StockJpBid2 import get_stockjpbid2 # 주식 종목에 대해 매도,매수에 관한 1차 ~ 10차 호가 , 호가잔량
from cp.CpDib.StockMst import get_stockmst # 주식 종목의 현재가에 관련된 데이터
from cp.CpDib.StockMst2 import get_stockmst2 # 주식 복수 종목에 대해 일괄 조회
from cp.CpDib.StockMstM import get_stockmstm  # 주식 복수 종목에 대해 간단한 내용을 일괄 조회 
from cp.CpDib.StockWeek import get_stockweek 

# print('*'*10, 'get_cpsvr8081 test', '*'*20)
# print('**'*10, 'get_cpsvr8081 test market_kind="코스닥"', '*'*20)
# records = get_cpsvr8081(
#     market_kind='코스닥',
#     order_kind='최근50일*',
#     stock_amount_kind='10만주*',
#     fields=['종목코드', '종목명', '전일대비', '전일대비율', '현재가', '거래량', '체결강도*'],
# )
# print(pd.DataFrame(records))
# print('**'*10, 'get_cpsvr8081 test market_kind="관리"', '*'*20)
# records = get_cpsvr8081(
#     market_kind='관리',
#     order_kind='최근50일*',
#     stock_amount_kind='10만주*',
#     fields=['종목코드', '종목명', '전일대비', '전일대비율', '현재가', '거래량', '체결강도*'],
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_cpsvr8082 test', '*'*20)
# print('**'*10, 'get_cpsvr8082 test recent_days="60개"', '*'*20)
# records = get_cpsvr8082(
#     code='A093640', # 종목코드 or 업종코드
#     recent_days='60개*', # 최근일수 구분:[20*, 60*, 120*]
#     fields = ['일자', '체결*', '주가', '전일*', '거래량']
# )
# print(pd.DataFrame(records))
# print('**'*10, 'get_cpsvr8082 test recent_days="120개"', '*'*20)
# records = get_cpsvr8082(
#     code='A093640', # 종목코드 or 업종코드
#     recent_days='120개*', # 최근일수 구분:[20*, 60*, 120*]
#     fields = ['일자', '체결*', '주가', '전일*', '거래량']
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_cpsvr8083 test', '*'*20)
# print('**'*10, 'get_cpsvr8083 test recent_minutes="60개"', '*'*20)
# records = get_cpsvr8083(
#     code='A093640', # 종목/업종/선물 코드
#     recent_minutes='60개의최근분수', # 최근분수 구분
#     fields= ['시간', '체결강도*', '주가', '전일대비*', '거래량'] 
# )
# print(pd.DataFrame(records))
# print('**'*10, 'get_cpsvr8082 test recent_minutes="150개"', '*'*20)
# records = get_cpsvr8083(
#     code='A093640', # 종목/업종/선물 코드
#     recent_minutes='150개의최근분수', # 최근분수 구분
#     fields= ['시간', '체결강도*', '주가', '전일대비*', '거래량'] 
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_cpsvr8300 test', '*'*20)
# print('**'*10, 'get_cpsvr8300 test period="월"', '*'*20)
# records = get_cpsvr8300(
#     code='BHI', # 해외지수코드
#     period='월', # 일/주/월 구분
#     count=10, # 요청개수
#     fields=['날짜', '시가', '고가', '저가', '종가', '거래량']
# )
# print(pd.DataFrame(records))
# print('**'*10, 'get_cpsvr8300 test period="일"', '*'*20)
# records = get_cpsvr8300(
#     code='BHI',
#     fields=['날짜', '시가', '고가', '저가', '종가', '거래량'],
#     period='일',
#     count=10
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_cpsvr8561 test', '*'*20)
# records = get_cpsvr8561()
# print(pd.DataFrame(records))


# print('*'*10, 'get_cpsvr8561t test', '*'*20)
# records = get_cpsvr8561t(
#     tcode=346,
#     fields=['종목코드','종목명','현재가','대비','대비율','거래량','전일동시간대비']
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_cpsvr8562 test', '*'*20)
# records = get_cpsvr8562(
#     code='A078070',
#     fields=['테마코드', '테마명']
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_cpsvr8563 test', '*'*20)
# print('**'*10, 'get_cpsvr8563 test inc_kind="5일대비상승율상위순"', '*'*20)
# records = get_cpsvr8563(
#   inc_kind='5일대비상승율상위순', # 상승율 구분:[전일대비상승율상위순, ~하위순, 5일대비~, 상승종목비율상위, ~하위]
#   fields=[
#       '테마코드', '테마명', '구성종목수', '*일전대비', '상승종목수', '하락종목수', '상승종목비율'
#   ]
# )
# print(pd.DataFrame(records))
# print('**'*10, 'get_cpsvr8563 test inc_kind="전일대비상승율상위순"', '*'*20)
# records = get_cpsvr8563(
#   inc_kind='전일대비상승율상위순', # 상승율 구분:[전일대비상승율상위순, ~하위순, 5일대비~, 상승종목비율상위, ~하위]
#   fields=[
#       '테마코드', '테마명', '구성종목수', '*일전대비', '상승종목수', '하락종목수', '상승종목비율'
#   ]
# )
# print(pd.DataFrame(records))



# print('*'*10, 'get_stockbid test', '*'*20)
# print('**'*10, 'get_stockbid test contract_type="체결가비교방식"', '*'*20)
# records = get_stockbid(
#     code='A078070', # 종목코드
#     count=10, # 요청개수: 최대80
#     contract_type='체결가비교방식', # 체결 비교 방식: [체결가비교방식, 호가비교방식]
#     addons=['종목코드', '누적*', '체결*'],
#     fields=[
#         '시각', '전일대비', '매도호가', '매수호가', '현재가', '거래량', '순간체결량', '체결상태', '체결강도', '시각(초)', '장구분플래그'
#     ]
# )
# print('**'*10, 'get_stockbid test contract_type="호가비교방식"', '*'*20)
# print(pd.DataFrame(records))
# records = get_stockbid(
#     code='A078070', # 종목코드
#     count=10, # 요청개수: 최대80
#     contract_type='호가비교방식', # 체결 비교 방식: [체결가비교방식, 호가비교방식]
#     addons=['종목코드', '누적*', '체결*'],
#     fields=[
#         '시각', '전일대비', '매도호가', '매수호가', '현재가', '거래량', '순간체결량', '체결상태', '체결강도', '시각(초)', '장구분플래그'
#     ]
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_stockindexir test', '*'*20)
# records = get_stockindexir(
#     ucode='006', # 업종코드
#     fields=[
#         '시간', '지수', '전일대비', '거래량', '거래대금'
#     ]
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_stockjpbid2 test', '*'*20)
# record = get_stockjpbid2(
#     code='A078070', # 종목코드
#     addons=['종목코드', '시각', '총매도잔량*', '시간외*'],
#     fields=['*호가', '*잔량', '*대비']
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_stockmst test', '*'*20)
# records = get_stockmst(
#     code='A078070', # 종목코드
#     fields=[
#         '종목코드', '종목명', '대신업종코드', '그룹코드', '시간', '소속구분', '대중소', '*한가', '*호가', '52*',
#         '누적거래대금', '관리구분', '거래정지구분', '불성실*', '누적*',
#     ]
# )
# print(pd.DataFrame([records]))


# print('*'*10, 'get_stockmst2 test', '*'*20)
# records = get_stockmst2(
#     codes=['A078070', 'A093640'], # 종목코드
#     fields=[
#         '종목코드', '종목명', '시간', '현재가', '전일대비', '시가', '고가', '저가', '매도호가', '매수호가',
#         '거래*', '상장주식수',
#     ]
# )
# print(pd.DataFrame(records))


# print('*'*10, 'get_stockmstm test', '*'*20)
# records = get_stockmstm(
#     codes=['A003540','A000060','A000010'],
#     fields = [
#         '종목코드', '종목명', '대비', '대비구분코드', '현재가', '매도호가', '매수호가', '거래량', '장구분플래그', '예상*'
#     ]
# )
# print(pd.DataFrame(records))


print('*'*10, 'get_stockweek test', '*'*20)
records = get_stockweek(
	code = 'A003540',
	fields=[
		'일자', '시가', '고가', '저가', '종가', '전일대비', '누적거래량',
		'외인*', '등락률', '대비부호', '기관*', '시간외*'
	],
	pages=100
)
df = pd.DataFrame(records)
print(df)
df.to_excel("GETSTOCKWEEK.xlsx")
















