total_list = []
while True:
    print("-----------------멋쟁이 사자처럼 전화번호부 -----------------")
    print("-----------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료---------- ")
    print("--------------------------------------------------------")

    choice_menu = input("원하시는 메뉴를 입력해주세요: ")

    if choice_menu == '1':
        name = input("이름을 입력해주세요 :")
        phone_number = input(name + "님의 번호를 입력해주세요 :")
        mail = input(name + "님의 메일을 입력해주세요 :")
        information = {'이름': name, '전화번호': phone_number, '메일': mail}
        total_list.append(information)
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

    elif choice_menu == "q":
        break

