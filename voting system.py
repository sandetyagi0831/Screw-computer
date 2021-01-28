# VOTING SYSTEM PROJECT
nom1 = input("Enter the first nominee name: ")
nom2 = input("Enter the Second nominee name: ")

nom1_votes=0
nom2_votes=0

voter_id=[1,2,3,4,5,6,7,8,9,10]
num_votes=len(voter_id)

while True:
    print("***** VOTE FOR YOUR FAVOURITE NOMINEE *****")
    age = int(input("Enter your age "))
    if age > 18:
        print("***** ALLOWED TO VOTE ******")
        if voter_id==[]:
            print("Votings are closed")
            if nom1_votes>nom2_votes:
                percent=(nom1_votes/num_votes)*100
                print(nom1," Won by ",percent," % votes")
                break
            elif nom2_votes>nom1_votes:
                percent=(nom2_votes/num_votes)*100
                print(nom2," Won by ",percent," % votes")
                break
        else:
            voter = int(input("Enter your voter ID: "))
            if voter in voter_id:
                print("Vote for your favourite nominee")
                voter_id.remove(voter)
                vote = int(input("Enter your vote either 1 or 2 : "))
                if vote==1:
                    nom1_votes+=1
                    print("Thank You For voting")
                elif vote==2:
                    nom2_votes+=1
                    print("Thank You for voting")
            else:
                print("You have already voted or you are not allowed to vote")
    else:
        print("***** NOT ALLOWED TO VOTE *****")
        break

