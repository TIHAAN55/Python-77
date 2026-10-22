print("Good morining, this is your assistant who has come to annoy you.")

hw = 4
complete  = 0
print("Start now, you wouldn't have time then.")
hw1 = input("Finished first task?")
if hw1 == "yes":
    complete += 1
    hw2 = input("Finished second task?")
    if hw2 == "yes":
        complete += 1
        hw3 = input("Finished third task?")
        if hw3 == "yes":
            complete += 1
            hw4 = input("Finished final task?")
            if hw4 == "yes":
                complete += 1
                if complete == 4:
                    print("Congrats, no more homework. I don't need to annoy you again!")