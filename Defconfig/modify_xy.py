#!/usr/bin/env python3
import yaml
import os

with open('/etc/openclash/config/xy.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = ['HK', 'SG', 'JP', 'TW', 'USA', 'RU', 'IEPL', 'HB', 'OT']
HK = []
SG = []
JP = []
TW = []
RU = []
USA = []
IEPL = []
HB = []
OT = []
testtime='300'
n = len(Proxy)
for p in x['proxies']:
    name = p['name']
    if 'IEPL' in name:
        Proxy.append(name)
        IEPL.append(name)
    elif '香' in name:
        Proxy.append(name)
        HK.append(name)
    elif '日本' in name:
        Proxy.append(name)
        JP.append(name)
    elif '新' in name:
        Proxy.append(name)
        SG.append(name)
    elif '台' in name:
        Proxy.append(name)
        TW.append(name)
    elif '美' in name:
        Proxy.append(name)
        USA.append(name)
    elif '俄' in name:
        Proxy.append(name)
        RU.append(name)
    elif '家宽' in name:
        Proxy.append(name)
        HB.append(name)
    else:
        Proxy.append(name)
        OT.append(name)
Google = Proxy[n:]
Disneyplus = Google
Netflix = Google
OpenAI = Google
Instagram = Proxy[:n]
Youtube = Proxy[:n]
Spotify = Proxy[:n] + ['DIRECT']
Github = Proxy[:n]
Twitter = Proxy[:n]
Telegram = Proxy[:n]
Microsoft = Spotify

pgs = []
pgs.append({'name':'Proxy', 'type':'select', 'proxies':Proxy})
pgs.append({'name':'Google', 'type':'select', 'proxies':Google})
pgs.append({'name':'Disneyplus', 'type':'select', 'proxies':Disneyplus})
pgs.append({'name':'Netflix', 'type':'select', 'proxies':Netflix})
pgs.append({'name':'OpenAI', 'type':'select', 'proxies':OpenAI})
pgs.append({'name':'Instagram', 'type':'select', 'proxies':Instagram})
pgs.append({'name':'Youtube', 'type':'select', 'proxies':Youtube})
pgs.append({'name':'Spotify', 'type':'select', 'proxies':Spotify})
pgs.append({'name':'Github', 'type':'select', 'proxies':Github})
pgs.append({'name':'Twitter', 'type':'select', 'proxies':Twitter})
pgs.append({'name':'Telegram', 'type':'select', 'proxies':Telegram})
pgs.append({'name':'Microsoft', 'type':'select', 'proxies':Microsoft})
pgs.append({'name':'HK', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':HK, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'SG', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':SG, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'TW', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':TW, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'JP', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':JP, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'USA', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':USA, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'RU', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':RU, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'IEPL', 'type': 'select', 'proxies':IEPL})
pgs.append({'name':'HB', 'type': 'select', 'proxies':HB})
pgs.append({'name':'OT', 'type': 'select', 'proxies':OT})
rps = {}
rps['Google1'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Domain_Google.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/google.mrs'}
rps['Google2'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Ip_Google.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geoip/google.mrs'}
rps['Youtube'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Youtube.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/youtube.mrs'}
rps['Disneyplus'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Disneyplus.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo/geosite/disney.mrs'}
rps['Netflix1'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Domain_Netflix.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/netflix.mrs'}
rps['Netflix2'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Ip_Netflix.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geoip/netflix.mrs'}
rps['Instagram'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Instagram.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo/geosite/instagram.mrs'}
rps['Facebook1'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Ip_Facebook.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo/geosite/facebook.mrs'}
rps['Facebook2'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Ip_Facebook.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo/geoip/facebook.mrs'}
rps['Spotify'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Spotify.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/spotify.mrs'}
rps['Github'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Github.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/github.mrs'}
rps['Twitter1'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Domain_Twitter.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/twitter.mrs'}
rps['Twitter2'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Ip_Twitter.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geoip/twitter.mrs'}
rps['Telegram1'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Domain_Telegram.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/telegram.mrs'}
rps['Telegram2'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Ip_Telegram.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geoip/telegram.mrs'}
rps['Microsoft'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Microsoft.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/microsoft.mrs'}
rps['OpenAI'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/OpenAI.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/openai.mrs'}
rps['Scholar'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Scholar.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo/geosite/category-scholar-!cn.mrs'}
rps['ProxyGFW'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/ProxyGFW.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/proxy.mrs'}
rps['Private1'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Domain_Private.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geosite/private.mrs'}
rps['Private2'] = {'type': 'http', 'behavior': 'mrs', 'path':'./rule_provider/Ip_Private.mrs',
                           'url':'https://github.com/MetaCubeX/meta-rules-dat/blob/meta/geo-lite/geoip/private.mrs'}
rs = []
rs.append('RULE-SET,Telegram2,Telegram')
rs.append('RULE-SET,Telegram1,Telegram')
rs.append('RULE-SET,Twitter1,Twitter')
rs.append('RULE-SET,Twitter2,Twitter')
rs.append('RULE-SET,Instagram,Instagram')
rs.append('RULE-SET,Facebook1,Instagram')
rs.append('RULE-SET,Facebook2,Instagram')
rs.append('RULE-SET,Youtube,Youtube')
rs.append('DOMAIN-SUFFIX,googleapis.cn,Google')
rs.append('RULE-SET,Google2,Google')
rs.append('RULE-SET,Google1,Google')
rs.append('RULE-SET,Spotify,Spotify')
rs.append('RULE-SET,Github,Github')
rs.append('RULE-SET,OpenAI,OpenAI')
rs.append('RULE-SET,Microsoft,Microsoft')
rs.append('RULE-SET,Disneyplus,Disneyplus')
rs.append('RULE-SET,Netflix1,Netflix')
rs.append('RULE-SET,Netflix2,Netflix')
rs.append('RULE-SET,Scholar,DIRECT')
rs.append('RULE-SET,ProxyGFW,Proxy')
rs.append('RULE-SET,Private1,DIRECT')
rs.append('RULE-SET,Private2,DIRECT')
rs.append('GEOIP,CN,DIRECT,no-resolve')
rs.append('GEOSITE,apple,DIRECT')
rs.append('MATCH,Proxy')
z = {}
for k in x.keys():
    if k == 'proxy-groups':
        z[k] = pgs
    elif k == 'rules':
        z[k] = rs 
    elif k == 'proxies':    
        z[k] = x[k]
z['rule-providers'] = rps
z['sniffer'] = {
        'enable': True,
        'force-dns-mapping': True,
        'parse-pure-ip': True,
        'override-destination': True,
        'sniff': {
            'HTTP': {
                'ports': [80, '8080-8880'],
                'override-destination': True
            },
            'TLS': {
                'ports': [443, 8443]
            },
            'QUIC': {
                'ports': [443, 8443]
            }
        },
        'force-domain': [
            '+.v2ex.com'
        ],
        'skip-domain': [
            'Mijia Cloud'
        ]
    }
z['dns'] = {'default-nameserver': ['223.5.5.5', '119.29.29.29'],
            'proxy-server-nameserver': ['https://dns.alidns.com/dns-query', 'https://doh.pub/dns-query'],
            'respect-rules': True}

if os.path.exists('/etc/openclash/config/config_xy.yaml'):
    os.system('rm /etc/openclash/config/config_xy.yaml')
    print('删除旧配置！')
with open('/etc/openclash/config/config_xy.yaml', 'w') as file:
    file.write(yaml.dump(z, allow_unicode=True))
    print('配置修改成功！')
