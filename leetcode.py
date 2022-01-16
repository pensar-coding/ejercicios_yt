"""
Determine si un tablero de Sudoku de 9 x 9 es válido. 
Solo las celdas llenas deben validarse de acuerdo con las siguientes reglas:

:) Chequear que el tablero introducido sea un tablero 9x9 
:) Cada fila debe contener los dígitos 1-9 sin repetición.
:) Cada columna debe contener los dígitos 1-9 sin repetición.
:) Cada uno de los nueve subcuadros de 3 x 3 de la cuadrícula debe contener 
los dígitos 1-9 sin repetición. 

#modularizar -> módulos 
"""



board = board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

class ValidateSudoku:
    def __init__(self,tablero) -> None:
        self.tablero = tablero
        self.lista_invertida = list()

    def chequeo_general(self):
        """
        Chequear que el tablero introducido sea un tablero 9x9 
        """
        #assert 
        assert len(self.tablero) == 9, "El tablero ingresado no respeta el formato 9x9" #filas
        for fila in self.tablero:
            assert len(fila) == 9, "El tablero ingresado no respeta el formato 9x9"

    
    def chequeo_filas(self,lista_a_chequear='tablero_general'):
        if lista_a_chequear == 'tablero_general':
            lista_a_chequear = self.tablero

        for fila in lista_a_chequear:
            for elemento in fila:
                if elemento != '.':
                    assert fila.count(elemento) == 1, "El tablero ingresado no es válido"


    def chequeo_columnas(self):

        for column_index in range(0,9):
            for row_index in range(0,9):
                self.lista_invertida.append(self.tablero[row_index][column_index])
            
            self.chequeo_filas([self.lista_invertida])

            self.lista_invertida.clear()


    def chequeo_subcuadros(self):
        #funcion mayor
        #tenemos 9 subcuadros = chequear de 3 en 3
        # de mis primeras 3 filas -> subcuadros del 0 al 3, 3 al 6, 6 al 9
        self.chequeo_3_subcuadros(0,3)
        self.chequeo_3_subcuadros(3,6)
        self.chequeo_3_subcuadros(6,9)

    def chequeo_3_subcuadros(self,rango1,rango2):
        self.lista_invertida.clear()
        for row_index in range(0,9):
            if row_index == 3 or row_index == 6:
                self.lista_invertida.clear()
            for column_index in range(rango1,rango2):
                self.lista_invertida.append(self.tablero[column_index][row_index])
                if len(self.lista_invertida) == 9:
                    self.chequeo_filas([self.lista_invertida])
                #chequeo filas
        
        


#instanciar objeto
if __name__ == "__main__":
    sudoku = ValidateSudoku(board)
    sudoku.chequeo_general()
    sudoku.chequeo_filas()
    sudoku.chequeo_columnas()
    sudoku.chequeo_subcuadros()
    print('El tablero de Sudoku ingresado es válido')