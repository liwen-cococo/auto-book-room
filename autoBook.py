# -*- coding:utf-8 -*-
import requests

class autoBooking(object):
    def __init__(self, id, psw):
        self.session = requests.session()

        # 登录到系统
        login_url = 'http://lib.tongji.edu.cn/ClientWeb/pro/ajax/login.aspx'
        data = {'id': id, 'pwd': psw, 'act': 'login'}
        login_response = self.session.post(login_url, data=data)
        if login_response.json()['msg'] == 'ok':
            print 'login successfully.'
        print login_response.content

        # 预定研读间
        reserve_url = 'http://lib.tongji.edu.cn/ClientWeb/pro/ajax/reserve.aspx'
        data = {'dev_id':'38410', 'lab_id':'38266', 'kind_id':'47530', 'type':'dev',
                'start':'2017-08-21 09:50', 'end':'2017-08-21 12:40',
                'start_time':'950', 'end_time':'1240', 'act':'set_resv'}
        reserve_response = self.session.post(reserve_url, data=data)
        print reserve_response.content

ab = autoBooking('', '')
