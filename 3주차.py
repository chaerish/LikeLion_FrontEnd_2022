

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import requests
import json
import re
from selenium import webdriver

def start():
    print("-------------- 멋쟁이 사자처럼 전화번호부 --------------")
    print("----------1) 추가 2) 조회 3) 수정 4) 삭제 5)메일 전송 q) 종료------------")
    print("-------------------------------------------------------------")
    

def weather_inform():


    city = "Seoul"
    apikey = "31158dc890e019a53430f5e8888f689c"
    lang = "kr"

    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

    result = requests.get(api)
    data = json.loads(result.text)

    name = data["name"]
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp_felt = data["main"]["feels_like"]

    
    
    return data["name"]+"의 날씨입니다.\n""날씨는 "+str(data["weather"][0]["description"])+"입니다.\n""현재 온도는 "+str(data["main"]["temp"])+"입니다.\n""하지만 체감 온도는 "+str(data["main"]["feels_like"])+"입니다."
   
def mail_sending(input_mail):
    
   
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
    message.set_content(weather_inform())

    message["Subject"] = "멋쟁이사자처럼 3주차!"
    message["From"] = "shfur1320@gmail.com"
    message["To"] = input_mail 

    with open("rankresult.txt","rb") as text:
        text_file = text.read()

    
    message.add_attachment(text_file,maintype='text',subtype='txt')

    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
    smtp.login("id","ps")
    sendEmail(input_mail)
    smtp.quit()




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







total_list = []
while True:
    start()
    question = input("원하시는 메뉴를 입력해주세요 : ")
    if question == "q":
        break
    if question == "1":
        name = input("이름을 입력해 주세요 : ")
        num = input(name+"님의 번호를 입력해 주세요 : ")
        mail = input(name+"님의 메일을 입력해 주세요 : ")
        total_list.append({"이름" : name, "전화번호" : num, "메일" : mail})
    if question == "2":
        name_check = input("조회를 원하는 이름을 입력해주세요 : ")
        for i in total_list:
            if i["이름"] == name_check:
                print(i)
    if question == "3":
        m_name = input("수정을 원하는 이름을 입력해주세요 : ")
        re_key, re_val = input("수정을 원하는 항목과 이름을 입력해주세요 : ").split()
        for i in total_list:
            if i["이름"] == m_name:
                i[re_key] = re_val
    if question == "4":
        del_name = input("삭제를 원하는 이름을 입력해주세요 : ")
        for i in total_list:
            if i["이름"] == del_name:
                total_list.remove(i)
    if question == "5":
        mail_name = input("메일 전송을 원하는 사람의 이름을 입력해주세요 : ")
        for i in total_list:
            if i["이름"] == mail_name:
                to_mail = i["메일"]
        save_fav("http://daum.net/","a","link_favorsch","chromedriver.exe")
        print("파일 저장 완료")
        mail_sending(to_mail)


        



#save_fav("http://daum.net/","a","link_favorsch","chromedriver.exe")
#mail_sending("leesd132@naver.com")

