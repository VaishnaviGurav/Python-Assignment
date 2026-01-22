def SumDigit(N):

    if N < 0:
        return -1
    elif N == 0:
        return 0
    else:
        return (N % 10) + SumDigit(N // 10)
    
def main():
    no = int(input("Enter number: "))
    ret = SumDigit(no)
    if ret == -1:
        print("Invalid Number")
    else:
        print("Sum of digits:", ret)

if __name__ == "__main__":
    main()
