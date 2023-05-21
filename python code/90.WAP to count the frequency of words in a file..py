from collections import Counter
with open("file.txt","r") as file:
    words = file.read().split()
    word_count = Counter(words)
    print("Word frequency:",word_count)
