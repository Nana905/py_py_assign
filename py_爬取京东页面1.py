import re
import requests
from bs4 import BeautifulSoup
def getHTML(url):
    try:
        headers = {
            'cookie':'__jdu=466792166; areaId=4; PCSYCityID=CN_500000_500100_0; shshshfpa=3058bfd3-26b3-cb2d-0f3a-caf7ad9233ae-1621411763; shshshfpb=rQ0rhO%2F2UrzLCISV%2FO3IpRw%3D%3D; user-key=14287f74-c798-4485-99e2-27e10503544e; pinId=VixQz4IkyZlYHMduD0WCsw; pin=15922994574_p; _tp=ozfRCcQIbf2NToEvzgWDgQ%3D%3D; _pst=15922994574_p; rkv=1.0; ipLoc-djd=4-113-9786-0; unpl=V2_ZzNtbRBeRkJ1CBRdeB1YAGIEFl1LVxBHcQpAAH0bX1JlBxEOclRCFnUUR1BnGlwUZwMZWEdcQxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZH4eWwNvABJaRWdzEkU4dlBzGVkDbzMTbUNnAUEpCEZUfRlUSGIEFVtKVEMScjhHZHg%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_c84f11c82554465181bc537e732f352b|1621568735836; __jdc=122270672; shshshfp=764831dead60e343a54dbedb7faa6a32; __jda=122270672.466792166.1621411760.1621585157.1621588987.6; qrsc=3; wlfstk_smdl=4xhvy8tpluwdx89k5vx4ba94xtwkgiik; TrackID=1Z7O4HYUyUuVYQLbEIc-OykvZHf36sL-9Wn96EEegcWw-DLoLhlIYrJgLXG0_3D3tmPo-77URqHCP9IhZqkNSK4Qf01VcdvJYngbpH13oKHgfZJYi2jgn3uy-zFV07qlq; ceshi3.com=000; thor=755EFA843ECF03F120E17591875EC15A89FE869BAFFA0AD67AAD7BD8238C2A18CAB84321C263249D7A3CBDCEF04661D14E6378A7126438E46A00A982A2BB7C659807987730D2E21BE484AD60E4D2E98BB5D32D945BC7F6766BD461406BC94CA67C8569A9C29AA4B2E31C843CEFD37FE42617E51C4A216EDCBF1C2E0A2347DA43D7574480B81E485B7EA67955A8A640CC; __jdb=122270672.18.466792166|6.1621588987; shshshsID=3f59607310ee4493bc3be58de4647762_14_1621590999292; 3AB9D23F7A4B3C9B=LH4ZZ2OY5C6YNXY233RPXTONYZOCO46TARTWJQXLURCUYHZ3SIHMEEQ2DI4SNNL3YHIH2465MBMQOJUU7F4ZGZFBVU',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'
        }
        r=requests.get(url,timeout=30,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return  r.text
    except:
        print('爬取信息失败')
        return ''

def analysis(result,html):
    try:
        price1=re.findall(r'<em>￥</em><i>.*?\.\d\d',html)
        name1=re.findall(r'[^(<em>￥</em>)]<em>.*?[\u4e00-\u9fa5].*?</em>',html)
        for i in range(len(price1)):
            try:
                price=price1[i].split('<i>')[1]
                name=name1[i]
                result.append([price,name])
            except:
                continue
    except:
        print('')
def printGOOD(result):
    count=1
    print("{:4}\t{:8}\t{:16}".format("序号",'价格','名字'))
    for i in result:
        print("{:4}\t{:8}\t{:16}".format(count,i[0],i[1]))
        count+=1

def main():
    keyword=input('请输入您想要搜索的信息：')
    url='https://search.jd.com/Search?keyword='+keyword+'&page=1&s=1&click=0'
    result=[]
    pages=1
    try :
        html=getHTML(url)
        analysis(result,html)
    except:
        print('爬取失败')
    printGOOD(result)
if __name__ == '__main__':
    main()
