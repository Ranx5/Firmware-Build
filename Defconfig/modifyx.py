#!/usr/bin/env python3
import yaml
import os

with open('/etc/openclash/config/uv.yaml', 'rb') as f1:
    x1 = yaml.safe_load(f1)
with open('/etc/openclash/config/abc.yaml', 'rb') as f2:
    x2 = yaml.safe_load(f2)
Proxy = ['HK', 'SGP', 'JP', 'TW', 'USA', 'SGP-ovo', 'JP-ovo', 'USA-ovo', 'IDN-ovo', 'HKG-ovo', 'AUS-ovo', 'DEU-ovo', 'FR-ovo', 'HK-cc', 'OT']
n = len(Proxy)
HK = []
SGP = []
JP = []
TW = []
USA = []
SGP_ovo = []
JP_ovo = []
USA_ovo = []
IDN_ovo = []
HKG_ovo = []
AUS_ovo = []
DEU_ovo = []
FR_ovo = []
HK_cc = []
OT = []
testtime='300'
x1['proxies'] = x1['proxies'] + x2['proxies']
for p in x1['proxies']:
    name = p['name']
    if '香港 - HY2' in name:
        Proxy.append(name)
        HKG_ovo.append(name)
    elif '香' in name:
        Proxy.append(name)
        HK.append(name)
    elif '日本 - HY2' in name:
        Proxy.append(name)
        JP_ovo.append(name)
    elif '日' in name:
        Proxy.append(name)
        JP.append(name)
    elif '新加坡 - HY2' in name:
        Proxy.append(name)
        SGP_ovo.append(name)
    elif '新' in name:
        Proxy.append(name)
        SGP.append(name)
    elif '台' in name:
        Proxy.append(name)
        TW.append(name)
    elif '美国 - HY2' in name:
        Proxy.append(name)
        USA_ovo.append(name)
    elif '美' in name:
        Proxy.append(name)
        USA.append(name)
    elif '印尼' in name:
        Proxy.append(name)
        IDN_ovo.append(name)
    elif '法国' in name:
        Proxy.append(name)
        FR_ovo.append(name)
    elif '悉尼' in name:
        Proxy.append(name)
        AUS_ovo.append(name)
    elif '德国' in name:
        Proxy.append(name)
        DEU_ovo.append(name)
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
pgs.append({'name':'SGP', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':SGP, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'SGP-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':SGP_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'TW', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':TW, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'JP', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':JP, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'JP-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':JP_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'USA', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':USA, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'USA-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':USA_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'IDN-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':IDN_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'HKG-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':HKG_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'AUS-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':AUS_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'DEU-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':DEU_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'FR-ovo', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':FR_ovo, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})
pgs.append({'name':'HK-cc', 'type': 'load-balance', 'strategy': 'consistent-hashing', 'disable-udp': False,
            'proxies':HK_cc, 'url': 'http://www.gstatic.com/generate_204', 'interval': testtime})

pgs.append({'name':'OT', 'type': 'select', 'proxies':OT})
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
rs.append('DOMAIN-SUFFIX,ipify.org,Youtube')
rs.append('DOMAIN-SUFFIX,ip.sb,Github')
rs.append('RULE-SET,Disneyplus,Disneyplus')
rs.append('RULE-SET,Netflix,Netflix')
rs.append('RULE-SET,NetflixIP,Netflix')
rs.append('RULE-SET,Scholar,DIRECT')
rs.append('RULE-SET,ProxyGFW,Proxy')
rs.append('GEOIP,CN,DIRECT,no-resolve')
rs.append('GEOSITE,apple,DIRECT')
rs.append('MATCH,Proxy')
z = {}
for k in x1.keys():
    if k == 'proxy-groups':
        z[k] = pgs
    elif k == 'rules':
        z[k] = rs 
    else:    
        z[k] = x1[k]
z['rule-providers'] = rps
os.system('rm /etc/openclash/config/myconfigx.yaml')
with open('/etc/openclash/config/myconfigx.yaml', 'w') as file:
    file.write(yaml.dump(z, allow_unicode=True))
