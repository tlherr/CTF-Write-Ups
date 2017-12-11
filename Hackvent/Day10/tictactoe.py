import sys
import os
import telnetlib

# Congratulations you won! 1/100
# Press enter to start again


def play_game():
    global GAMES
    print(GAMES)
    print("Starting new game")
    if GAMES != 0:
        tn.read_until(bytes("start again", "utf-8"), timeout=10)
        print("Entering to start again")
        tn.write(bytes('\r\n', 'utf-8'))

    print("Starting Moves")
    tn.read_until(bytes("Field:", 'utf-8'))
    tn.write(bytes('7\r\n', 'utf-8'))
    tn.read_until(bytes("Field:", 'utf-8'))
    tn.write(bytes('3\r\n', 'utf-8'))
    tn.read_until(bytes("Field:", 'utf-8'))
    tn.write(bytes('9\r\n', 'utf-8'))
    tn.read_until(bytes("Field:", 'utf-8'))
    tn.write(bytes('6\r\n', 'utf-8'))

    tn.read_until(bytes("Press enter to start again", 'utf-8'))
    GAMES += 1


if __name__ == "__main__":
    global GAMES
    GAMES = 0
    tn = telnetlib.Telnet("challenges.hackvent.hacking-lab.com", 1037)
    tn.set_debuglevel(1)

    # First prompt
    tn.read_until(bytes("Press enter to start the game", "utf-8"))

    tn.write(bytes('\r\n', 'utf-8'))
    while GAMES != 100:
        play_game()
    tn.read_all()
    tn.close()
