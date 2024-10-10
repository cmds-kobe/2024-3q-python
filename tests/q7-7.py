OK_FORMAT = True

test = {   'name': 'q7-7',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans77_model_digest = hashlib.sha256(pickle.dumps(ans77_model)).hexdigest()\n'
                                               ">>> assert ans77_model_digest == '1a48107615d99c3433c397904f286d0e859e1147bc10fdc51f5ccacfc486debd'\n"
                                               '>>> ans77_ytest_digest = hashlib.sha256(pickle.dumps(ans77_ytest)).hexdigest()\n'
                                               ">>> assert ans77_ytest_digest == '999be15539009bf3762ec619388c99cfa7f2c0d96215acecc1227f6bcbbc7a2b'\n"
                                               '>>> ans77_ypred_digest = hashlib.sha256(pickle.dumps(ans77_ypred)).hexdigest()\n'
                                               ">>> assert ans77_ypred_digest == '6127ca42a8275219c119c9bc1bf82691a6d81d8b22aa612473e1c9f4bad565f0'\n"
                                               '>>> ans77_yprob_digest = hashlib.sha256(pickle.dumps(ans77_yprob)).hexdigest()\n'
                                               ">>> assert ans77_yprob_digest == '7ead0e5c1090ee7250cb901673659605a80bd16c197386045200af0fcf21828e'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
