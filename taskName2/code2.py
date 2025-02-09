input_line = "apple orange banana banana orange"
#input_line = "a s d f g h j k l"
#input_line = 'aba aba; aba @?"'

lower_english = "abcdefghijklmnopqrstuvwxyz"
lower_russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
clean_string = ""
words_and_their_quantities_dict = {}
max_frequency = 0

lower_string = input_line.lower()

for character in lower_string:
    if character in lower_english or character in lower_russian or character == " ":
        clean_string += character

no_double_spaces_list = list(filter(None, clean_string.split()))
#print(no_double_spaces_list)

for word in no_double_spaces_list:
    if word not in words_and_their_quantities_dict:
        words_and_their_quantities_dict[word] = 1
    else:
        words_and_their_quantities_dict[word] += 1
    
    if words_and_their_quantities_dict[word] > max_frequency:
        max_frequency = words_and_their_quantities_dict[word]

most_frequent_words = []
for word, freq in words_and_their_quantities_dict.items():
    if freq == max_frequency:
        most_frequent_words.append(word)
#print(most_frequent_words)

#earliest_word = min(most_frequent_words)
print(sorted(most_frequent_words)[0])

print(f"{earliest_word} - наиболее часто встречающееся слово")

