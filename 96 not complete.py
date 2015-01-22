F = open('96 (Sudoku).txt')
Grids = []
for Gr in range(50):
    Grid = []
    for Row in range(10):
        if Row == 0:
            F.readline()
        else:
            Grid.append(F.readline()[0:9])
    Grids.append(Grid)
F.close()

def Test(Grid, Num, R, C):
    #Return False when test "Fail", True when test "Pass".
    
    if Num in Grid[R]: #Check the Row
        return False
    
    for Row in range(9): #Check the Column
        if Num == Grid[Row][C]:
            return False
    
    #Check inside the Cell
    Cell_Row = R / 3
    Cell_Col = C / 3
    if R % 3 == 0: R1, R2 = 1, 2
    if R % 3 == 1: R1, R2 = 0, 2
    if R % 3 == 2: R1, R2 = 0, 1

    if C % 3 == 0: C1, C2 = 1, 2
    if C % 3 == 1: C1, C2 = 0, 2
    if C % 3 == 2: C1, C2 = 0, 1

    if Num == Grid[Cell_Row * 3 + R1][Cell_Col * 3 + C1] : return False
    if Num == Grid[Cell_Row * 3 + R2][Cell_Col * 3 + C1] : return False
    if Num == Grid[Cell_Row * 3 + R1][Cell_Col * 3 + C2] : return False
    if Num == Grid[Cell_Row * 3 + R2][Cell_Col * 3 + C2] : return False

    return True

def Checking(Grid):
    TheGrid = []
    for Row in range(9):
        RowText = ''
        for Col in range(9):
            if Grid[Row][Col] != '0':
                RowText += '0'
                continue
            Vals = []
            for Num in range(1,10):
                if Test(Grid, str(Num), Row, Col):
                    Vals.append(Num)

            if len(Vals) == 0: return "Wrong Guess"
            if len(Vals) == 1: return [Row, Col, Vals[0]]
            RowText += str(len(Vals))
        TheGrid.append(RowText)
    return TheGrid

def FillIfUniqueNum(Grid):
    Checked = Checking(Grid)
    while len(Checked) == 3:
        Row = Grid[Checked[0]]
        Col = Checked[1]
        Grid[Checked[0]] = Row[:Col] + str(Checked[2]) + Row[Col+1:]
        Checked = Checking(Grid)

    if Checked == "Wrong Guess" : return "Wrong Guess"
    return Checked

def DisplayGrid(Grid):
    '''
  012 345 678
0 *** *** ***
1 *** *** ***
2 *** *** ***

3 *** *** ***
............
'''
    Text =  '  012 345 678\n'
    Text += '0 ' + Grid[0][0:3] + ' ' + Grid[0][3:6] + ' ' + Grid[0][6:9] + '\n'
    Text += '1 ' + Grid[1][0:3] + ' ' + Grid[1][3:6] + ' ' + Grid[1][6:9] + '\n'
    Text += '2 ' + Grid[2][0:3] + ' ' + Grid[2][3:6] + ' ' + Grid[2][6:9] + '\n\n'

    Text += '3 ' + Grid[3][0:3] + ' ' + Grid[3][3:6] + ' ' + Grid[3][6:9] + '\n'
    Text += '4 ' + Grid[4][0:3] + ' ' + Grid[4][3:6] + ' ' + Grid[4][6:9] + '\n'
    Text += '5 ' + Grid[5][0:3] + ' ' + Grid[5][3:6] + ' ' + Grid[5][6:9] + '\n\n'

    Text += '6 ' + Grid[6][0:3] + ' ' + Grid[6][3:6] + ' ' + Grid[6][6:9] + '\n'
    Text += '7 ' + Grid[7][0:3] + ' ' + Grid[7][3:6] + ' ' + Grid[7][6:9] + '\n'
    Text += '8 ' + Grid[8][0:3] + ' ' + Grid[8][3:6] + ' ' + Grid[8][6:9]
    print Text

def EnterNumber(Text):
    while True:
        try:
            Num = int(raw_input(Text))
            if 0 <= Num <= 9:
                return Num
            else:
                print '\nPlease Enter The Number from 0 to 9 .....'
        except:
            print '\nPlease Enter a Number'

FinishedGrid = ['0'*9 for i in range(9)]
def Guess(Grid, Details):
    Checked = FillIfUniqueNum(Grid)
    TestGrid = Grid[:]

    print 'The correct grid display.'
    DisplayGrid(TestGrid)
    print '\nNumber of Nums in each blanks.'
    DisplayGrid(Checked)
    if len(Details[0]) != 0: print 'Entered Rows and Columns before.\n', Details
    print '\n\nEnter the most suitable cells Row and Column index.'
    Row = EnterNumber('Row Index :')
    Col = EnterNumber('Row Index :')
    Details[len(Details) - 1].append([Row, Col])
    RowText = TestGrid[Row]

    Vals = []
    for Num in range(1,10):
        if Test(TestGrid, str(Num), Row, Col):
            Vals.append(Num)

    for Val in Vals:
        TestGrid[Row] = RowText[:Col] + str(Val) + RowText[Col+1:]
        if FillIfUniqueNum(TestGrid) == "Wrong Guess":
            print 'Guess Was Wrong...................................................................'
            continue
        if FillIfUniqueNum(TestGrid) == FinishedGrid:
            Grid[:] = TestGrid
            return "Grid has been filled corectly."
        if Guess(TestGrid, Details) == "Grid has been filled corectly.":
            Grid[:] = TestGrid
            return "Grid has been filled corectly."

for GridNumber in range(50):
    Checked = FillIfUniqueNum(Grids[GridNumber])

    if Checked != FinishedGrid:
        Details = [[]]
        while Guess(Grids[GridNumber], Details) != "Grid has been filled corectly.":
            print 'Previous Guess was wrong. Lets Guess again.....'
            Details.append([])

    print 'Grid', GridNumber, 'has been completed...\n'
    DisplayGrid(Grids[GridNumber])
    raw_input('Press any key to continue...')
    print '\n\n'
