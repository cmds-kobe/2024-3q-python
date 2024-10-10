OK_FORMAT = True

test = {   'name': 'q4-3v2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest = hashlib.sha256(pickle.dumps(ans43.values)).hexdigest()\n'
                                               ">>> assert digest == 'c51a71eed44a0fc2e6bd8a7da5b29e31cdc177f31984ebd902dd1cc1000c9a0f'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
