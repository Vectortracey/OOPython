"""
main function for the program, with menu to choose action
"""

from unorderedlist import UnorderedList
from errors import NoIndexValue
from errors import ValueNotFound
from sort import insertion_sort, recursive_sort

class Handler():
    """
    class to handle the menu and inputs
    """

    print("1) Append to end of list.")
    print("2) Add new data to element at chosen index.")
    print("3) Return number of elements in list.")
    print("4) Return value of chosen index.")
    print("5) Returns index of chosen data. ")
    print("6) Print out the list. ")
    print("7) Remove node. ")
    print("8) Sort list.")
    print("9) Sort list, recursive style.")
    print("q) Quit.")


    unlinked_list = UnorderedList()
    while True:


        choice = input("--> ")


        if choice == "1":
            input_append = input("What to append?: ")
            unlinked_list.append(input_append)

        elif choice == "2":
            input_index = input("What index to replace?: ")
            input_data = input("With what data?: ")
            try:
                unlinked_list.set(int(input_index), input_data)
            except NoIndexValue:
                print("Can't find index")

        elif choice == "3":
            print(unlinked_list.size())


        elif choice == "4":
            input_indexpos = input("What index do you want to know data for?: ")
            input_indexpos = int(input_indexpos)
            try:
                print(unlinked_list.get(input_indexpos))
            except NoIndexValue:
                print("Can't find index")


        elif choice == "5":
            index_search = input("Index pos for what data?: ")
            try:
                print(unlinked_list.index_of(index_search))
            except ValueNotFound:
                print("Can't find chosen data")


        elif choice == "6":
            print(unlinked_list.print_list())


        elif choice == "7":
            input_data = input("What data do you want to remove?: ")
            try:
                unlinked_list.remove(input_data)
            except ValueNotFound:
                print("Error: No match of data in list")

        elif choice == "8":
            insertion_sort(unlinked_list)

        elif choice == "9":
            num = unlinked_list.size()
            print(recursive_sort(unlinked_list, num))

        elif choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break


        else:
            print("That is not a valid choice. You can only choose \
            from the menu.")
