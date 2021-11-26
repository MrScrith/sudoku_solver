class sudoku_cell():
    known_value = 0
    possible_values = []

    def __init__(self):
        self.known_value = 0
        self.possible_values = [False, False, False, False, False, False, False, False, False]

    def printme(self):
        retval = " "
        if not self.known_value == 0:
            retval = str(self.known_value)
        return retval

class sudoku_table():
    _values = []
    _columns = []
    _rows = []
    _cubes = []

    def __init__(self, start_list):
        self._rows = [[], [], [], [], [], [], [], [], []]
        self._values = []
        self._columns = [[], [], [], [], [], [], [], [], []]
        self._cubes = [[], [], [], [], [], [], [], [], []]
        for i in range(0, 9):
            for j in range(0, 9):
                sc = sudoku_cell()

                self._values.append(sc)
                self._rows[i].append(sc)
                self._columns[j].append(sc)
                if i < 3:
                    if j < 3:
                        self._cubes[0].append(sc)
                    elif j < 6:
                        self._cubes[1].append(sc)
                    else:
                        self._cubes[2].append(sc)
                elif i < 6:
                    if j < 3:
                        self._cubes[3].append(sc)
                    elif j < 6:
                        self._cubes[4].append(sc)
                    else:
                        self._cubes[5].append(sc)
                else:
                    if j < 3:
                        self._cubes[6].append(sc)
                    elif j < 6:
                        self._cubes[7].append(sc)
                    else:
                        self._cubes[8].append(sc)

        for t in start_list:
            r = t[0]
            c = t[1]
            v = t[2]
            self._rows[r][c].known_value = v

    def printme(self):
        # ---------------------------------------
        # | 1 | 2 | 3 || 4 | 5 | 6 || 7 | 8 | 9 |
        # +---+---+---++---+---+---++---+---+---+
        # | 4 | 5 | 6 || 7 | 8 | 9 || 1 | 2 | 3 |
        # +---+---+---++---+---+---++---+---+---+
        # | 7 | 8 | 9 || 1 | 2 | 3 || 4 | 5 | 6 |
        # =======================================

        str = "---------------------------------------\n"
        for i in range(0, 9):
            str = str + "| " + self._rows[i][0].printme() + " | " + self._rows[i][1].printme() + " | " + self._rows[i][2].printme()
            str = str + " || " + self._rows[i][3].printme() + " | " + self._rows[i][4].printme() + " | " + self._rows[i][5].printme()
            str = str + " || " + self._rows[i][6].printme() + " | " + self._rows[i][7].printme() + " | " + self._rows[i][8].printme()
            str = str + " |\n"
            if i < 8:
                str = str + "+---+---+---++---+---+---++---+---+---+\n"


        str = str + "---------------------------------------\n"

        return str