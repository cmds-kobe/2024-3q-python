OK_FORMAT = True

test = {   'name': 'q7-5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans75_s_digest = hashlib.sha256(pickle.dumps(ans75_s)).hexdigest()\n'
                                               ">>> assert ans75_s_digest == 'a14e70886f3549518856ed964741650a83a16399244ee4c31d8750c25e9cf3bb'\n"
                                               '>>> ans75_c_digest = hashlib.sha256(pickle.dumps(ans75_c)).hexdigest()\n'
                                               ">>> assert ans75_c_digest == '44c4e07020ab892adae65f1ad87b85def10d3dce73802ae780ba4014850626bb'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
