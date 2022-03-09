def printInstructions(instructions):
    print(instructions)

def getUserScore(userName):
    content = []
    i = 0
    try:
        f = open('score.txt', 'r')
        #firstline = f.readline()
        #print(content)
        for line in f:
            #print(line, end="\n")
            content.append(line.split(','))
            #print(content[i][0])
            if userName == content[i][0]:
                print("Taki sam gracz, wynik: %s" %content[i][1])
                f.close()
                return content[i][1]
            #else:
                #print("Nowy gracz\n\n")
                #f.close()
            i += 1
        return "-1"

    except IOError:
        print("Brak pliku zapisu, tworze nowy.")
        f = open('score.txt', 'w')
        f.write(userName+",0\n")
        f.close()
        return "-1"
    print("\n\n%s" %content)
    f.close()

def updateUserScore(newUser, userName, score):
    import os
    content = []
    i = 0
    if bool(newUser) == True:
        f = open('score.txt', 'a')
        f.write(userName+","+score+"\n")
        f.close()
    else:
        q = open('score.tmp', 'w')
        f = open('score.txt', 'r')
        for line in f:
            #print(line, end="\n")
            content.append(line.split(','))
            #print(content[i][0])
            if userName == content[i][0]:
                q.write(score+"\n")
                q.close()
            else:
                q.write(line+"\n")
            q.close()
            os.remove('score.txt')
            os.rename('score.tmp','score.txt')
        i += 1
        f.close()


#us = getUserScore("sdf")
#a = updateUserScore(1,"Maciek","100")

#print(us)
