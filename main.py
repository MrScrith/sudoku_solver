# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sudoku import *





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_list = []
    start_list.append((0, 1, 6))
    start_list.append((0, 2, 9))
    start_list.append((0, 6, 1))
    start_list.append((1, 0, 3))
    start_list.append((1, 5, 2))
    start_list.append((2, 0, 2))
    start_list.append((2, 1, 1))
    start_list.append((2, 3, 7))
    start_list.append((2, 5, 9))
    start_list.append((2, 6, 3))
    start_list.append((2, 7, 5))
    start_list.append((3, 7, 4))
    start_list.append((4, 2, 3))
    start_list.append((4, 5, 1))
    start_list.append((4, 7, 2))
    start_list.append((5, 0, 7))
    start_list.append((5, 3, 4))
    start_list.append((5, 6, 6))
    start_list.append((5, 8, 8))
    start_list.append((6, 0, 6))
    start_list.append((6, 3, 2))
    start_list.append((6, 7, 8))
    start_list.append((7, 2, 8))
    start_list.append((7, 5, 3))
    start_list.append((8, 0, 5))
    start_list.append((8, 2, 7))
    start_list.append((8, 4, 4))
    sb = sudoku_table(start_list)

    print(sb.printme())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
