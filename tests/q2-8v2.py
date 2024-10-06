OK_FORMAT = True

test = {   'name': 'q2-8v2',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> result = prime_factorization(24)\n>>> assert sorted(result) == [2, 2, 2, 3]\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> result = prime_factorization(60)\n>>> assert sorted(result) == [2, 2, 3, 5]\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> result = prime_factorization(17)\n>>> assert sorted(result) == [17]\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> result = prime_factorization(100)\n>>> assert sorted(result) == [2, 2, 5, 5]\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> result = prime_factorization(2)\n>>> assert sorted(result) == [2]\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> result = prime_factorization(12345678901234567890)\n>>> assert sorted(result) == [2, 3, 3, 5, 101, 3541, 3607, 3803, 27961]\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
