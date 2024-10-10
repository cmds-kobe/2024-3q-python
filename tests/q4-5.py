OK_FORMAT = True

test = {   'name': 'q4-5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest1 = hashlib.sha256(pickle.dumps(ans45.values)).hexdigest()\n'
                                               ">>> assert digest1 == '2b2def3827e01487d9cfe042f291b25678a713d3c2016790a0886f661002bd55'\n"
                                               '>>> digest2 = hashlib.sha256(pickle.dumps(ans45_summary.values)).hexdigest()\n'
                                               ">>> assert digest2 == '025b5b9fb982f458387d116aa4e994b811e7e5521ea033e6979ac7faaf6f2d0f'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
