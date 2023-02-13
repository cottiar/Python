import socket

def check(host,port,timeout=2):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #presumably 
    sock.settimeout(timeout)
    try:
       sock.connect((host,port))
    except:
       return False
    else:
       sock.close()
       return True

hosts = ["UssAntApps436t.cotyww.com", "UssAntApps439t.cotyww.com", "UssAntApps531t.cotyww.com", "UssAntApps763t.cotyww.com", "UssAntApps764t.cotyww.com", "UssAntApps765t.cotyww.com"
, "UssAntApps445p.cotyww.com", "UssAntApps446p.cotyww.com", "UssAntApps447p.cotyww.com", "UssAntApps448p.cotyww.com", "UssAntApps449p.cotyww.com", "UssAntApps450p.cotyww.com"
, "UssAntApps774p.cotyww.com", "UssAntApps775p.cotyww.com", "UssAntApps775p.cotyww.com", "UssAntApps776p.cotyww.com", "UssAntApps777p.cotyww.com", "UssAntApps778p.cotyww.com", "UssAntApps779p.cotyww.com"]
ports = [19999, 29999, 39999, 49999, 59999, 69999, 79999]
for host in hosts:
    for port in ports:        
        print(host + ":" + str(port) + " -> " + str(check(host,port,timeout=600)))
    print("======")