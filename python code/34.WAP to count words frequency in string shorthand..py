s=input("Enter the string:")
words=s.split()
unique_words=set(words)
for word in unique_words:
    print(f"{word}:{words.count(word)}")
