from urllib.error import HTTPError
import urllib.request

def check(host,port):       
   try:
    conn = urllib.request.urlopen("http://" + host + ":" + str(port))    
    return(conn.getcode())
   except HTTPError as e:
    return str(e.code)

hosts = ["UssAntApps436t.cotyww.com", "UssAntApps439t.cotyww.com", "UssAntApps531t.cotyww.com", "UssAntApps763t.cotyww.com", "UssAntApps764t.cotyww.com", "UssAntApps765t.cotyww.com"
, "UssAntApps445p.cotyww.com", "UssAntApps446p.cotyww.com", "UssAntApps447p.cotyww.com", "UssAntApps448p.cotyww.com", "UssAntApps449p.cotyww.com", "UssAntApps450p.cotyww.com"
, "UssAntApps774p.cotyww.com", "UssAntApps775p.cotyww.com", "UssAntApps775p.cotyww.com", "UssAntApps776p.cotyww.com", "UssAntApps777p.cotyww.com", "UssAntApps778p.cotyww.com", "UssAntApps779p.cotyww.com"]
ports = [19999, 29999, 39999, 49999, 59999, 69999, 79999]
for host in hosts:
    for port in ports:        
      result = check(host,port)
      if(result.isnumeric()):
         print(host + ":" + str(port) + " -> " + result)
      else:
         continue
         #print(host + ":" + str(port) + " -> " + "NA")
         
    print("======")