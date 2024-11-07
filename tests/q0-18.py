OK_FORMAT = True

test = {   'name': 'q0-18',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> result = ans18\n'
                                               '>>> ax = result.get_axes()[0]\n'
                                               '>>> points = ax.collections[0].get_offsets()\n'
                                               '>>> expected_data = np.array([[5.7, 61.2], [5.6, 56.2], [11.5, 63.2], [16.6, 63.7], [19.8, 63.0], [23.9, 72.9], [28.0, 75.8], [29.2, 73.5], [26.7, '
                                               '69.0], [19.5, 63.4], [15.8, 65.8], [7.9, 57.9]])\n'
                                               '>>> assert np.array_equal(points.data, expected_data)\n'
                                               '>>> xlim = ax.get_xlim()\n'
                                               '>>> ylim = ax.get_ylim()\n'
                                               '>>> assert (xlim, ylim) == ((0.0, 30.0), (50.0, 80.0))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
