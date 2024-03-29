#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for a in range(list_length):
        try:
            results = my_list_1[a] / my_list_2[a]
        except (ValueError, TypeError):
            print("wrong type")
            results = 0
        except ZeroDivisionError:
            print("division by 0")
            results = 0
        except IndexError:
            print("out of range")
            results = 0
        finally:
            new_list.append(results)
    return new_list
