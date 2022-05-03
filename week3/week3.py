#-*- coding: euc-kr -*-
import sys
import io
from typing import Text
import requests
import json
import smtplib
from email.message import EmailMessage
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from selenium import webdriver

city = "Seoul"
apikey = "246cd9fc7ce04d457364184f763e7e92"
lang = "kr"
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
data = json.loads(result.text)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
message = EmailMessage()
location = data["name"]
weather_description = data["weather"][0]["description"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

content = f"{location}의 날씨입니다.\n" \
          f"날씨는 {weather_description}입니다.\n" \
          f"현재 온도는 {temp}입니다.\n" \
          f"하지만 체감 온도는 {feels_like}입니다."

message.set_content(content)
message["Subject"] = "멋쟁이 사자처럼 3주차 과제 추인식"
message["From"] = "chooinsik@gmail.com"

url = "http://www.daum.net"
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url)
response = driver.page_source.encode('utf-8', errors='replace')
soup = BeautifulSoup(response, 'html.parser')
results = soup.findAll("a", "link_favorsch")
rank = 1

search_rank_file = open("rankresult.txt","a")
search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    rank += 1
driver.close()

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


book={}
while True :
    print("-"*21+" 멋쟁이 사자처럼 "+"-"*21)
    print("-"*10+"1) 추가 2) 조회 3) 수정 4) 삭제 5)메일 전송 q) 종료"+"-"*10)
    print("-"*59+"\n")
    menu=input("원하시는 메뉴를 입력해주세요 : ")
    if menu=="1" :
        name=input("이름을 입력해주세요 : ")
        book['이름']=name
        num=input(name+"님의 번호를 입력해주세요 : ")
        book["전화번호"]=num
        mail=input(name+"님의 메일을 입력해주세요 : ")
        book["메일"]=mail
        print("저장이 완료되었습니다.")

    elif menu=="2" :
        name=input("조회를 원하시는 이름을 입력해주세요 : ")
        if name in book.values() :
            print(book)
        else :
            print("전화번호부에 없는 이름입니다.")
    
    elif menu=="3" :
        name=input("수정을 원하는 이름을 입력해주세요 : ")
        new_key,new_value=input("수정을 원하는 항목과 이름을 입력해주세요 : ").split()
        if new_key=="이름":
            book["이름"]=new_value
        elif new_key=="전화번호":
            book["전화번호"]=new_value
        elif new_key=="메일":
            book["메일"]=new_value

    elif menu=="4" :
        name=input("삭제를 원하는 이름을 입력해주세요 : ")
        del book['이름']
        del book['메일']
        del book['전화번호']
    
    elif menu=="5" :
        name=input("메일 전송을 원하는 사람의 이름을 입력해주세요 : ")
        for i in book:
            if book["이름"]== name:
                mail=book["메일"]


        message["To"] = mail

        with open("rankresult.txt","rb") as text:
            text_file = text.read()
            print("파일 저장이 완료되었습니다.")

        message.add_attachment(text_file,maintype='text',subtype='txt',filename=text.name)

        smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
        smtp.login("ID","Password")
        smtp.send_message(message)
        smtp.quit()
        print("정상적으로 메일이 발송되었습니다.")
    elif menu=="q" :
        break


