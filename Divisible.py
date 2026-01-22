def Divisible(Number):
    if Number % 3== 0 and Number % 5==0:
        return True
    else:
        return False
    

def main():
    print("Enter number:")
    Value = int(input())
    bRet = Divisible(Value)

    if bRet == True:
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")
    
if __name__ == "__main__":
    main()