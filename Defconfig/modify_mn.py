#!/usr/bin/env python3
import yaml
import os

with open('/etc/openclash/config/mn.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = {'HK':[], 'HK05':[], 'HK20':[], 'SG':[], 'SG20':[], 'JP':[], 'TW':[],'TW20':[], 'KR':[], 'US':[], 'BETA':[], 'OT':[], 'All':[]}
testtime='300'
n = len(Proxy)
ProxySet = set()
pgs = []
for p in x['proxies']:
    name = p['name']
    if 'BETA' in name:
        Proxy['All'].append(name)
        Proxy['BETA'].append(name)
        ProxySet.add('BETA')
    elif '0.5x' in name:
        Proxy['All'].append(name)
        Proxy['HK05'].append(name)
        ProxySet.add('HK05')
    elif '2x' in name:
        if 'HongKong' in name:
            Proxy['All'].append(name)
            Proxy['HK20'].append(name)
            ProxySet.add('HK20')
        elif 'Singapore' in name:
            Proxy['All'].append(name)
            Proxy['SG20'].append(name)
            ProxySet.add('SG20')
        elif 'Taiwan' in name:
            Proxy['All'].append(name)
            Proxy['TW20'].append(name)
            ProxySet.add('TW20')
    elif 'HongKong' in name:
        Proxy['All'].append(name)
        Proxy['HK'].append(name)
        ProxySet.add('HK')
    elif 'Japan' in name:
        Proxy['All'].append(name)
        Proxy['JP'].append(name)
        ProxySet.add('JP')
    elif 'Singapore' in name:
        Proxy['All'].append(name)
        Proxy['SG'].append(name)
        ProxySet.add('SG')
    elif 'Taiwan' in name:
        Proxy['All'].append(name)
        Proxy['TW'].append(name)
        ProxySet.add('TW')
    elif 'UnitedStates' in name:
        Proxy['All'].append(name)
        Proxy['US'].append(name)
        ProxySet.add('US')
    elif 'Korea' in name:
        Proxy['All'].append(name)
        Proxy['KR'].append(name)
        ProxySet.add('KR')
    else:
        Proxy['All'].append(name)
        Proxy['OT'].append(name)
        ProxySet.add('OT')
ProxySet = list(ProxySet)
Strategy1 = ['Google', 'DisneyPlus', 'Netflix', 'OpenAI']
Strategy2 = ['Instagram', 'YouTube', 'GitHub', 'Twitter', 'Telegram']
Strategy3 = ['Spotify', 'Microsoft', 'Emby']
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
rs.append('DOMAIN-SUFFIX,emby.moe,Emby')
rs.append('GEOSITE,apple,DIRECT')
rs.append('RULE-SET,Apple,DIRECT,no-resolve')
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

if os.path.exists('/etc/openclash/config/config_mn.yaml'):
    os.system('rm /etc/openclash/config/config_mn.yaml')
    print('删除旧配置！')
with open('/etc/openclash/config/config_mn.yaml', 'w') as file:
    file.write(yaml.dump(z, allow_unicode=True))
    print('配置修改成功！')
