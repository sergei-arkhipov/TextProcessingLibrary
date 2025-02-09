input_line = "one   two, one! two: three one two three one tho three One"
# input_line = "She     sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
# input_line = 'aba aba; aba @?"'

lower_english = "abcdefghijklmnopqrstuvwxyz"
lower_russian = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
clean_string = ""
words_indices_dict = {}

lower_string = input_line.lower()

for character in lower_string:
    if character in lower_english or character in lower_russian or character == " ":
        clean_string += character

no_double_spaces_list = list(filter(None, clean_string.split()))
#print(no_double_spaces_list)

#words_indices_dict = {key: [value, -2] for key, value in zip([i for i in range (0, len(no_double_spaces_list))], no_double_spaces_list)}
# print(words_indices_dict)

# for count in words_indices_dict:
#     if count == 0:
#         words_indices_dict[count][1] = -1
#         print(words_indices_dict[count][1], end=" ")
#     else:
#         for x in range(count-1, -1, -1):
#             if words_indices_dict[count][0] == words_indices_dict[x][0]:
#                 words_indices_dict[count][1] = x
#                 break
#             else:
#                 words_indices_dict[count][1] = -1
#         print(words_indices_dict[count][1], end=" ")

#     print(words_indices_dict[count])



# lst = []
# for i in range(len(no_double_spaces_list)):
#     lst.append(-1)


lst = [-1 for i in range(len(no_double_spaces_list))]
print(lst)
print(no_double_spaces_list)

# [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# ['one', 'two', 'one', 'two', 'three', 'one', 'two', 'three', 'one', 'tho', 'three', 'one']

dct = {}

# dct = {'one' : 0, 'two' : 1 }

for i in range(len(no_double_spaces_list)):


    if no_double_spaces_list[i] not in dct:
        dct[no_double_spaces_list[i]] = i

    else:
        lst[i] = dct[no_double_spaces_list[i]]
        dct[no_double_spaces_list[i]] = i

print(*lst, end =" ")

