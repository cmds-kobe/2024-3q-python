OK_FORMAT = True

test = {   'name': 'q4-3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> digest = hashlib.sha256(pickle.dumps(ans43)).hexdigest()\n'
                                               ">>> assert digest == 'd3d95cace2e55ffdbd59f7fc4b748d8c9c273c36738748871d7680752c530c76'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
