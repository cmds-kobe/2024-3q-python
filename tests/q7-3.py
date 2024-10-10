OK_FORMAT = True

test = {   'name': 'q7-3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans73_c_digest = hashlib.sha256(pickle.dumps(ans73_c)).hexdigest()\n'
                                               ">>> assert ans73_c_digest == '6e25b5d122091010dcadfa93b39a04fd00c6ee41de6234be967e1d83dac74f84'\n"
                                               '>>> ans73_digest = hashlib.sha256(pickle.dumps(ans73)).hexdigest()\n'
                                               ">>> assert ans73_digest == 'bf684a8b320ae00ec80f69d9439b00f8a8a4c8bd9837534c6970d0a24b54d632'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
