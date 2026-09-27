#!/usr/bin/env ruby
require 'yaml'

source = "config.yaml"
output = "profiles/config_cx.yaml"

data = YAML.load_file(source, aliases: true)

HK_YD = data["proxies"].select {|n| n["name"].include?("香港") && n["name"].include?("移联")}.map {|n| n["name"]}
HK_DX = data["proxies"].select {|n| n["name"].include?("香港") && n["name"].include?("电信")}.map {|n| n["name"]}
JP_YD = data["proxies"].select {|n| n["name"].include?("日本") && n["name"].include?("移联")}.map {|n| n["name"]}
JP_DX = data["proxies"].select {|n| n["name"].include?("日本") && n["name"].include?("电信")}.map {|n| n["name"]}
SG_YD = data["proxies"].select {|n| n["name"].include?("新加坡") && n["name"].include?("移联")}.map {|n| n["name"]}
SG_DX = data["proxies"].select {|n| n["name"].include?("新加坡") && n["name"].include?("电信")}.map {|n| n["name"]}
TW = data["proxies"].select {|n| n["name"].include?("台湾")}.map {|n| n["name"]}
US = data["proxies"].select {|n| n["name"].include?("美国")}.map {|n| n["name"]}
UK = data["proxies"].select {|n| n["name"].include?("英国")}.map {|n| n["name"]}
DE = data["proxies"].select {|n| n["name"].include?("德国")}.map {|n| n["name"]}
KR = data["proxies"].select {|n| n["name"].include?("韩国")}.map {|n| n["name"]}
Akile = data["proxies"].select { |n| n["name"].include?("Akile")}.map {|n| n["name"] }
exclude = ["剩余", "套餐"]
node_name = data["proxies"].reject { |n| exclude.any? { |e| n["name"].to_s.include?(e) } }.map { |n| n["name"] }

Strategy1 = ['Google', 'DisneyPlus', 'Netflix', 'OpenAI']
Strategy2 = ['Instagram', 'YouTube', 'GitHub', 'Twitter', 'Telegram', 'Emby']
Strategy3 = ['Spotify', 'Microsoft']

ProxySet1 = {"Akile" => Akile, "香港-移联" => HK_YD, "香港-电信" => HK_DX, "日本-移联" => JP_YD, "日本-电信" => JP_DX, "新加坡-移联" => SG_YD, "新加坡-电信" => SG_DX}.select { |_, proxies| proxies.any? }
Proxy1 = ProxySet1.keys
ProxySet2 = {"台湾" => TW, "美国" => US, "英国" => UK, "德国" => DE, "韩国" => KR}.select { |_, proxies| proxies.any? }
Proxy2 = ProxySet2.keys

proxy_groups = [{"name" => "Proxy", "type" => "select", "proxies" => Proxy1 + Proxy2 + node_name}]

Strategy1.each do |group|
  proxy_groups << {"name" => group, "type" => "select", "proxies" => node_name}                         
end

Strategy2.each do |group|
  proxy_groups << {"name" => group, "type" => "select", "proxies" => Proxy1 + Proxy2}
end

Strategy3.each do |group|
  proxy_groups << {"name" => group, "type" => "select", "proxies" => Proxy1 + Proxy2 + ["DIRECT"]}
end

Proxy1.each do |group|
  proxy_groups << {"name" => group,
                        "type" => "load-balance",
                        "strategy" => "consistent-hashing",
                        "url" => "http://www.gstatic.com/generate_204",
                        "interval" => "300",
                        "disable-udp" => false,
                        "proxies" => ProxySet1[group]}
end
Proxy2.each do |group|
  proxy_groups << {"name" => group, "type" => "select", "proxies" => ProxySet2[group]}
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
