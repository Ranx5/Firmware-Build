#!/usr/bin/env python3
import yaml
import os

with open('/etc/openclash/config/xy.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = {'HK':[], 'HK_ss':[], 'SG':[], 'SG_ss':[], 'JP':[], 'JP_ss':[], 'TW':[], 'TW_ss':[], 'US':[], 'US_ss':[], 'UK':[], 'UK_ss':[], 'MYS':[], 'ARG':[], 'OT':[], 'All':[]}
testtime='300'
n = len(Proxy)
ProxySet = set()
pgs = []
for p in x['proxies']:
    name = p['name']
    Proxy['All'].append(name)
    if 'Hong Kong' in name:
        if 'SS' in name:
            Proxy['HK_ss'].append(name)
            ProxySet.add('HK_ss')
        else:
            Proxy['HK'].append(name)
            ProxySet.add('HK')
    elif 'Japan' in name:
        if 'SS' in name:
            Proxy['JP_ss'].append(name)
            ProxySet.add('JP_ss')
        else:
            Proxy['JP'].append(name)
            ProxySet.add('JP')
    elif 'Singapore' in name:
        if 'SS' in name:
            Proxy['SG_ss'].append(name)
            ProxySet.add('SG_ss')
        else:
            Proxy['SG'].append(name)
            ProxySet.add('SG')
    elif 'Taiwan' in name:
        if 'SS' in name:
            Proxy['TW_ss'].append(name)
            ProxySet.add('TW_ss')
        else:
            Proxy['TW'].append(name)
            ProxySet.add('TW')
    elif 'USA' in name:
        if 'SS' in name:
            Proxy['US_ss'].append(name)
            ProxySet.add('US_ss')
        else:
            Proxy['US'].append(name)
            ProxySet.add('US')
    elif 'UK' in name:
        if 'SS' in name:
            Proxy['UK_ss'].append(name)
            ProxySet.add('UK_ss')
        else:
            Proxy['UK'].append(name)
            ProxySet.add('UK')
    elif 'Malaysia' in name:
        Proxy['MYS'].append(name)
        ProxySet.add('MYS')
    elif 'Argentina' in name:
        Proxy['ARG'].append(name)
        ProxySet.add('ARG')
    else:
        Proxy['OT'].append(name)
        ProxySet.add('OT')
ProxySet = list(ProxySet)
Strategy1 = ['Google', 'DisneyPlus', 'Netflix', 'OpenAI']
Strategy2 = ['Instagram', 'YouTube', 'GitHub', 'Twitter', 'Telegram']
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
rps['Apple'] = {'type': 'http', 'behavior': 'ipcidr', 'path':'./rule_provider/Apple.yaml',
                           'url':'https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/refs/heads/meta/geo-lite/geoip/apple.yaml'}
rs = []
rs.append('GEOIP,private,DIRECT,no-resolve')
rs.append('GEOIP,cloudflare,Proxy,no-resolve')
rs.append('GEOSITE,cloudflare,Proxy')
rs.append('GEOIP,telegram,Telegram,no-resolve')
rs.append('GEOSITE,twitter,Twitter')
rs.append('GEOSITE,instagram,Instagram')
rs.append('GEOSITE,facebook,Instagram')
rs.append('GEOSITE,youtube,YouTube')
rs.append('GEOSITE,google,Google')
rs.append('GEOIP,google,Google,no-resolve')
rs.append('GEOSITE,spotify,Spotify')
rs.append('GEOSITE,github,GitHub')
rs.append('GEOSITE,openai,OpenAI')
rs.append('GEOSITE,microsoft,Microsoft')
rs.append('GEOSITE,disney,DisneyPlus')
rs.append('GEOSITE,netflix,Netflix')
rs.append('GEOIP,netflix,Netflix,no-resolve')
rs.append('GEOSITE,apple,DIRECT')
rs.append('RULE-SET,Apple,DIRECT,no-resolve')
rs.append('GEOSITE,cn,DIRECT')
rs.append('GEOIP,CN,DIRECT,no-resolve')
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
z['dns'] = {'default-nameserver': ['223.5.5.5', '119.29.29.29'],
            'proxy-server-nameserver': ['https://dns.alidns.com/dns-query', 'https://doh.pub/dns-query'],
            'respect-rules': True}

if os.path.exists('/etc/openclash/config/config_xy.yaml'):
    os.system('rm /etc/openclash/config/config_xy.yaml')
    print('删除旧配置！')
with open('/etc/openclash/config/config_xy.yaml', 'w') as file:
    file.write(yaml.dump(z, allow_unicode=True))
    print('配置修改成功！')
