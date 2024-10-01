OK_FORMAT = True

test = {   'name': 'q2-2',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert check_pass(95, 70, 70) == True, 'テスト1失敗: 英語が95点以上の場合、合格するはずです'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert check_pass(80, 80, 80) == True, 'テスト2失敗: 3教科合計が240点以上の場合、合格するはずです'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert check_pass(94, 70, 70) == False, 'テスト3失敗: 条件を満たさない場合、不合格になるはずです'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert check_pass(95, 80, 80) == True, 'テスト4失敗: 両方の条件を満たす場合、合格するはずです'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert check_pass(95, 72, 73) == True, 'テスト5失敗: 境界値（英語95点、合計240点）で合格するはずです'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert check_pass(100, 50, 50) == True, 'テスト6失敗: 英語が満点なら他の科目が低くても合格するはずです'\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
