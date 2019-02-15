import uuid
import datetime
import hashlib

def main():
    filename=uuid.uuid4().hex+'.txt'
    f= open(filename,"w+")
    for i in range(100):
         text='<time>'+str(datetime.datetime.utcnow())+'</time>'+'<test>resultado suma :'+str(uuid.uuid4())+str( abs(hash(str(datetime.datetime.utcnow()))) % (10 ** 8))+' :  line %d\r\n' % (i+1)
         f.write(text)
    f.close() 

if __name__=="__main__":
    main()
