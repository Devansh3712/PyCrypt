#modules
import pycryptcli
from pycryptcli import techniques
import click
from time import sleep

#list of categories of techniques
list_of_techniques = {
  'cipher' : ['ASCII', 'Caesar Cipher', 'Vignere Cipher', 'Morse Code', 'Tap Code'],
  'numeric' : ['Binary', 'Octal', 'Hexadecimal'],
  'encoding' : ['Base16', 'Base32', 'Base64', 'Base85'],
  'hash function' : ['MD5', 'SHA224', 'SHA256', 'SHA384', 'SHA512', 'SHA-3-216', 'SHA-3-512', '256-bit BLAKE2', '512-bit BLAKE2']
}

@click.group()
def pycrypt():
	"Cryption tool made using python"

@pycrypt.command()
def all():
	"Lists all available cryption techniques"

	print("List of Techniques:\n")
	for i in list_of_techniques:
		print(i + ":", end = " ")
		print(*list_of_techniques[i], sep = ", ")
		print()

@click.option("-c", "--category", help = "Returns cryption techniques from given category")
@pycrypt.command()
def categories(category: str):
	"Lists cryption techniques of the given category"

	if category.lower() in list_of_techniques:
		print(*list_of_techniques[category], sep = ", ")

	else:
		print(f'{category} not found')

@click.option("-t", "--technique", help = "Add the technique to be used")
@click.option("-i", "--input_file", type = click.File('r'), required = True, help = "Add the input file")
@click.option("-o", "--output_file", type = click.File('w'), required = True, help = "Add the output file")
@click.option("-k", "--key", help = "Key, if there is any", required = False)
@pycrypt.command()
def encrypt(technique: str, input_file, output_file, key: str):
	"Encrypt using the provided technique"

	string = input_file.read()

	if technique.lower() == 'ascii':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.ascii(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'caesercipher':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.caeserCipher(string, key)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'vigenerecipher':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.vigenereCipher(string, key)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'morsecode':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.morseCode(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'tapcode':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.tapCode(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'binary':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.binary(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'octal':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.octal(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'hexadecimal':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.encryption.hexadecimal(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base16':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.base16(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base32':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.base32(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base64':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.base64(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base85':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.base85(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'md5':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.md5(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha224':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.sha224(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha256':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.sha256(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha384':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.sha384(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha512':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.sha512(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha3_216':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.sha3_216(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha3_512':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.sha3_512(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'blake2_256':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.blake2_256(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'blake2_512':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Encrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.encryption.blake2_512(string)
		print(result)
		output_file.write(result)

@click.option("-t", "--technique", help = "Add the technique to be used")
@click.option("-i", "--input_file", type = click.File('r'), required = True, help = "Add the input file")
@click.option("-o", "--output_file", type = click.File('w'), required = True, help = "Add the output file")
@click.option("-k", "--key", help = "Key, if there is any", required = False)
@pycrypt.command()
def decrypt(technique: str, input_file, output_file, key: str):
	"Decrypt using the given technique"

	string = input_file.read()

	if technique.lower() == 'ascii':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.ascii(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'caesercipher':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.caeserCipher(string, key)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'vigenerecipher':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.vigenereCipher(string, key)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'morsecode':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.morseCode(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'tapcode':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.tapCode(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'binary':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.binary(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'octal':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.octal(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'hexadecimal':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
		    for i in bar:
		        sleep(0.02)
		result = techniques.decryption.hexadecimal(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base16':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.base16(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base32':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.base32(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base64':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.base64(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'base85':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.base85(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'md5':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.md5(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha224':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.sha224(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha256':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.sha256(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha384':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.sha384(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha512':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.sha512(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha3_216':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.sha3_216(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'sha3_512':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.sha3_512(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'blake2_256':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniquesdecryption.blake2_256(string)
		print(result)
		output_file.write(result)

	elif technique.lower() == 'blake2_512':
		fill_char = click.style('=')
		with click.progressbar(range(100), label='Decrypting', fill_char=fill_char) as bar:
			for i in bar:
				sleep(0.02)
		result = techniques.decryption.blake2_512(string)
		print(result)
		output_file.write(result)

if __name__ == "__main__":
	pycrypt(prog_name = "pycrypt")