#This is the chess board validator script.
#This checks if the state of the chess board is valid or not.
#(Exactly 1 black and white king, no more than 8 pawns per player,
#  no more than 16 pieces per player.)

tiles = {'1a': '', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '',
	 '2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '',
         '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
         '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
         '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
         '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
         '7a': '', '7b': '', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '',
         '8a': '', '8b': '', '8c': '', '8d': '', '8e': '', '8f': '', '8g': '', '8h': ''}


def validBoard(board):

    #Define a local counter that keeps track of number of pieces on board.
    bk_count, wk_count = 0, 0
    bpawn_count, wpawn_count = 0, 0
    w_pieces, b_pieces = 0, 0

    #Loop through dictionary values.
    for v in board.values():
        if v=='bking' or v=='bqueen' or v=='brook' or v=='bbishop' or v =='bknight' or v=='bpawn': b_pieces+=1
        elif if v=='wking' or v=='wqueen' or v=='wrook' or v=='wbishop' or v =='wknight' or v=='wpawn': b_wieces+=1

        if v == 'bking': bk_count+=1
        elif v == 'wking': wk_count+=1
        elif v == 'bpawn': bpawn_count+=1
        elif v == 'wpawn': wpawn_count+=1

    #Check whether number of pieces is valid.
    if bk_count!=1 or wk_count!=1:
        print('Error: Invalid number of kings.')
        return False

    if bpawn_count>8 or wpawn_count >8:
        print ('Error: Too many pawns on board.')
        return False

    if b_pieces>16 or w_pieces>16:
        print ('Error: Too many pieces on board.')
        return False

    return True


validBoard(tiles)



