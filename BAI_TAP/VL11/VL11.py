import math
def Nhap():
	x = int(input())
	return x

def KtNguyenTo(x):
	if x<2:
		return 0
	for i in range(2,int(math.sqrt(x)+1),1):
		if x%i==0:
			return 0 
	return 1

def main():
	x = Nhap()
	if(KtNguyenTo(x)==1):
		print("YES")
	else:
		print("NO")

if __name__ == "__main__":
	main()