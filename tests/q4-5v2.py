OK_FORMAT = True

test = {   'name': 'q4-5v2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest1 = hashlib.sha256(pickle.dumps(ans45.values)).hexdigest()\n'
                                               ">>> assert digest1 == 'd7e8ce52861ae1cb7ba72dd902093eb1e0f5be4f7d0a2deb0c1f607a6119fcef'\n"
                                               '>>> digest2 = hashlib.sha256(pickle.dumps(ans45_summary.values)).hexdigest()\n'
                                               ">>> assert digest2 == '025b5b9fb982f458387d116aa4e994b811e7e5521ea033e6979ac7faaf6f2d0f'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
