#!/usr/bin/env python3
import yaml
import os

with open('/etc/openclash/config/abc.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = {'HKG':[], 'SGP':[], 'JPN':[], 'TW':[], 'IDN':[], 'AUS':[], 'USA':[],  'FR':[], 'DEU':[], 'OT':[], 'All':[]}
testtime='300'
n = len(Proxy)
ProxySet = set()
pgs = []
for p in x['proxies']:
    name = p['name']
    if '香港' in name:
        Proxy['All'].append(name)
        Proxy['HKG'].append(name)
        ProxySet.add('HKG')
    elif '新加坡' in name:
        Proxy['All'].append(name)
        Proxy['SGP'].append(name)
        ProxySet.add('SGP')
    elif '日本' in name:
        Proxy['All'].append(name)
        Proxy['JPN'].append(name)
        ProxySet.add('JPN')
    elif '台湾' in name:
        Proxy['All'].append(name)
        Proxy['TW'].append(name)
        ProxySet.add('TW')
    elif '印尼' in name:
        Proxy['All'].append(name)
        Proxy['IDN'].append(name)
        ProxySet.add('IDN')
    elif '悉尼' in name:
        Proxy['All'].append(name)
        Proxy['AUS'].append(name)
        ProxySet.add('AUS')
    elif '美国' in name:
        Proxy['All'].append(name)
        Proxy['USA'].append(name)
        ProxySet.add('USA')
    elif '法国' in name:
        Proxy['All'].append(name)
        Proxy['FR'].append(name)
        ProxySet.add('FR')
    elif '德国' in name:
        Proxy['All'].append(name)
        Proxy['DEU'].append(name)
        ProxySet.add('DEU')
    else:
        Proxy['All'].append(name)
        Proxy['OT'].append(name)
        ProxySet.add('OT')
ProxySet = list(ProxySet)
Strategy1 = ['Google', 'DisneyPlus', 'Netflix', 'OpenAI']
Strategy2 = ['Instagram', 'YouTube', 'GitHub', 'Twitter', 'Telegram', 'PornHub']
Strategy3 = ['Spotify', 'Microsoft']
pgs.append({'name':'Proxy', 'type':'select', 'proxies':ProxySet+Proxy['All']})
for s in Strategy1:
    pgs.append({'name':s, 'type':'select', 'proxies':Proxy['All']})
for s in Strategy2:
    pgs.append({'name':s, 'type':'select', 'proxies':ProxySet})
for s in Strategy3:
    pgs.append({'name':s, 'type':'select', 'proxies':ProxySet + ['DIRECT']})
for s in ProxySet:
    if s != 'OT':
        pgs.append({'name':s, 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
                    'proxies':Proxy[s], 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
if Proxy['OT']:
    pgs.append({'name':'OT', 'type': 'select', 'proxies':Proxy['OT']})
    
rps = {}
rps['ProxyGFW'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/ProxyGFW.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/ProxyGFWlist.yaml'}

rs = []
rs.append('GEOIP,private,DIRECT,no-resolve')
rs.append('GEOIP,cloudflare,Proxy,no-resolve')
rs.append('GEOSITE,cloudflare,Proxy')
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
