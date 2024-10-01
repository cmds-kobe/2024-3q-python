OK_FORMAT = True

test = {   'name': 'q2-8',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = prime_factorization(24)\n'
                                               '>>> assert result == [\'2\', \'2\', \'2\', \'3\'], f"Test 1 Failed: 24の素因数分解が正しくありません。期待値: [\'2\', \'2\', \'2\', \'3\'], 実際の値: {result}"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> result = prime_factorization(60)\n'
                                               '>>> assert result == [\'2\', \'2\', \'3\', \'5\'], f"Test 2 Failed: 60の素因数分解が正しくありません。期待値: [\'2\', \'2\', \'3\', \'5\'], 実際の値: {result}"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> result = prime_factorization(17)\n>>> assert result == [\'17\'], f"Test 3 Failed: 17の素因数分解が正しくありません。期待値: [\'17\'], 実際の値: {result}"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> result = prime_factorization(100)\n'
                                               '>>> assert result == [\'2\', \'2\', \'5\', \'5\'], f"Test 4 Failed: 100の素因数分解が正しくありません。期待値: [\'2\', \'2\', \'5\', \'5\'], 実際の値: {result}"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> result = prime_factorization(2)\n>>> assert result == [\'2\'], f"Test 5 Failed: 2の素因数分解が正しくありません。期待値: [\'2\'], 実際の値: {result}"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> result = prime_factorization(1000000)\n'
                                               '>>> assert result == [\'2\', \'2\', \'2\', \'2\', \'2\', \'2\', \'5\', \'5\', \'5\', \'5\', \'5\', \'5\'], f"Test 7 Failed: '
                                               '1000000の素因数分解が正しくありません。期待値: [\'2\', \'2\', \'2\', \'2\', \'2\', \'2\', \'5\', \'5\', \'5\', \'5\', \'5\', \'5\'], 実際の値: {result}"\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
