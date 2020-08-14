from selenium import webdriver
import requests, sys, webbrowser, bs4, os, metadata_parser, json,lxml.html
import mysql.connector
def search(url):
 res = requests.get(url)
 res.raise_for_status()
 soup = bs4.BeautifulSoup(res.text,"lxml")
 chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" #note the double \ syntax
 webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
 print("\n******************************************\n")


 selector='div#gsc_sa_ccl > div > div > div > h3 > a '
 foundElements = soup.select(selector)
 for i in range(len(foundElements)):
     link='https://scholar.google.com/'+foundElements[i].get('href') 
     response = requests.get(link) 
     sp = bs4.BeautifulSoup(response.text,"lxml")
     sel='#gsc_prf_i > div'
     find=sp.select(sel)
    
     result=str(find[0])
     x1='' 
     f=0
     for i in result:
         if(i=='<'):
            f=1
         if(f==0):
            x1=x1+i
         if(i=='>'):
            f=0    
     import unidecode
     name = unidecode.unidecode(x1)
     print(name)
     #x1=x1.decode('utf8')
     result=str(find[1])
     x='' 
     f=0
     for i in result:
         if(i=='<'):
            f=1
         if(f==0):
            x=x+i
         if(i=='>'):
            f=0    
     import unidecode
     info = unidecode.unidecode(x)
     print(info)
     print('\n********************************\n')
 browser = webdriver.Chrome()
 browser.get(url)
 doc = browser.find_elements_by_xpath('//*[@id="gsc_authors_bottom_pag"]/div/button[2]')[0]
 doc.click()
 next=browser.current_url
 browser.quit()
 search(next,sys.argv[1])
def main():
  search('https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:'+sys.argv[1])  
	
if __name__ == "__main__":
    main()
      