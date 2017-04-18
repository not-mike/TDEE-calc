#!/usr/bin/env python
from __future__ import division

# unit converters
def kg2lb(kgs):
	weight = round(kgs * 2.20462262185, 4)
	return weight

def lb2kg(lbs):
	weight = round(lbs *  0.45359237, 4)
	return weight

def in2cm(inches):
	height = inches * 2.54
	return height

def pct(num):
	percent = num/100
	return percent

class CalcBMR(object):
	"""This class is used to generate a "CalcBMR" object, along with basic user info (ht, wt, etc), and calculates estimates 
	of Basal Metabolic Rate (BMR) using one of the three most common formulae: 1) Harris-Benedict (Rev.), 
	Mifflin-St. Jeor, or 3) Katch-McArdle."""

	def __init__(self, name, age, gender, mass, height, bf, activityFactor, goal):
		self.name = name
		self.age = age
		self.gender = gender
		self.mass = mass
		self.height = height
		self.bf = bf
		self.activityFactor = activityFactor
		self.goal = goal
	
	# BMR Formulae
	def HarrisBenedictRev(self):
		"""Harris-Benedict is least preferred, as it overestimates esp. in OVERWEIGHT individuals.
		(Mass in kg, height in cm)"""
		if self.gender == "male":
			BMR = round(88.362 + 13.397 * lb2kg(self.mass) + 4.799 * in2cm(self.height) - 5.677 * self.age, 2)
			return BMR
		if self.gender == "female":
			BMR = round(447.593 + 9.247 * lb2kg(self.mass) + 3.098 * in2cm(self.height) - 4.330 * self.age, 2)
			return BMR

	def MifflinStJeor(self):
		"""Mifflin-StJeor may overestimate esp. in OVERWEIGHT individuals. Preffered when bf% unknown. 
		(Mass in kg, height in cm)"""
		if self.gender == "male":
			BMR = round(5 + 10 * lb2kg(self.mass) + 6.25 * in2cm(self.height) - 5 * self.age, 2)
			return BMR
		if self.gender == "female":
			BMR = round(-161 + 10 * lb2kg(self.mass) + 6.25 * in2cm(self.height) - 5 * self.age, 2)
			return BMR

	def KatchMcArdle(self):
		"""Katch-McArdle Formula is most accurate for individuals w/ known bf%"""
		if not(0 <= self.bf <= 100):
			return "Unable to calculate w/o bodyfat estimate."
		LBM = lb2kg(self.mass) * (1 - pct(self.bf))
		BMR = round(370 + (21.6 * LBM), 2)
		return BMR

	''' Formulae Tests
	print "Test Input: 29 y/o Male, 177.8cm (5'10\"), 86.1826kg (190lb), 18% Body Fat"
	print "**************************************************************************"  
	print "BMR by Harris-Benedict (Revised): ", HarrisBenedictRev(29, "male", lb2kg(190), 177.8)
	print "BMR by Mifflin-St. Jeor: ", MifflinStJeor(29, "female", lb2kg(190), 177.8)
	print "RDEE by Katch-McArdle: ", KatchMcArdle(lb2kg(190), pct(18))
	'''
	def calcTDEE(self):
		"""This method returns a User's daily maintenance estimate based on provided inputs."""
		if (0 <= self.bf <= 100):
			maint = self.KatchMcArdle() * self.activityFactor
			return maint
		else:
			maint = self.MifflinStJeor() * self.activityFactor
			return maint 

	def getGoal(self):
		goals = {
		1: "BEAST MODE (GAIN 2lb/wk)",
		2: "SMALL LIFT (GAIN 1lb/wk)",
		3: "MAINTAIN",
		4: "WEIGHT REDUCTION (LOSE 1lb/wk)",
		5: "LEAN TIMES (LOSE 2lb/wk)",
		}
		return goals.get(self.goal)

	def __repr__(self):
		return "USER REPORT: {0}.\n\
		Stats are: \n \
		Gender: {1}\n \
		Age: {2}\n \
		Height: {3}in\n \
		Weight: {4}lb\n \
		Body Fat (%): {5}\n\
		Activity Factor: {6}\n\
		Goal: {7}".format(self.name, self.gender, self.age, self.height, self.mass, \
			self.bf, self.activityFactor, self.getGoal())
