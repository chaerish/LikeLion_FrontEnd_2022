from bs4 import BeautifulSoup
import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import re
import json
from selenium import webdriver

number_list = []

# 날씨 정보
city = "Seoul"
apikey = "2953b480aff6da7b85ab8d2a244ebcfd"
lang = "kr"
units = "metric"
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units={units}"""

result = requests.get(api)
data = json.loads(result.text)

content = (data["name"] + "의 날씨입니다." + "\n" + "날씨는 " + data["weather"][0]["description"] + "입니다."
           + "\n" + "현재 온도는 " + str(data["main"]["temp"]) + "입니다." + "\n" + "하지만 체감 온도는 " + str(
            data["main"]["feels_like"]) + "입니다.")

#실시간 검색어
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
    rank += 1

driver.close()

while True:
    print("\n", "-"*14, "🦁 멋쟁이 사자처럼 전화번호부 🦁", "-"*14)
    print("-"*5, "1) 추가 2) 조회 3) 수정 4) 삭제 5)메일 전송 q)종료", "-"*5)
    print("-" * 56, "\n")

    menu_select = input("원하시는 메뉴를 입력해주세요 : ")

    if (menu_select == "1"):
        name = input("이름을 입력해주세요 : ")
        number = input(name + "님의 번호를 입력해주세요 : ")
        mail = input(name + "님의 메일을 입력해주세요 : ")

        number_list.append({"이름": name, "전화번호": number, "메일": mail})
        print("저장이 완료되었습니다.")

    elif (menu_select == "2"):
        ask_name = input("조회를 원하는 이름을 입력해주세요 : ")
        find_name = next((item for item in number_list if item['이름'] == ask_name), None)
        print(find_name)

    elif (menu_select == "3"):
        change_name = input("수정을 원하는 이름을 입력해주세요 : ")
        change_items = input("수정을 원하는 항목을 입력해주세요 : ")
        change_items_value = input("수정을 원하는 내용을 입력해주세요 : ")

        change_index = next((index for (index, item) in enumerate(number_list) if item['이름'] == change_name), None)
        number_list[change_index][change_items] = change_items_value

    elif (menu_select == "4"):
        del_name = input("삭제를 원하는 이름을 입력해주세요 : ")

        del_index = next((index for (index, item) in enumerate(number_list) if item['이름'] == del_name), None)
        del number_list[del_index]

        print(number_list)

    elif (menu_select == "5"):
        mail_name = input("메일 전송을 원하는 사람의 이름을 입력해주세요 : ")
        mail_email = next((item for item in number_list if item['이름'] == mail_name), None)
        email_address = str(mail_email["메일"])

        # 메일 보내기
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 465

        message = EmailMessage()
        message.set_content(content)

        message["Subject"] = "멋쟁이 사자처럼 과제"
        message["From"] = "ssidaburim@gmail.com"
        message["To"] = email_address

        with open("rankresult.txt","rb") as text:
            text_file = text.read()
            print("파일 저장이 완료되었습니다.")

        message.add_attachment(text_file,maintype='text',subtype='txt')

        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login("ID@gmail.com", "PW")
        smtp.send_message(message)
        smtp.quit()
        print("정상적으로 메일이 발송되었습니다.")

    elif (menu_select == "q"):
        break

    else:
        print("메뉴 번호가 올바르지 않습니다. 다시 입력해 주세요")
