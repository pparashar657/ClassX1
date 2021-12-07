s1 = int(input('Enter side 1: '))
s2 = int(input('Enter side 2: '))
s3 = int(input('Enter side 3: '))

if ((s1**2 + s2**2 == s3**2) or
    (s2**2 + s3**2 == s1**2) or
        (s1**2 + s3**2 == s2**2)):
    print("The triangle is right-angled triangle.")
else:
    print('The triangle is not right-angled triangle.')
