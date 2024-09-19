OK_FORMAT = True

test = {   'name': 'q1-7',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': ">>> result = calculate_order('Apple', 100, 10)\n"
                                               ">>> assert result['product_name'] == 'Apple', '商品名が正しくありません'\n"
                                               ">>> assert result['unit_price'] == 100, '単価が正しくありません'\n"
                                               ">>> assert result['quantity'] == 10, '数量が正しくありません'\n"
                                               ">>> assert result['tax_excluded_price'] == 1000, '税抜価格が正しくありません'\n"
                                               ">>> assert result['tax'] == 100, '消費税が正しくありません'\n"
                                               ">>> assert result['total_price'] == 1100, '合計価格が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> result = calculate_order('Banana', 200, 5)\n"
                                               ">>> assert result['product_name'] == 'Banana', '商品名が正しくありません'\n"
                                               ">>> assert result['unit_price'] == 200, '単価が正しくありません'\n"
                                               ">>> assert result['quantity'] == 5, '数量が正しくありません'\n"
                                               ">>> assert result['tax_excluded_price'] == 1000, '税抜価格が正しくありません'\n"
                                               ">>> assert result['tax'] == 100, '消費税が正しくありません'\n"
                                               ">>> assert result['total_price'] == 1100, '合計価格が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> result = calculate_order('Cherry', 50, 100)\n"
                                               ">>> assert result['product_name'] == 'Cherry', '商品名が正しくありません'\n"
                                               ">>> assert result['unit_price'] == 50, '単価が正しくありません'\n"
                                               ">>> assert result['quantity'] == 100, '数量が正しくありません'\n"
                                               ">>> assert result['tax_excluded_price'] == 5000, '税抜価格が正しくありません'\n"
                                               ">>> assert result['tax'] == 500, '消費税が正しくありません'\n"
                                               ">>> assert result['total_price'] == 5500, '合計価格が正しくありません'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
