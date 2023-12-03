calib_doc = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


# calib_doc.splitlines()
# num_str_dict = {"nine": "9", "six": "6"}

#part 2 module, i don't like that... it doesn't work xD 

#Alone. I lay Defeated. But I'm not dead! yet.

letter_num_calib_doc = calib_doc.split("\n")




def find_first_line_num():
    char_index_num = [0]
    back_char_index_num = [-1]

    num_word = ""
    back_num_word = ""

    for line in letter_num_calib_doc:
        print(line)
        num_word = ""
        for char in line:
            print(char)
            if char.isdigit():
                pass
            elif char in "two":
                num_word += char
                print ("num_word", num_word)
                if num_word == "two":
                    letter_num_calib_doc = str(letter_num_calib_doc).replace(char, "2", 1)
                    num_word = ""
                    break

            elif char in "eight":
                num_word += char
                print ("num_word", num_word)
                if num_word == "eight":
                    letter_num_calib_doc = str(letter_num_calib_doc).replace(char, "8", 1)
                    num_word = ""
                    break

            elif char in "one":
                num_word += char
                print ("num_word", num_word)
                if num_word == "one":
                    letter_num_calib_doc = str(letter_num_calib_doc).replace(char, "1", 1)
                    num_word = ""
                    break
                
            elif char in "three":
                num_word += char
                print ("num_word", num_word)
                if num_word == "three":
                    letter_num_calib_doc = str(letter_num_calib_doc).replace(char, "3", 1)
                    num_word = ""
                    break
                
            elif char in "four":
                num_word += char
                print ("num_word", num_word)
                if num_word == "four":
                    letter_num_calib_doc = str(letter_num_calib_doc).replace(char, "4", 1)
                    num_word = ""
                    break
                
            elif char in "five":
                num_word += char
                print ("num_word", num_word)
                if num_word == "five":
                    letter_num_calib_doc = str(letter_num_calib_doc).replace(char, "5", 1)
                    num_word = ""
                    break
                




        # elif char in "nine":
        #     num_word += char
        #     if num_word == "nine":
        #         str(letter_num_calib_doc).replace("nine", "9", 1)
        #         num_word = ""
        #         break

        # elif char in "one":
        #     num_word += char
        #     if num_word == "one":
        #         str(letter_num_calib_doc).replace("one", "1", 1)
        #         num_word = ""
        #         break 

            else:
                num_word = ""


    print(letter_num_calib_doc)

def find_last_line_num():
    pass

# num_str_dict = {"nine": "9", "six": "6", "one": "1", "two": "2", "three": "3", "four": "4", "seven": "7", "eight": "8"}
# calib_doc_num_dict = {}

# Iterate through each character in the document
# for char in calib_doc:
#     # If the character is a digit, add it directly to the result dictionary
#     if char.isdigit():
#         calib_doc_num_dict[char] = True
#     # If the character is a letter, check if it's part of a numeric word
#     elif char.isalpha():
#         current_word = char
#         while char.isalpha():
#             char = next(iter(calib_doc), '')
#             current_word += char
#         # If the word is in the mapping dictionary, replace it with the corresponding number
#         if current_word.lower() in num_str_dict:
#             calib_doc_num_dict[current_word] = num_str_dict[current_word.lower()]

# print(calib_doc_num_dict)


# for char in calib_doc:
#     if char in "one":
#         calib_doc_num_dict[char] += char
#         if calib_doc_num_dict[char] == "one":
#             calib_doc_num_dict[char: True]
#         else:
#             calib_doc_num_dict[char: False]

# print(calib_doc_num_dict)


# prev_char = ""

# for char in calib_doc:
#     if char == "o":
#         prev_char = char
#     elif char == "t":
#         prev_char = char
#     elif char == "f":
#         prev_char = char
#     elif char == "s":
#         prev_char = char
#     elif char == "e":
#         prev_char = char
#     elif char == "n":
#         prev_char = char
    

#     if prev_char == "o" and char == "n":
#         calib_doc = calib_doc.replace("one", "1")
#     elif prev_char == "t" and char == "w":
#         calib_doc = calib_doc.replace("two", "2")
#     elif prev_char == "t" and char == "h":
#         calib_doc = calib_doc.replace("three", "3")
#     elif prev_char == "f" and char == "o":
#         calib_doc = calib_doc.replace("four", "4")
#     elif prev_char == "f" and char == "i":
#         calib_doc = calib_doc.replace("five", "5")
#     elif prev_char == "s" and char == "i":
#         calib_doc = calib_doc.replace("six", "6")
#     elif prev_char == "s" and char == "e":
#         calib_doc = calib_doc.replace("seven", "7")
#     elif prev_char == "e" and char == "i":
#         calib_doc = calib_doc.replace("eight", "8")
#     elif prev_char == "n" and char == "i":
#         calib_doc = calib_doc.replace("nine", "9")



# calib_doc = calib_doc.replace("nine", "9")
# calib_doc = calib_doc.replace("eight", "8")
# calib_doc = calib_doc.replace("seven", "7")
# calib_doc = calib_doc.replace("six", "6")
# calib_doc = calib_doc.replace("five", "5")
# calib_doc = calib_doc.replace("four", "4")
# calib_doc = calib_doc.replace("three", "3")
# calib_doc = calib_doc.replace("two", "2")
# calib_doc = calib_doc.replace("one", "1")

calib_doc = str(calib_doc)

#remove every letter from the string
new_calib_doc = "".join([char for char in calib_doc if not char.isalpha()])


#Split the string into line
calib_doc = new_calib_doc.split("\n")

final_num = 0

#calculate
for i, line_num in enumerate(calib_doc):
    if line_num:
        new_line_num = line_num[0], line_num[-1]
        prev_line_num = int(line_num)
    
    # line_num = calib_doc[i]
    # new_line_num = line_num[0], line_num[-1]

        line_num = new_line_num[0] + new_line_num[-1]

        final_num += int(line_num)

        print(line_num)
   
print("Final number is", final_num)





# droplist = ("123", "5641", "4654")

# new_calib_doc = [int(element) for element in new_calib_doc]

# for i, lign in enumerate(droplist_int):
#     if lign > 2:
#         droplist_int[i] = lign, lign
