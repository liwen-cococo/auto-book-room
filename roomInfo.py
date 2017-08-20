# -*- coding:utf-8 -*-
import requests

session = requests.session()
login_url = 'http://lib.tongji.edu.cn/ClientWeb/pro/ajax/device.aspx'
data = {'dev_order':'',
        'kind_order':'',
        'classkind':'1',
        'display':'cld',
        'md':'d',
        'class_id':'47529',
        'purpose':'',
        'cld_name':'default',
        'date':'20170821',
        'act':'get_rsv_sta'
        }
response = session.get(login_url, data=data)
rooms_info = response.json()['data']
print rooms_info[0]['ts']

for room_id, room in enumerate(rooms_info, 202):
    print 'room' + str(room_id)
    ts = room['ts']
    for booking in ts:
        print booking['start'], '-', booking['end'],
        for i in booking['owner']:
            print i,
        print ' # '
        for i in booking['member']:
            print i,

    print "\n"

