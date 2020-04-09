while True:
    km = float(input('请输入公里数：'))
    if km <= 0:
        print('公里数输入错误，重新输入：')
        break
    else:
        if km <= 2 and km > 0:
            print('您需要支付8元车费！')
        if km >2 and km <= 12:
            cost = 8 + (km - 2) * 1.2
            print('您需要支付 %s'%cost,'元车费！')
        if km > 12:
            cost = 8 +(12 - 2) * 1.2 + (km -12)*1.5
            print('您需要支付%s'%cost,'元车费!')