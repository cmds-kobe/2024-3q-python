OK_FORMAT = True

test = {   'name': 'q7-8',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans78_prob_digest = hashlib.sha256(pickle.dumps(ans78_prob)).hexdigest()\n'
                                               ">>> assert ans78_prob_digest == '5cd3791bc9cdc506d3a3efa5cf2e2554c253f1f87f17939717b02f1bb6446035'\n"
                                               '>>> ans78_fi_digest = hashlib.sha256(pickle.dumps(ans78_fi)).hexdigest()\n'
                                               ">>> assert ans78_fi_digest == '8d1e1b6c324baa06e071bdd9d56f736270b1f31aa2757ba04cb00787a4b4b5f6'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
