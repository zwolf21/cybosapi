
DESCRIPTION = {
	'summary': '증시 자금 동향 데이터 를 요청하고 수신 7819'
	'point': '''
 -CpSvr7819C 화면이 6개월 1년으로 기간 자금 동향을 알 수 있어 의미 있으므로 생략해야할 모듈

 '''
}

MODULE_NAME = 'dscbo1.CpSvr8082'

METHODS_INTERFACES = {

	'SetInputValue': {
		'code': {
			'position': 0,
			'type': ['str'],
			'essential': True,
		},
		'recent_period': {
			'position': 1,
			'type': ['char'],
			'essential': True,
			'options': {
				ord('1'): '20개의최근일수',
				ord('2'): '60개의최근일수',
				ord('3'): '120개의최근일수',
			},
		},
	},
	'GetHeaderValue': {
		'type': {
			'position': 0,
			'type': ['long'],
			'essential': True,
			'options': {
				0: 'rows',
			},
		}
	},
	'GetDataValue': {
		'type': {
			'position': 0,
			'type': ['long'],
			'essential': True,
			'options': {
				0: '일자',
				1: '수치',
				3: '전일대비',
			},
		},
		'index': {
			'position': 1,
			'type': ['long'],
			'essential': True,
		},
	},	
}
