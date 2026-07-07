#Task2 Tic Toc Toe AI
import math
import time

board=[[" "]*3 for _ in range(3)]
player="X"
ai="O"

def show_board():
    n=1
    print()
    for r in range(3):
        row=[]
        for c in range(3):
            row.append(str(n) if board[r][c]==" " else board[r][c]); n+=1
        print(" | ".join(row))
        if r<2: print("--+---+--")
    print()

def check_winner(s):
    for i in range(3):
        if all(board[i][j]==s for j in range(3)): return True
        if all(board[j][i]==s for j in range(3)): return True
    return (board[0][0]==board[1][1]==board[2][2]==s) or (board[0][2]==board[1][1]==board[2][0]==s)

def full():
    return all(board[r][c]!=" " for r in range(3) for c in range(3))

def pos_to_rc(p):
    p-=1
    return p//3,p%3

#Player move

def player_move():
    while True:
        try:
            p=int(input("Enter move (1-9): "))
            if not 1<=p<=9: raise ValueError
            r,c=pos_to_rc(p)
            if board[r][c]!=" ":
                print("Already taken."); continue
            board[r][c]=player
            return
        except:
            print("Invalid input.")

def minimax(ai_turn):
    if check_winner(ai): return 10
    if check_winner(player): return -10
    if full(): return 0
    if ai_turn:
        best=-999
        for r in range(3):
            for c in range(3):
                if board[r][c]==" ":
                    board[r][c]=ai
                    best=max(best,minimax(False))
                    board[r][c]=" "
        return best
    best=999
    for r in range(3):
        for c in range(3):
            if board[r][c]==" ":
                board[r][c]=player
                best=min(best,minimax(True))
                board[r][c]=" "
    return best

#AI move

def ai_move():
    print("\nAI is thinking",end="",flush=True)
    for _ in range(3):
        time.sleep(0.5); print(".",end="",flush=True)
    print()
    best=-999; move=None
    for r in range(3):
        for c in range(3):
            if board[r][c]==" ":
                board[r][c]=ai
                score=minimax(False)
                board[r][c]=" "
                if score>best:
                    best=score; move=(r,c)
    board[move[0]][move[1]]=ai

def reset():
    for r in range(3):
        for c in range(3):
            board[r][c]=" "

ps=ascore=ds=0
print("="*35);print("TIC TAC TOE AI");print("="*35)
while True:
    sym=input("Choose X or O: ").upper()
    if sym in ("X","O"):
        player=sym; ai="O" if sym=="X" else "X"; break
print("You:",player," AI:",ai)
while True:
    f=input("Who plays first? (player/ai): ").lower()
    if f in ("player","ai"):
        first=f; break

while True:
    reset()
    turn=first
    move=1
    while True:
        show_board()
        print("Move Number:",move)
        if turn=="player":
            player_move()
            if check_winner(player):
                show_board(); print("You Win!"); ps+=1; break
            turn="ai"
        else:
            ai_move()
            if check_winner(ai):
                show_board(); print("AI Wins!"); ascore+=1; break
            turn="player"
        if full():
            show_board(); print("Draw!"); ds+=1; break
        move+=1
    print(f"\nScore -> You:{ps}  AI:{ascore}  Draw:{ds}")
    if input("Play again? (y/n): ").lower()!="y":
        print("Thanks for playing!")
        break

