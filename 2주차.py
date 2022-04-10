def start():
    print("-------------- 멋쟁이 사자처럼 전화번호부 --------------")
    print("----------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료------------")
    print("-------------------------------------------------------------")
    
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

