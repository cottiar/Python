from icmplib import ping

def host_up(hostname:str):
    host = ping(hostname, count=5, interval=0.2)
    return host.packets_sent == host.packets_received

hosts = ["UssAntApps436t.cotyww.com"]
ports = [19999, 29999, 39999, 49999, 59999, 69999, 79999]
for host in hosts:
    for port in ports:
        _url = host + ":" + str(port)
        try:
            if host_up(_url):
                print(f"{_url} is valid")
        except:
            print(f"{_url} is not valid")