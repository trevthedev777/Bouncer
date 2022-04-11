# Ask For Age
age = input('How Old Are you?\n')

if int(age) >= 18 and int(age) <= 21:
    print('You Can Enter But you Need A Wrist Band')
elif int(age) >= 21:
    print('Enjoy The Party!:)')
else:
    print("You Can't Enter As You Are Underage")
# 18 - 21 Writband
# 21+ drink, normal entry
# too young