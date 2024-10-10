OK_FORMAT = True

test = {   'name': 'q7-4v2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle\n'
                                               '>>> import hashlib\n'
                                               '>>> ans74_c_digest = hashlib.sha256(pickle.dumps(ans74_c)).hexdigest()\n'
                                               ">>> assert ans74_c_digest == '7fcbcd12d9a1df49186dbda3fc607a2c760dc46aba3ccf99c469dc34d52c01ef'\n"
                                               '>>> ans74_m_digest = hashlib.sha256(pickle.dumps(ans74_m)).hexdigest()\n'
                                               ">>> assert ans74_m_digest == 'df47eaa3ab5f106d6c354bcd4d1398443c7e8c9b69412515e3dc47dbbc7567dc'\n"
                                               '>>> ans74_s_digest = hashlib.sha256(pickle.dumps(ans74_s)).hexdigest()\n'
                                               ">>> assert ans74_s_digest == 'b123511fcb968b68fac70193102847fd2caed71bfe2a5b3faa93052e6fd76d60'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
