OK_FORMAT = True

test = {   'name': 'q5-6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans56\n'
                                               '>>> ax = result.get_axes()[0]\n'
                                               '>>> children = ax.get_children()\n'
                                               '>>> wedges = [child for child in children if isinstance(child, plt.matplotlib.patches.Wedge)]\n'
                                               '>>> thetas = []\n'
                                               '>>> for w in wedges:\n'
                                               '...     thetas.append(round(w.theta1, 1))\n'
                                               '>>> assert thetas == [0.0, 135.7, 211.3, 273.6, 333.7, 343.4]\n'
                                               '>>> labels = []\n'
                                               '>>> for w in wedges:\n'
                                               '...     labels.append(str(w.get_label()))\n'
                                               ">>> assert labels == ['晴曇', '晴', '雨曇', '晴雨曇', '晴雨', 'その他']\n"
                                               '>>> title = ax.get_title()\n'
                                               ">>> assert title == '2022年神戸市の天気'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
