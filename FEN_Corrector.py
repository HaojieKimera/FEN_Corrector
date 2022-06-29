
import chess
import chess.svg
from time import sleep
#lista de tipo de fichas negras que existen
fenChar_Bla = ["p", "q","k", "b", "n", "r"]
#lista de tipo de fichas blancas que existen
fenChar_Whi = ["P", "Q", "K", "B", "N", "R"]
#Posiciones de la tabla en formato de array
chess_pos=["a8","b8","c8","d8","e8","f8","g8","h8",
           "a7","b7","c7","d7","e7","f7","g7","h7",
           "a6","b6","c6","d6","e6","f6","g6","h6",
           "a5","b5","c5","d5","e5","f5","g5","h5",
           "a4","b4","c4","d4","e4","f4","g4","h4",
           "a3","b3","c3","d3","e3","f3","g3","h3",
           "a2","b2","c2","d2","e2","f2","g2","h2",
           "a1","b1","c1","d1","e1","f1","g1","h1"]
#generar Imagenes svg a partir de objeto de clase tabla del libreria chess y un string para su nombre
def generarImagen(board,nombreFichero):
    boardsvg = chess.svg.board(board=board)
    f = open(nombreFichero, "w")
    f.write(boardsvg)
    f.close()
#funcion para detectar si se permite promocionar un peon en caballo o reina
def check_de_promocion(listaPiezas1,listaPiezas2,origen,destino,pos):
    #listaPiezas1:array de las piezas del primer tablero (antes de realizar el movienmiento de la ficha, suponiendo que un tablero que no hay error en ella)
    #listaPiezas2:lista de las piezas del segundo tablero (despues de realizar el moviemiento de la ficha,creado a partir del fen obtenido pero que existe problemas de reconocer los tipos de piezas pero no de color que hay sobre ella)
    #int:numero entero que indica el elemento del vector chess_pos es la posicion origen del movimiento de la ficha
    #int:numero entero que indica el elemento del vector chess_pos es la posicion destino del movimiento de la ficha
    #pos:string que define el origen y destino por ejemplo a7a8, donde se le añaderá un char para indicar el promoción que se va hacer y devolvemos con esta funcion. 
    if(listaPiezas1[origen]=="P" and "8" in chess_pos[destino]):
    #promocion de peones blancos
        if(listaPiezas2[destino]=="N"):
            #solo en caso de que se ha detectado que la ficha en el destino es un caballo se determina como caballo la pieza objetivo de la promoción(supondremos que se ha determinado bien el caballo)
            pos=pos+"n"
        else:
            #en resto de casos solo se condera que ha promocionado a reina, sin expectar la probabilidad de promocionar a torre o alfil ya que la probabilidad es muy diminuta
            pos=pos+"q"
    elif(listaPiezas1[origen]=="p" and "1" in chess_pos[destino]):
    #promocion de peones negros
        if(listaPiezas2[destino]=="n"):
            #solo en caso de que se ha detectado que la ficha en el destino es un caballo se determina como caballo la pieza objetivo de la promoción(supondremos que se ha determinado bien el caballo)
            pos=pos+"n"
        else:
            #en resto de casos solo se condera que ha promocionado a reina, sin expectar la probabilidad de promocionar a torre o alfil ya que la probabilidad es muy diminuta
            pos=pos+"q"
    return pos
#funcion para mover las piezas del tablero que recibe un estructura fen erroneo (también se permite fen sin errores) que indica la situacion del tablero trás un movimiento que tiene errores en los tipos piezas que tiene anotado(no de color ni posicion)
def getUCI(fen1,fen2,color):
#fen1:string de un fen del tablero que aun no ha realizado el movimiento
#fen2:string de un fen que hemos recibido tras haber hecho un analisis de imagen que nos ha devuelto mal los tipo de piezas
#color:booleano que indica a quién le toca mover la pieza
    board = chess.Board(fen1)
    board2=chess.Board(fen2)
    f = open("notacion.FEN", "a")
    #se transforma los fens en formato ascii y quitamos los espacios y salto de lineas para convertirlos en dos arrays
    string_board1=str(board).replace(" ", "").replace("\n","")
    string_board2=str(board2).replace(" ", "").replace("\n","")
    to_array1 = list(string_board1)
    to_array2 = list(string_board2)
    #contador para anotar numero de diferencias que existen entre los dos fens
    count=0
    #un array que contendrá los indices donde los dos arrays son diferentes
    diff=[]

    for x in range(64):
        #leemos de los dos array y hacemos que solo existan la diferencia de fecha blanca y negra
        if(to_array1[x] in fenChar_Bla):
            a1="+"
        elif(to_array1[x] in fenChar_Whi):
            a1="-"
        else:
            a1="."
        if(to_array2[x] in fenChar_Bla):
            a2="+"
        elif(to_array2[x] in fenChar_Whi):
            a2="-"
        else:
            a2="."
        if(a1!=a2):
            diff.append(x)
            count=count+1

    print("Cuenta:%",count)
    print(diff)
    #habra 2 differencias si ha habido movimientos de ficha
    if count==2:
        #movimientos normales
        if(color):
            if(to_array1[diff[0]] in fenChar_Whi):
                pos=str(chess_pos[diff[0]]+chess_pos[diff[1]])
                destino=diff[1]
                origen=diff[0]
                pos=check_de_promocion(to_array1,to_array2,origen,destino,pos)
            else:
                pos=str(chess_pos[diff[1]]+chess_pos[diff[0]])
                destino=diff[0]
                origen=diff[1]
                pos=check_de_promocion(to_array1,to_array2,origen,destino,pos)

        else:
            if(to_array1[diff[0]] in fenChar_Bla):
                pos=str(chess_pos[diff[0]]+chess_pos[diff[1]])
                destino=diff[1]
                origen=diff[0]
                pos=check_de_promocion(to_array1,to_array2,origen,destino,pos)
            else:
                pos=str(chess_pos[diff[1]]+chess_pos[diff[0]])
                destino=diff[0]
                origen=diff[1]
                pos=check_de_promocion(to_array1,to_array2,origen,destino,pos)
        #comprobamos si el movimiento es legal antes realizar el moviemietno
        if(chess.Move.from_uci(pos) in board.legal_moves):
            move=chess.Move.from_uci(pos)
            print(pos)
            board.push(move)
            f.write(board.fen()+"\n")

    #solo en caso de enroque hay 4 cambios
    elif(count==4):
        
        
        if(color):
            #posiciones a1 y e1
            if(diff[0]==56 and diff[3]==60):
                pos="e1c1"
            else:
                pos="e1g1"
        else:
            #posiciones a8 y e8
            if(diff[0]==0 and diff[3]==4):
                pos="e8c8"
            else:
                pos="e8g8"
        if(chess.Move.from_uci(pos) in board.legal_moves):
            move=chess.Move.from_uci(pos)
            print(pos)
            board.push(move)
            f.write(board.fen()+"\n")
        else:
            print("error")
    #devolvemos un objeto de tipo Board que ha relizado el movimiento de la ficha en caso de que el fen2 ha sido un fen que solo ha tenido problemas de detectar el tipo de ficha de cada color y es posterior de un moviento, en otro caso se devolverá el mismo board
    f.close()
    return board;

def visualizarNotacion():
    f = open("notacion.FEN", "r")
    lines = f.readlines()
    contador=0;
    for line in lines:
        contador += 1
        generarImagen(chess.Board(line),"Paso"+str(contador)+".SVG")
    f.close
