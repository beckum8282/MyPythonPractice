import pickle
class contact:
    def __init__(self, name ,phone):
        self.name=name
        self.phone=phone;
pbook=[];

def add(name,phone):
  pbook.append(contact(name,phone));

def delete(name):
  for x in pbook:
    if x.name==name:
      pbook.remove(x);
      
def printbook():
        global pbook;
        for x in pbook:
                print(x.name,x.phone);

def SaveContact():
        global pbook;
        file=open("Contact.pb","wb")
        pickle.dump(pbook,file)
def LoadContact():
        global pbook;
        file=open("Contact.pb","rb");
        pbook=pickle.load(file);
        printbook();
def modify(name,name1,phone1):
  for x in pbook:
    if x.name==name:
      x.name=name1
      x.phone=phone1;
while(True):
  print("1. 연락처 추가");
  print("2. 연락처 삭제");
  print("3. 연락처 수정");
  print("4. 전체 출력");
  print("5. 파일로 연락처 저장");
  print("6. 저장된 연락처 가져오기")
  print("7. 종료");
  m=input("명령을 입력하세요\n");
  if m=='1':
    i,j=input("공백으로 구분하여 이름,전번 입력 : ").split();
    add(i,j);
  if m=='2':
    d=input("삭제할 이름 입력: ");
    delete(d);
  if m=='3':
    d,i,j=input("수정할 이름과 바뀐뒤 이름, 전번 입력: ").split();
    modify(d,i,j);
  if m=='4':
    printbook();
  if m=='5':
        SaveContact();
        print("저장되었습니다");
  if m=='6':
          LoadContact();
          print("저장된 전화번호부를 가져왔습니다");
  if m=='7':
    break;
