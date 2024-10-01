OK_FORMAT = True

test = {   'name': 'q2-5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> x = complex(3, 4)\n'
                                               '>>> y = complex(1, 2)\n'
                                               '>>> (sum, dif, pro, quo) = complex_operations(x, y)\n'
                                               '>>> assert sum == 4 + 6j\n'
                                               '>>> assert dif == 2 + 2j\n'
                                               '>>> assert pro == -5 + 10j\n'
                                               '>>> assert round(quo.real, 1) == 2.2\n'
                                               '>>> assert round(quo.imag, 1) == -0.4\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> x = complex(1, 1)\n'
                                               '>>> y = complex(2, 0)\n'
                                               '>>> (sum, dif, pro, quo) = complex_operations(x, y)\n'
                                               '>>> assert sum == 3 + 1j\n'
                                               '>>> assert dif == -1 + 1j\n'
                                               '>>> assert pro == 2 + 2j\n'
                                               '>>> assert round(quo.real, 1) == 0.5\n'
                                               '>>> assert round(quo.imag, 1) == 0.5\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> x = complex(1, 1)\n'
                                               '>>> y = complex(0, 0)\n'
                                               '>>> (sum, dif, pro, quo) = complex_operations(x, y)\n'
                                               '>>> assert sum == 1 + 1j\n'
                                               '>>> assert dif == 1 + 1j\n'
                                               '>>> assert pro == 0j\n'
                                               ">>> assert quo == '定義されていません'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
