import uuid
import datetime
import hashlib
import time

def main():
    filename=uuid.uuid4().hex+'.txt'
    f= open(filename,"w+")
    ts = time.time()
    for i in range(100):
        ts = time.time()
        uid=uuid.uuid4()
        text='<time>'+str(datetime.datetime.utcnow())+'</time>'+'<test>resultado suma :'+str(abs(hash(str(uid))) % (10 ** 8))+' + '+str( abs(hash(str(ts))) % (10 ** 8))+' :  line %d\r\n' % (i+1)+'</test><resultado>'+ str(abs(hash(str(uid))) % (10 ** 8)+abs(hash(str(ts))) % (10 ** 8))+'</resultado><elapsed>'+str(time.time()-ts)+'</elapsed><idtest>'+str(uuid.uuid4())+'</idtest>'
        f.write(text)
    f.close() 

if __name__=="__main__":
    main()
