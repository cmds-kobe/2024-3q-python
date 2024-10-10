OK_FORMAT = True

test = {   'name': 'q6-2v2',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> assert ans62_shape == (2372, 6)\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans62_digest = hashlib.sha256(pickle.dumps(ans62.values)).hexdigest()\n'
                                               ">>> assert ans62_digest == 'e8f7d433441a282bde9c117e7ce8f6cb29cf21b0340f0100ed8357a247d80a26'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
