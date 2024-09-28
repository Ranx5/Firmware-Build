
#!/usr/bin/env python3
import yaml
import os

with open('/etc/openclash/config/abc.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = ['HKG','SGP', 'JPN', 'IDN', 'AUS', 'USA', 'DEU', 'FR']
HKG = []
SGP = []
JPN = []
IDN = []
AUS = []
USA = []
DEU = []
FR =[]
testtime='300'
n = len(Proxy)
for p in x['proxies']:
    name = p['name']
    if '香' in name:
        Proxy.append(name)
        HKG.append(name)
    elif '新' in name:
        Proxy.append(name)
        SGP.append(name)
    elif '日' in name:
        Proxy.append(name)
        JPN.append(name)
    elif '悉尼' in name:
        Proxy.append(name)
        AUS.append(name)
    elif '印尼' in name:
        Proxy.append(name)
        IDN.append(name)
    elif '美国' in name:
        Proxy.append(name)
        USA.append(name)
    elif '德国' in name:
        Proxy.append(name)
        DEU.append(name)
    elif '法国' in name:
        Proxy.append(name)
        FR.append(name)
    else:
        Proxy.append(name)
pgs = []
pgs.append({'name':'Proxy', 'type':'select', 'proxies':Proxy})
pgs.append({'name':'Google', 'type':'select', 'proxies':Proxy[n:]})
pgs.append({'name':'DisneyPlus', 'type':'select', 'proxies':Proxy[n:]})
pgs.append({'name':'Netflix', 'type':'select', 'proxies':Proxy[n:]})
pgs.append({'name':'OpenAI', 'type':'select', 'proxies':Proxy[n:]})
pgs.append({'name':'Instagram', 'type':'select', 'proxies':Proxy[:n]})
pgs.append({'name':'YouTube', 'type':'select', 'proxies':Proxy[:n]+['DIRECT']})
pgs.append({'name':'Spotify', 'type':'select', 'proxies':Proxy[:n]})
pgs.append({'name':'GitHub', 'type':'select', 'proxies':Proxy[:n]})
pgs.append({'name':'Twitter', 'type':'select', 'proxies':Proxy[:n]})
pgs.append({'name':'Telegram', 'type':'select', 'proxies':Proxy[:n]})
pgs.append({'name':'Microsoft', 'type':'select', 'proxies':Proxy[:n]+['DIRECT']})
pgs.append({'name':'DNS', 'type':'select', 'proxies':Proxy)
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
rps['ProxyGFW'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/ProxyGFW.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/ProxyGFWlist.yaml'}

rs = []
rs.append('GEOIP,private,DIRECT,no-resolve')
rs.append('IP-SUFFIX,1.1.1.1/24,DNS,no-resolve')
rs.append('IP-SUFFIX,8.8.8.8/24,DNS,no-resolve')
rs.append('GEOIP,telegram,Telegram,no-resolve')
rs.append('GEOSITE,twitter,Twitter')
rs.append('GEOIP,twitter,Twitter,no-resolve')
rs.append('GEOSITE,instagram,Instagram')
rs.append('GEOSITE,facebook,Instagram')
rs.append('GEOSITE,youtube,YouTube')
rs.append('DOMAIN-SUFFIX,googleapis.cn,Google')
rs.append('GEOSITE,google,Google')
rs.append('GEOSITE,spotify,Spotify')
rs.append('GEOSITE,github,GitHub')
rs.append('GEOSITE,openai,OpenAI')
rs.append('GEOSITE,microsoft,Microsoft')
rs.append('GEOSITE,disney,DisneyPlus')
rs.append('GEOSITE,netflix,Netflix')
rs.append('GEOIP,netflix,Netflix,no-resolve')
rs.append('GEOSITE,category-scholar-cn,DIRECT')
rs.append('RULE-SET,ProxyGFW,Proxy')
rs.append('GEOIP,CN,DIRECT,no-resolve')
rs.append('GEOSITE,apple,DIRECT')
rs.append('DOMAIN-SUFFIX,ip.sb,GitHub')
rs.append('DOMAIN-SUFFIX,ipify.org,YouTube')
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

if os.path.exists('/etc/openclash/config/config_abc.yaml'):
    os.system('rm /etc/openclash/config/config_abc.yaml')
    print('删除旧配置！')
with open('/etc/openclash/config/config_abc.yaml', 'w') as file:
    file.write(yaml.dump(z, allow_unicode=True))
    print('配置修改成功！')
