# Ask For Age
print('Please enter an age so we can allocate you your place in the party')
age = input('How Old Are you?\n')

if age != '':
    if int(age) >= 18 and int(age) <= 21:
        # 18 - 21 Writband
        print('You Can Enter But you Need A Wrist Band')
    elif int(age) >= 21:
        # 21+ drink, normal entry
        print('Enjoy The Party!:)')
    else:
        # too young
        print("You Can't Enter As You Are Underage")
else:
    print('Please enter an age')

