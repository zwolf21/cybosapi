import pandas as pd

from cp.core import naver_upjong

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


def get_theme_table(count=None):
	theme_list = get_cpsvr8561()
	if count is not None:
		theme_list = theme_list[:count]
	themes = []
	for theme in theme_list:
		theme_cd = theme['테마코드']
		code_list = get_cpsvr8561t(tcode=theme_cd)
		for codeset in code_list:
			codeset.update(theme)
			themes.append(codeset)
	return themes


def get_base_records():
	theme_df = pd.DataFrame(get_theme_table())
	code_df = pd.DataFrame(get_code_table())
	base_df = pd.merge(code_df, theme_df, how='left')

	def get_code_annotation(code):
		ccm = CpCodeManager(code)
		annotate = {
			'부구분': ccm.stock_section_kind,
			'소속부': ccm.stock_market_kind,
		}
		return annotate

	annomap = {cd: get_code_annotation(cd) for cd in base_df['종목코드']}

	base_df['부구분'] = base_df['종목코드'].apply(lambda cd: annomap[cd]['부구분'])
	base_df['소속부'] = base_df['종목코드'].apply(lambda cd: annomap[cd]['소속부'])
	base_df['표준종목코드'] = base_df['종목코드'].str[1:]

	nupjong_df = pd.DataFrame(naver_upjong.scrap())
	base_df = pd.merge(base_df, nupjong_df, how='left')
	return base_df








