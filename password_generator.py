letters = "abcdef"
# combinations=[]
for f in letters:
    print(f)
    for e in letters:
        print(f+e)
        for g in letters:
            print(f+e+g)
            for h in letters:
                print(f+e+g+h)
                for i in letters:
                    print(f+e+g+h+i)
                    break


    # for j in range(len(letters)):
    #     combination = letters[j:j+i]
    #     combinations.append(combination)


# with open("passwords.txt", "w") as f:
#     for combination in letters:for i in range(1, len(letters) + 1):
#         f.write(f"{combination}\n")