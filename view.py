#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template,request,redirect,url_for,jsonify
from script.changeconf import changeconf
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nowstat/',methods=['GET'])
def nowstat():
    tlsstat = os.popen('./script/changeconf.sh 3').read().strip('\n')
    almstat = os.popen('./script/changeconf.sh 4').read().strip('\n')
    return jsonify({'tlsstat':tlsstat,'almstat':almstat})

@app.route('/tls/', methods=['POST'])
def tls():
    version = request.form.get('version')
    tlsstr = ""
    if(version=='auto'):
        tlsstr = '"TLSv1 TLSv1.1 TLSv1.2 TLSv1.3"'
    elif(version=='v0'):
        tlsstr = "TLSv1"
    elif(version=='v1'):
        tlsstr = "TLSv1.1"
    elif(version=='v2'):
        tlsstr = "TLSv1.2"
    elif(version=='v3'):
        tlsstr = "TLSv1.3"
    cmd = './script/changeconf.sh 0 '+tlsstr
    os.system(cmd)
    return redirect(url_for('index'))

@app.route('/algorithm/', methods=['POST'])
def algorithm():
    alm1 = request.form.get('alm1')
    alm2 = request.form.get('alm2')
    alm3 = request.form.get('alm3')
    alm4 = request.form.get('alm4')
    alm5 = request.form.get('alm5')
    alm6 = request.form.get('alm6')
    alm7 = request.form.get('alm7')
    almlist = []
    if(alm1 == 'true'):
        almlist.append("3DES") 
    if(alm2 == 'true'):
        almlist.append("AES")
    if(alm3 == 'true'):
        almlist.append("AESGCM")
    if(alm4 == 'true'):
        almlist.append("Camellia")
    if(alm5 == 'true'):
        almlist.append("IDEA")
    if(alm6 == 'true'):
        almlist.append("RC4")
    if(alm7 == 'true'):
        almlist.append("SEED")
    almstr = ":".join(almlist)
    cmd = './script/changeconf.sh 1 '+almstr
    os.system(cmd)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)