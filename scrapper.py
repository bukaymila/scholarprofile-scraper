from bs4 import BeautifulSoup
import requests

def main(url):
    y=0
    count = 0
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
    fullurl = url + '&view_op=list_works&sortby=pubdate&cstart='+ str(count)+'&pagesize=100'

    response=requests.get(fullurl,headers=headers)
    soup=BeautifulSoup(response.content, 'lxml')
    name=soup.select('#gsc_prf_in')[0].get_text()
    length=len(soup.select('.gsc_a_at'))

    with open(name + ".txt", "w", newline ="", encoding = "UTF-8") as file:
        while length == 100:
            for x in range(length):
                file.write(soup.select('.gsc_a_at')[x].get_text() + "\n")
                file.write(soup.select('.gs_gray')[y].get_text() + "\n")
                file.write(soup.select('.gs_gray')[y+1].get_text() + "\n")
                file.write(soup.select('.gsc_a_h.gsc_a_hc.gs_ibl')[x].get_text() + "\n")
                file.write("\n")
                y=y+2
            count+=100
            fullurl = url + '&view_op=list_works&sortby=pubdate&cstart='+ str(count)+'&pagesize=100'
            response=requests.get(fullurl,headers=headers)
            soup=BeautifulSoup(response.content, 'lxml')
            length=len(soup.select('.gsc_a_at'))
            y=0
        else:
            for x in range(length):
                file.write(soup.select('.gsc_a_at')[x].get_text() + "\n")
                file.write(soup.select('.gs_gray')[y].get_text() + "\n")
                file.write(soup.select('.gs_gray')[y+1].get_text() + "\n")
                file.write(soup.select('.gsc_a_h.gsc_a_hc.gs_ibl')[x].get_text() + "\n")
                file.write("\n")
                y=y+2       
    file.close()
    return "Done"