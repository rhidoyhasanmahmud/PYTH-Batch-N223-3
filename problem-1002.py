def compare(word1, word2):
    word = ""
    words = ""
    for i in word1:
        word += i
    for j in word2:
        words += j

    if word == words:
        print(f'\'{word}\' is same as \'{words}\'')
        return True
    print(f'\'{word}\' is not same as \'{words}\'')
    return False

word1 = []
word2 = []
while True:
    lst1 = input("Enter Items of word1 'e' To exit: ")

    if lst1 == "e":
        break
    word1.append(lst1)
print("Word1 is:", word1, '\n')

while True:
    lst2 = input("Enter Items of word2 'e' To exit: ")

    if lst2 == "e":
        break
    word2.append(lst2)
print("Word2 is:", word2, "\n")
print(compare(word1, word2))