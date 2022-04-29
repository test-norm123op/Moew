import urllib.parse
import requests
import sys
import json
import os

dir = os.path.dirname(os.path.abspath(__file__))

def searchApi(query):
    base_url = "https://music.youtube.com/"
    sr_url=base_url+"search?q="+urllib.parse.quote_plus(query)
    sr_res={"results":[]}
    headers={"user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0","referer":sr_url}
    payload={
    "context":{
        "client":{
            "clientName":"WEB_REMIX",
            "clientVersion":"1.20220214.00.00"
        }
    },
    "query":query
    }
    res = requests.post("https://music.youtube.com/youtubei/v1/search?key=gadaghjadgdajdgajdgadvadavdajdavdda",headers=headers,json=payload)
    js=json.loads(res.content)
    main=js['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']
    for x in main:
        try:
            if x['musicShelfRenderer']['title']['runs'][0]['text'] == 'Top result':
                k=x['musicShelfRenderer']['contents']
                for song in k:
                    #print(song['musicResponsiveListItemRenderer']['thumbnail']['musicThumbnailRenderer']["thumbnail"]['thumbnails'])
                    sr_res['results'].append({"thumbnail":song['musicResponsiveListItemRenderer']['thumbnail']['musicThumbnailRenderer']["thumbnail"]['thumbnails'][0]['url'],
                    "mId":song['musicResponsiveListItemRenderer']['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']['playNavigationEndpoint']['watchEndpoint']['videoId'],
                    "title":song['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text'],
                    "duration":song['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][-1]['text'],
                    "type":song['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']
                    })
                    #sr_res['mId'].append(song['musicResponsiveListItemRenderer']['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']['playNavigationEndpoint']['watchEndpoint']['videoId'])
                    #sr_res['title'].append(song['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text'])
        
            if x['musicShelfRenderer']['title']['runs'][0]['text'] == 'Songs':
                k=x['musicShelfRenderer']['contents']
                for song in k:
                    sr_res['results'].append({"thumbnail":song['musicResponsiveListItemRenderer']['thumbnail']['musicThumbnailRenderer']["thumbnail"]['thumbnails'][0]['url'],
                    "mId":song['musicResponsiveListItemRenderer']['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']['playNavigationEndpoint']['watchEndpoint']['videoId'],
                    "title":song['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text'],
                    "duration":song['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][-1]['text'],
                    "type":song['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']
                    })
                    #sr_res['thumbnail'].append(song['musicResponsiveListItemRenderer']['thumbnail']['musicThumbnailRenderer']["thumbnail"]['thumbnails'][0]['url'])
                    #sr_res['mId'].append(song['musicResponsiveListItemRenderer']['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']['playNavigationEndpoint']['watchEndpoint']['videoId'])
                    #sr_res['title'].append(song['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text'])
            if x['musicShelfRenderer']['title']['runs'][0]['text'] == 'Videos':
                k=x['musicShelfRenderer']['contents']
                for song in k:
                    sr_res['results'].append({"thumbnail":song['musicResponsiveListItemRenderer']['thumbnail']['musicThumbnailRenderer']["thumbnail"]['thumbnails'][0]['url'],
                    "mId":song['musicResponsiveListItemRenderer']['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']['playNavigationEndpoint']['watchEndpoint']['videoId'],
                    "title":song['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text'],
                    "duration":song['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][-1]['text'],
                    "type":song['musicResponsiveListItemRenderer']['flexColumns'][1]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text']
                    })
                    #sr_res['thumbnail'].append(song['musicResponsiveListItemRenderer']['thumbnail']['musicThumbnailRenderer']["thumbnail"]['thumbnails'][0]['url'])
                    #sr_res['mId'].append(song['musicResponsiveListItemRenderer']['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']['playNavigationEndpoint']['watchEndpoint']['videoId'])
                    #sr_res['title'].append(song['musicResponsiveListItemRenderer']['flexColumns'][0]['musicResponsiveListItemFlexColumnRenderer']['text']['runs'][0]['text'])
                break
        except:
            continue
    return sr_res

def thumbdown(url,id):
    response = requests.get(url)
    if response.status_code == 200:
        with open(dir+"/data/thumb/"+str(id)+".jpg", 'wb') as f:
            f.write(response.content)

def prindata(data):
    #print(data)
    searchfile=open(dir+"/data/searchres.txt", 'w')
    midfile=open(dir+"/data/mid.txt", 'w')
    thumbfile=open(dir+"/data/thumb.txt", 'w')
    id=0
    for song in data['results']:
        title=song['title']
        thumbdown(song['thumbnail'],id)
        searchfile.write(title+"\n"+song['type']+" • "+song['duration']+"\x00icon\x1f"+dir+"/data/thumb/"+str(id)+".jpg"+"\x0f")
        midfile.write(song['mId']+"\n")
        thumbfile.write(song['thumbnail']+"\n")
        id=id+1
    searchfile.close()
    midfile.close()
    thumbfile.close()
    

def main():
    appcodefile=open(dir+"/data/appcode.txt", 'w')
    if sys.argv[-1] == "":
        appcodefile.write("1")
    else:
        appcodefile.write("0")
        data=searchApi(sys.argv[-1])
        prindata(data)
    appcodefile.close()


main()


