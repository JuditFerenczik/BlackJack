import random
import tkinter




def load_images(card_images):
    suits=['heart', 'club', 'diamond','spade']
    face_cards=['jack', 'king', 'queen']
    for suit in suits:
        for card in range(1,11):
            name ='.\cards\{}_{}.{}'.format(str(card), suit, 'ppm')
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, ))
        for card in face_cards:
            name ='.\cards\{}_{}.{}'.format(str(card), suit, 'ppm')
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image, ))


            
def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised' ).pack(side='left')
    return next_card

def score_hand(hand):
    score=0
    ace=False
    for next_card in hand:
        card_value= next_card[0]
        if card_value ==1 and not ace:
            ace = True
            card_value=11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace=False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_store_label.set(dealer_score)
    player_score  = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("Draw")


def deal_player():
    dealer_score = score_hand(dealer_hand)
    player_hand.append(deal_card(player_card_frame))
    player_score= score_hand(player_hand)
    player_store_label.set(player_score)
    if player_score >21:
        result_text.set("Dealer wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("Draw")


def shuffle():
    random.shuffle(deck)


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    result_text.set("")
    dealer_hand = []
    player_hand = []
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_store_label.set(score_hand(dealer_hand))
    deal_player()


mainWindow = tkinter.Tk()
mainWindow.title("Black Jack")
mainWindow.geometry('640x80')
mainWindow.configure(background="green")
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable = result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow,relief='sunken', borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_store_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_store_label, background="green", fg="white").grid(row=1, column=0)
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_store_label = tkinter.IntVar()

tkinter.Label(card_frame,text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_store_label, background="green", fg="white").grid(row=3, column=0)
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)
#load cards            
cards = []
load_images(cards)
#print(cards)
deck = list(cards)
#random.shuffle(deck)
firstround = True
dealer_hand = []
player_hand = []
shuffle()
new_game()
#deal_player()
#dealer_hand.append(deal_card(dealer_card_frame))
#dealer_store_label.set(score_hand(dealer_hand))
#deal_player()

mainWindow.mainloop()