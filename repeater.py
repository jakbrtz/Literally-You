import random
import re

def owo(input):
	faces = [ "(・`ω´・)", "UwU", ">w<", "^w^" , ":heart_eyes:" , ":love_letter:" ]
	return (input
		.replace('r', 'w')
        .replace('R', 'W')
        .replace('l', 'w')
        .replace('L', 'W')
        .replace("NA", "NYA")
        .replace("NE", "NYE")
        .replace("NI", "NYI")
        .replace("NO", "NYO")
        .replace("NU", "NYU")
        .replace("Na", "Nya")
        .replace("Ne", "Nye")
        .replace("Ni", "Nyi")
        .replace("No", "Nyo")
        .replace("Nu", "Nyu")
        .replace("na", "nya")
        .replace("ne", "nye")
        .replace("ni", "nyi")
        .replace("no", "nyo")
        .replace("nu", "nyu")
        .replace("ou", "ow")
        .replace("oU", "oW")
        .replace("Ou", "Ow")
        .replace("OU", "OW")
        .replace("ove", "uv")
        .replace("OVE", "UV")
        .replace("ith", "iff")
        .replace("ITH", "IFF")
		.replace("! ", "! " + random.choice(faces) + " ")
		+ " " + random.choice(faces))

def clap(input):
	return input.replace(" ", " :clap: ")

def lisp(input):
	output = ''
	i = 0
	while i < len(input):
		curr = input[i]
		prev = ''
		if i > 0:
			prev = input[i-1]
		next = ''
		if i + 1 < len(input):
			next = input[i+1]
		if i + 2 < len(input):
			next2 = input[i+2]
		c = 'c'
		t = 't'
		if (IsUpper(curr)):
			c = 'C'
			t = 'T'
		if (curr == 's'  or  curr == 'S'  or  curr == 'z'  or  curr == 'Z'):
			if (prev != 'S' and prev != 's' and prev != 'Z' and prev != 'z' and prev != 'T' and prev != 't'):
				output += t
			if ((prev != 'S' and prev != 's' and prev != 'Z' and prev != 'z')  or 
				(next == 'S'  or  next == 's'  or  next == 'Z'  or  next == 'z')):
				if (IsUpper(next)  or  (not IsLetter(next) and IsUpper(prev))):
					output += 'H'
				else:
					output += 'h'
			if (not IsLetter(next2) and (next == 'E'  or  next == 'e')):
				i+=1
		elif (curr == 'c'  or  curr == 'C'):
			if (next == 'e'  or  next == 'i'  or  next == 'y'  or  next == 'E'  or  next == 'I'  or  next == 'Y'):
				if (not (prev == 's'  or  prev == 'S'  or  prev == 'x'  or  prev == 'X')):
					output += tell
					if (IsUpper(next)  or  (not IsLetter(next) and IsUpper(prev))):
						output += 'H'
					else:
						output += 'h'
					if (not IsLetter(next2) and (next == 'E'  or  next == 'e')):
						i+=1
			elif not ((next == 'h'  or  next == 'H') and (prev == 't'  or  prev == 'T')):
				output += curr
		elif (curr == 'x'  or  curr == 'X'):
			output += c
			if (IsUpper(next)  or  (not IsLetter(next) and IsUpper(prev))):
				output += 'TH'
			else:
				output += 'th'
		else:
			output += curr
		i+=1
	return output

def IsLetter(c):
	return (c>='a' and c<='z') or (c>='A' and c<='Z')
	
def IsUpper(c):
	return (c>='A' and c<='Z')
	
def dobby(input, author):
	input = (input
		.replace("yours", "master's")
		.replace("your", "master's")
		.replace("you", "master")
		)
	if (input[:2] == "I " or input[:2] == "i "):
		input = author + " " + input[2:]
	input = (input
		.replace(" i "," " + author + " ")
		.replace(" I "," " + author + " ")
		.replace(" me "," " + author + " ")
		.replace(" Me "," " + author + " ")
		.replace(" ME "," " + author.capitalize() + " ")
		.replace(" mE "," " + author.capitalize() + " ")
		.replace(" my "," " + author + "'s ")
		.replace(" My "," " + author + "'s ")
		.replace(" MY "," " + author.capitalize() + "'s ")
		.replace(" mY "," " + author.capitalize() + "'s ")
		)
	return input