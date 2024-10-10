OK_FORMAT = True

test = {   'name': 'q4-2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest = hashlib.sha256(pickle.dumps(ans42)).hexdigest()\n'
                                               ">>> assert digest == '5554c0894f754ebeb25374653014a35c0a74ccd1c41f951e0dc40d4ec29682a8'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
