#-*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


book={}
while True :
    print("-"*21+" 멋쟁이 사자처럼 "+"-"*21)
    print("-"*10+"1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료"+"-"*10)
    print("-"*59+"\n")
    menu=input("원하시는 메뉴를 입력해주세요 : ")
    if menu=="1" :
        name=input("이름을 입력해주세요 : ")
        book['이름']=name
        num=input(name+"님의 번호를 입력해주세요 : ")
        book["전화번호"]=num
        mail=input(name+"님의 메일을 입력해주세요 : ")
        book["메일"]=mail

    elif menu=="2" :
        name_2=input("조회를 원하시는 이름을 입력해주세요 : ")
        if name_2 in book.values() :
            print(book)
        else :
            print("전화번호부에 없는 이름입니다.")
    
    elif menu=="3" :
        name_3=input("수정을 원하는 이름을 입력해주세요 : ")
        new_key,new_value=input("수정을 원하는 항목과 이름을 입력해주세요 : ").split()
        if new_key=="이름":
            book["이름"]=new_value
        elif new_key=="전화번호":
            book["전화번호"]=new_value
        elif new_key=="메일":
            book["메일"]=new_value

    elif menu=="4" :
        name_4=input("삭제를 원하는 이름을 입력해주세요 : ")
        del book['이름']
        del book['메일']
        del book['전화번호']
        
    elif menu=="q" :
        break


