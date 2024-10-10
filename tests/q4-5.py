OK_FORMAT = True

test = {   'name': 'q4-5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest1 = hashlib.sha256(pickle.dumps(ans45)).hexdigest()\n'
                                               ">>> assert digest1 == '06c542ce695470b58991605424050e01dee31a091097c199a8175bab40ab7a21'\n"
                                               '>>> digest2 = hashlib.sha256(pickle.dumps(ans45_summary)).hexdigest()\n'
                                               ">>> assert digest2 == 'c5525be848f7a76072208742319aafae18000b86265b15f0f51fb10d1fdabd52'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
