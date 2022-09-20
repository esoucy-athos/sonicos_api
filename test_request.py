#!user/bin/env python

import json
import requests
from requests.auth import HTTPDigestAuth

if __name__ == "__main__":
    with open('./devices.json', 'r') as f:
        data = json.load(f)
    snw1 = data['graham-fw']
    user = snw1['username']
    pw = snw1['password']
    host = snw1['ip']
    prt = snw1['port']
    headers = {
        'Accept': "*/*",
        'Content-Type': 'application/json; charset=UTF-8',
    }
    sess = requests.Session()
    #sess.auth = HTTPDigestAuth(user, pw)
    sess.headers = headers
    auth_path = "/api/sonicos/auth"
    request_path = "/api/sonicos/address-objects/ipv4"
    url_base = "https://" + host + ":" + str(prt)
    url_auth = url_base + auth_path
    url_request = url_base + request_path
    response = sess.head(url_auth, verify=False)
    #response = sess.get(url_request, verify=False)
    print(sess.headers)
    print(response)
    print(response.headers)