import requests
import json
import pandas as pd

headers = {
    'authority': '10-1-10-4-91-p.vpn.ucass.edu.cn',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    'accept': 'text/plain, */*; q=0.01',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55',
    'sec-ch-ua-platform': '"macOS"',
    'origin': 'https://10-1-10-4-91-p.vpn.ucass.edu.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://10-1-10-4-91-p.vpn.ucass.edu.cn/page/Default.aspx',
    'accept-language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,zh-HK;q=0.4',
    'cookie': 'HMACCOUNT_-_hm.baidu.com=3E863FE60F349301; HMACCOUNT_BFESS_-_hm.baidu.com=3E863FE60F349301; Hm_lvt_c69f27ad39d01ca2dde8645fb268cd6c=1644975714; USSUserID=gfYU5FekxRDDYEnOmgnIJoBF0BaX7X1nSvWUczTUiunM3zMO5da+6w==; Ecp_ClientId_-_cnki.net=4220216094300706300; _trs_uv_-_eyearbook.cn=kzow4tb2_4832_6llv; sdp_user_token=844ea559-f0b3-49a2-b837-c5fdf43971c8; USSDocInfo=; USSUserInfo=27JmdRjJ6jKjgS6rEJ+LmeMD5WtOJxKstsR5mZaQEHyDyJWTVkvYMg==; ASP.NET_SessionId=bz3dlbon1tsc0plkx3wi2mtr; FormalUser=FormalUser; USSToken=gfYU5FekxRDDYEnOmgnIJuEPPknClzL8UOpR2ijTcm5bOAoF2BzI+45ebFZrhJH2EMuFXRWGmaRCB7W4N1Khjw==',
}

params = (
    ('sf_request_type', 'ajax'),
)

data = {
  'ID': '013f52f2-cff1-4181-8053-e4d553e2e551',
  'act': 'click',
  'sequenceIDs': '',
  'sortField': 'fdXIndex',
  'sortOrder': 'asc',
  'pageIndex': '0',
  'pageSize': '5'
}

data = {
  'ID': '85bd082d-c42e-4c19-9364-7288c1f0621d',
  'act': 'click',
  'sequenceIDs': '11735943',
  'sortField': 'fdXIndex',
  'sortOrder': 'asc',
  'pageIndex': '0',
  'pageSize': '40'
}

response = requests.post('https://10-1-10-4-91-p.vpn.ucass.edu.cn/page/JSONResult.aspx', headers=headers, params=params, data=data)
response = json.loads(response.text)
print(response)



#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://10-1-10-4-91-p.vpn.ucass.edu.cn/page/JSONResult.aspx?sf_request_type=ajax', headers=headers, data=data)
