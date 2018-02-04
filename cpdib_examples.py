import pandas as pd

from cp.CpDib.CpSvr8081 import get_cpsvr8081 # 종목 실시간 체결강도
from cp.CpDib.CpSvr8082 import get_cpsvr8082 # 종목/업종별 일별 체결강도
from cp.CpDib.CpSvr8083 import get_cpsvr8083 # 종목/업종 ,선물 시간대별 체결강도



print('*'*10, 'get_cpsvr8081 test', '*'*20)
print('**'*10, 'get_cpsvr8081 test market_kind="코스닥"', '*'*20)
records = get_cpsvr8081(
    market_kind='코스닥',
    order_kind='최근50일*',
    stock_amount_kind='10만주*',
    fields=['종목코드', '종목명', '전일대비', '전일대비율', '현재가', '거래량', '체결강도*'],
)
print(pd.DataFrame(records))
print('**'*10, 'get_cpsvr8081 test market_kind="관리"', '*'*20)
records = get_cpsvr8081(
    market_kind='관리',
    order_kind='최근50일*',
    stock_amount_kind='10만주*',
    fields=['종목코드', '종목명', '전일대비', '전일대비율', '현재가', '거래량', '체결강도*'],
)
print(pd.DataFrame(records))



print('*'*10, 'get_cpsvr8082 test', '*'*20)
print('**'*10, 'get_cpsvr8082 test recent_days="60개"', '*'*20)
records = get_cpsvr8082(
    code='A093640', # 종목코드 or 업종코드
    recent_days='60개*', # 최근일수 구분:[20*, 60*, 120*]
    fields = ['일자', '체결*', '주가', '전일*', '거래량']
)
print(pd.DataFrame(records))
print('**'*10, 'get_cpsvr8082 test recent_days="120개"', '*'*20)
records = get_cpsvr8082(
    code='A093640', # 종목코드 or 업종코드
    recent_days='120개*', # 최근일수 구분:[20*, 60*, 120*]
    fields = ['일자', '체결*', '주가', '전일*', '거래량']
)
print(pd.DataFrame(records))



print('*'*10, 'get_cpsvr8083 test', '*'*20)
print('**'*10, 'get_cpsvr8083 test recent_minutes="60개"', '*'*20)
records = get_cpsvr8083(
    code='A093640', # 종목/업종/선물 코드
    recent_minutes='60개의최근분수', # 최근분수 구분
    fields= ['시간', '체결강도*', '주가', '전일대비*', '거래량'] 
)
print(pd.DataFrame(records))
print('**'*10, 'get_cpsvr8082 test recent_minutes="150개"', '*'*20)
records = get_cpsvr8083(
    code='A093640', # 종목/업종/선물 코드
    recent_minutes='150개의최근분수', # 최근분수 구분
    fields= ['시간', '체결강도*', '주가', '전일대비*', '거래량'] 
)
print(pd.DataFrame(records))




