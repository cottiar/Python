import requests

hosts = ["19999", "29999", "39999", "49999", "59999", "69999"]
ports = [19999, 29999, 39999, 49999, 59999, 69999]
for x in ports:
    print("UssAntApps436t" + str(requests.get("http://UssAntApps436t.cotyww.com:" + str(x), auth=("SASRV_iWayMoniPrd", "feTg^!ipIJ4cqfrU")).getcode()))