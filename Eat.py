#!/usr/bin/env python

from CalcBMR import CalcBMR
import os
import time
import textwrap

flag = False
yes = set(['yes', 'y', 'ye', ''])
no = set(['no', 'n'])

# Get Name
os.system('cls' if os.name == 'nt' else 'clear')
name = raw_input("Hello! What is your name? ")
os.system('cls' if os.name == 'nt' else 'clear')
print "Welcome, " + name + "!"
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

# Describe Eat
print "\033[95mEAT.\033[0m"
print "*****"
string = "This is a tool for connecting people with great food. \
Making healthy choices doesn't have to be difficult, and it certainly shouldn't mean giving up \
on delicious dining options! I hope that this will take some of the guesswork out of the process \
so you can spend less time counting calories and more time eating great food with friends!\n"
for line in textwrap.wrap(string, replace_whitespace=False):
	print line
print "\nI really hope you enjoy it!\n"
raw_input("Press ENTER to Continue...")
os.system('cls' if os.name == 'nt' else 'clear')

# Get User Stats
while(flag==False):
	print "First, I need to get just a little information about you..."
	os.system('cls' if os.name == 'nt' else 'clear')
	age = input("How old are you, " + name + "? ")
	os.system('cls' if os.name == 'nt' else 'clear')
	gender = raw_input("And are you a male or a female? ").lower()
	os.system('cls' if os.name == 'nt' else 'clear')
	mass = input("And about how much do you weigh (in lbs)? ")
	os.system('cls' if os.name == 'nt' else 'clear')
	heightFt = input("How tall are you in feet? ")
	heightIn = input("And how many inches? ")
	height = (heightFt * 12) + heightIn
	os.system('cls' if os.name == 'nt' else 'clear')
	choice = raw_input("Great! Finally, do you know what your bodyfat percentage is? ('yes' or 'no'): ").lower()
	if choice in yes:
		bf = input("Please enter it as a whole number (i.e. 18% bodyfat = 18): ")
	else:
		bf = "Unknown"
	os.system('cls' if os.name == 'nt' else 'clear')
	print "OK! Now, let's make sure that I got everything right. \n"
	print "You said that you are a {0}yr old {1}, who is {2}'{3}\" and weighs {4}lbs.\n".format(age, gender, \
																					heightFt, heightIn, mass)
	if bf != "Unknown":
		print "Your current bodyfat percentage is {0}%. \n".format(bf)
	choice = raw_input("Is that right? ('yes' or 'no'): ").lower()
	if choice in yes:
		flag = True
		os.system('cls' if os.name == 'nt' else 'clear')
	else:
		flag = False
	print("OOPS! I'm sorry. Let's try again.")
	os.system('cls' if os.name == 'nt' else 'clear')

USER = CalcBMR(name, age, gender, mass, height, bf, 0, 3)

string = "AWESOME! Next we'll get an estimate for how many calories your body requires each day. \
Nutritionists call this your \033[95m\033[4mTOTAL DAILY ENERGY EXPENDITURE (TDEE)\033[0m. It is one \
of the most important pieces of information when planning to meet your health and fitness goals. Your \
\033[95mTDEE\033[0m accounts for all the activities your body does from work and exercise, sleep and tissue repair, \
even the calories you burn eating food!"
for line in textwrap.wrap(string, replace_whitespace=False):
	print line
raw_input("\nPress ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

print "\033[95m\033[4mTDEE\033[0m consists of several components: \n"
string = "\033[95m\033[4mBasal Metabolic Rate (BMR)\033[0m: This is the number of calories your \
body would burn doing absolutely nothing - your base level.\n\
\033[95m\033[4mNon-Exercise Associated Thermogenesis (NEAT)\033[0m: These are all the calories \
you burn doing everything NOT exercise related (working, reading, shopping, walking, etc).\n\
\033[95m\033[4mExercise Associated Thermogenesis (EAT)\033[0m: These are the calories you burn \
during active exercise, for example lifting weights at the gym or running on a track.\n\
\033[95m\033[4mThermic Effect of Food (TEF)\033[0m: These are the calories your body expends in \
digestion as it breaks down the various nutrients you eat throughout the day. It depends a LOT on \
what you eat and not so much on when you eat it. For example, around 25% of the calories you consume \
from protein sources go to digesting that protein! Its slightly lower for carbs (5-25%) and much less \
for fats (only about 5%)."
for line in textwrap.wrap(string, replace_whitespace=False):
	print line
raw_input("\nPress ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

string = "There are a number of methods for calculating the Basal Metabolic Rate each with their own pros and cons. We went ahead and calculated yours \
using a few of the most commonly used methods. Based on what you told us your results were:"
for line in textwrap.wrap(string, replace_whitespace=False):
	print line
print "\nBMR by \033[95m\033[4mHarris-Benedict (Rev.)\033[0m: ", USER.HarrisBenedictRev(), "kCals"
print "BMR by \033[95m\033[4mMifflin-St. Jeor\033[0m: ", USER.MifflinStJeor(), "kCals"
print "RMR by \033[95m\033[4mKatch-McArdle\033[0m: ", USER.KatchMcArdle(), "kCals"

raw_input("\nPress ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

string = "Remember, \033[95mBMR/RMR\033[0m is an estimate of how many calories your body burns doing nothing. \
(Thankfully!) you're not in a coma, so we need to adjust this estimate to account for all of the other lifestyle \
factors that determine your \033[95mTotal Daily Energy Expenditure\033[0m." 
for line in textwrap.wrap(string,replace_whitespace=False):
	print line
print "\n"
string = "We still need to account for your work, exercise, and other daily activities. Again, there are a number \
of methods to accomplish this. One common approach is to increase our calories by an activity factor that considers \
our total cost of living."
for line in textwrap.wrap(string,replace_whitespace=False):
	print line

raw_input("\nPress ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

print "Thinking about your work, lifestyle, and exercise habits, which of the following best describes you?\n"
string = "1.2 = Sedentary (Desk job, and Little Formal Exercise)\n\
1.3-1.4 = Lightly Active (Light daily activity AND light exercise 1-3 days a week)\n\
1.5-1.6 = Moderately Active (Moderately daily Activity & Moderate exercise 3-5 days a week)\n\
1.7-1.8 = Very Active (Physically demanding lifestyle & Hard exercise 6-7 days a week)\n\
1.9-2.2 = Extremely Active (Athlete in ENDURANCE training or VERY HARD physical job)\n"
for line in textwrap.wrap(string, replace_whitespace=False):
	print line

while not(1.2 <= USER.activityFactor <= 2.2):
	USER.activityFactor = input("\nPlease enter a value from 1.2-2.2: ")

os.system('cls' if os.name == 'nt' else 'clear')

print "We're almost done!\n" 
print "Based on the information you've provided, \n\
your Total Daily Energy Expenditure estimate is: {0} kCals\n".format(USER.calcTDEE())
print "\033[95mTDEE\033[0m or \"Maintenance\" is an estimate of how many calories you would \
need to eat each day to stay at your current weight."
raw_input("\nPress ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

string = "Of course, one size does not fit all, and we each have different health and fitness goals. In the simplest terms, you must \
eat slightly more than your maintenance level in order to gain weight and slightly less than maintenance in order to lose weight."
for line in textwrap.wrap(string, replace_whitespace=False):
	print line
print "\n"
string = "How much more (or less) depends on how quickly you wish to gain or lose the weight (for good health it is suggested that one not exceed TDEE \
by more than about 10-20%). Gaining/losing about 1-2lbs per week is considered healthy and sustainable for most people."
for line in textwrap.wrap(string, replace_whitespace=False):
	print line
raw_input("\nPress ENTER to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

print "How would you describe your goals?\n"
string = "[1] BEAST MODE (GAIN 2lb/wk)\n\
[2] SMALL LIFT (GAIN 1lb/wk)\n\
[3] MAINTAIN (Happy right where you are?)\n\
[4] WEIGHT REDUCTION (LOSE 1lb/wk)\n\
[5] LEAN TIMES (LOSE 2lb/wk)"
for line in textwrap.wrap(string, replace_whitespace=False):
	print line

USER.goal = input("\nPlease make a selection: ")
os.system('cls' if os.name == 'nt' else 'clear')

print repr(USER)
