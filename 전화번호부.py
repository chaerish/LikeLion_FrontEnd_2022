total_list=[]

while True:
    print("\n------------멋쟁이 사자처럼 전화번호부------------")
    print("------1) 추가 2) 조회 3) 수정 4)삭제 q) 종료------")
    print("-------------------------------------------------\n")

    menu = input("원하시는 메뉴를 입력해주세요 : ")

    if menu == "1":
        name = input("이름을 입력해주세요 : ")
        number = input(name + "님의 번호를 입력해주세요 : ")
        mail = input(name + "님의 메일을 입력해주세요 : ")
        total_list.append({"이름" : name, "번호" : number, "메일" : mail})

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
                if orign == "번호":
                    i["번호"] = fix
                elif orign == "메일":
                    i["메일"] = fix
                else:
                    print(" ")
    
    if menu =="4":
        namedel = input("삭제를 원하시는 이름을 입력해주세요 : ")
        for i in total_list:
            if i["이름"] == namedel:
                del i["이름"]
                del i["번호"]
                del i["메일"] 
            else:
                print(" ")
                
    if menu == "q":
        break