import subprocess
import time
import os

dir = os.path.dirname(os.path.abspath(__file__))

def playM(url):
    #streamlinkfile=open(dir+"/data/stlink.txt", 'r+')
    #data=streamlinkfile.read().split("\n")
    searchfile=open(dir+"/data/searchres.txt", 'r')
    title=searchfile.read().split("\n")[0]
    cmd=""+url
    subprocess.Popen(['pkill','vlc'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
    time.sleep(0.2)
    subprocess.Popen(['notify-send','Moew Moew',title,"-i","~/moew/data/thumb.jpg"])
    subprocess.Popen(['cvlc',cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
    #streamlinkfile.write("")
    #streamlinkfile.close()


def main(url):
    playM(url)



