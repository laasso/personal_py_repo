text =str(input('Introduce a text to count the frequency of the words'))
text = text.lower()
text_list = text.split()
count_word = {}

for word in range(0,len(text_list)):
    print(text_list[word])
    count_word[text_list[word]] = +1
    if word in count_word[text_list[word]]:
        count_word[text_list[word]] = +1


print (count_word)
print(text_list)