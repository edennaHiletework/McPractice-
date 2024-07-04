def main():
    input_string = input("Enter a string: ")
    yourString = deVowel(input_string)
    print(yourString)

def deVowel(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in input_string:
        if letter not in vowels:
            result += letter
    return result
main()

import math  # Import math module here
def main():
    while True:
        numbers = [2, 4, 6, 8]
        multiplier = int(input("Enter a number to multiply by: "))
        results = mathStuff(numbers, multiplier)  # Call mathStuff function
        print("Results:", results)

        choice = input("Continue? (y/n): ")  # Fixed the prompt message
        if choice.lower() != 'y':
            break

def mathStuff(numbers, multiplier):
    multiplied_list = [num * multiplier for num in numbers]
    return multiplied_list


main()





