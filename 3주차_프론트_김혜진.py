from bs4 import BeautifulSoup
import requests
from datetime import datetime
from selenium import webdriver
import json
import smtplib
from email.message import EmailMessage

total_list=[]

def save_fav(url, tag, class_name, chrome_driver_path):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("http://www.daum.net")
    response = driver.page_source.encode('utf-8', errors='replace')
    soup = BeautifulSoup(response, 'html.parser')
    results = soup.findAll("a", "link_favorsch")
    rank = 1

    search_rank_file = open("rankresult.txt","a")

    search_rank_file.write(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
    for result in results:
        search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
        print(rank, "위 : ", result.get_text(), "\n")
        rank += 1


city = "Seoul"
apikey = "3ba864bdb31f02abada676b78ac8b15e"
lang = "kr"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

result = requests.get(api)
data = json.loads(result.text)



while True:
    print("\n------------멋쟁이 사자처럼 전화번호부------------")
    print("------1) 추가 2) 조회 3) 수정 4)삭제 5)메일 전송  q) 종료------")
    print("-------------------------------------------------\n")

    menu = input("원하시는 메뉴를 입력해주세요 : ")

    if menu == "1":
        name = input("이름을 입력해주세요 : ")
        number = input(name + "님의 번호를 입력해주세요 : ")
        mail = input(name + "님의 메일을 입력해주세요 : ")
        total_list.append({"이름": name, "번호": number, "메일": mail})

    if menu == "2":
        namesearch = input("조회를 원하는 이름을 입력해주세요: ")
        for i in total_list:
            if i["이름"] == namesearch:
                print(i)
            else:
                print(" ")

    if menu == "3":
        namefix = input("수정을 원하는 이름을 입력해주세요: ")
        for i in total_list:
            if i["이름"] == namefix:
                orign, fix = input("수정을 원하는 항목과 내용을 입력해주세요 : ").split()
                if (orign == "번호"):
                    i["번호"] = fix
                elif (orign == "메일"):
                    i["메일"] = fix
                else:
                    print(" ")

    if menu == "4":
        namedel = input("삭제를 원하시는 이름을 입력해주세요 : ")
        for i in total_list:
            if i["이름"] == namedel:
                del i["이름"]
                del i["번호"]
                del i["메일"]
            else:
                print(" ")

    if menu == "5":
        namemail = input("메일 전송을 원하는 사람의 이름을 입력해주세요 : ")
        for i in total_list:
            if i["이름"] == namemail:
                SMTP_SERVER = "smtp.gmail.com"
                SMTP_PORT = 465

                message = EmailMessage()
                message.set_content(data["name"] + "의 날씨입니다." + "\n" + "날씨는 " + data["weather"][0][
                    "description"] + "입니다." + "\n" + "현재 온도는 " + str(
                    data["main"]["temp"]) + "입니다." + "\n" + "하지만 체감 온도는 " + str(data["main"]["feels_like"]) + "입니다.")

                message['Subject'] = '멋사 10기 프론트 김혜진 3주차 과제 .'
                message['From'] = 'fallinlemon@gmail.com'
                message['To'] = i["메일"]

                with open("rankresult.txt", "rb") as text:
                    text_file = text.read()
                    print("파일 저장이 완료되었습니다.")
                message.add_attachment(text_file, maintype='text', subtype='txt')
                print("정상적으로 메일이 발송되었습니다.")

                smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
                smtp.login('ID', 'PS')
                smtp.send_message(message)
                smtp.quit()
    if menu == "q":
        break

