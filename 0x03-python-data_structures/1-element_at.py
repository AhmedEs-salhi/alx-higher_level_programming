def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if idx < 0 or idx > len(my_list):
            return None
        if my_list[idx] == my_list[i]:
            return my_list[i]
