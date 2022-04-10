number_list = []

while True:
    print("\n", "-"*14, "🦁 멋쟁이 사자처럼 전화번호부 🦁", "-"*14)
    print("-"*10, "1) 추가 2) 조회 3) 수정 4) 삭제 q)종료", "-"*10)
    print("-" * 56, "\n")

    menu_select = input("원하시는 메뉴를 입력해주세요 : ")

    if (menu_select == "1"):
        name = input("이름을 입력해주세요 : ")
        number = input(name + "님의 번호를 입력해주세요 : ")
        mail = input(name + "님의 메일을 입력해주세요 : ")

        number_list.append({"이름": name, "전화번호": number, "메일": mail})

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

    elif (menu_select == "q"):
        break

    else:
        print("메뉴 번호가 올바르지 않습니다. 다시 입력해 주세요")


