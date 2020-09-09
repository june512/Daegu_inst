import tkinter

window=tkinter.Tk()
window.title("InstaTeg Top10")     # 위젯 이름
window.geometry("600x600")      # 위젯 크기
window.resizable(False, False)  # 크기 고정

class FrameFront:
    case = 0
    def page_three(self,str_1):     # 지역의 카테고리에 따른 WordCloud를 보여주고 해쉬태그 Top10 보여주는 페이지
        if FrameFront.case == 1 :   # 어느 지역을 선택했는 지 확인하는 구문
            str_1 = '서울 ' + str_1
        elif FrameFront.case == 2 :
            str_1 = '대전 ' + str_1
        elif FrameFront.case == 3 :
            str_1 = '광주 ' + str_1
        elif FrameFront.case == 4 :
            str_1 = '부산 ' + str_1
        elif FrameFront.case == 5 :
            str_1 = '인천 ' + str_1
        elif FrameFront.case == 6 :
            str_1 = '대구 ' + str_1
        elif FrameFront.case == 7 :
            str_1 = '울산 ' + str_1
        frame4 = tkinter.Frame(window, bd=2, bg='lightskyblue')     # Frame을 새로이 만들어서 새로운 페이지 작성
        frame4.place(x=0,y=0,anchor="nw",width=600,height=600)
        label=tkinter.Label(frame4, text=str_1,bg='white')          # 지역이름과 카테고리 라벨
        label.place(anchor = "nw",x=40,y=30,width=520,height=60)
        label=tkinter.Label(frame4, text='TOP 10',bg='white')       # Top 10 라벨
        label.place(anchor = "nw",x=430,y=300,width=130,height=20)
        text1=tkinter.Text(frame4)                                  # WordCloud 출력하는 부분
        text1.place(x=40,y=110,anchor="nw",width=375,height=440)
        text2=tkinter.Text(frame4)
        text2.place(x=430,y=330,anchor="nw",width=130,height=220)
        b3_1=tkinter.Button(frame4, text="카페", bg='white',command=FrameFront.category1)   # 선택한 카테고리로 가기 
        b3_1.place(x=430, y=110, anchor="nw",width=60,height=60)
        b3_2=tkinter.Button(frame4, text="호텔", bg='white',command=FrameFront.category2)
        b3_2.place(x=430, y=180, anchor="nw",width=60,height=60)
        b3_3=tkinter.Button(frame4, text="공방", bg='white',command=FrameFront.category3)
        b3_3.place(x=500, y=110, anchor="nw",width=60,height=60)
        b3_4=tkinter.Button(frame4, text="맛집", bg='white',command=FrameFront.category4)
        b3_4.place(x=500, y=180, anchor="nw",width=60,height=60)
        b3_5=tkinter.Button(frame4, text="뒤로", bg='white',command=FrameFront.category5)   # 이전 페이지로 돌아가기
        b3_5.place(x=430,y=250, anchor="nw",width=130,height=30)

    @staticmethod
    def category1():
        FrameFront.page_three(0,'카페')     # 카페 카테고리를 가지고 세번째 페이지로 이동
    @staticmethod
    def category2():
        FrameFront.page_three(0,'호텔')     # 호텔 카테고리를 가지고 세번째 페이지로 이동
    @staticmethod
    def category3():
        FrameFront.page_three(0,'공방')     # 공방 카테고리를 가지고 세번째 페이지로 이동
    @staticmethod
    def category4():
        FrameFront.page_three(0,'맛집')     # 맛집 카테고리를 가지고 세번째 페이지로 이동
    @staticmethod
    def category5():                        # 지역의 이름을 가지고 두번째 페이지로 이동
        if FrameFront.case == 1 : 
            FrameFront.page_two(0,'서울')
        elif FrameFront.case == 2 :
            FrameFront.page_two(0,'대전')
        elif FrameFront.case == 3 :
            FrameFront.page_two(0,'광주')
        elif FrameFront.case == 4 :
            FrameFront.page_two(0,'부산')
        elif FrameFront.case == 5 :
            FrameFront.page_two(0,'인천')
        elif FrameFront.case == 6 :
            FrameFront.page_two(0,'대구')
        elif FrameFront.case == 7 :
            FrameFront.page_two(0,'울산')

    def page_two(self,str_1):   # 지역의 전체 해쉬태그 키워드를 보여주는 페이지
        frame3 = tkinter.Frame(window, bd=2, bg='lightskyblue')     # Frame을 새로이 만들어서 새로운 페이지 작성
        frame3.place(x=0,y=0,anchor="nw",width=600,height=600)
        label=tkinter.Label(frame3, text=str_1,bg='white')          # 지역의 이름 라벨
        label.place(anchor = "nw",x=40,y=30,width=520,height=60)
        text1=tkinter.Text(frame3)                                  # WordCloud 출력할 부분
        text1.place(x=40,y=110,anchor="nw",width=440,height=440)
        b3_1=tkinter.Button(frame3, text="카페", bg='white',command=FrameFront.category1)   # 각각의 카테고리 선택 버튼
        b3_1.place(x=500, y=110, anchor="nw",width=60,height=60)
        b3_2=tkinter.Button(frame3, text="호텔", bg='white',command=FrameFront.category2)
        b3_2.place(x=500, y=205, anchor="nw",width=60,height=60)
        b3_3=tkinter.Button(frame3, text="공방", bg='white',command=FrameFront.category3)
        b3_3.place(x=500, y=300, anchor="nw",width=60,height=60)
        b3_4=tkinter.Button(frame3, text="맛집", bg='white',command=FrameFront.category4)
        b3_4.place(x=500, y=395, anchor="nw",width=60,height=60)
        b3_5=tkinter.Button(frame3, text="뒤로", bg='white',command=FrameFront.page_one)    # 첫번째 페이지로 이동
        b3_5.place(x=500, y=490, anchor="nw",width=60,height=60)

    @staticmethod
    def read1():    # 서울을 가지고 두번째 페이지로 이동 
        FrameFront.case = 1
        FrameFront.page_two(0,'서울')
    @staticmethod
    def read2():    # 대전을 가지고 두번째 페이지로 이동 
        FrameFront.case = 2
        FrameFront.page_two(0,'대전')
    @staticmethod
    def read3():    # 광주를 가지고 두번째 페이지로 이동 
        FrameFront.case = 3
        FrameFront.page_two(0,'광주')
    @staticmethod
    def read4():    # 부산을 가지고 두번째 페이지로 이동 
        FrameFront.case = 4
        FrameFront.page_two(0,'부산')
    @staticmethod
    def read5():    # 인천을 가지고 두번째 페이지로 이동 
        FrameFront.case = 5
        FrameFront.page_two(0,'인천')
    @staticmethod
    def read6():    # 대구를 가지고 두번째 페이지로 이동 
        FrameFront.case = 6
        FrameFront.page_two(0,'대구')
    @staticmethod
    def read7():    # 울산을 가지고 두번째 페이지로 이동 
        FrameFront.case = 7
        FrameFront.page_two(0,'울산')

    @staticmethod
    def page_one(): # 지역을 선택하는 첫번째 페이지
        frame2=tkinter.Frame(window, bd=2, bg='lightskyblue')      # Frame을 새로이 만들어서 새로운 페이지 작성
        frame2.place(x=0,y=0,anchor="nw",width=600,height=600)
        b1_1=tkinter.Button(frame2, text="서울", bg='white',command=FrameFront.read1)   # 각각의 지역을 선택하는 버튼
        b1_1.place(x=70, y=60, anchor="nw",width=210,height=60)
        b1_2=tkinter.Button(frame2, text="대전", bg='white',command=FrameFront.read2)
        b1_2.place(x=70, y=200, anchor="nw",width=210,height=60)
        b1_3=tkinter.Button(frame2, text="광주", bg='white',command=FrameFront.read3)
        b1_3.place(x=70, y=340, anchor="nw",width=210,height=60)
        b1_4=tkinter.Button(frame2, text="부산", bg='white',command=FrameFront.read4)
        b1_4.place(x=70, y=480, anchor="nw",width=210,height=60)
        b2_1=tkinter.Button(frame2, text="인천", bg='white',command=FrameFront.read5)
        b2_1.place(x=320, y=60, anchor="nw",width=210,height=60)
        b2_2=tkinter.Button(frame2, text="대구", bg='white',command=FrameFront.read6)
        b2_2.place(x=320, y=200, anchor="nw",width=210,height=60)
        b2_3=tkinter.Button(frame2, text="울산", bg='white',command=FrameFront.read7)
        b2_3.place(x=320, y=340, anchor="nw",width=210,height=60)
        b2_4=tkinter.Button(frame2, text="EXIT", bg='white', command = quit)    # 위젯을 종료하는 버튼
        b2_4.place(x=320, y=480, anchor="nw",width=210,height=60)

    
    def __init__(self):     # 처음 페이지
        frame1=tkinter.Frame(window, bd=2, bg='lightskyblue')   # Frame을 새로이 만들어서 새로운 페이지 작성
        frame1.pack(fill="both", expand=True)

        text1=tkinter.Text(frame1)                              # 이미지 파일 출력 부분
        text1.place(x=70,y=30,anchor="nw",width=450,height=450)
        
        b1=tkinter.Button(frame1, text="START", bg='white',command=FrameFront.page_one)     # 시작 버튼
        b1.place(x=70, y=510, anchor="nw",width=450,height=60)
    

FrameFront()
window.mainloop()
