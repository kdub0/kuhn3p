from kuhn3p import deck, dealer, players

num_hands   = 3000
the_players = [players.Chump(0.99, 0.01, 0.0), 
	       players.Chump(0.0, 1.0, 0.0), 
	       players.Bluffer(0.2) ]

total = [0, 0, 0]
for hand in range(num_hands):
	first          = hand % 3
	second         = (first + 1) % 3
	third          = (second + 1) % 3

	this_players   = [the_players[first], the_players[second], the_players[third]]

	(state, delta) = dealer.play_hand(this_players, deck.shuffled())
	for i in range(3):
		total[(first + i)%3] += delta[i]

for i in range(3):
	print the_players[i], total[i]
