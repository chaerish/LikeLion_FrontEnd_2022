from datetime import datetime

import requests
import smtplib
from email.message import EmailMessage
import re
import json

from selenium.webdriver.chrome import webdriver
from bs4 import BeautifulSoup


city = "Seoul"
apikey = "apikey"
lang = "kr"
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric" # ? 앞쪽은 공통내용
result = requests.get(api)
data = json.loads(result.text)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")
        
message = EmailMessage()
country = data["name"]
weather = data["weather"][0]["description"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]

content = f"{country}의 날씨입니다.\n날씨는 {weather}입니다.\n현재 온도는 {temp}입니다.\n하지만 체감 온도는 {feels_like}입니다."

message.set_content(content)
message["Subject"] = "[3주차 과제] 이서연"
message["From"] = "id"

# 크롤링 API
def save_fav(url, tag, class_name, chrome_driver_path):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(url = url)
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    rank = 1

    results = soup.findAll(tag, class_name)

    search_rank_file = open("rankresult.txt","a")

    # 실시간 검색어 txt 파일 만들기
    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+ "\n")
        rank += 1

phone_info = []

while True:
    print("--------------🦁 멋쟁이 사자처럼 전화번호부 🦁--------------")
    print("----------1) 추가 2) 조회 3) 수정 4) 삭제 5) 메일 전송 q) 종료----------")
    print("------------------------------------------------------------")

    select = input("원하시는 메뉴를 입력해주세요: ")
    if select == "q":
        break
    
    elif select == "1":
        phone_info.append({"이름": "", "전화번호": "", "메일": ""})
        name = input("이름을 입력해주세요: ")
        ph_num = input(name + "님의 번호를 입력해주세요: ")
        mail = input(name + "님의 메일을 입력해주세요: ")
        phone_info[-1]["이름"] = name
        phone_info[-1]["전화번호"] = ph_num
        phone_info[-1]["메일"] = mail 
        for i in phone_info:
            if i["이름"] == name:
                print("저장이 완료되었습니다!")
         
    elif select == "2":
        name = input("조회를 원하는 이름을 입력해주세요: ")
        for i in phone_info:
            if i["이름"] == name:
                print(i)
            else:
                continue
            
    elif select == "3":
        name = input("수정을 원하는 이름을 입력해주세요 : ")
        type, edit = input("수정을 원하는 항목과 이름을 입력해주세요 : ").split()
        for i in phone_info:
            if i["이름"] == name:
                i[type] = edit

    elif select == "4":
        name = input("삭제를 원하는 이름을 입력해주세요 : ")
        for i in phone_info:
            if i["이름"] == name:
                phone_info.remove(i)
                
    elif select == "5":
        name = input("메일 전송을 원하는 사람의 이름을 입력해주세요: ")
        for i in phone_info:
            if i["이름"] == name:
                mail = i["메일"]
        message["To"] = mail
        
        with open("rankresult.txt","rb") as f:
            text_file = f.read()
        message.add_attachment(text_file, maintype = 'text', subtype = 'txt', filename = f.name)
        
        smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
        smtp.login("id", "ps")
        sendEmail(mail)
        smtp.quit()