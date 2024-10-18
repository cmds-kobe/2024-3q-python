OK_FORMAT = True

test = {   'name': 'q7-4v3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans74_c_digest = hashlib.sha256(pickle.dumps(ans74_c)).hexdigest()\n'
                                               ">>> assert ans74_c_digest == '7fcbcd12d9a1df49186dbda3fc607a2c760dc46aba3ccf99c469dc34d52c01ef'\n"
                                               '>>> ans74_m_digest = hashlib.sha256(pickle.dumps(ans74_m)).hexdigest()\n'
                                               ">>> assert ans74_m_digest == 'a57bf6de186489af3761c22cecd21722f79813fc127799f1a150f76c66caab65'\n"
                                               '>>> ans74_s_digest = hashlib.sha256(pickle.dumps(ans74_s)).hexdigest()\n'
                                               ">>> assert ans74_s_digest == 'e880564cc046cf1721bba3a8e3ca9a014f1242e74eedda9055133368feefae85'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
