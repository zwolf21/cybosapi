import win32com.client

from ..utils import *

DESCRIPTION = {

'summary': '연결상태',

'point': '''

	-value = CpCybos.IsConnect

(읽기전용) CYBOS의 통신 연결상태를 반환 합니다

반환값: 0- 연결 끊김, 1- 연결 정상

   '''

}

