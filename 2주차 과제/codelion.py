def print_menu():
    print("-------------- 멋쟁이 사자처럼 전화번호부 --------------")
    print("--------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료--------")
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
        phone_book.append({"이름": name,"전화번호": phone,"메일": email})
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
                del(x["이름"])
                del(x["전화번호"])
                del(x["메일"])
            else:
                print("정보를 찾을수 없습니다.")


    if menu == "q":
        break
    

    
