from email import message
import requests
import json #자바스크립트
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib  #서버연결 
from email.message import EmailMessage
from selenium import webdriver
from time import sleep
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager



#메일 로그인
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT="465"

#실시간 검색어 크롤링

# 크롤링 API
def save_fav(url, tag, class_name,chrome_driver_path):
    # options = Options()
    # options.headless = True  # 브라우저 자동화 작업을 화면에 표시하지 않게 됨
    # driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url = url)
    
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    rank = 1

    results = soup.findAll(tag, class_name)

    search_rank_file = open("rankresult.txt","w")

    # 실시간 검색어 txt 파일 만들기
    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+ "\n")
        rank += 1

#연락처 시작
contact_list=[] #연락처리스트

while True:
    print("---------------\U0001F981 멋쟁이 사자처럼 전화번호부 \U0001F981---------------")
    print("------------1) 추가 2) 조회 3) 수정 4) 삭제 5)메일 전송 q) 종료------------")
    print("---------------------------------------------------------------")

    menu=input("원하시는 메뉴를 입력해주세요: ")

    if menu=="1": #추가
        name=input("이름을 입력해주세요: ")
        num=input(name+"님의 번호를 입력해주세요: ")
        email=input(name+"님의 메일을 입력해주세요: ")
        contact_list.append({"이름":name,"번호":num,"이메일":email})
        print("저장이 완료되었습니다.")

    if menu=="2": #조회

        for i in contact_list:
            print(contact_list)


    if menu=="3": #수정
        name1=input("수정을 원하는 이름을 입력해주세요: ")

        
        for i in contact_list:
            if i["이름"]==name1:
                a,b=input("수정을 원하는 항목과 내용을 입력해주세요: ").split()

                if a=="번호":
                    i["번호"]=b

                if a=="메일":
                    i["이메일"]=b

                else:
                    print("정보가 없습니다.")
                    break
                
         

    if menu=="4" : #삭제
        name2=input("삭제를 원하시는 이름을 입력해주세요: ")

        for i in contact_list:
            if i["이름"]==name2:
                del i["이름"]
                del i["번호"]
                del i["이메일"]
            


            else:
                print("정보가 없습니다.")
                break
    
    if menu=="5": #메일 전송 
        mailname=input("메일 전송을 원하는 사람의 이름을 입력해주세요: ")

        for i in contact_list:
            if i["이름"]==mailname:

                save_fav('https://www.daum.net/','a','link_favorsch','chromedriver.exe')
                
                city="Seoul"
                apikey="62ef3b638e9da2ddb2c31cb396f3c1d4"
                lang="kr"
                api=f"""http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric""" 
                result=requests.get(api)
                data=json.loads(result.text)
   
                message=EmailMessage()
                message.set_content(f"""{data["name"]}의 날씨입니다.날씨는 {data["weather"][0]["description"]}입니다.현재 온도는 {data["main"]["temp"]}입니다.하지만 체감 온도는 {data["main"]["feels_like"]} 입니다.""")

                message["Subject"]="멋사 과제입니다!"
                message["From"]="aoa8432@gmail.com"
                message["To"]=i["이메일"]

                with open("rankresult.txt",'rb') as text:
                     text_file=text.read()
                     message.add_attachment(text_file,maintype='text',subtype='txt',filename='rankresult.txt')
                
                smtp=smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
                smtp.login("aoa8432@gmail.com","codus0416!")
                smtp.send_message(message)
                smtp.quit()

                print("메일이 전송되었습니다.")


            else:
                print("정보가 없습니다.")    

            

    if menu=="q": #종료
        break