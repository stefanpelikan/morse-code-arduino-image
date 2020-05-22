# Python program to implement Morse Code Translator 
import base64
''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'} 

# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 

			# Looks up the dictionary and adds the 
			# correspponding morse code 
			# along with a space to separate 
			# morse codes for different characters 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			# 1 space indicates different characters 
			# and 2 indicates different words 
			cipher += ' '

	return cipher 

# Function to decrypt the string 
# from morse to english 
def decrypt(message): 

	# extra space added at the end to access the 
	# last morse code 
	message += ' '

	decipher = '' 
	citext = '' 
	for letter in message: 

		# checks for space 
		if (letter != ' '): 

			# counter to keep track of space 
			i = 0

			# storing morse code of a single character 
			citext += letter 

		# in case of space 
		else: 
			# if i = 1 that indicates a new character 
			i += 1

			# if i = 2 that indicates a new word 
			if i == 2 : 

				# adding space to separate words 
				decipher += ' '
			else: 

				# accessing the keys using their values (reverse of encryption) 
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 

	return decipher 

# Hard-coded driver function to run the program 
def main(): 


	content = open("hello_test.txt").read()
	message_array = ""

	#this reproduces the cat command, sort of. the .read() blasts something into the terminal

	words = content.split(" ")
	with open('hello_test_morse.txt', 'w') as f: 
		for word in words:
			result = encrypt(word.upper()) 
			print (result)
			# textFile.write(result)
			message_array += (result)
		f.write(message_array) 


	# message = open("morse_string.txt").read()
	# result = decrypt(message)
	# result_bytes = result.encode('ASCI')
	# fh = open("new_output1.jpg", "wb")
	# output = base64.b16decode(result)
	# fh.write(output)
	# fh.close()
	# with open("post_morse.txt", "wb") as binary_file:
	#     binary_file.write(result)
		# print (result) 

		    # file = open("string_file.txt", "w")


	# fh = open("postmorse_output.jpg", "wb")
	# output = base64.b16decode(result)
	# fh.write(output)
	# fh.close()

# Executes the main function 
if __name__ == '__main__': 
	main() 
