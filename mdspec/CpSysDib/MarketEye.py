
DESCRIPTION = {
	'summary': '',
	'point': '''
	'''
}

SetInputValue = {
	'args': {
		0: {
			'type': ['long', ['long']],
			'name': 'fields',
			'options': {
				0: '종목코드',
				1: '시간',
			}
		},
		1: {
			'type': ['string', ['string']],
			'name': 'code',
			'options': None,
		},
		2: {
			'type': ['char'],
			'name': 'contract_compare_method',
			'options': {
				ord('1'): '체결가비교방식',
				ord('2'): '호가비교방식'
			}
		}
	}
}

SetHeaderValue = {
	'args': {
		0: {
			'type': ['long'],

		}
	}
}
