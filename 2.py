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
  for x in pbook:
    print(x.name,x.phone);

def modify(name,name1,phone1):
  for x in pbook:
    if x.name==name:
      x.name=name1
      x.phone=phone1;
while(True):
  print("1.연락처 추가");
  print("2.연락처 삭제");
  print("3.연락처 수정");
  print("4.전체 출력");
  print("5.종료");
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
    break;
    
##    #
##  elif m==2:
##    #
##  elif m==3:
##    #
##  elif m==4:
##    #
##  elif m==5:
        
