def love_calculator(boy, girl):
    boy = boy.upper()
    girl = girl.upper()
    common_letters = set(boy) & set(girl)
    love_percentage = len(common_letters) / max(len(boy), len(girl)) * 100
    return love_percentage

boy=input("Enter the name of Boy: ")
girl = input("Enter the name of Girl: ")
love_percentage = love_calculator(boy, girl)

if love_percentage > 1:
    print(f"The love percentage between {boy} and {girl} is {love_percentage:.1f}%")
else:
    print("Sorry, the love percentage is too low to be displayed.")