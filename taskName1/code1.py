input_line = "one two one tho three one"
#input_line = "She    sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
#input_line = 'aba aba; aba @?"'

lower_english = "abcdefghijklmnopqrstuvwxyz"
lower_russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
clean_string = ""
words_and_their_quantities_dict = {}

lower_string = input_line.lower()

for character in lower_string:
    if character in lower_english or character in lower_russian or character == " ":
        clean_string += character

no_double_spaces_list = list(filter(None, clean_string.split()))
#print(no_double_spaces_list)

lst = []

for count in no_double_spaces_list:
    if count not in words_and_their_quantities_dict:
        words_and_their_quantities_dict[count] = 0
    else:
        words_and_their_quantities_dict[count] += 1

    lst.append(words_and_their_quantities_dict[count])

print(*lst, end =" ")

# **input :** "one two one tho three one"  
# **output:** 0 0 1 0 0


# Выводим результат
# 0 0 1 0 0
