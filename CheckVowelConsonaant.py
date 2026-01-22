def CheckVowelsConsonants(input_string):
    vowels = 0
    consonants = 0
    for char in input_string.lower():
        if char.isalpha():
            if char in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    print("Number of Vowels:", vowels)
    print("Number of Consonants:", consonants)
    



def main():
    str_input = input("Enter a string: ")
    CheckVowelsConsonants(str_input)

if __name__ == "__main__":
    main()
    