from random import choice
def main():
    list=["Rock","Paper","Scissors"]
    print "Let's start"
    print "You have Rock,Paper and Scissors"
    con="true"
    while con=="true":
        
        p1=raw_input("Select one : ").lower()
        p2=choice(list).lower()
        print "I choose %s" % p2
        p2.lower()

        if  p1==p2:
           print "It's a draw :| "
        elif p1=="rock":
            if p2=="paper":
                print "Sorry! It's a wrap up. You lose :P"
            else:
                print "Whoa! You ROCK. You Win :D"
        elif p1=="paper":
            if p2=="rock":
                print "*Sigh* You win"
            else:
                print "Yay! Better luck next time. You lose"
        elif p1=="scissors":
            if p2=="paper":
                print "Ouch!That hurt. You win :("
            else:
                print "Finally I broke you. You lose"
        else:
            print "Invalid choice"
        print "Wanna play again? Yes or No?"
        a=raw_input().lower()
        if a=="yes":
            con="true"
        else:
            con="false"
main()
print "It was fun!!"