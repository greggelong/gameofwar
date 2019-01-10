## this version during a war each table 3 extra cards and there is a check to see if there is enought
## added a global variable warwin 
## addign a comment to playwar 3

from cdh import Hand,Deck


myhand = Hand('greg')  #or we could import this way see playwar for difference
yourhand = Hand('mj')
wardeck = Deck()
wardeck.shuffle()
print('deck count',wardeck.count())
print('hand count',myhand.count())
wardeck.deal_war(myhand,yourhand)
print('dealing......')
print('deck count',wardeck.count())
print('hand count',myhand.count())
print(myhand)
print('the first card:',myhand.cards[0])



table = [] 

def turnover():
    print("*"*15)
    input("press key to trunover")
    print("*"*15)
    card1 = myhand.pick()
    card2 = yourhand.pick()
    print("*"*15)
    print(myhand.label,"has:",card1)
    print("*"*15)
    print(yourhand.label,"has:",card2)
    print("*"*15)
    
    if card1.is_better(card2):
        print("*"*15)
        print(myhand.label,"wins")
        print("*"*15)
        myhand.add_card(card1)  # need to put it in the front of the list as we deal from the back table.append(card1)
        myhand.add_card(card2)  # changed it in cdh class
        if len(table)>0:
            for crd in table:
                myhand.add_card(crd)
            table.clear() #del table[:]     
         
    
    elif card1.is_same(card2):
        global warwin
        print("*"*15)
        print("it's a war")
        input("put three on the table")
        print("*"*15)
        if len(myhand.cards) < 4:
            print(myhand.label,"looses, not enough cards")
            warwin = True
            return
        elif len(yourhand.cards) <4:
            print(yourhand.label,"looses, not enough cards")
            warwin = True
            return
        else:
            table.append(card1)  
            table.append(card2) 
            for tm in range(3):
                table.append(myhand.pick())
                table.append(yourhand.pick())
            print("it's a war now!!")    
        
        
    else:
        print("*"*15)
        print(yourhand.label,"wins")
        print("*"*15)
        yourhand.add_card(card1)
        yourhand.add_card(card2)
        if len(table)>0:
            for crd in table:
                yourhand.add_card(crd)
            table.clear()    

global warwin
warwin = False
while myhand.count() >0 and yourhand.count() > 0 and warwin == False:
    
    print(myhand.label,myhand.count())
    print(yourhand.label,yourhand.count())
    print("Table has:")
    for crd in table:
        print(crd)
    
    turnover()