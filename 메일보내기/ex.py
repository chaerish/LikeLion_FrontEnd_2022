# -*- coding: euc-kr -*-
import sys
import io
import json
import smtplib
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver

city = "Seoul"
apikey = "c95ee96228cac19bdac02620f00af210"
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
message["Subject"] = "이것은 제목입니다."
message["From"] = "bjb6478@gmail.com"

url = "http://www.daum.net"
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get(url)
response = driver.page_source.encode('utf-8', errors='replace')
soup = BeautifulSoup(response, 'html.parser')

results = soup.findAll("a", "link_favorsch")
rank = 1

search_rank_file = open("rankresult.txt", "a")
search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank) + "위:" + result.get_text() + "\n")
    rank += 1
driver.close()

#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

total_list = {}
while True:
    print("-----------------멋쟁이 사자처럼 전화번호부 -----------------")
    print("-----------1) 추가 2) 조회 3) 수정 4) 삭제 5)메일 전송 q) 종료---------- ")
    print("--------------------------------------------------------")

    choice_menu = input("원하시는 메뉴를 입력해주세요: ")
    if choice_menu == '1':
        name = input("이름을 입력해주세요 : ")
        total_list['이름'] = name
        num = input(name + "님의 번호를 입력해주세요 : ")
        total_list["전화번호"] = num
        mail = input(name + "님의 메일을 입력해주세요 : ")
        total_list["메일"] = mail
    elif choice_menu == '2':
        name = input("조회를 원하는 이름은 입력해주세요 :")
        for i in total_list:
            if name == i['이름']:
                print(i)
            else:
                print("등록되지 않은 정보입니다.")
    elif choice_menu == '3':
        name = input("수정을 원하는 이름을 입력해주세요 : ")
        for i in total_list:
            if name == i['이름']:
                key,value = ("수정을 원하는 항목과 내용을 입력해주세요 :").split()

                if(key == "전화번호"):
                    i['전화번호']=value
                elif(key == "메일"):
                    i['메일']=value
            else:
                print("등록되지 않은 정보입니다.")

    elif choice_menu =='4':
        name = input("삭제를 원하는 이름을 입력해주세요 :")
        for i in total_list:
           if name == i['이름']:
            del i['이름']
            del i['전화번호']
            del i['메일']

    elif choice_menu == "5":
        name = input("메일 전송을 원하는 사람의 이름을 입력해주세요 : ")
        for i in total_list:
            if total_list["이름"] == name:
                mail = total_list["메일"]

        message["To"] = mail

        with open("rankresult.txt", "rb") as text:
            text_file = text.read()
            print("파일 저장이 완료되었습니다.")
        message.add_attachment(text_file, maintype='text', subtype='txt', filename=text.name)

        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login("id", "pw")
        smtp.send_message(message)
        print("메일 전송이 완료되었습니다.")
        smtp.quit()
    elif choice_menu == "q":
        break

