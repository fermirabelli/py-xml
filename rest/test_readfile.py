import uuid

def main():
    f=open("guru99.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print(contents)
        print(uuid.uuid4().hex+'.txt')
    f.close()
#print(__name__)
if __name__=="__main__":
    main()
