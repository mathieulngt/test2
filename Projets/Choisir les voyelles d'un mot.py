print("Sélection des voyelles dans: Hello world")

chaine = "Hello world"

for letter in chaine :
	if letter in "aeiouyAEIOUY":
		print(letter, end=" ")