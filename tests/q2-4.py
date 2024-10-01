OK_FORMAT = True

test = {   'name': 'q2-4',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> result = divide_groups(30, 5)\n>>> assert result == (6, 0), f'期待する結果: (6, 0), 実際の結果: {result}'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> result = divide_groups(31, 5)\n>>> assert result == (7, 1), f'期待する結果: (7, 1), 実際の結果: {result}'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> result = divide_groups(20, 1)\n>>> assert result == (20, 0), f'期待する結果: (20, 0), 実際の結果: {result}'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> result = divide_groups(15, 15)\n>>> assert result == (1, 0), f'期待する結果: (1, 0), 実際の結果: {result}'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> result = divide_groups(7, 10)\n>>> assert result == (1, 7), f'期待する結果: (1, 7), 実際の結果: {result}'\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
