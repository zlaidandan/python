#-*- coding: UTF-8 -*-
import urllib
import urllib2
import json
import random
import time
import thread

str_url = 'http://'
str_json = '{\"id\":\"edf62e0da5fb14e99bb4a25dfcfde6ae1\",\"imp\":[{\"splash\":0,\"impid\":\"825cd07f51114ce29b8dd6d6b3558105\",\"bidfloor\":0,\"bidfloorcur\":\"CNY\",\"w\":640,\"h\":100,\"instl\":0}],\"app\":{\"aid\":\"7e09b1302fdc47d7a9569a14bbc68028\",\"name\":\"安卓横幅2\",\"cat\":[\"60007\"],\"ver\":\"0\",\"bundle\":\"com.adsmogo\",\"paid\":0,\"storeurl\":\"https://adsmogo.com/mogo.apk\",\"Keywords\":\"\",\"Pid\":\"00000000000000000000000000000000\"},\"device\":{\"mac\":\"6B47CE2DB3F75BE40EAE0202E7EDBEE443532766\",\"dpid\":\"f37383b345d71aca\",\"ua\":\"Mozilla/5.0 (Linux; U; Android 3.1; zh-cn; GT-P7510 Build/HMJ37) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13\",\"ip\":\"110.249.163.214\",\"country\":\"cn\",\"carrier\":\"00000\",\"language\":\"zh\",\"make\":\"samsung\",\"model\":\"GT-P7510\",\"os\":\"Android\",\"osv\":\"3.1\",\"connectiontype\":1,\"devicetype\":2,\"loc\":\"38.02523227142858,114.53447685714286\",\"sw\":800,\"sh\":1280,\"orientation\":1}}'

headers = {"Content-Type":"application/json"}
urllib2.socket.setdefaulttimeout(2)

def run():
    while True:
        try:
            req = urllib2.Request(str_url, str_json, headers)
            response = urllib2.urlopen(req)

            if response.getcode() == 200:
                str_result = response.read()
                response.close()
                #print str_result
                try:
                    json_s = json.loads(json.dumps(json.loads(json.dumps(json.loads(str_result)["seatbid"][0]))["bid"][0]))
                    curl = json_s["curl"]
                    iurl = json_s["iurl"]
                    cturl = json_s["cturl"][0]

                    req = urllib2.Request(iurl)
                    response = urllib2.urlopen(req)
                    print "iurl:%s" %( response.getcode())
                    response.close()
                    if random.uniform(0,1000) < 5:
                        req = urllib2.Request(cturl)
                        response = urllib2.urlopen(req)
                        print "iurl:%s" %( response.getcode())
                        response.close()
                        req = urllib2.Request(curl)
                        response = urllib2.urlopen(req)
                        print "iurl:%s" %( response.getcode())
                        response.close()

                except Exception, e:
                   print 'err'
        except Exception, e:
            print 'timeout'
        time.sleep(0.5)

def exe():
    for i in range(0, 100):
        thread.start_new_thread(run,())


if __name__ == '__main__':
    exe()
    while True:
        time.sleep(3600)
