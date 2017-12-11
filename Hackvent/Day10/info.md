#Day 10: Just play the game
## Haven't you ever been bored at school?
### Santa is in trouble. He's elves are busy playing TicTacToe. Beat them and help Sata to save christmas!

Get an invitation to use netcat to connect to:

nc challenges.hackvent.hacking-lab.com 1037

Have to play tic tac toe and play 100 games to win, won first game with this strategy:

```
If their first move is in the center, it's a little bit trickier. Again, form a diagonal. If their next move is in the corner, you can trap them by placing your next piece at the intersection of the row and column of the previous two X's. If their next move is at an edge, you'll be forced to settle for a draw.
```

After winning recieve message that this is only win 1 out of 100 needed for the key, so either have to automate this or break it somehow

After scripting it we get:

Telnet(challenges.hackvent.hacking-lab.com,1037): recv b'-- \nCongratulations you won! 100/100\n\nHV17-y0ue-kn'
Telnet(challenges.hackvent.hacking-lab.com,1037): recv b'0w-7h4t-g4me-sure\nPress enter to start again\n'


