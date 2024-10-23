OK_FORMAT = True

test = {   'name': 'q5-5v3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans54\n'
                                               '>>> ax = result.get_axes()[0]\n'
                                               '>>> lines = ax.get_lines()\n'
                                               '>>> x_data = list(lines[0].get_xdata())\n'
                                               '>>> y0_data = list(lines[0].get_ydata())\n'
                                               '>>> y1_data = list(lines[1].get_ydata())\n'
                                               '>>> y2_data = list(lines[2].get_ydata())\n'
                                               '>>> assert (x_data, y0_data, y1_data, y2_data) == ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [5.7, 5.6, 11.5, 16.6, 19.8, 23.9, 28.0, 29.2, 26.7, 19.5, '
                                               '15.8, 7.9], [2.8, 2.5, 7.9, 13.1, 16.4, 21.1, 25.7, 26.9, 23.6, 16.4, 12.5, 4.7], [8.8, 9.3, 15.1, 20.6, 23.6, 27.2, 31.3, 32.3, 30.5, 23.0, 19.3, '
                                               '11.3])\n'
                                               '>>> xl = ax.get_xlabel()\n'
                                               '>>> yl = ax.get_ylabel()\n'
                                               '>>> t = ax.get_title()\n'
                                               ">>> assert (xl, yl, t) == ('日付', '気温（度）', '2022年神戸市の気温')\n"
                                               '>>> xlim = ax.get_xlim()\n'
                                               '>>> ylim = ax.get_ylim()\n'
                                               '>>> assert (xlim, ylim) == ((1.0, 12.0), (0.0, 40.0))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
