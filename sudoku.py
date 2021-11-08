# Sudoku Solver AI

import sys

class ai:
    def __init__(self):
        """Initializing the array to solve"""
        with open(sys.argv[1], 'r') as f:
            grid = f.read()

        # converting the grid to a readable list
        arr = []
        inp = []
        index=0
        ind=0
        while index<=81:
            ind += 9
            arr.append(grid[index:ind])
            inp.append(grid[index:ind])
            index=ind+1
            ind+=1
        self.input = inp
        self.arr = arr
        
    def main(self):
        """Main AI solver"""
        while ("-" in self.arr[0]) or ("-" in self.arr[1]) or ("-" in self.arr[2]) or ("-" in self.arr[3]) or ("-" in self.arr[4]) or ("-" in self.arr[5]) or ("-" in self.arr[6]) or ("-" in self.arr[7]) or ("-" in self.arr[8]):
            for i in range(9):
                for j in range(9):
                    # checking if the value is missing
                    if self.arr[i][j]=="-":
                        #poss = ['1','2','3','4','5','6','7','8','9']
                        possibilities = ['1','2','3','4','5','6','7','8','9']
                        # checking the rows
                        for k in range(9):
                            if self.arr[i][k]!="-" and self.arr[i][k] in possibilities:
                                possibilities.remove(self.arr[i][k])


                        # checking the columns
                        for k in range(9):
                            if self.arr[k][j] in possibilities:
                                possibilities.remove(self.arr[k][j])
                        

                        
                        # checking the box
                        if i<=2:
                            if j<=2: # top left
                                for x in range(3):
                                    for y in range(3):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                            elif j<=5:
                                for x in range(3):
                                    for y in range(3,6):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                            else:
                                for x in range(3):
                                    for y in range(6,9):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                        elif i<=5:
                            if j<=2: # top left
                                for x in range(3,6):
                                    for y in range(3):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                            elif j<=5:
                                for x in range(3,6):
                                    for y in range(3,6):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                            else:
                                for x in range(3,6):
                                    for y in range(6,9):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                        else:
                            if j<=2: # top left
                                for x in range(6,9):
                                    for y in range(3):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                            elif j<=5:
                                for x in range(6,9):
                                    for y in range(3,6):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                            else:
                                for x in range(6,9):
                                    for y in range(6,9):
                                        if self.arr[x][y]!="-" and self.arr[x][y] in possibilities:
                                            possibilities.remove(self.arr[x][y])
                        
                        # updating the answers
                        if len(possibilities)==1:
                            lis = list(self.arr[i])
                            lis[j]=possibilities[0]
                            self.arr[i] = "".join(lis)
            

            

    def show(self):
        """Displaying the result"""
        print("Input:")
        for i in self.input:
            print(i)
        print()
        print("Output:")
        for i in self.arr:
            print(i)
    
    def solve(self):
        """Putting everything into place"""
        self.main()
        self.show()



sudoku = ai()
sudoku.solve()
