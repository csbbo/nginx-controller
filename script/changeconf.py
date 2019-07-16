#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
def changeconf(tls_index:list,cipher_index:list,confpath='conf/nginx.conf',conf_template='./origin.conf'):
    tlslist = ['TLSv1','TLSv1.1','TLSv1.2','SSLv3']
    cipherlist = ['3DES','AES','AESGCM','CAMELLIA','IDEA','RC4','SEED']
    cipher_out = []
    tls_out = []
    for i in tls_index:
        if i > len(tlslist):
            print('index out of range!in function changeconf')
            return
        tls_out.append(tlslist[i])
    tls_out_str = ' '.join(tls_out)
    for i in cipher_index:
        if i > len(cipherlist):
            print('index out of range!in function changeconf')
            return
        cipher_out.append(cipherlist[i])
    cipher_out_str = ":".join(cipher_out)
    if not os.system("cp "+confpath+" "+confpath+'.back'):
        with open(conf_template,'r') as f:
            conf = f.read()
        print('[+] read  template ok')
        with open(confpath, 'w') as f:
            f.write(conf%(tls_out_str, cipher_out_str))
        print('[+] write conf ok')
        os.system('sudo make reload')
    else:
        print('cant cp conf file,check permissions!')
if __name__ == '__main__':
    changeconf([0,1,2,3],[0,1,2,5],'conf/nginx.conf','./origin.conf')
