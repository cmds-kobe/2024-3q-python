OK_FORMAT = True

test = {   'name': 'q7-1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans71_digest = hashlib.sha256(pickle.dumps(ans71)).hexdigest()\n'
                                               ">>> assert ans71_digest == '5829b150c1e76836916e7af2e0a0dad56e722cbcb2046c9a5839b29d73020a50'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
