OK_FORMAT = True

test = {   'name': 'q4-1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest = hashlib.sha256(pickle.dumps(ans41)).hexdigest()\n'
                                               ">>> assert digest == '7a9c733c8062a703fcca49b841d4553a0f7e4c58095ccfb057e4ba4ad03296cb'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
