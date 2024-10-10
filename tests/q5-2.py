OK_FORMAT = True

test = {   'name': 'q5-2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans52\n'
                                               '>>> assert len(result.get_axes()) > 0\n'
                                               '>>> axes = result.get_axes()[0]\n'
                                               '>>> lines = axes.get_lines()\n'
                                               '>>> x_data = lines[0].get_xdata()\n'
                                               '>>> y_data = lines[0].get_ydata()\n'
                                               '>>> expected_x = range(1, 13)\n'
                                               '>>> expected_y = [5.7, 5.6, 11.5, 16.6, 19.8, 23.9, 28.0, 29.2, 26.7, 19.5, 15.8, 7.9]\n'
                                               '>>> assert list(x_data) == list(expected_x)\n'
                                               '>>> assert list(y_data) == expected_y\n'
                                               '>>> xlim = axes.get_xlim()\n'
                                               '>>> ylim = axes.get_ylim()\n'
                                               '>>> assert xlim == (1.0, 12.0)\n'
                                               '>>> assert ylim == (0.0, 40.0)\n'
                                               '>>> xticks = axes.get_xticks()\n'
                                               '>>> yticks = axes.get_yticks()\n'
                                               '>>> assert list(xticks) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]\n'
                                               '>>> assert list(yticks) == [0, 10, 20, 30, 40]\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
