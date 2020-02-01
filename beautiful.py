a = input()

while(True):
    a = str(int(a)+1)
    if(len(set(a))==4):
        print(a)
        break;