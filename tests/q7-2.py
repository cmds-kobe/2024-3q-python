OK_FORMAT = True

test = {   'name': 'q7-2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> ans72 = [int(x) for x in ans72]\n'
                                               '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans72_digest = hashlib.sha256(pickle.dumps(ans72)).hexdigest()\n'
                                               ">>> assert ans72_digest == '70a9f96fd5af1a8bd7dbaa1af09c7f3f876165759fae9bd6758b55569519ec38'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
