#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup  
import requests  
import csv  
import bs4   
import time
import random

#检查url地址  
def check_link(url):  
    try:   
        r = requests.get(url)  
        r.raise_for_status()  
        r.encoding = r.apparent_encoding
        if r.status_code==200:
            new_r = r.text.replace('<br/>',' ') 
            new_r = new_r.replace('<hr/>','; ')   
            return new_r  
    except requests.ConnectionError:  
        print('无法链接服务器！！！')  
 
#爬取资源
def get_contents(urlist,rurl,url):  
    soup = BeautifulSoup(rurl, 'html.parser')
    trs = soup.find_all('tr') 
    
    for tr in trs:  
        ui = []  
        for td in tr:  
            ui.append(td.string)  
        urlist.append(ui)  
        
    for tr_node in trs:
        div_node = tr_node.find('div')
        if div_node != None:
            ui.append(div_node.text[20:]) 
            
    urlist.append(url) 
    #print(urlist)
    #print()
    #print( urlist[-1])
    
#保存资源  
def save_contents(urlist):  
    with open("‪企业认定信息表demo2019.csv",'a',newline='', encoding='utf-8') as f:  
        writer = csv.writer(f)  

        if urlist[2][3] == None:
            print('不存在')
            pass
        
        else:
            temp_list = []
            for i in range(1,11):
                temp_list.append(urlist[i][3])
            for i in range(12,29):
                temp_list.append(urlist[i][3])
            for i in range(30,32):
                temp_list.append(urlist[i][3])
            temp_list.append(urlist[-2][3])
            temp_list.append(urlist[-1])
            writer.writerow(temp_list)
            #writer.writerow(urlist)
            print('OK')
        
def main():  
    urlist = []
    for net in range(2019000000,2021000000): 
        print(net)    
        url = "http://www.njkjjr.cn/WeixinKjjr/DKInfo.jsp?DJXH=%s" % net  
        rs = check_link(url)  
        get_contents(urlist,rs,url)
        #print(urlist)
        save_contents(urlist)
        urlist = []
        time.sleep(random.random())
    print('done')

if __name__ == "__main__":
    main() 


# In[ ]:




