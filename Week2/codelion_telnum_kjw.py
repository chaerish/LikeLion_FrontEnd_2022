import random

print('-' * 14 + '멋쟁이사자처럼 전화번호부 '+ '-' * 14)
print('-' * 10 + '1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료 '+ '-' * 10)
print('-' * 50)

while True:
    user_sel = input("원하시는 메뉴를 입력해주세요 : ")

    if user_sel == 'q':
        break

    elif user_sel == '1':
        user_name = input("이름을 입력해주세요 : ")
        user_num = input("{}님의 번호를 입력해주세요 : " .format(user_name))
        user_mail = input("{}님의 메일을 입력해주세요 : " .format(user_name))
        user = {'이름': user_name, '전화번호': user_num, '메일': user_mail}

    elif user_sel == '2':
        user_name = input("조회를 원하는 이름을 입력해주세요 : ")
        if user_name == list(user.keys())[0]:
            print(user)

    elif user_sel == '3':
        user_name = input("수정을 원하는 이름을 입력해주세요 : ")
        user_change, user_changeto = input("수정을 원하는 항목과 이름을 입력해주세요 : ").split( )
        user[user_change] = user_changeto

    elif user_sel == '4':
         user_name = input("삭제를 원하는 이름을 입력해주세요 : ")
         if user_name == list(user.keys())[0]:
             user.clear()



