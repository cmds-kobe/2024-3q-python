OK_FORMAT = True

test = {   'name': 'q6-3v4',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> assert ans63_shape == (1186, 2)\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def df2digest(df):\n'
                                               "...     return hashlib.sha256(str(tuple(df.values.tolist())).encode('utf-8')).hexdigest()\n"
                                               ">>> assert df2digest(ans63) == '9e8a85e38e8a2707422eeb5385465e963e60a955ee1ad709fb1dc1805cac6e50'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
