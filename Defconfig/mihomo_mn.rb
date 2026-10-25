#!/usr/bin/env ruby
require 'yaml'

source = "config_mn.yaml"
output = "profiles/config_mn.yaml"

data = YAML.load_file(source, aliases: true)

HK = data["proxies"].select { |n| n["name"].include?("HongKong") }.select { |n| !n["name"].include?("BETA") }.map { |n| n["name"]}
TW = data["proxies"].select { |n| n["name"].include?("Taiwan")}.map { |n| n["name"] }
JP = data["proxies"].select { |n| n["name"].include?("Japan")}.map { |n| n["name"] }
SG = data["proxies"].select { |n| n["name"].include?("Singapore")}.map { |n| n["name"] }
US = data["proxies"].select { |n| n["name"].include?("UnitedStates")}.map { |n| n["name"] }
BETA = data["proxies"].select { |n| n["name"].include?("BETA")}.map { |n| n["name"] }
Akile = data["proxies"].select { |n| n["name"].include?("Akile")}.map { |n| n["name"] }
exclude = ["官网", "剩余", "套餐"]
node_name = data["proxies"].reject { |n| exclude.any? { |e| n["name"].to_s.include?(e) } }.map { |n| n["name"] }

ProxySet = {"HK" => HK, "TW" => TW, "JP" => JP, "SG" => SG, "US" => US, "BETA" => BETA}.select { |_, proxies| proxies.any? }
Proxy = ProxySet.keys

if Akile.any?
  Proxy1 = ["Akile"] + Proxy
  proxy_groups = [{"name" => "Proxy", "type" => "select", "proxies" => Proxy1 + node_name}]
  proxy_groups << {"name" => "Akile", "type" => "select", "proxies" => Akile}
else
  Proxy1 = Proxy
  proxy_groups = [{"name" => "Proxy", "type" => "select", "proxies" => Proxy1 + node_name}]
end

Strategy1 = ['Google', 'DisneyPlus', 'Netflix', 'OpenAI']
Strategy2 = ['Instagram', 'YouTube', 'GitHub', 'Twitter', 'Telegram']
Strategy3 = ['Spotify', 'Emby', 'Microsoft']

Strategy1.each do |group|
  proxy_groups << {"name" => group, "type" => "select", "proxies" => node_name}                         
end

Strategy2.each do |group|
  proxy_groups << {"name" => group, "type" => "select", "proxies" => Proxy1}
end

Strategy3.each do |group|
  proxy_groups << {"name" => group, "type" => "select", "proxies" => Proxy1 + ["DIRECT"]}
end

Proxy.each do |group|
  proxy_groups << {"name" => group,
                        "type" => "load-balance",
                        "strategy" => "consistent-hashing",
                        "url" => "http://www.gstatic.com/generate_204",
                        "interval" => "300",
                        "disable-udp" => false,
                        "proxies" => ProxySet[group]}
end
config = {}
config["dns"] = {
                        "default-nameserver" => ["223.5.5.5", "119.29.29.29"],
                        "proxy-server-nameserver" => ["https://dns.alidns.com/dns-query", "https://doh.pub/dns-query"],
                        "respect-rules" => true
}
config["proxies"] = data["proxies"]
config["proxy-groups"] = proxy_groups
config["rule-providers"] = {"Apple" => {"type" => "http", "behavior" => "ipcidr", "path" => "./rule_provider/Apple.yaml", 
                            "url" => "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/refs/heads/meta/geo-lite/geoip/apple.yaml"}}
config["rules"] = [
                        "GEOIP,private,DIRECT,no-resolve",
                        "GEOIP,cloudflare,Proxy,no-resolve",
                        "GEOSITE,cloudflare,Proxy",
                        "AND,((NETWORK,UDP),(DST-PORT,443)),REJECT",
                        "GEOIP,telegram,Telegram,no-resolve",
                        "GEOSITE,twitter,Twitter",
                        "GEOSITE,instagram,Instagram",
                        "GEOSITE,facebook,Instagram",
                        "GEOSITE,youtube,YouTube",
                        "GEOSITE,google,Google",
                        "GEOIP,google,Google,no-resolve",
                        "GEOSITE,spotify,Spotify",
                        "GEOSITE,github,GitHub",
                        "GEOSITE,openai,OpenAI",
                        "GEOSITE,microsoft,Microsoft",
                        "GEOSITE,disney,DisneyPlus",
                        "GEOSITE,netflix,Netflix",
                        "GEOIP,netflix,Netflix,no-resolve",
                        "GEOSITE,apple,DIRECT",
                        "RULE-SET,Apple,DIRECT,no-resolve",
                        "DOMAIN-SUFFIX,emby.moe,Emby",
                        "DOMAIN-SUFFIX,xxlb.net,Emby",
                        "DOMAIN-SUFFIX,symcd.com,Emby",
                        "DOMAIN-SUFFIX,edge4k.com,Emby",
                        "DOMAIN-SUFFIX,kakaocdn.net,Emby",
                        "DOMAIN-SUFFIX,kakao.com,Emby",
                        "GEOSITE,cn,DIRECT",
                        "GEOIP,CN,DIRECT,no-resolve",
                        "MATCH,Proxy"
]
File.write(output, config.to_yaml)
