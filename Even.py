def Even(Number):
    for i in range(1, Number + 1):
        if i % 2 == 0:
           print(i, end=' ')
    
def main():
    print("Enter number:")
    
    No = int(input())
    Even(No)
    

if __name__ == "__main__":
    main()