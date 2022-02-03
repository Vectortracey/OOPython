"""
main function for the program, with menu to choose action
"""
import sys
from unorderedlist import UnorderedList
from errors import NoIndexValue
from errors import ValueNotFound


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
    print("q) Quit.")


    unlinked_list = UnorderedList()
    while True:
        print("\nWhat do you want to do?")


        choice = input("--> ")



        if choice == "q":
            print("Goodbye!")
            sys.exit()


        elif choice == "1":
            input_append = input("What do you want to append?: ")
            unlinked_list.append(input_append)

        elif choice == "2":
            input_index = input("which index do you want to replace?: ")
            input_data = input("With what data?: ")
            try:
                unlinked_list.set(int(input_index), input_data)
            except NoIndexValue:
                print("Can't find that index")

        elif choice == "3":
            print(unlinked_list.size())


        elif choice == "4":
            input_indexpos = input("which index do you want to know the the data from?: ")
            input_indexpos = int(input_indexpos)
            try:
                print(unlinked_list.get(input_indexpos))
            except NoIndexValue:
                print("Can't find the index")


        elif choice == "5":
            index_search = input("Index position for what data?: ")
            try:
                print(unlinked_list.index_of(index_search))
            except ValueNotFound:
                print("Can't find chosen data")


        elif choice == "6":
            unlinked_list.print_list()


        elif choice == "7":
            input_data = input("What data do you want to remove?: ")
            try:
                unlinked_list.remove(input_data)
            except ValueNotFound:
                print("Error: No match of data in list")
        else:
            print("That is not a valid choice. You can only choose \
            from the menu.")
