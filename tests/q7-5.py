OK_FORMAT = True

test = {   'name': 'q7-5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def df2digest(df):\n'
                                               "...     return hashlib.sha256(str(tuple(df.values.tolist())).encode('utf-8')).hexdigest()\n"
                                               ">>> assert df2digest(ans75_s) == 'bf96610b450afe0d459e90333a44a8e28f6efccc829a90146ac17ade98473e7b'\n"
                                               ">>> assert df2digest(ans75_c) == '75505ecf234c265ad233561a8ce94047cbe347e42008b2dc211e31ecfe940c64'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
