from patternpieces import PatternPieces
from piece import Piece
from piecesbank import PiecesBank
from ui import UI

def main():

    pb = PiecesBank()
    print(pb.pieceslist[200].path)

    app = UI()
    app.scale = 3
    app.createTable(pb)
    app.mainloop()


if __name__ == '__main__':
    main()