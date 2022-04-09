contact_list=[] #연락처리스트

while True:
    print("---------------\U0001F981 멋쟁이 사자처럼 전화번호부 \U0001F981---------------")
    print("------------1) 추가 2) 조회 3) 수정 4) 삭제 q) 종료------------")
    print("---------------------------------------------------------------")

    menu=input("원하시는 메뉴를 입력해주세요: ")

    if menu=="1": #추가
        name=input("이름을 입력해주세요: ")
        num=input(name+"님의 번호를 입력해주세요: ")
        email=input(name+"님의 메일을 입력해주세요: ")
        contact_list.append({"이름":name,"번호":num,"이메일":email})

    if menu=="2": #조회

        for i in contact_list:
            print(contact_list)


    if menu=="3": #수정
        name1=input("수정을 원하는 이름을 입력해주세요: ")

        
        for i in contact_list:
            if i["이름"]==name1:
                a,b=input("수정을 원하는 항목과 내용을 입력해주세요: ").split()

                if a=="번호":
                    i["번호"]=b

                if a=="메일":
                    i["이메일"]=b

                else:
                    print("정보가 없습니다.")
                    break
                
         

    if menu=="4" : #삭제
        name2=input("삭제를 원하시는 이름을 입력해주세요: ")

        for i in contact_list:
            if i["이름"]==name2:
                del i["이름"]
                del i["번호"]
                del i["이메일"]
            


            else:
                print("정보가 없습니다.")
                break


    if menu=="q": #종료
        break



            
            

        
    
    
            

        
        





