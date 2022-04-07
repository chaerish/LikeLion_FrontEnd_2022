phone_info = []

while True:
    print("--------------🦁 멋쟁이 사자처럼 전화번호부 🦁--------------")
    print("----------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료----------")
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