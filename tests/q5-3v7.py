OK_FORMAT = True

test = {   'name': 'q5-3v7',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans53\n'
                                               '>>> assert len(result.get_axes()) > 0\n'
                                               '>>> axes = result.get_axes()[0]\n'
                                               '>>> lines = axes.get_lines()\n'
                                               '>>> x_data = lines[0].get_xdata()\n'
                                               '>>> y_data = lines[0].get_ydata()\n'
                                               '>>> expected_y = [5.7, 5.6, 11.5, 16.6, 19.8, 23.9, 28.0, 29.2, 26.7, 19.5, 15.8, 7.9]\n'
                                               '>>> assert x_data.tolist() == [1640995200000000000, 1643673600000000000, 1646092800000000000, 1648771200000000000, 1651363200000000000, '
                                               '1654041600000000000, 1656633600000000000, 1659312000000000000, 1661990400000000000, 1664582400000000000, 1667260800000000000, 1669852800000000000]\n'
                                               '>>> assert list(y_data) == expected_y\n'
                                               '>>> xlim = axes.get_xlim()\n'
                                               '>>> ylim = axes.get_ylim()\n'
                                               '>>> assert (xlim, ylim) == ((18976.3, 19343.7), (0.0, 40.0))\n'
                                               '>>> xticks = axes.get_xticks()\n'
                                               '>>> yticks = axes.get_yticks()\n'
                                               '>>> assert list(xticks) == [18993.0, 19024.0, 19052.0, 19083.0, 19113.0, 19144.0, 19174.0, 19205.0, 19236.0, 19266.0, 19297.0, 19327.0]\n'
                                               '>>> assert list(yticks) == [0, 10, 20, 30, 40]\n'
                                               '>>> xlabel = axes.get_xlabel()\n'
                                               '>>> ylabel = axes.get_ylabel()\n'
                                               '>>> title = axes.get_title()\n'
                                               ">>> assert (xlabel, ylabel, title) == ('日付', '気温平均（度）', '2022年神戸市の気温')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
