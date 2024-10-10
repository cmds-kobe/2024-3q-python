OK_FORMAT = True

test = {   'name': 'q6-1',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> assert ans61_shape == (5848, 10)\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans61_digest = pickle.dumps(ans61.values)\n'
                                               '>>> ans61_digest = hashlib.sha256(ans61_digest).hexdigest()\n'
                                               ">>> assert ans61_digest == 'afe1d5af40cc8260736ce0c3092755b4b42e36b112f8a75c9df57f0988b9a618'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
