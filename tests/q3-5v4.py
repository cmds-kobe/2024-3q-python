OK_FORMAT = True

test = {   'name': 'q3-5v4',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert scan_rates == '0.001 0.002 0.001 0.003 0.002'\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.array_equal(rates, np.array([0.001, 0.002, 0.001, 0.003, 0.002]))\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> assert np.array_equal(np.round(after_one_year, decimals=3), np.array([10000.1, 10000.2, 10000.1, 10000.3, 10000.2]))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
