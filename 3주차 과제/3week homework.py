from selenium import webdriver
from email.message import EmailMessage
from datetime import datetime
import requests
import json
import smtplib

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

def send_mail():
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    message = EmailMessage()
    message.set_content("3주차 과제 테스트")

    message["Subject"] = "실시간 검색 및 오늘의 날씨 "
    message["From"] = "tomcat030519@gmail.com"
    message["To"] = "tomcat030519@gmail.com"

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login("tomcat030519@gmail.com", "020408gk")
    smtp.send_message(message)
    smtp.quit()


def today_weather():
    city = "Seoul"
    apikey = "b9e39dd17d769909cef50b73e80381b8"
    lang = "kr"
    api = f"""http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

    result = requests.get(api)

    data = json.loads(result.text)

    return data["name"] + "의 날씨입니다. \n" + "날씨는 " + str(data["weather"][0]["description"]) + "입니다.\n" + "현재 온도는 " + str( data["main"]["temp"]) + "입니다.\n" + "하지만 체감 온도는 " + str(data["main"]["feels_like"]) + "입니다.\n"

def print_menu():
    print("-------------- 멋쟁이 사자처럼 전화번호부 --------------")
    print("--------1) 추가 2) 조회 3) 수정 4) 삭제  5) 메일 전송 q) 종료--------")
    print("-----------------------------------------------------")


phone_book = []
set_phone_book = set(phone_book)

while True:
    print("")
    print_menu()
    print("")
    menu = input("원하시는 메뉴를 입력해주세요: ")

    if menu == "1":
        name = input("이름을 입력해주세요 : ")
        phone = input(name + "님의 번호를 입력해주세요 : ")
        email = input(name + "님의 메일을 입력해주세요 : ")
        phone_book.append({"이름": name, "전화번호": phone, "메일": email})
        print(phone_book)

    if menu == "2":
        name = input("조회를 원하는 이름을 입력해주세요: ")
        for x in phone_book:
            if x["이름"] == name:
                print(x)
            else:
                print("정보를 찰을수 없습니다.")

    if menu == "3":
        name = input("수정을 원하는 이름을 입력해주세요: ")
        fix = input("수정을 원하는 항목과 이름을 입력해주세요: ")
        fix = list(fix.split())
        for x in phone_book:
            if x["이름"] == name:
                x[fix[0]] = fix[1]
            else:
                print("정보를 찾을수 없습니다.")

    if menu == "4":
        name = input("삭제를 원하는 이름을 입력해주세요: ")
        for x in phone_book:
            if x["이름"] == name:
                del (x["이름"])
                del (x["전화번호"])
                del (x["메일"])
            else:
                print("정보를 찾을수 없습니다.")

    if menu == "5":
        name = input("메일 전송을 원하는 사람의 이름을 입력하세요: ")

        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 465

        message = EmailMessage()
        message.set_content(today_weather())

        message["Subject"] = "실시간 검색 및 오늘의 날씨 "
        message["From"] = "tomcat030519@gmail.com"
        message["To"] = "tomcat030519@gmail.com"

        with open(save_fav("http://daum.net/","a","link_favorsch","./chromedriver"),"rb") as text:
            text_file = text.read()
        message.add_attachment(text_file,maintype='text',subtype='txt')

        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login("id", "ps")
        smtp.send_message(message)

        smtp.quit()

    if menu == "q":
        break