OK_FORMAT = True

test = {   'name': 'q1-7v2',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> assert product_name == 'INTEL Core i5-12400F'\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> assert int(unit_price) == 26980\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert int(quantity) == 5\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert int(tax_excluded_price) == 134900\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert int(tax) == 13490\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert int(total_price) == 148390\n', 'hidden': False, 'locked': False},
                                   {   'code': ">>> assert pmessage == '============（注文票）============\\n注文商品      :INTEL Core i5-12400F\\n＠26,980円×5個\\n税抜価格      :   134,900円\\n消費税       :    "
                                               "13,490円\\n合計金額      :   148,390円\\n================================='\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
