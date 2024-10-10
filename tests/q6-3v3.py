OK_FORMAT = True

test = {   'name': 'q6-3v3',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> assert ans63_shape == (1186, 2)\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               ">>> assert hashlib.sha256(pickle.dumps(ans63.values)).hexdigest() == 'f354695bb3e8f02828c8b828bc66c4b3e10763f669175ced238054414ae4277f'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
