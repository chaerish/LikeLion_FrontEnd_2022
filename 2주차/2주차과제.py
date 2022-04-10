phone_book = []
while True:
    print("\n")
    print ("--------------🦁 멋쟁이 사자처럼 전화번호부 🦁--------------")
    print ("-----------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료-----------")
    print ("------------------------------------------------------------\n")
    num = input("원하시는 메뉴를 입력해주세요 : ")
    print("\n")

    if num == "1":
        name = input("이름을 입력해주세요 : ")
        phone_num = input(name+"님의 전화번호를 입력해주세요 : ")
        mail = input(name+"님의 메일을 입력해주세요 : ")
        phone_book.append({"이름" : name, "전화번호" : phone_num, "메일" : mail})
    
    elif num == "2":
        name = input("조회를 원하는 이름을 입력해주세요 : ")
        for i in phone_book:
            if i["이름"] == name:
                print(i)
            else :
                print(name + "님이 존재하지 않습니다")

    elif num == "3":
        name = input("수정을 원하는 이름을 입력해주세요 : ")
        for i in phone_book:
            
            if i["이름"]==name:
                ctgory, content = input("수정을 원하는 항목과 내용을 입력해주세요 : ").split()
                
                if ctgory == "전화번호":
                    i["전화번호"] = content
                   
                elif ctgory == "메일":
                    i["메일"] = content
                else : 
                    print("변경하려는 항목을 다시 입력해주세요")
            else :
                print(name + "님이 존재하지 않습니다")
    elif num == "4":
        name = input("삭제를 원하는 이름을 입력해주세요 : ")

        for i in phone_book:
            if i["이름"] == name:
                phone_book.remove(i)


    elif num == "q":
        break

    else:
        print("잘못 입력하셨습니다.")
