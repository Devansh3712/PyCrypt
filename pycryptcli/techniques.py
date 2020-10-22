#modules
import base64
import hashlib

#---<encryption>---#
class encryption:
	#cipher
	def ascii(string):
	    c = ""
	    for i in string:
	        c = c + str(ord(i))
	        c = c + ' '
	    return c[:-1]

	def caeserCipher(string, key):
		key = int(key)
		c = ""
		for i in range (len(string)):
			a = string[i]
			if ord(a) not in range(65,91) and ord(a) not in range (97,124):
				c += a
			elif a.isupper():
				c += chr((ord(a) + key - 65) % 26 + 65)
			else:
				c += chr((ord(a) + key - 97) % 26 + 97)
		return c

	def vigenereCipher(string, key):
	    c = ""
	    a = [ord(i) for i in (string)]
	    b = [ord(j) for j in (key)]
	    for x in range (len(n)):
	        d = (a[x] + b[x % len(k)]) % 26
	        if d.islower():
	        	c = c + chr(65 + d)
	        else:
	        	c = c+ chr(97 + d)
	    return c

	def morseCode(string):
		code = {
			' ':'|',
			'a':'.-',
			'b':'-...',
			'c':'-.-.',
			'd':'-..',
			'e':'.',
			'f':'..-.',
			'g':'--.',
			'h':'....',
			'i':'..',
			'j':'.---',
			'k':'-.-',
			'l':'.-..',
			'm':'--',
			'n':'-.',
			'o':'---',
			'p':'.--.',
			'q':'--.-',
			'r':'.-.',
			's':'...',
			't':'-',
			'u':'..-',
			'v':'...-',
			'w':'.--',
			'x':'-..-',
			'y':'-.--',
			'z':'--..',
			'0':'-----',
			'1':'.----',
			'2':'..---',
			'3':'...--',
			'4':'....-',
			'5':'.....',
			'6':'-....',
			'7':'--...',
			'8':'---..',
			'9':'----.'
		}
		b = ""
		for i in string:
			if i.isalpha() == True:
				i = i.lower()
			if i in code:
				b += code[i]
			else:
				b += "#"
			b += " "
		return b[:-1]

	def tapCode(string):
		code = {
		    "A": ". .",
		    "B": ". ..",
		    "C": ". ...",
		    "D": ". ....",
		    "E": ". .....",
		    "F": ".. .",
		    "G": ".. ..",
		    "H": ".. ...",
		    "I": ".. ....",
		    "J": ".. .....",
		    "K": ". ...",
		    "L": "... .",
		    "M": "... ..",
		    "N": "... ...",
		    "O": "... ....",
		    "P": "... .....",
		    "Q": ".... .",
		    "R": ".... ..",
		    "S": ".... ...",
		    "T": ".... ....",
		    "U": ".... .....",
		    "V": "..... .",
		    "W": "..... ..",
		    "X": "..... ...",
		    "Y": "..... ....",
		    "Z": "..... .....",
		}
		c = ""
		for i in string:
			i = i.upper()
			if i != " ":
				c += code[i] + " "
			else:
				c += "/ "
		return c

	#numeric
	def binary(string):
	    c = bin(int(string))[2:]
	    return c

	def octal(string):
	    c = oct(int(string))[2:]
	    return c

	def hexadecimal(string):
	    c = hex(int(string))[2:]
	    return c

	#encoding
	def base16(string):
	    m = string.encode("ascii")
	    a = base64.b16encode(m)
	    c = a.decode("ascii")
	    return c

	def base32(string):
	    m = string.encode("ascii")
	    a = base64.b32encode(m)
	    c = a.decode("ascii")
	    return c

	def base64(string):
	    m = string.encode("ascii")
	    a = base64.b64encode(m)
	    c = a.decode("ascii")
	    return c

	def base85(string):
	    m = string.encode("ascii")
	    a = base64.b85encode(m)
	    c = a.decode("ascii")
	    return c

	#hash function
	def md5(string):
		n = string.encode()
		c = hashlib.md5(n).hexdigest()
		return c 

	def sha224(string):
		n = string.encode()
		c = hashlib.sha224(n).hexdigest()
		return c

	def sha256(string):
		n = string.encode()
		c = hashlib.sha256(n).hexdigest() 
		return c
	
	def sha384(string):
		n = string.encode()
		c = hashlib.sha384(n).hexdigest() 
		return c

	def sha512(string):
		n = string.encode()
		c = hashlib.sha512(n).hexdigest() 
		return c

	def sha3_256(string):
		n = string.encode()
		c = hashlib.sha3_256(n).hexdigest() 
		return c

	def sha3_512(string):
		n = string.encode()
		c = hashlib.sha3_512(n).hexdigest() 
		return c

	def blake2_256(string):
		n = string.encode()
		c = hashlib.blake2s(n).hexdigest() 
		return c

	def blake2_512(string):
		n = string.encode()
		c = hashlib.blake2b(n).hexdigest() 
		return c
#---</encryption>---#

#---<decryption>---#
class decryption:
	#cipher
	def ascii(string):
		n = string.split(" ")
		c = ""
		for i in n:
			c = c + str(chr(int(i)))
		return c

	def caeserCipher(string, key):
		key = int(key)
		c = ""
		for i in range (len(string)):
			a = string[i]
			if ord(a) not in range (65,91) and ord(a) not in range (97,124):
				c += a
			elif a.isupper():
				c += chr((ord(a) - key - 65) % 26 + 65)
			else:
				c += chr((ord(a) - key - 97) % 26 + 97)
		return c

	def vigenereCipher(string, key):
		c = ""
		a = [ord(i) for i in (string)]
		b = [ord(i) for j in (key)]
		for x in range (len(n)):
			d = (a[x] - b[x % len(key)]) % 26
			if d.islower():
				c += chr(65 + d)
			else:
				c += chr(97 + d)
		return c

	def morseCode(string):
		code={
			'|':' ',
			'.-':'a',
			'-...':'b',
			'-.-.':'c',
			'-..':'d',
			'.':'e',
			'..-.':'f',
			'--.':'g',
			'....':'h',
			'..':'i',
			'.---':'j',
			'-.-':'k',
			'.-..':'l',
			'--':'m',
			'-.':'n',
			'---':'o',
			'.--.':'p',
			'--.-':'q',
			'.-.':'r',
			'...':'s',
			'-':'t',
			'..-':'u',
			'...-':'v',
			'.--':'w',
			'-..-':'x',
			'-.--':'y',
			'--..':'z',
			'-----':'0',
			'.----':'1',
			'..---':'2',
			'...--':'3',
			'....-':'4',
			'.....':'5',
			'-....':'6',
			'--...':'7',
			'---..':'8',
			'----.':'9'
		}
		b = ""
		n = string.split()
		for i in n:
			if i in code:
				b += code[i]
			else:
				b += "#"
		return b

	def tapCode(string):
		code = {
		    "A": ". .",
		    "B": ". ..",
		    "C": ". ...",
		    "D": ". ....",
		    "E": ". .....",
		    "F": ".. .",
		    "G": ".. ..",
		    "H": ".. ...",
		    "I": ".. ....",
		    "J": ".. .....",
		    "K": ". ...",
		    "L": "... .",
		    "M": "... ..",
		    "N": "... ...",
		    "O": "... ....",
		    "P": "... .....",
		    "Q": ".... .",
		    "R": ".... ..",
		    "S": ".... ...",
		    "T": ".... ....",
		    "U": ".... .....",
		    "V": "..... .",
		    "W": "..... ..",
		    "X": "..... ...",
		    "Y": "..... ....",
		    "Z": "..... .....",
		}
		b = ""
		n = string.split(" ")
		for i in n:
			if i != "/":
				b += list(code.keys())[list(code.values()).index(i)]
			else:
				b += " "
		return b

	#numeric
	def binary(string):
		c = int(string, 2)
		return c

	def octal(string):
		c = int(string, 8)
		return c

	def hexadecimal(string):
		c = int(string, 16)
		return c

	#encoding
	def base16(string):
		m = string.encode("ascii")
		a = base64.b16decode(m)
		c = a.decode("ascii")
		return c

	def base32(string):
		m = string.encode("ascii")
		a = base64.b32decode(m)
		c = a.decode("ascii")
		return c

	def base64(string):
		m = string.encode("ascii")
		a = base64.b64decode(m)
		c = a.decode("ascii")
		return c

	def base85(string):
		m = string.encode("ascii")
		a = base64.b85decode(m)
		c = a.decode("ascii")
		return c
#---</decryption>---#