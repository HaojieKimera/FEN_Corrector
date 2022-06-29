import chess
import chess.svg
from FEN_Corrector import getUCI,visualizarNotacion,generarImagen

if __name__ == "__main__":
    #test de movimiento normal 
    board =chess.Board("r3k2r/pp1bb1pp/nqpppp1n/8/8/NPPPPQ1N/P2BBPPP/R3K2R w KQkq - 1 10")#estado inicial de tablero que no existe error
    color=True#indicador de turno
    board2=chess.Board("r3k2r/pp1bb1pp/nqqqqQ1n/8/8/NPPPQ2Q/P2BBPPP/R3K2R b KQkq - 0 10")#Simulación de fen del proximo movimiento  erroneo

    board=getUCI(board.fen(),board2.fen(),color)#ejecución de la correción
    
    generarImagen(board,"testMovimiento1.SVG")#imagen del tablero corregido 
    generarImagen(board2,"testMovimiento1_MAL.SVG")#imagen del tablero sin corregir
    color=False
    
    board=getUCI(board.fen(),"r3k2r/pp1bb1pp/n1qqqQ1n/8/8/NqPPP2N/P2BBPPP/R3K2R w KQkq - 0 11",color)#llegada de otro fen erroneo y su correción
    generarImagen(board,"testMovimiento2.SVG")
    generarImagen(chess.Board("r3k2r/pp1bb1pp/n1qqqQ1n/8/8/NqPPP2N/P2BBPPP/R3K2R w KQkq - 0 11"),"testMovimiento2_MAL.SVG")#Simulación de fen del proximo movimiento  errone
    
    #test de enroque
    board = chess.Board("r3k2r/pp1bb1pp/nqpppp1n/8/8/NPPPPQ1N/P2BBPPP/R3K2R w KQkq - 1 10")#estado inicial de tablero que no existe error
    color=True#indicador de turno
    board2=chess.Board("r3k2r/pp1bb1pp/nqqqpp1n/8/8/NPPPPQ1N/P2BBPPP/2KR3R b kq - 2 10")#Simulación de fen erroneo

    board=getUCI(board.fen(),board2.fen(),color)#ejecución de la correción

    generarImagen(board,"testEnroque1.SVG")#imagen del tablero corregido 
    generarImagen(board2,"testEnroque1_MAL.SVG")#imagen del tablero sin corregir
    color=False#indicador de turno
    
    board=getUCI(board.fen(),"r4rk1/pp1bb1pp/nqpppp1n/8/8/NPNNNQ1N/P2BBPPP/2KR3R w - - 3 11",color)#llegada de otro fen erroneo y su correción
    generarImagen(chess.Board("r4rk1/pp1bb1pp/nqpppp1n/8/8/NPNNNQ1N/P2BBPPP/2KR3R w - - 3 11"),"testEnroque2_MAL.SVG")#imagen del tablero sin corregir
    generarImagen(board,"testEnroque2.SVG")#imagen del tablero corregido 

    #test de promocion
    board =chess.Board("r3k2r/pP1bb1pp/nq1p1p1n/8/8/N1PPP2N/P2BBPpP/R3K2R w KQkq - 0 14")#estado inicial de tablero que no existe error
    color=True#indicador de turno
    board2=chess.Board("N3k2r/p2bb1qp/bq1p1p1n/8/8/N1PQP2N/P2BBPpP/R3K2R b KQk - 0 14")#Simulación de fen del proximo movimiento  errone

    
    board=getUCI(board.fen(),board2.fen(),color)#ejecución de la correción

    generarImagen(board,"testPromo1.SVG")#imagen del tablero corregido 
    generarImagen(board2,"testPromo1_MAL.SVG")#imagen del tablero sin corregir
    color=False#indicador de turno
    
    board=getUCI(board.fen(),"N3k2r/p2pp1pp/nq1p1p1n/8/8/N1QQP2N/P2BBQ1Q/N3K2q w Qk - 0 15",color)#llegada de otro fen erroneo y su correción
    generarImagen(board,"testPromo2.SVG")#imagen del tablero corregido 
    generarImagen(chess.Board("N3k2r/p2pp1pp/nq1p1p1n/8/8/N1QQP2N/P2BBP1P/R3K2q w Qk - 0 15"),"testPromo2_MAL.SVG")#imagen del tablero sin corregir
    
    visualizarNotacion();#Prueba de visualización através de un fichero
