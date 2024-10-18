OK_FORMAT = True

test = {   'name': 'q6-7v4',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def df2digest(df):\n'
                                               "...     return hashlib.sha256(str(tuple(df.values.tolist())).encode('utf-8')).hexdigest()\n"
                                               ">>> assert df2digest(ans67) == '37bdec84735c89e5928333b299c9742d53ddb4f57edc113b40caa63c72579aea'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
