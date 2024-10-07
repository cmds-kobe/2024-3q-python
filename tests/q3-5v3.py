OK_FORMAT = True

test = {   'name': 'q3-5v3',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert scan_rates == '0.001 0.002 0.001 0.003 0.002'\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.array_equal(rates, np.array([0.001, 0.002, 0.001, 0.003, 0.002]))\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> assert np.array_equal(np.round(after_one_year, decimals=3), np.array([1000.01, 1000.02, 1000.01, 1000.03, 1000.02]))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
