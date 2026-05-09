def game():
    return 1223

score = game()
f = open("highscore.txt", "r")
highscore = int(f.read())
print(highscore)
f.close()

if ( highscore < score ):
    f = open("highscore.txt", "w")
    highscore = (f.write(str(score)))
    print(highscore)
    f.close() 