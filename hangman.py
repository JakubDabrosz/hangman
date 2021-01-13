import random
import pics



fu_counter = 0
hidden_word = ''
hidden = ''

word = random.choice(pics.words) #randomly choice from pics.words =]


display = []
for _ in range(len(word)): # '_____' hidden word
	display += "_"


while fu_counter < len(pics.hm) and hidden != word:

	print (hidden_word.join(display)) # display hidden word
	guess = input('Guess a word, type letter: ').lower() # basic str input with lower cases, cuz lower cases in words list
	if guess in word and guess not in hidden:
		for items in range(len(word)):
			if word[items] == guess:
				display[items] = guess #unhidden 
	else:
		fu_counter += 1
		print(pics.hm[fu_counter-1])

	hidden = hidden_word.join(display) # for display only (string as one line not list)


if len(pics.hm) == fu_counter:
	print ('You died boi. Upss! Sorry! You lost*. Play again.')
else:
	print (f"You win! You guessed a {hidden}")





	






