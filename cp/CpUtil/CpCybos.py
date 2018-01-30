import win32com.client

DESCRIPTION = {

'summary': '연결상태',

'point': '''

	-value = CpCybos.IsConnect

	(읽기전용) CYBOS의 통신 연결상태를 반환 합니다

	반환값: 0- 연결 끊김, 1- 연결 정상

   '''
}

MODULE_NAME = 'CpUtil.CpCybos'

def is_connected():
	cp = win32com.client.Dispatch(MODULE_NAME)
	retmap = {
		0: '연결끊김',
		1: '연결정상',
	}
	value = cp.IsConnect
	return retmap.get(value)

def get_server_type():
	cp = win32com.client.Dispatch(MODULE_NAME)
	retmap = {
		0: '연결끊김',
		1: 'CYBOSPLUS',
		2: 'HTS',
	}
	value = cp.IsConnect
	return retmap.get(value)

def get_limit_request_remain_time():
	'''요청 개수를 재계산하기까지 남은 시간을 반환합니다. 즉 리턴한 시간동안 남은 요청개수보다 더 요청하면 요청제한이 됩니다
	'''
	cp = win32com.client.Dispatch(MODULE_NAME)
	return cp.LimitRequestRemainTime
	
def get_limit_remain_count(limit_type=2):
	'''요청 개수를 재계산하기까지 남은 시간을 반환합니다. 즉 리턴한 시간동안 남은 요청개수보다 더 요청하면 요청제한이 됩니다
	'''
	cp = win32com.client.Dispatch(MODULE_NAME)
	return cp.GetLimitRemainCount(limit_type)
