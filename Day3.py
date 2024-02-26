gear_ratio_doc = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

special_char = set("!@#$%^&*()_+{}[];:'\"<>,?/~`")

special_char_pos_doc = {}

gear_ratio_pos_doc = {}

gear_ratio_doc_size_y = 0
gear_ratio_doc_size_x = 0



def set_gear_ratio_doc_size():
    gear_ratio_doc_line = gear_ratio_doc.split("\n")
    gear_ratio_doc_size_x = len(gear_ratio_doc_line)
    gear_ratio_doc_size_y = (len(gear_ratio_doc) / (gear_ratio_doc_size_x - 1))

def get_special_character_location():
    for line_i, line in enumerate(gear_ratio_doc):
        for char in line:
            gear_ratio_pos_doc[line_i] = char 
            if char in special_char:
                special_char_pos_doc[line_i] = char

def check_if_char_is_near_special_char():
    num_list = ()
    num = 0

    for special_pos, special_char in special_char_pos_doc.items():
        
        special_pos_list = special_pos - (gear_ratio_doc_size_y + 1), special_pos - (gear_ratio_doc_size_y), special_pos - (gear_ratio_doc_size_y - 1)

        print(special_pos, special_char, special_pos_list)

        for pos, char in gear_ratio_pos_doc.items():
            
            

            if pos in special_pos_list and str(char).isdigit():
                print(pos, char)


            # if pos == special_pos - (gear_ratio_doc_size_y + 1) and str(char).isdigit(): #topleft
            #     # num = char
            #     print(pos, char)

            # elif pos == special_pos - gear_ratio_doc_size_y and str(char).isdigit(): #top
            #     # num = char
            #     print(pos, char)

            # elif pos == special_pos - (gear_ratio_doc_size_y - 1) and str(char).isdigit(): #topright
            #     # num = char
            #     print(pos, char)

            # elif pos == special_pos - 1 and str(char).isdigit(): #left
            #     # num = char
            #     print(pos, char)

            # elif pos == special_pos + 1 and str(char).isdigit(): #right
            #     # num = char
            #     print(pos, char)

            # elif pos == special_pos + (gear_ratio_doc_size_y - 1) and str(char).isdigit(): #bottomleft
            #     # num = char
            #     print(pos, char)

            # elif pos == special_pos + gear_ratio_doc_size_y and str(char).isdigit(): #bottom
            #     # num = char
            #     print(pos, char)

            # elif pos == special_pos + (gear_ratio_doc_size_y + 1) and str(char).isdigit(): #bottomright
            #     # num = char
            #     print(pos, char)            
                
                

            # num_list += num
            

            
            
            


def print_values_tester():
    # print(gear_ratio_pos_doc)
    # print(special_char_pos_doc)
    pass



set_gear_ratio_doc_size()
get_special_character_location()
check_if_char_is_near_special_char()
print_values_tester()

# print(special_char_pos_doc)