#!/usr/bin/python3
from termcolor import colored

print('Ticket Calculator')

MinTicket = 75
PostedSpeed = input('What is the posted speed?: ')
while not PostedSpeed.isdigit():
    print('Please enter an integer for the posted speed.')
    PostedSpeed = input('What is the posted speed?: ')


ActualSpeed = input('What was your actual speed?: ')
while not ActualSpeed.isdigit():
    print('Please enter an integer for the actual speed.')
    ActualSpeed = input('What was your actual speed?: ')


SpeedOver = int(ActualSpeed) - int(PostedSpeed)

if SpeedOver <= 0:
    print(colored('What the hell are you doing? You were not speeding!', 'green', attrs=['blink', 'bold']))
    exit()


SchoolZone = input('Did this happen in a School Zone (Y or N): ')
while SchoolZone != 'Y' and SchoolZone != 'y' and SchoolZone != 'N' and SchoolZone != 'n':
    print('I said Y or N, not \"' + SchoolZone + '\"')
    SchoolZone = input('Did this happen in a School Zone (Y or N): ')

SpeedOverTicket = SpeedOver * 6

if SpeedOver >= 30:
    BadSpeedTicket = 160
else:
    BadSpeedTicket = 0
Ticket = MinTicket + int(SpeedOverTicket) + int(BadSpeedTicket)
if SchoolZone == 'Y' or SchoolZone == 'y':
    Ticket = Ticket * 2
    HorriblePerson = 1
else:
    HorriblePerson = 0


print(colored('Your total ticket amount is $' + str(Ticket), 'green'))
if HorriblePerson == 1:
    print(colored('You are horrible for speeding in a school zone', 'red', attrs=['bold', 'blink']))

