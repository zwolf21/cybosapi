import win32com.client

from ..utils import *

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
