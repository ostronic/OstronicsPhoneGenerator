# OstronicsPhoneGenerator
Generates Phone numbers of any of the three nations in bulk: NIGERIA, AUSTRALIA, UNITED STATES

# USAGE
python OstronicsPhonegen.py -h

python Ostronicsphonegen.py -Usa -n 500

usage: OstronicsPhonegen.py [-h] [-Ng] [-Aus] [-Usa] [-n value]

optional arguments:
  -h, --help            show this help message and exit
  -Ng, --Nigeria        Add the < -Ng > command to generate Nigerian numbers
  -Aus, --Australia     Add the < -Aus > command to generate Australia numbers
  -Usa, --United_States
                        Add the < -USa > command to generate United States numbers
  -n value              Add the < -n > < value > command to print out amount of value numbers. The default
                        value if < -n > is not specified is 100
                        
# PREFACE
Suppose you're in a bounty program , e.g ; a network provider, and you need to fuzz an input which accepts phone numbers, then this code is for you. I'm working to add more functionalties to the code, so test it out , report any issues faced, and feel free to pull requests if you want to be part of this project.
