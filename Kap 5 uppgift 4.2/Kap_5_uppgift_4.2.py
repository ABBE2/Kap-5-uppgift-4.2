p = int(input("hur mycket kostar bensinen/liter?"))

if p<10:
    print("Det var billigt!")
elif p>9 and p<16:
    print("Tanka full tank!")
elif p>15 and p<21:
    print("Tanka tio liter")
else:
    print("Nu saljer jag bilen och cyklar istallet")