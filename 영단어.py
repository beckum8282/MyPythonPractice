import random
class Word:
    def __init__(self, Eng ,Kor):
        self.Kor=Kor
        self.Eng=Eng;
Words=[];
file=open("C:\work\words1200_o.txt","r"); #경로

u=1;
English=" ";
Korean=" ";
def init():
        global Words;
        lines=file.readlines()
        for line in lines:
                English=line[7:23];
                Korean=line[30:];
                English=English.strip();
                Korean=Korean.strip();
                Words.append(Word(English,Korean));
def quiz(Eng,Kor):
        global Words;
        print(Kor+" : ");
        a=input();
        ans(a,Eng,Kor);
        
def ans(answer,correct,kor):
        global u;
        if answer==correct:
                print("정답");
                u=0;
        else:
                print("오답");
                if len(correct) <u:
                                u=0;
                                print("완전히 틀리셨습니다, 다시 공부하세요");
                                start();
                print("힌트 : ");
                for x in range(u):
                        print(correct[x],end="");
                print("");
                u+=1;
                quiz(correct,kor);


def start():
        while True:
                P=random.choice(Words);
                quiz(P.Eng,P.Kor);
init();
start();

file.close();
