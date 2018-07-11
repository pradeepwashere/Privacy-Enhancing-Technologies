import math
import random
import math
import sys
import numpy as np
import gmpy
from decimal import *

def genPrime(k):																#Function To Generate Primes
	try_count = 1000
	try_count_ = try_count
	while try_count > 0:
		n = random.randrange(2**(k-1),2**(k))
		try_count = try_count - 1
		if checkPrime(n) == True:
			return n

def checkPrime(n):																# Function to Check for Primality 
		KnownPrimes = [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
					,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
					,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
					,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
					,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
					,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
					,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
					,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
					,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
					,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009
					]
		if(n&1 != 0): 														#Check for even
			for p in KnownPrimes:											#Check if factor of given primes
				if(n % p == 0):
					return False
			return checkRabin(n)

# def checkRabin(n):															# Rabin Function  to Check for Primality 
# 	phi = n-1
# 	pow2 = 0
# 	# while phi&1 ==0:
# 	while phi%2 == 0 :				  #Find the exponent,phi in 2^{phi} 
# 		phi=phi/2
# 		pow2=pow2+1						# (n-1)  = (phi) * 2^(pow2)
# 	checkCount = 0
# 	while checkCount < 128:
# 		a =random.randrange(2,n-1)   #Check 128 random bases to increase probability of correctness
# 		rem = pow(a,phi,n)			 #Check for a^{d} = 1 mod n
# 		if (rem != 1):				 #Check for Composite
# 			i = 0
# 			while rem!= (n-1):
# 				if i == pow2-1:		# d.a^2, d.a^4, d.a^8. Only for (i == pow2) = > rem = n-1 = -1 mod n
# 					return False
# 				else:
# 					i = i+1
# 					rem = (rem**2)%n
# 		checkCount = checkCount+2
# 	return True


def gen():
	check = False
	while (check == False):
		a =  genPrime(1024)
		b =  genPrime(1024)
		if ((a != None and b != None and a!=b)):
			check =True
			return a,b

def getgcd(x,y):
    while y > 0:
        x, y = y, pow(x,1,y)
    return x

def getlcm(x, y):
    return x * y / getgcd(x, y)

def getn(x,y):
	return a*b


def invgcd(a, b):				# Find such that ax + by = gcd(a,b) = 1 mod m
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = invgcd(b % a, a)
		return (g, x - (b // a) * y, y) # b//a returns integral result

def modinv(a, m):
	g, x, y = invgcd(a, m)
	return x % m

def gen2():						#Random Number Generator
	k = 2048
	check = False
	while (check == False):
		r =  random.randrange(2**(k-1),2**(k))
		if (r != None ):
			if(getgcd(r,n)==1):
				check =True
				return r

def getpubpriv(a,b):			# Obtain all public and Private parameters for the encryption
	n 		= getn(a,b)
	g 		= n + 1
	lambDa  = (a-1) * (b-1)
	mew 	= modinv(lambDa, n)
	public  = (n,g)
	private = (lambDa, mew)
	return (n,g,lambDa,mew,public,private)

def Doencrypt(g,n,m):
	r = gen2()
	n_2 = pow(n,2)
	if (m<0):				  #To allow encrption of negative coefficients in polynomial required by Q2
		m1 = m * -1	
	else:
		m1=m

	encp1 = pow(g,m1,n_2)
	encp2 = pow(r,n,n_2)
	enc = (encp1*encp2)% (n_2)
	return enc

def getMessage():			# Used in the Pallier Encryption of Q1
	k = 1024
	choice = input("(1) Random message, (2) Input Message? ")
	if choice ==1:
		m = random.randrange(2**(k-1),2**(k))
	else:
		m = input("What is your message? ")
		print "Your message is: ", m
		type(m)
	return m

def Dodecrypt(enc,lamdDa,mew,n):	# Decryption Function
	n_2 = pow(n,2)
	dec1	= pow(enc,lambDa,n_2)
	dec2    = (dec1 - 1)/n 
	dec3 	= (dec2 * mew) %n
	if (n-dec3<dec3):				# Allows decryption of negative coefficients
		return (dec3-n)
	return dec3

def Display(m,mdec):
	print 'Message is',m
	print 'Decryption is',mdec

def Docheck(m,mdec):
	if m==mdec:
		print 'Successful Decryption'

def DispPubPriv(public,private):
	print 'public Params',public
	print '\n'
	print 'private Params', private
	print '\n'

def GetSizeandInputs():				# Input for Party 1
		s = raw_input()
		numbers = map(int, s.split())
		my_new_list = [i for i in numbers]
		size = len(numbers)
		return my_new_list,size

def GetSizeandInputs2():			# Input for Party 2
		s = raw_input()
		numbers = map(int, s.split())
		my_new_list = [i for i in numbers]
		size = len(numbers)
		return my_new_list,size

def DispInput(p1,p2):			# Display set and set size
	print 'Party 1'
	print 'Elements', p1
	print '\n'
	print 'Party 2'
	print 'Elements', p2

def GetSets():						# Call the Input Function
	print("Input the elements of P1 in order. Type each element followed by a space.  Eg. >> 2 3 4 5 ")
	p1,s1 = GetSizeandInputs()
	print("Input the elements of P2 in order. Type each element followed by a space   Eg  >> 4 5 6 7")
	p2,s2 = GetSizeandInputs2()
	return p1,s1,p2,s2

##################################################################		Question 2 and 3 Starts Here
																		#Step 1 (at P1)
def SendEncList(poly1,g,n,o):											#  Encrypt the Coefficients of the Polynomial by P1. 
	EncList=[]
	n_2 = pow(n,2)
	for i in xrange(0,o+1):												#  If the coefficient is negative, use the homomorphism property to compute an encryption
		c = Doencrypt(g,n,abs(int(poly1[i])))							#  This EncList is sent to P2 in the CoeffPow function along with the public parameters
		if(poly1[i]<0):
			c = gmpy.invert(c,n_2)				 						#  Note that this library has only been used here. The recursive function that was originally implemented
		EncList.append(c)													#  was hitting a recursive limit for this input. However the original recursive function has been used everywhere
	return EncList 															#  else to compute the inverse
##################################################################
##################################################################
																		#Step 2 (at P2)  [FOR Q3]
def CoeffPowQ3(EncList,a,n,g):
																		# Evaluating the function with (each value belonging to set P2) .
	n_2 = pow(n,2)														# Randomization also happens at this step
	Ans = 1																# Return tuples to P1
	o = len(EncList) - 1												# computing Enc(rP(y)+y) = Enc(y)*Enc(P(y))^r
	r1 =random.randrange(1,10) 
	for d in range(0,o+1):
		poower = EncList[d]												# EncList[0] is the constant term
		a_poower = a**d
		power= int (poower)
		Ans = Ans * pow(power,a_poower,n_2)

	exp = r1
	r1 = pow(Ans,exp,n_2)
	r2 = r1*Doencrypt(g,n,a) 										# Important step in the encryption, computing Enc(rP(y)+y) = Enc(y)*Enc(P(y))^r
	return r2 														# The tuples are collected together in a list and permuted at the recieving end of this function
																	# End of function for Q3

##################################################################
																	#Step 2 (at P2)	   [FOR Q2]
def CoeffPowQ2(EncList,a,n):									# Implemented using algorithm defined in the paper
																# Evaluating the function with (each value belonging to set P2) .
	n_2 = pow(n,2)												# Randomization happens at this step
	Ans = 1														# Return tuples to P1
	o = len(EncList) - 1
	r =random.randrange(1,10) 
	for d in range(0,o+1):
		poower = EncList[d]										# EncList[0] is the constant term
		a_poower = a**d
		power= int (poower)
		Ans = Ans * pow(power,a_poower,n_2)

	exp = a*r
	r1 = pow(Ans,exp,n_2)										# Algorithm as defined in the paper
	r2 = pow(Ans,r,n_2)
	return r1,r2 												# The tuples are collected together in a list and permuted at the recieving end of this function
																# End of function For Q2

##################################################################
def RecieveEncListandPubParamfromP1(p1EncList,n,g): 			
	p2EncList  = []
	p2n        = n
	p2g 	   = g
	p2EncList  = p1EncList
	return p2EncList,p2n,p2g
##################################################################
def RecieveTuplesFromP2(z):
	p1z = []
	p1z = z
	return p1z

##############  MAIN FUNCTION ####################################
##################################################################
##################################################################
print '\n'
print 'SETUP PHASE'
a, b = gen()											# Obtaining two Primes
n,g,lambDa,mew,public,private = getpubpriv(a,b)			# Setup phase of P1 happens here. P1 creates it's public and private variables for the encryption
														# Generating the random r used in Paillier Encryption
														# Get the Input sets

choice = input("(0) Just Encryption and Decryption (1) TestBench for union and Intersection, (2) Input Message for union and Intersection? ")
print '\n'
if choice == 0:
		m = getMessage()
		c = Doencrypt(g,n,m)
		mdec = Dodecrypt(c,lambDa,mew,n) 								# Decrypt Phase using cipher, private and public variables
		Display(m,mdec)
		Docheck(m,mdec) 												# Check if decryption Sucessful
		exit()

elif choice ==2:
	p1,s1,p2,s2 = GetSets()
else:
	p1 = [9,32,17,45,98,23,54,234,87]
	p2 = [19,65,17,54,8,76,29,81,87,36,23]

DispInput(p1,p2)
print '\n'
poly1 = np.poly1d(p1, True)								# Generate the Polynomial function on the set items for P1
print 'Generating polynomial from elements in set belonging to P1'
print '\n'
print poly1
print '\n'
o = poly1.order

p1EncList = []
p2EncList = []
DecList = []
TupleList = []
TuplePart1 = []
TuplePart2 = []
RecieveBuffer=[]
AnswerBuffer =[]

####################################################################################################################################
p1EncList = SendEncList(poly1,g,n,o)						  								#  ( Step 1.1 )[@ P1] 	Compute encrypted values of the coefficients of the polynomial
print 'Computing encrypted values of the coefficients of the polynomial'
####################################################################################################################################
p2EncList,p2n,p2g = RecieveEncListandPubParamfromP1(p1EncList,n,g) 							#  (Step 1.2)[P1 -> P2] P2 recieves Encrypted List of Coefficient from P1 along with the public parameter
print 'P2 recieving Encrypted List of Coefficient from P1 along with the public parameter'
####################################################################################################################################
print 'For each value,a, in set of P2, evaluating the polynomial function for the a'		# ( Step 2.1 )[@ P2]  For each value,a, in set of P2, evaluate the polynomial function for the a
for a in p2:
	r1,r2  = CoeffPowQ2(p2EncList,a,p2n)													# Recieving function for Q2.
	TuplePart1.append(r1)
	TuplePart2.append(r2)																	#Creating Tuples from elements Recieved
	z = zip(TuplePart1,TuplePart2)                     		  								# Tuples are collected and permuted
	random.shuffle(z,random.random)															# Encrypted values are collected and permuted, ready to be sent to P1


	r3 	   = CoeffPowQ3(p2EncList,a,p2n,p2g)												# Recieving function for Q3
	RecieveBuffer.append(r3)                    		  									
	random.shuffle(RecieveBuffer,random.random)												# Encrypted values are collected and permuted, ready to be sent to P1


print 'Tuples are being collected and permuted'
													
####################################################################################################################################
p1q2 = RecieveTuplesFromP2(z)						    #  (Step 2.2)[P2 -> P1] P2 Send the permuted tuples to P1  Q2Tuples
p1q3 = RecieveTuplesFromP2(RecieveBuffer)				#  (Step 2.2)[P2 -> P1] P2 Send the permuted tuples to P1  Q3Tuples

print 'P2 Sending the permuted tuples to P1'
####################################################################################################################################
print 'P1 recieves the tuples, decrypts the tuple'		# Processing for Q3 (intersection) of two sets
print '\n'
print '\n'
print 'Results of Tuple Decryption at P1 :'

print 'Processing Intersection of Sets Now'
print '\n'
for r1 in p1q3:
	r1d    = Dodecrypt(r1,lambDa,mew,n) 				# ( Step 3 )[@ P1] P1 recieves the tuples, decrypts the tuple
	for cmp in p1: 										# P1 gets a random value on decryption in case of no intersection, and outputs all values..
		if(r1d == cmp): 								# ..for which there is an intersection ( it belongs to set of P1)
			# print r1d 								# The complexity is O(n^2)
			print 'Match ! Printing ! '
			AnswerBuffer.append(int(r1d))

print '\n'
####################################################################################################################################
####################################################################################################################################
print '\n'												# Processing for Q2 (Union) of two sets
print 'Processing Union of Sets Now'
print '\n'
for r1,r2 in p1q2:
	r1d    = Dodecrypt(r1,lambDa,mew,n) 				# ( Step 3 )[@ P1] P1 recieves the tuples, decrypts the tuple
	r2d    = Dodecrypt(r2,lambDa,mew,n)	
	if(r1d==0 and r2d==0):								# If both values are zero, it is ignored
		print 'Zero Value on Decryption. Not adding to set'
	else:
		print 'Non Zero Value on Decryption. Add to set'
		ch = r1d/r2d  								    # Compute the value otherwise and add to set
		p1.append(int(ch))

print '\n'
####################################################################################################################################
print '\n'
print 'The output (intersection of the sets) @P1 is as follows'
print AnswerBuffer
print '\n'

####################################################################################################################################
print '\n'
print 'The output (union of the sets) @P1 is as follows'
print p1
print '\n'