OK_FORMAT = True

test = {   'name': 'q2-7',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert draw_pyramid(1) == '1'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> expected_output = '1\\n11\\n111'\n>>> assert draw_pyramid(3) == expected_output\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> expected_output = '1\\n11\\n111\\n1111\\n11111'\n>>> assert draw_pyramid(5) == expected_output\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert draw_pyramid(0) == ''\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
