OK_FORMAT = True

test = {   'name': 'q6-2v3',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> assert ans62_shape == (2372, 6)\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def df2digest(df):\n'
                                               "...     return hashlib.sha256(str(tuple(df.values.tolist())).encode('utf-8')).hexdigest()\n"
                                               ">>> assert df2digest(ans62) == '8f3c51770fb6b5dbc351044e3b8e608faf4d2749bd92d8b284731b21ec0b5b18'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
