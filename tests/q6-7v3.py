OK_FORMAT = True

test = {   'name': 'q6-7v3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans67_digest = hashlib.sha256(pickle.dumps(ans67.values)).hexdigest()\n'
                                               ">>> assert ans67_digest == '711520e47093df224145a8eb710b0c11f761f88a8502dca4ff9e4690373cd08d'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
