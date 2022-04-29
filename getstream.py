import subprocess
import sys
import requests
import os
import play

dir = os.path.dirname(os.path.abspath(__file__))

def ytDl(id):
    dl_url="https://youtube.com/watch?v="+id
    out = subprocess.Popen(['youtube-dl','-f','251','-g',dl_url],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    stdout,stderr=out.communicate()
    #streamlinkfile=open(dir+"/data/stlink.txt", 'w')
    #streamlinkfile.write(stdout.decode("utf-8").strip()+"\n")
    #streamlinkfile.close()
    print(stdout.decode("utf-8").strip())
    return stdout.decode("utf-8").strip()

def getMid(index):
    midfile=open(dir+"/data/mid.txt", 'r')
    data=midfile.read().split("\n")
   #print(index,type(index))
    return data[index]

def currentpalying(index):
    searchfile=open(dir+"/data/searchres.txt", 'r')
    data=searchfile.read().split("\n")
    #streamlinkfile=open(dir+"/data/stlink.txt", 'a')
    #streamlinkfile.write(data[index]+"\n")
    #streamlinkfile.close()

def thumbdownload(index):
    thumbfile=open(dir+"/data/thumb.txt", 'r')
    data=thumbfile.read().split("\n")
    response = requests.get(data[index])
    if response.status_code == 200:
        with open(dir+"/data/thumb.jpg", 'wb') as f:
            f.write(response.content)


def main():
    appcodefile=open(dir+"/data/appcode.txt", 'w')
    if sys.argv[-1] != "":
        appcodefile.write("0")
        index=getMid(int(sys.argv[-1]))
        u=ytDl(index)
        #currentpalying(int(sys.argv[-1]))
        thumbdownload(int(sys.argv[-1]))
        play.main(u)
    else:
        appcodefile.write("1")
    appcodefile.close()

main()

