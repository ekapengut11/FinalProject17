
#How many people are playing in this game
print(' Welcome to Fantasy Football! ')

# def function test for interger
def checkforint(something):
    while True:
            ok=True
            try:
                something = int(something)
            except ValueError:
                something = input("That is not a valid number, please give an integer answer. ")
                ok = False
            if ok == True:
                return something

x = checkforint(input("How many players are playing? "))

#Name of every player

class player():
    # input names of all players

    def __init__(self, number):
        # self.x = 0
        self.name=input("What is this player's name? ")
        self.number=number
        self.team = []


playerlist=[]
for a in range(int(x)):
    print(f"{x} players")
    playerlist.append(player(a+1))

    #all of the football players in the game by position
qblist = ["Aaron Rodgers", "Tom Brady", "Drew Brees", "Matt Ryan", "Cam Newton", "Jameis Winston", "Kirk Cousins", "Derek Carr", "Russell Wilson", "Marcus Mariota", "Ben Roethlisberger", "Andrew Luck", "Philip Rivers", "Dak Prescott", "Eli Manning",   "Matthew Stafford",   "Andy Dalton",   "Jay Cutler",   'Carson Wentz',   'Tyrod Taylor',   'Carson Palmer',   'Joe Flacco', 'Alex Smith',   'Sam Bradford',   'Trevor Siemian',
'Jared Goff',
'Brian Hoyer', 'Tom Savage',   'Mitch Trubisky',   'DeShone Kizer',   'Blake Bortles',   'Deshaun Watson',   'Jimmy Garoppolo',   'Josh McCown',
'Chad Henne',
'Paxton Lynch',
'Cody Kessler',
'Brock Osweiler',
'Patrick Mahomes',
'Robert Griffin III',
'Scott Tolzien',
'Matt Moore',
'Christian Hackenberg',
'Matt Barkley',
'Colin Kaepernick',
'Bryce Petty',
'Teddy Bridgewater',
'Nathan Peterman',
'Landry Jones',
'AJ McCarron']
rblist = ['T. Gurley', 'D. Johnson', 'E. Elliott',
'L. McCoy',
'D. Lewis',
'M. Gordon',
'M. Ingram',
'K. Drake',
'A. Kamara',
'D. Henry',
'C. Anderson',
'A. Collins',
'C. Hyde',
'J. Williams',
'D. Freeman',
'F. Gore',
'L. Murray',
'L. Fournette',
'C. McCaffrey',
'S. Perine',
'B. Powell',
'M. Lynch',
'D. Johnson',
'J. Mixon',
'J. Howard',
'I. Crowell',
'T. Riddick',
'L. Miller',
'J. McKinnon',
'T. Coleman',
'A. Hunt',
'M. Brown',
'S. Ridley',
'W. Gallman',
'G. Bernard',
'J. Stewart',
'K. Williams',
'P. Barber',
'L. Blount',
'A. Blue',
'T. Green',
'M. Davis',
'T. Yeldon',
'D. Booker',
'M. Mack',
'J. Allen',
'M. Breida',
'K. Bibbs',
'T. Cohen',
'B. Bolden',
'C. Thompson',
'A. Peterson',
]
wrlist = ['Brandin Cooks',
 		 'Antonio Brown',
 		 'Michael Thomas',
 		 'Adam Thielen',
 		 'Julio Jones',
 		 'Stefon Diggs',
 		 'Chris Hogan',
 		 'Alshon Jeffery',
 		 'JuJu Smith=Schuster',
  		 'Dede Westbrook',
  		 'Martavis Bryant',
  		 'Marqise Lee',
  		 'Keelan Cole',
  		 'Ted Ginn',
  		 'Mohamed Sanu',
  		 'Nelson Agholor',
  		 'Rishard Matthews',
  		 'Danny Amendola',
  		 'Eric Decker',
  		 'Corey Davis',
  		 'Torrey Smith',
  		 'Brandon Coleman',
  		 'Kenny Britt',
  		'Willie Snead',
  		 'Allen Hurns',
  		 'Laquon Treadwell',
		 'Jaydon Mickens',
		 'Tommylee Lewis',
		 'Deandre Hopkins',  ]

telist= [ 'R. Gronkowski',
 	'T. Kelce',
 	'J. Reed',
 	'G. Olsen',
 	'J. Graham',
 	'Z. Ertz',
 	'K. Rudolph',
 	'T. Eifert',
 	'H. Henry',
  	'D. Walker',
  	'M. Bennett',
  	'J. Doyle',
  	'E. Ebron',
  	'J. Witten',
  	'J. Thomas',
  	'C. Fleener',
  	'V. McDonald',
  	'C. Clay',
  	'C. Brate',
  	'T. Higbee',
  	'A. Hooper',
  	'C. Fiedorowicz',
  	'A. Gates',
  	'E. Engram',
  	'O. Howard',
  	'A. Seferian=Jenkins',
  	'Z. Miller',
  	'B. Watson',
  	'J. Cook',
  	'D. Allen',
  	'D. Njoku',
  	'G. Kittle',   ]

flexlist = [rblist, wrlist]

kickerlist= [ 'J. Tucker',
 	'S. Gostkowski',
 	'M. Bryant',
 	'W. Lutz',
 	'D. Bailey',
 	'M. Crosby',
 	'B. Walsh',
 	'M. Prater',
 	'D. Hopkins',
  	'A. Vinatieri',
  	'C. Sturgis',
  	'C. Santos',
  	'S. Janikowski',
  	'C. Boswell',
  	'B. McManus',
  	'N. Folk',
  	'G. Gano',
  	'Y. Koo',
  	'K. Fairbairn',
  	'S. Hauschka',
  	'K. Forbath',
  	'R. Succop',
  	'P. Dawson',
  	'J. Myers',
  	'C. Parkey',
  	'R. Bullock',
  	'A. Rosas',
  	'Z. Gonzalez',
  	'R. Gould',
  	'G. Zuerlein',
  	'C. Barth',
  	'C. Catanzaro',   ]


deflist= [ 'Seahawks',
 	'Broncos',
 	'Steelers',
 	'Patriots',
 	'Texans',
 	'Cardinals',
 	'Chiefs',
 	'Vikings',
 	'Giants',
  	'Rams',
  	'Eagles',
  	'Panthers',
  	'Buccaneers',
  	'Jaguars',
  	'Ravens',
  	'Falcons',
  	'Chargers',
  	'Packers',
  	'Raiders',
  	'Colts',
  	'Lions',
  	'Titans',
  	'Bengals',
  	'Dolphins',
  	'Cowboys',
  	'49ers',
  	'Bills',
  	'Redskins',
  	'Bears',
  	'Jets',
  	'Saints',
  	'Browns',  ]
# defines positions, and lists in them
positions = [qblist, rblist, wrlist, telist, rblist, wrlist, flexlist, kickerlist, deflist]

# directions for game
print(f'(These are the directions for picking players for your teams. For the sake of the game, please do not deviate from these directions. One player will start by picking a player, hence beginning the first round. The rest of the players then pick their first player. Then, the last player to pick in the first round picks his second player first, proceeded by the second to last seed, etc. This snake path continues for the duration of picking teams. NOTE CAPITALIZATION AND SPACES ARE IMPORTANT. MAKE SURE TO TYPE FULL NAME OF PLAYER YOU WANT TO SELECT.')


# This loop will let all the players pick their teams
y = 0
while y < 1:
    for player in playerlist:
        choice0 = int(input('What player is choosing? 1 = player1 2 = player2 etc. ')) - 1
        print("Enter intergers only for this part!! ")
        choice1 = int(input('What do you want? 0= qb  1= rb1 2= wr1 3= te 4= rb2 5= wr2 6=flex 7=kicker 8=defense ' ))
        current_position = positions[choice1]
        print(positions[choice1])
        print(" Enter one of the names in the list. Capatilization and spaces count!! ")
        choice2 = input("What player do you want? " )
        if choice2 in positions[choice1]:
            playerlist[choice0].team.append(choice2)
            positions[choice1].remove(choice2)
            print(playerlist[choice0].team)
        else:
            print("You are bad, pick again ")
            choice3 = input("What player do you want? " )
            if choice3 in positions[choice1]:
                playerlist[choice0].team.append(choice3)
                positions[choice1].remove(choice3)
                print(playerlist[choice0].team)
            else:
                print("You don't deserve to go again. Next player. ")
    y = y+ 1

print("From now on, all inputs should be INTEGERS!! ")


z = 0
for z in range(x):
    for players in playerlist:
         choice0 = checkforint(choice0, input('What player is choosing? 1 = player1 2 = player2 etc. ')) - 1
# make a function for this loop
         print(playerlist[choice0].team)
         statQB1 = checkforint(input("How many passing yards did your QB have? "))
         statQB2 = int(input("How many rushing yards did your QB have? "))
         statQB3 = int(input("How many passing touchdowns did your QB have? "))
         statQB4 = int(input("How many rushing touchdowns did your QB have? "))
         statQB5 = int(input("How many interceptions did your QB have? "))
         statQB6 = int(input("How many receptions did your QB have? "))
         statQB7 = int(input("How many receiving yards did your QB have? "))
         statQB8 = int(input("How many receiving touchdowns did your QB have? "))
         statQB9 = int(input("How many two-point conversions did your QB have? "))
         statQB10 = int(input("How many fumbles lost did your QB have? "))
         statQB11 = int(input("How many fumbles recovered for a touchdown did your QB have? "))
         QBpoints = statQB1/25 + statQB2/10 + statQB3*4 + statQB4*6 - statQB5*2 + statQB6 + statQB7/10 + statQB8*6 + statQB9*2 - statQB10*2 + statQB11*6
         print(f"Your QB got {QBpoints} this week!" )
         statRB1_1 = int(input("How many passing yards did your RB1 have? "))
         statRB1_2 = int(input("How many rushing yards did your RB1 have? "))
         statRB1_3 = int(input("How many passing touchdowns did your RB1 have? "))
         statRB1_4 = int(input("How many rushing touchdowns did your RB1 have? "))
         statRB1_5 = int(input("How many interceptions did your RB1 have? "))
         statRB1_6 = int(input("How many receptions did your RB1 have? "))
         statRB1_7 = int(input("How many receiving yards did your RB1 have? "))
         statRB1_8 = int(input("How many receiving touchdowns did your RB1 have? "))
         statRB1_9 = int(input("How many two-point conversions did your RB1 have? "))
         statRB1_10 = int(input("How many fumbles lost did your RB1 have? "))
         statRB1_11 = int(input("How many fumbles recovered for a touchdown did your RB1 have? "))
         RB1points = statRB1_1/25 + statRB1_2/10 + statRB1_3*4 + statRB1_4*6 - statRB1_5*2 + statRB1_6 + statRB1_7/10 + statRB1_8*6 + statRB1_9*2 - statRB1_10*2 + statRB1_11*6
         print(f"Your RB1 got {RB1points} this week!" )
         statWR1_1 = int(input("How many passing yards did your WR1 have? "))
         statWR1_2 = int(input("How many rushing yards did your WR1 have? "))
         statWR1_3 = int(input("How many passing touchdowns did your WR1 have? "))
         statWR1_4 = int(input("How many rushing touchdowns did your WR1 have? "))
         statWR1_5 = int(input("How many interceptions did your WR1 have? "))
         statWR1_6 = int(input("How many receptions did your WR1 have? "))
         statWR1_7 = int(input("How many receiving yards did your WR1 have? "))
         statWR1_8 = int(input("How many receiving touchdowns did your WR1 have? "))
         statWR1_9 = int(input("How many two-point conversions did your WR1 have? "))
         statWR1_10 = int(input("How many fumbles lost did your WR1 have? "))
         statWR1_11 = int(input("How many fumbles recovered for a touchdown did your WR1 have? "))
         WR1points = statWR1_1/25 + statWR1_2/10 + statWR1_3*4 + statWR1_4*6 - statWR1_5*2 + statWR1_6 + statWR1_7/10 + statWR1_8*6 + statWR1_9*2 - statWR1_10*2 + statWR1_11*6
         print(f"Your WR1 got {WR1points} this week!" )
         statTE1 = int(input("How many passing yards did your TE have? "))
         statTE2 = int(input("How many rushing yards did your TE have? "))
         statTE3 = int(input("How many passing touchdowns did your TE have? "))
         statTE4 = int(input("How many rushing touchdowns did your TE have? "))
         statTE5 = int(input("How many interceptions did your TE have? "))
         statTE6 = int(input("How many receptions did your TE have? "))
         statTE7 = int(input("How many receiving yards did your TE have? "))
         statTE8 = int(input("How many receiving touchdowns did your TE have? "))
         statTE9 = int(input("How many two-point conversions did your TE have? "))
         statTE10 = int(input("How many fumbles lost did your TE have? "))
         statTE11 = int(input("How many fumbles recovered for a touchdown did your TE have? "))
         TEpoints = statTE1/25 + statTE2/10 + statTE3*4 + statTE4*6 - statTE5*2 + statTE6 + statTE7/10 + statTE8*6 + statTE9*2 - statTE10*2 + statTE11*6
         print(f"Your TE got {TEpoints} this week!" )
         statRB2_1 = int(input("How many passing yards did your RB2 have? "))
         statRB2_2 = int(input("How many rushing yards did your RB2 have? "))
         statRB2_3 = int(input("How many passing touchdowns did your RB2 have? "))
         statRB2_4 = int(input("How many rushing touchdowns did your RB2 have? "))
         statRB2_5 = int(input("How many interceptions did your RB2 have? "))
         statRB2_6 = int(input("How many receptions did your RB2 have? "))
         statRB2_7 = int(input("How many receiving yards did your RB2 have? "))
         statRB2_8 = int(input("How many receiving touchdowns did your RB2 have? "))
         statRB2_9 = int(input("How many two-point conversions did your RB2 have? "))
         statRB2_10 = int(input("How many fumbles lost did your RB2 have? "))
         statRB2_11 = int(input("How many fumbles recovered for a touchdown did your RB2 have? "))
         RB2points = statRB2_1/25 + statRB2_2/10 + statRB2_3*4 + statRB2_4*6 - statRB2_5*2 + statRB2_6 + statRB2_7/10 + statRB2_8*6 + statRB2_9*2 - statRB2_10*2 + statRB2_11*6
         print(f"Your RB2 got {RB2points} this week!" )
         statWR2_1 = int(input("How many passing yards did your WR2 have? "))
         statWR2_2 = int(input("How many rushing yards did your WR2 have? "))
         statWR2_3 = int(input("How many passing touchdowns did your WR2 have? "))
         statWR2_4 = int(input("How many rushing touchdowns did your WR2 have? "))
         statWR2_5 = int(input("How many interceptions did your WR2 have? "))
         statWR2_6 = int(input("How many receptions did your WR2 have? "))
         statWR2_7 = int(input("How many receiving yards did your WR2 have? "))
         statWR2_8 = int(input("How many receiving touchdowns did your WR2 have? "))
         statWR2_9 = int(input("How many two-point conversions did your WR2 have? "))
         statWR2_10 = int(input("How many fumbles lost did your WR2 have? "))
         statWR2_11 = int(input("How many fumbles recovered for a touchdown did your WR2 have? "))
         WR2points = statWR2_1/25 + statWR2_2/10 + statWR2_3*4 + statWR2_4*6 - statWR2_5*2 + statWR2_6 + statWR2_7/10 + statWR2_8*6 + statWR2_9*2 - statWR2_10*2 + statWR2_11*6
         print(f"Your WR2 got {WR2points} this week!" )
         statF1 = int(input("How many passing yards did your Flex have? "))
         statF2 = int(input("How many rushing yards did your Flex have? "))
         statF3 = int(input("How many passing touchdowns did your Flex have? "))
         statF4 = int(input("How many rushing touchdowns did your Flex have? "))
         statF5 = int(input("How many interceptions did your Flex have? "))
         statF6 = int(input("How many receptions did your Flex have? "))
         statF7 = int(input("How many receiving yards did your Flex have? "))
         statF8 = int(input("How many receiving touchdowns did your Flex have? "))
         statF9 = int(input("How many two-point conversions did your Flex have? "))
         statF10 = int(input("How many fumbles lost did your Flex have? "))
         statF11 = int(input("How many fumbles recovered for a touchdown did your Flex have? "))
         Flexpoints = statF1/25 + statF2/10 + statF3*4 + statF4*6 - statF5*2 + statF6 + statF7/10 + statF8*6 + statF9*2 - statF10*2 + statF11*6
         print(f"Your Flex got {Flexpoints} this week!" )
         statK1 = int(input("How many PAT's did your Kicker make? "))
         statK2 = int(input("How many 0-49 yard Field Goals did your Kicker make? "))
         statK3 = int(input("How many 50+ yard Field Goals did your Kicker make? "))
         Kpoints = statK1 + statK2*3 + statK3*5
         print(f"Your Kicker got {Kpoints} this week!" )
         statD1 = int(input("How many sacks did your Defense have? "))
         statD2 = int(input("How many interceptions did your Defense have? "))
         statD3 = int(input("How many fumbles recovered did your Defense have? "))
         statD4 = int(input("How many safeties did your Defense force? "))
         statD5 = int(input("How many defensive touchdowns did your Defense have? "))
         statD6 = int(input("How many kick or punt return touchdowns did your Defense have? "))
         statD7 = int(input("How many two-point conversion returns did your Defense have? "))
         answerD8 = int(input("How many points did your defense allow? "))
         if answerD8 == 0:
            statD8 = 10
         elif 1 <= answerD8 <= 6:
            statD8 = 7
         elif 7 <= answerD8 <= 13:
            statD8 = 4
         elif 14 <= answerD8 <= 20:
            statD8 = 1
         elif 21 <= answerD8 <= 27:
            statD8 = 0
         elif 28 <= answerD8 <= 34:
            statD8 = -1
         elif 35 <= answerD8:
            statD8 = -4
         else:
             print("You did not enter a number. Don't be stupid. Redo that. ")

         Dpoints = statD1 + statD2*2 + statD3*2 + statD4*2 + statD5*6 + statD6*6 + statD7*2 + statD8
         print(f"Your Defense got {Dpoints} this week!" )
         playerlist[choice0].score = Dpoints + Kpoints + WR2points + WR1points + RB2points + RB1points + QBpoints + TEpoints + Flexpoints
         print(f' {playerlist[choice0]} got {playerlist[choice0].score} this week! ')
    z = z +1

w = 0
topscorer = playerlist[0].score
topscorer.player = playerlist[0]
for w in x:
    if topscorer <= playerlist[w].score:
        topscorer = playerlist[w].score
        topscorer.player = playerlist[w]
    else:
        topscorer = topscorer
    w = w + 1

print(f' Congratulations to {topscorer.player} for being the topscorer of the week with a score of {topscorer} ')




















