# find the sum of the numbers using loops
# numbers = [1, 4, 5093, 32444, 2200, 122]
# sum = 0
# for number in numbers:
#     sum = sum + number
#     print(sum)
# print(f"Total of the numbers : {sum}")

# print the given string with double characters
word = input("Enter the word :")
# letter = word
double_letter_word = ""

for letter in word:
    # double_letter = letter*2
    double_letter_word = double_letter_word + letter*2
    print(letter*2)

print(double_letter_word)
