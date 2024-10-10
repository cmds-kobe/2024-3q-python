OK_FORMAT = True

test = {   'name': 'q4-2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest = hashlib.sha256(pickle.dumps(ans42.values)).hexdigest()\n'
                                               ">>> assert digest == '726b1b89adcb2b0a3a8103915de96a2f0378a168d078dfbca8693a6e11daeaed'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
