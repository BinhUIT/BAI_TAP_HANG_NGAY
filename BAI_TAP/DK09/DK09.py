def Nhap():
    n=int(input()) 
    return n 
def kiemtra(n):
    if(n<=0):
        return False
    if(n>=100000):
        return False
    return True
def kiemtranhuan(n):
    dk1=(n%4==0) and (n%100!=0)
    dk2=n%400==0
    if(dk1 or dk2):
        return True
    else:
        return False
def main():
    n=Nhap()
    if(kiemtra(n)==False):
        print("INVALID") 
    else:
        if(kiemtranhuan(n)):
            print("YES")
        else:
            print("NO")
if __name__=="__main__":
    main()
            

