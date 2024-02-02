# ostronics Phone Generator v1

# Things to be implemented;
#   Phone numbers validation and color coding
#   Play a music while the code runs
#   Threading or concurrency

import random
import os, sys
import platform
from pyfiglet import Figlet
from tqdm import tqdm
import time
import argparse

# Calling the parser globally to accept arguments to determine the countries number to print    
parser = argparse.ArgumentParser()

# Accepting the Argument { -Ng } for Nigeria input
parser.add_argument('-Ng', '--Nigeria', dest='baba_blue', action='store_true', help="Add the < -Ng > command to generate Nigerian numbers")

# Accepting the Argument { -Aus } for Australia input
parser.add_argument('-Aus', '--Australia', dest='ozzy_man', action='store_true', help="Add the < -Aus > command to generate Australia numbers")

# Accepting the Argument { -Usa } for United States input
parser.add_argument('-Usa', '--United_States', dest='states_man_on_the_rock', action='store_true', help="Add the < -USa > command to generate United States numbers")

parser.add_argument('-n', type=int, default=100, metavar='value', help="Add the < -n > < value > command to print out amount of value numbers. The default value if < -n > is not specified is 100 ")

args = parser.parse_args()

# Get the maximum number of generated phone numbers from the user
max_numbers = args.n # int(input("Enter the number of phone numbers to generate: "))

# Define the digits
num = '0123456789'

def clear_screen():
    ''' Clear the terminal screen '''

    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def prompt():
    """Print a beautiful ostronics text to the screen"""
    
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('Ostronic Phone Generator'))
    time.sleep(5)
    clear_screen()


# Nigeria number function
def Nigeria_Numbers(country_code):
    
    # Calling the beautiful text
    prompt()

    # Opening a file to save the generated numbers in
    file = open('Nigeriaphone.txt', 'w')

    # Define area codes Nigeria
    codes = ['070', '080', '081', '090', '091']

    # Loop for generating phone numbers
    for _ in tqdm(range(max_numbers)):
        # Generate a random phone number
        area = random.choice(codes)
        a, b, c, d, e, f, g, h = random.choices(num, k=8)
        numbers = area + a + b + c + d + e + f + g + h
        agbado = numbers.lstrip("0")

        # Write to file and print the generated phone number
        file.write(numbers + '\n')
        print('PHONE', str(country_code) + agbado)

    # Close the file
    file.close()


# Australia number function
def Australia_numbers(country_code):

    # Calling the beautiful text
    prompt()

    # Opening a file to save the generated numbers in
    file = open('Australiaphone.txt', 'w')

    # Define area codes for Autralia
    codes = ['2', '3', '4', '7', '8']

    # Loop for generating phone numbers
    for _ in tqdm(range(max_numbers)):
        # Generate a random phone number
        area = random.choice(codes)
        a, b, c, d, e, f, g, h = random.choices(num, k=8)
        number = area + a + b + c + d + e + f + g + h

        # Write to file and print the generated phone number
        file.write(number + '\n')
        print('PHONE', str(country_code) + number)

    # Close the file
    file.close()


# United States number function
def United_States_number(country_code):
    
    # Calling the beautiful text
    prompt()

    # Opening a file to save the generated numbers in
    file = open('UnitedStatesphone.txt', 'w')

    # Define area codes for United States
    codes = ['907', '205' , '251', '256', '334', '479', '501', '870', '480', '520', '602', '623', '928', '209', '310', '323', '408', '415', '510', 
            '530', '559', '562', '619', '626', '650', '661', '707', '714', '760', '805', '818', '831', '858', '909', '916', '925', '949', '951', '213',
            '303', '719', '970', '203', '860', '239', '305', '321', '352', '386', '407', '561', '727', '772', '813', '850', '863', '904', '941', '954', 
            '229', '404', '478', '706', '770', '912', '202', '302', '319', '515', '563', '641', '712', '808', '208', '217', '309', '312', '618', '630', '708', '773', '815', '847', 
            '219', '260', '317', '574', '765', '812', '316', '620', '785', '913', '270', '502', '606', '859', '225', '318', '337', '504', '985', '413', '508', '617', '781', '978', '231', '248', '269', '313', 
            '517', '586', '616', '734', '810', '906', '989', '301', '410', '207', '218', '320', '507', '612', '651', '763', '952', '314', '417', '573', '636', '660', '816', '228', '601', '662', '406', 
            '252', '336', '704', '828', '910', '919', '701', '308', '402', '603', '201', '609', '732', '856', '908', '973', '505', '575', '702', '775', '212', '315', '516', '518', '585', '607', '631', '716', '718', '845', '914', 
            '216', '330', '419', '440', '513', '614', '740', '937', '405', '580', '918', '503', '541', '215', '412', '570', '610', '717', '724', '814', '401', '210', '214', '254', '281', '325', '361', '409', '432', '512', '713', 
            '806', '817', '830', '903', '915', '936', '940', '956', '972', '979', '803', '843', '864', '605', '423', '615', '731', '865', '901', '931', '435', '801', '276', '434', '540', '703', '757', '804', '802', 
            '206', '253', '360', '425', '509', '262', '414', '608', '715', '920', '304', '307']

    # Loop for generating phone numbers
    for _ in tqdm(range(max_numbers)):
        # Generate a random phone number
        area = random.choice(codes)
        a, b, c, d, e, f, g = random.choices(num, k=7)
        number = area + a + b + c + d + e + f + g

        # Write to file and print the generated phone number
        file.write(number + '\n')
        print('PHONE', str(country_code) + number)

    # Close the file
    file.close()

if __name__ == '__main__':
    # Calling the function based on the parsed arguments
    try:
        if args.baba_blue:
            Nigeria_Numbers('+234')
        elif args.ozzy_man:
            Australia_numbers('+61')
        elif args.states_man_on_the_rock:
            United_States_number('+1')
        else:
            print('Usage: python OstronicsPhoneGen.py   < -Ng | -Aus | -Usa >   -n < number value >, default is 100.')
    except KeyboardInterrupt:
        print('Program terminated!!! :) Have a nice day ostronics ♥')
        time.sleep(3)
        quit()
