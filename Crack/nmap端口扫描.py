import nmap

tgtHost = '192.168.100.1'
tgtPorts = range(20,80)

nmScan = nmap.PortScanner()
for tgtPort in tgtPorts:
    nmScan.scan(tgtHost,str(tgtPort))
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print('[%s]state:%s' % (tgtPort,state))