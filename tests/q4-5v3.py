OK_FORMAT = True

test = {   'name': 'q4-5v3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import hashlib\n'
                                               '>>> \n'
                                               '>>> def df2digest(df):\n'
                                               "...     return hashlib.sha256(str(tuple(df.values.tolist())).encode('utf-8')).hexdigest()\n"
                                               ">>> assert df2digest(ans45) == 'b456932849c966386d2a738e80966680d020753792ef13295da8beb59af41b15'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> \n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
