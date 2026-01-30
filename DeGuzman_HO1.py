num_list = []

word = input("Enter a word: ")
for i in range(len(word)):
    num = input(f"Enter a number {i + 1}: ")
    num_list.append(int(num))
print(num_list)   
print("The length of the word is", len(word))
print("The average of the numbers is", sum(num_list) / len(num_list))
if len(word) > sum(num_list) / len(num_list):
    print(f"The length of the word '{word}' is above the average of the numbers.")
else:
    print(f"The length of the word '{word}' is below the average of the numbers.")