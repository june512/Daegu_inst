from bs4 import BeautifulSoup 
import selenium.webdriver as webdriver
import urllib.parse # url 구문 분석
from urllib.request import Request, urlopen # url을 열고 읽기, url 오프너
from time import sleep  # 시간설정 
import pandas as pd 

search = input("검색어를 입력하세요 : " )   # 인스타그램 해쉬태그 검색할 단어 입력
search = urllib.parse.quote(search)
url = 'https://www.instagram.com/explore/tags/'+str(search)+'/' # 사이트 주소에 검색할 단어를 추가하여 사이트 이동
driver = webdriver.Chrome('C:\chomedriver\chromedriver.exe')   # chromewebdriver를 사용하기 위해 경로 입력  

driver.get(url) # Webdriver를 통해 url 열기
sleep(5)    # 창 오픈하는 데 시간이 약 5초소요되므로 5초간 Sleep을 시킴 

SCROLL_PAUSE_TIME = 1.0 # 스크롤을 할때 시간 설정
reallink = []   # 하이퍼링크 저장할 리스트

while True:
    pageString = driver.page_source # 웹에 보이는 그대로의 HTML, Chrome 개발자 도구의 Element 탭 내용 
    bsObj = BeautifulSoup(pageString, "lxml")   

    for link1 in bsObj.find_all(name="div",attrs={"class":"Nnq7C weEfm"}):  # 조건에 맞는 모든 태그들을 가져옴
        try:    # 오류가 나지않을 때 
            title = link1.select('a')[0]    # 1개의 스크롤당 3개의 사진 하이퍼링크를 리스트에 저장
            real = title.attrs['href']
            reallink.append(real) 
            title = link1.select('a')[1] 
            real = title.attrs['href']
            reallink.append(real) 
            title = link1.select('a')[2] 
            real = title.attrs['href']
            reallink.append(real) 
        except:     # 오류가 났을 때
            title = link1.select('a')[0]    # 스크롤당 무조건 3개가 되지 않음으로 예외처리를 하여 실행
            real = title.attrs['href']
            reallink.append(real) 

    last_height = driver.execute_script("return document.body.scrollHeight")    # 웹사이트의 전체 스크롤 크기를 받아옴
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # 스크롤 이동   
    sleep(SCROLL_PAUSE_TIME)    # 걸리는 시간동안 Sleep
    new_height = driver.execute_script("return document.body.scrollHeight")     # 현재 스크롤의 크기를 변수에 저장
    if len(reallink) >= 450:    # 리스트 범위를 450이상 되면 break
        break
    else :  # 그러지 않을 시에 밑에 구문 실행 
        if new_height == last_height:   # 현재 스크롤 크기와 전체 스크롤 크기가 같아지면 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # 스크롤 이동
            sleep(SCROLL_PAUSE_TIME)    # 걸리는 시간동안 Sleep
            new_height = driver.execute_script("return document.body.scrollHeight")     # 현재 스크롤의 크기를 변수에 저장


csvtext = []    # id와 해쉬태그를 저장할 리스트

reallinknum = len(reallink)
print("총"+str(reallinknum)+"개의 데이터.")     # 총 몇개의 하이퍼링크를 저장 했는지 출력

for i in range(0,reallinknum):      # 하이퍼링크를 i에 순차적으로 입력하
    csvtext.append([])      # 2차원 배열을 하기 위해서 
    req = Request('https://www.instagram.com/p'+reallink[i],headers={'User-Agent': 'Mozilla/5.0'})  # 하이퍼링크에 접속

    webpage = urlopen(req).read()   #url을 열기
    soup = BeautifulSoup(webpage,"lxml",from_encoding='utf-8')  
    soup1 = soup.find("meta",attrs={"property":"og:description"})   # 아이디를 검색후 변수에 저장
    
    reallink1 = soup1['content']    
    reallink1 = reallink1[reallink1.find("@")+1:reallink1.find(")")]
    reallink1 = reallink1[:20]
    if reallink1 == '':     # 아이디가 빈칸일때 
        reallink1 = 'Null'  # Null 값입력
    csvtext[i].append(reallink1)    # 아이디를 리스트에 저장
    
    for reallink2 in soup.find_all("meta",attrs={"property":"instapp:hashtags"}):   # 해쉬태그를 검색후 변수에 저장
        reallink2 = reallink2['content']    
        csvtext[i].append(reallink2)    # 해쉬태그를 리스트에 저장


    print(str(i+1)+"개의 데이터 받아오는 중.")  
    print(csvtext)
    data = pd.DataFrame(csvtext)    # DataFrame화 하기
    data.to_csv('instagangju.txt', encoding='utf-8')    # 텍스트파일 저장 
                           
print("저장성공")   
