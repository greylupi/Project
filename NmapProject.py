import nmap3
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("Host", help="enter a domain or IP address")
args = parser.parse_args()

host = sys.argv[1]

nmap = nmap3.Nmap()
os_results = nmap.nmap_version_detection(host)
print(os_results)



print('============================================================')

for i in range(len(os_results[host]['ports'])):
        variable = os_results[host]['ports'][i]['portid']
        variable2 = os_results[host]['ports'][i]['service']['name']
        variable3 = os_results[host]['ports'][i]['service']['version']
        print ('[*] Discovered Port: ' + variable)
        print ('[*] Service : ' + variable2)
        print ('[*] Version : ' + variable3)
        print ('============================================================')

