OK_FORMAT = True

test = {   'name': 'q6-2v3',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> assert ans62_shape == (2372, 6)\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def df2digest(df):\n'
                                               "...     return hashlib.sha256(str(tuple(ans61.values.tolist())).encode('utf-8')).hexdigest()\n"
                                               ">>> assert df2digest(ans62) == 'd4795f707932a570a380160382ca9d1443e45b59850dab7001d039a0dafb3430'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> \n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}