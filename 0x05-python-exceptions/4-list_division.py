#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for num in range(list_length):
        try:
            result = my_list_1[num] / my_list_2[num]
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            my_list.append(result)

    return my_list
