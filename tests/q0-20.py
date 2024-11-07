OK_FORMAT = True

test = {   'name': 'q0-20',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans20\n'
                                               '>>> ax = result.get_axes()[0]\n'
                                               '>>> bar_heights = [bar.get_height() for bar in ax.containers[0]]\n'
                                               '>>> assert bar_heights == [37.7, 21.0, 17.3, 16.7, 2.7, 4.6]\n'
                                               '>>> ylim = ax.get_ylim()\n'
                                               '>>> assert ylim == (0.0, 50.0)\n'
                                               '>>> xlabel = ax.get_xlabel()\n'
                                               '>>> ylabel = ax.get_ylabel()\n'
                                               '>>> title = ax.get_title()\n'
                                               ">>> assert (xlabel, ylabel, title) == ('天気', '割合', '2022年神戸市の天気')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
