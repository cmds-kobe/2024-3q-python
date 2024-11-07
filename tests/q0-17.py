OK_FORMAT = True

test = {   'name': 'q0-17',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans17\n'
                                               '>>> assert len(result.get_axes()) > 0\n'
                                               '>>> axes = result.get_axes()[0]\n'
                                               '>>> lines = axes.get_lines()\n'
                                               '>>> x_data = lines[0].get_xdata()\n'
                                               '>>> y_data = lines[0].get_ydata()\n'
                                               '>>> expected_x = range(1, 13)\n'
                                               '>>> expected_y = [5.7, 5.6, 11.5, 16.6, 19.8, 23.9, 28.0, 29.2, 26.7, 19.5, 15.8, 7.9]\n'
                                               '>>> assert list(x_data) == list(expected_x)\n'
                                               '>>> assert list(y_data) == expected_y\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
