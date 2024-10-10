OK_FORMAT = True

test = {   'name': 'q6-7',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans67_digest = hashlib.sha256(pickle.dumps(ans67)).hexdigest()\n'
                                               ">>> assert ans67_digest == '6408ae322b2b09ae588845054fe23bddee3435b8a92a368db8d1d7ffea2e86e8'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
