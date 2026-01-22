def ChkGreater(Value1,Value2):
    if Value1 > Value2:
        return True
    else:
        return False
    
def main():

    bRet = ChkGreater(10,20)

    if bRet == True:
        print("First number is greater")
    else:
        print("Second number is greater")
      
if __name__ == "__main__":
    main()
