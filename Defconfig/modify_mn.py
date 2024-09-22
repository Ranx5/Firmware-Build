#!/usr/bin/env python3
import yaml
import os

with open('/etc/openclash/config/mn.yaml', 'rb') as f:
    x = yaml.safe_load(f)
Proxy = {'HK':[], 'HK05':[], 'HK15':[], 'SGP':[], 'JP':[], 'TW':[], 'KR':[], 'USA':[], 'BETA':[], 'OT':[], 'All':[]}
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
    elif '1.5x' in name:
        Proxy['All'].append(name)
        Proxy['HK15'].append(name)
        ProxySet.add('HK15')
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
        Proxy['SGP'].append(name)
        ProxySet.add('SGP')
    elif 'Taiwan' in name:
        Proxy['All'].append(name)
        Proxy['TW'].append(name)
        ProxySet.add('TW')
    elif 'UnitedStates' in name:
        Proxy['All'].append(name)
        Proxy['USA'].append(name)
        ProxySet.add('USA')
    elif 'Korea' in name:
        Proxy['All'].append(name)
        Proxy['KR'].append(name)
        ProxySet.add('KR')
    else:
        Proxy['All'].append(name)
        Proxy['OT'].append(name)
        ProxySet.add('OT')
ProxySet = list(ProxySet)
Strategy1 = ['Google', 'Disneyplus', 'Netflix', 'OpenAI']
Strategy2 = ['Instagram', 'YouTube', 'GitHub', 'Twitter', 'Telegram', 'PornHub']
Strategy3 = ['Spotify', 'Microsoft']
for s in Strategy1:
    pgs.append({'name':s, 'type':'select', 'proxies':Proxy['All']})
for s in Strategy2:
    pgs.append({'name':s, 'type':'select', 'proxies':ProxySet})
for s in Strategy3:
    pgs.append({'name':s, 'type':'select', 'proxies':ProxySet + ['Direct']})
for s in ProxySet:
    if s != 'OT':
        pgs.append({'name':s, 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
                    'proxies':Proxy[s], 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
if Proxy['OT']:
    pgs.append({'name':'OT', 'type': 'select', 'proxies':Proxy['OT']})
    
rps = {}
rps['Google'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Google.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Google.yaml'}
rps['Youtube'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Youtube.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/YouTube.yaml'}
rps['Disneyplus'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Disneyplus.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/DisneyPlus.yaml'}
rps['Netflix'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Netflix.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Netflix.yaml'}
rps['Instagram'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Instagram.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Instagram.yaml'}
rps['Facebook'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Facebook.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Facebook.yaml'}
rps['Spotify'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Spotify.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Spotify.yaml'}
rps['Pornhub'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Spotify.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Pornhub.yaml'}
rps['Github'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Github.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Github.yaml'}
rps['Twitter'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Twitter.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Twitter.yaml'}
rps['Telegram'] = {'type': 'http', 'behavior': 'ipcidr', 'path':'./rule_provider/Telegram.yaml',
                           'url':'https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt'}
rps['NetflixIP'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/NetflixIP.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/NetflixIP.yaml'}
rps['Microsoft'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Microsoft.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Microsoft.yaml'}
rps['OpenAI'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/OpenAI.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/OpenAi.yaml'}
rps['Scholar'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/Scholar.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/Ruleset/Scholar.yaml'}
rps['ProxyGFW'] = {'type': 'http', 'behavior': 'classical', 'path':'./rule_provider/ProxyGFW.yaml',
                           'url':'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Providers/ProxyGFWlist.yaml'}
rs = []
rs.append('RULE-SET,Telegram,Telegram')
rs.append('RULE-SET,Twitter,Twitter')
rs.append('RULE-SET,Instagram,Instagram')
rs.append('RULE-SET,Facebook,Instagram')
rs.append('RULE-SET,Youtube,Youtube')
rs.append('DOMAIN-SUFFIX,googleapis.cn,Google')
rs.append('RULE-SET,Google,Google')
rs.append('RULE-SET,Spotify,Spotify')
rs.append('RULE-SET,Github,Github')
rs.append('RULE-SET,OpenAI,OpenAI')
rs.append('RULE-SET,Microsoft,Microsoft')
rs.append('RULE-SET,Disneyplus,Disneyplus')
rs.append('RULE-SET,Netflix,Netflix')
rs.append('RULE-SET,NetflixIP,Netflix')
rs.append('RULE-SET,Scholar,DIRECT')
rs.append('RULE-SET,Pornhub,Pornhub')
rs.append('RULE-SET,ProxyGFW,Proxy')
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

if os.path.exists('/etc/openclash/config/config_mn.yaml'):
    os.system('rm /etc/openclash/config/config_mn.yaml')
    print('删除旧配置！')
with open('/etc/openclash/config/config_mn.yaml', 'w') as file:
    file.write(yaml.dump(z, allow_unicode=True))
    print('配置修改成功！')
