# SOS game constants

class Constants:
    # Constants

    # Cell sides: Top:(Left, Right, Middle), Middle and Bottom
    # Circular clockwise starting with TL
    CellSides = (128, 64, 32, 16, 8, 4, 2, 1)
    TL,TM,TR,MR,BR,BM,BL,ML = CellSides
    # Set all sides to inside edge of board
    DefaultMask = TL | TM | TR | MR | BR | BM | BL | ML
    PinOrder=((-1, -1, TL), (-1, 0, TM), (-1, 1, TR), (0, 1, MR), (1, 1, BR), (1, 0, BM), (1, -1, BL), (0, -1, ML))
    pass