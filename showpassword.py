import zipfile
import optparse
from threading import Thread
def extractFile(zfile,password):
    try:
        zfile.extractall(pwd=password)
        print '[+]found password'+password+"\n"
    except:
        pass
def main():
    parser= optparse.OptionParser('zipcracker '+'-f<zipfile> -d <password list>')
    parser.add_option('-f',dest='zname',type='string',help='spcify zipfile')
    parser.add_option('-d',dest='dname',type='string',help='specify password file')
    (options,args)=parser.parse_args()
    if(options.zname==None)|(options.dname==None):
        print parser.usage
        exit(0)
    else:
        zname=options.zname
        dname=options.dname
        zfile=zipfile.ZipFile(zname)
        passfile=open(dname)
        for line in passfile.readlines():
            password=line.strip('\n')
            t=Thread(target=extractFile,args=(zfile,password))
            t.start()
if __name__=='__main__':
    main()
