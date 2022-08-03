#https://stackoverflow.com/questions/14409661/dice-generator-using-class-in-python
#Make the option to re roll specific dice
import random,os,time,requests
from nba_api.stats.static import players
from inputimeout import inputimeout, TimeoutOccurred
import sys

class Die(object):
    def __init__(self,money=10000):
        self.player = 0
        self.money = money

    def print_team(self,human_team):
        for p in self.human_team:
            print(p,' - ',100-int(self.players_original.index(p)))
        # print('YOUR TOTAL IS ',(100-(self.score/2)),'Note:Higher is better')
        # print('Probability of you winning is',100-(int(self.score))+random.randint(0,10)+20,'%')
        # self.probability = 100-(int(self.score))+random.randint(0,10)+20
        print('-----------------------------------------------------------------------')
    def check_balance(self,money):
        print('Your balance is $',self.money)
        if self.money<0:
            print('You are in debt!')

    def probability(self,human_team):
        self.human_team = human_team
        self.score = 0
        for l in self.human_team:
            self.score +=self.players_original.index(l)
        print('Your total is ',(100-(self.score/2)),'Note:Higher is better')
        print('Probability of you winning is',100-(int(self.score))+random.randint(0,10)+20,'%')
        self.probability = 100-(int(self.score))+random.randint(0,10)+20
        print('-----------------------------------------------------------------------')
        return (100-(int(self.score))+random.randint(0,10)+20)

    def menu(self):
        print('-----------------------------------------------------------------------')
        print('Welcome to the dice game!')
        print('You roll a dice 6 times and you will get your dream basketball team!')
        print('Its a 20 sided dice! with 80 being the worst player and 100 being the best player')
        print('-----------------------------------------------------------------------')
        try:
            if input("Start? [Y/n] ").lower() == "y":
                self.play()
            else:
                print('Goodbye!')
                os._exit(0)
        except:
            print('Error!, try again later')
    
    def give_stats(self,player):
        player_info = "https://www.balldontlie.io/api/v1/players?search="+ player
        player_info_response = requests.get(player_info)

        print('player weight:', player_info_response.json()['data'][0]['weight_pounds'],end=' ||| ')
        print('player height:', player_info_response.json()['data'][0]['height_feet'], player_info_response.json()['data'][0]['height_inches'])
        print('player position:', player_info_response.json()['data'][0]['position'])
        print('----------------------------------')

    def play(self):
        self.human_team = []

        self.players = [
        'Kevin Durant',
        'Giannis Antetokounmpo',
        'LeBron James',
        'Stephen Curry',
        'James Harden',
        'Nikola Jokic',
        'Luka Doncic',
        'Kawhi Leonard',
        'Anthony Davis',
        'Damian Lillard',
        'Jayson Tatum',
        'Devin Booker',
        'Bradley Beal',
        'Jimmy Butler',
        'Chris Paul',
        'Trae Young',
        'Donovan Mitchell',
        'Jaylen Brown',
        'Kyrie Irving',
        'Klay Thompson',
        ]
        self.players_original = [
        'Kevin Durant',
        'Giannis Antetokounmpo',
        'LeBron James',
        'Stephen Curry',
        'James Harden',
        'Nikola Jokic',
        'Luka Doncic',
        'Kawhi Leonard',
        'Anthony Davis',
        'Damian Lillard',
        'Jayson Tatum',
        'Devin Booker',
        'Bradley Beal',
        'Jimmy Butler',
        'Chris Paul',
        'Trae Young',
        'Donovan Mitchell',
        'Jaylen Brown',
        'Kyrie Irving',
        'Klay Thompson',
        ]
        
        self.score = 0
        for i in range(6):
            self.player = random.choice(self.players) #gets a random player from the list
            self.players.index(self.player)
            self.score +=self.players.index(self.player)
            print('You rolled a 20 sided die and got a',100-int(self.players.index(self.player)),'Which is',self.player) # displays a message to show what player you got
            self.give_stats(self.player)
            time.sleep(1)
            self.human_team.append(self.player)# adds the player to the human team
            self.players.remove(self.player)# removes the player from the list so it doesn't get picked again
        self.print_team(self.human_team)
        self.probability(self.human_team)
        self.check_balance(self.money)
    
        # print('YOUR TOTAL IS ',(100-(self.score/2)),'Note:Higher is better')
        # print('Probability of you winning is',100-(int(self.score))+random.randint(0,10)+20,'%')
        # self.probability = 100-(int(self.score))+random.randint(0,10)+20
        # print('-----------------------------------------------------------------------')


        #input('Press anything to continue')
        print('----------------------------------')
        #Later on, when you have the time/energy you can add a player class so you can add more players or even allow the computer to add their team
        #You could also reverse the lis so best player is 50 and worst player is 1
        #i will append to it later
        print('There is a $1000 charge for rerolling')
        loop = True
        while loop:
            try:
                self.rejected_player=int(input('Enter the number of the player you want to re-roll, and 0 if you have none '))
                if (self.rejected_player>0) and (self.rejected_player<=6):
                    self.money -= 1000
                    self.check_balance(self.money)
                    self.rejected_player -=1 #because the list starts at 0
                    new_player = self.reroll_players(self.rejected_player,self.probability)
                    print('You have re-rolled',new_player,'instead of',self.human_team[self.rejected_player])
                    self.human_team[self.rejected_player] = new_player
                    self.give_stats(self.human_team[self.rejected_player])
                    time.sleep(4)
                    clear()
                    # print('Your team is ....\n','\n'.join(self.human_team))
                    self.print_team(self.human_team)
                    self.probability(self.human_team)
                elif self.rejected_player == 0:
                    print('You have no players to re-roll')
                    loop = False
                else:
                    print('Invalid input')
                    time.sleep(10)
                    continue
            except KeyboardInterrupt:
                print('Goodbye!')
                os._exit(0)
            except:
                print('')
    def reroll_players(self,rejected_player,probability):

        self.rejected_player = rejected_player
        self.player = random.choice(self.players)
        return self.player
    
    def __str__(self):
        return self.probability

    def play_start(self,name,round):  
        frames =[
"""
                 
/|             
\|=--             
   ##            o
              o    \\
                /   \O
          o    O_/   T
               T    /|
         o     |\  | |
_______________|_|________


""",
"""
                 
/|             o
\|=--      o      o
   ##
        o           \\
                /   \O
               O_/   T
       o       T    /|
               |\  | |
_______________|_|________


""",
"""
          o
/|      o       o
\|=--            o
   ##o
                   \\
    o           /   \O
               O_/   T
               T    /|
   o           |\  | |
_______________|_|________


""",
"""
          
/|           o
\|=--    o       o
   ## 
      o            \\
                /   \O
 o             O_/   T
               T    /|
o              |\  | |
_______________|_|________


""",
"""
          o
/|   o         o
\|=--            o
   ##
                   \\
                /   \O
               O_/   T
               T    /|
               |\  | |
_______________|_|________


""",
"""
   o       o
/|             o
\|=--            o
   ##
                   \\
                /   \O
               O_/   T
               T    /|
               |\  | |
_______________|_|________


""",
"""   o
           o
/|             o
\|=--            o
   ##
                   \\
                /   \O
               O_/   T
               T    /|
               |\  | |
_______________|_|________


"""
        ]

        tries = 0
        print('It is now',name,'\'s turn')
        time.sleep(2)
        while tries<3:
            for i in frames:
                clear()
                print(i)
                print('press enter to shoot')
                try:
                    #self.probability =73.3
                    # self.probability = self.probability - random.randint(0,10)
                    # if self.probability <= 0:
                        #print('It is a draw')
                    shot = inputimeout(prompt='>>', timeout=self.probability/100)#self.probability[0]-2/10))#random.uniform(0.1,0.5) )#change to 0.5 later
                    shot = shot.strip()
                    if (shot == '') and (i == frames[4]):
                        print('You got a goal!!!')
                        return True                 
                    elif shot == '':
                        print('You missed')
                        return False
                except KeyboardInterrupt:
                    os._exit(0)
                except:
                    continue


def clear():
  os.system('clear')


  
print('Welcome player 1')
player1 = Die()
player2 = Die()
player1.menu()
time.sleep(2)
clear()
print('Welcome player 2')
player2.menu()
time.sleep(2)
clear()
print('-----------------------------------------------------------------')
print('''
o- - -  \o          __|
   o/   /|          vv`\
  /|     |              |
   |    / \_            |
  / \   |               |
 /  |                   |

''')
print('-----------------------------------------------------------------')
print('probability of player 1 winning is',player1.__str__(),'%')
print('probability of player 2 winning is',player2.__str__(),'%')
print('-----------------------------------------------------------------')
play = True
while play:
    play_choice = input('Do you want to play? [Y/n] ').lower()
    if play_choice.lower() == 'y':
        #coin_flip = random.randint(1,2)
        print('-----------------------------------------------------------------')
        print('The game has started!')
        print('-----------------------------------------------------------------')
        time.sleep(1)
        print('-----------------------------------------------------------------')
        print('Player 1 will go first')
        print('-----------------------------------------------------------------')
        time.sleep(1)
        print('-----------------------------------------------------------------')
        print('-----------------------------------------------------------------')
        print('Player 2 will go first')
        print('-----------------------------------------------------------------')
        time.sleep(2)
        print('-----------------------------------------------------------------')
        round = 0
        while (player1.play_start('player1',round)) and player2.play_start('player2',round):
            print('One more round!')
            round +=1
            time.sleep(2)
        print('-----------------------------------------------------------------')
        print('Game has finished!')
