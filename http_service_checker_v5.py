from urllib.error import HTTPError
import urllib.request as urllib2

def check(protocol, host, port):   
   result = False
   error = None
   try:
      urllib2.urlopen(protocol + "://" + host + ":" + port, timeout=60000)
      result = True
      return port + " -> " + str(result) + ": " + str(error)
   except urllib2.URLError as exc:
      error = '{0}'.format(str(exc))
      #return port + "->" + str(result) + ": " + str(error)
      #return port + " -> " + "Service Exists"
      if error.lower().find("certificate") != -1 or error.lower().find("unauthorized") != -1:
         return port + " -> " + "Service Exists"
      else: 
         return port + " -> " + "Service Does Not Exist"
   #except urllib2.HTTPError as exc:
   #   error = 'HTTP Error: {0}'.format(str(exc))
   #   return port + "->" + str(result) + ": " + str(error)
   except Exception as exc:
      error = 'Unknown error: {0}'.format(str(exc))
      #return port + "->" + str(result) + ": " + str(error)
      return port + " -> " + "Service Does Not Exist"      
      #if error.lower().find("remote end closed connection without response") >0:
      #   return port + " -> " + "Service Does Not Exist"
      #else: 
      #   return port + " -> " + "Service Exists"
#A2A
a2a_hosts = ["UssAntApps436t.cotyww.com", "UssAntApps439t.cotyww.com", "UssAntApps531t.cotyww.com", "UssAntApps763t.cotyww.com", "UssAntApps764t.cotyww.com", "UssAntApps765t.cotyww.com"
, "UssAntApps445p.cotyww.com", "UssAntApps446p.cotyww.com", "UssAntApps447p.cotyww.com", "UssAntApps448p.cotyww.com", "UssAntApps449p.cotyww.com", "UssAntApps450p.cotyww.com"
, "UssAntApps774p.cotyww.com", "UssAntApps775p.cotyww.com", "UssAntApps775p.cotyww.com", "UssAntApps776p.cotyww.com", "UssAntApps777p.cotyww.com", "UssAntApps778p.cotyww.com", "UssAntApps779p.cotyww.com"]

#B2B
b2b_hosts = ["UssAntApps437t.cotyww.com", "UssAntApps615t.cotyww.com", "UssAntApps616t.cotyww.com"
, "UssAntApps443p.cotyww.com", "UssAntApps444p.cotyww.com", "UssAntApps761p.cotyww.com", "UssAntApps762p.cotyww.com"]

#AS2
as2_hosts = ["UssAntApps527t.cotyww.com", "UssAntApps721t.cotyww.com"
, "UssAntApps544p.cotyww.com", "UssAntApps545p.cotyww.com"]

portsToScan = [19999, 29999, 39999, 49999, 59999, 69999, 79999]
for host in as2_hosts:
   print("host: " + host)
   for port in portsToScan:              
      print(check("https", host, str(port)))
   print("======")
