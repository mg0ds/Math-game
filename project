
import gametasks
import gameclasses


try:
    mathInstructions = "Rozwiaz rownanie. dobra odpowiedz to +1\n"
    binaryInstructions = "Podaj liczbe w systemie binarnym, dobra odpowiedz to +1\n "
    bg = gameclasses.BinaryGame()
    mg = gameclasses.MathGame()

    print("Podaj Soje imie:\n")
    userName = input()
    score = int(gametasks.getUserScore(userName))

    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    print("Witaj, Twoj wynik to %s\n" %score)

    userChoice = 0
    while userChoice != "-1":
        print("Math Game (1) czy Binary Game (2)?\n")
        game = input()
        while game != "1" and game != "2":
            print("W co gramy? Math Game (1) czy Binary Game (2)?\n")
            game = input()
        print("ile chcesz pytan? (1-10)\n")
        numPrompt = input()
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print("Zla ilosc pytan, ile chcesz? (1-10)\n")
                numPrompt = input()

        if game == "1":
            mg.noOfQuestions = num
            gametasks.printInstructions(mathInstructions)
            score = score + mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            gametasks.printInstructions(binaryInstructions)
            score = score + bg.generateQuestions()
        print("Twoj wynik to %s\n" %score)
        print("wcisnij klawisz aby kontynuowac albo \"-1\" zeby wyjsc\n")
        userChoice = input()

    gametasks.updateUserScore(newUser, userName, str(score))
except Exception as e:
    print("Jakis blad ?\nKoniec programu.\n")
    print("error: ", e)
