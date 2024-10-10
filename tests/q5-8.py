OK_FORMAT = True

test = {   'name': 'q5-8',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans58\n'
                                               '>>> ax = result.get_axes()[0]\n'
                                               '>>> bars = ax.containers[0]\n'
                                               '>>> heights = []\n'
                                               '>>> for b in bars:\n'
                                               '...     heights.append(b.get_height())\n'
                                               '>>> assert heights == [1.0, 15.0, 22.0, 38.0, 20.0, 14.0, 9.0, 34.0, 28.0, 28.0, 30.0, 21.0, 16.0, 37.0, 39.0]\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
