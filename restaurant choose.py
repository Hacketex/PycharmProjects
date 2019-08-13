# author=pratik
# created date=3 aug 2019
# last modified date=5 aug 2019
# https://github.com/hacketex
print("\t\t\tfind Best Restaurant for you")
a = "-" * 55
print(a)
vgt = input("Is anyone in your party a vegetarian? (yes/no):  ")
vegan = input("Is anyone in your party a vegan? (yes/no):  ")
gluten = input("Is anyone in your party a Gluten-Free? (yes/no):  ")
print(a)
(yes, no) = ("yes", "no")
(r1, r2, r3) = ("Main Street Pizza Company", "Corner Cafe", "The Chef's Kitchen")
(r4, r5) = ("Mama's fine Italian", "Joe's Gourmet Burgers")
if vgt == yes and vegan == yes and gluten == yes:
    print("here are your restaurant choices :\n%s\n%s\n%s\n%s" % (r1, r2, r3, r4))
elif vgt == yes and vegan == no and gluten == yes:
    print('here are your restaurant choices :\n% s\n% s\n% s' % (r1, r2, r3))
elif vgt == yes and vegan == no and gluten == no:
    print("here are your restaurant choices :\n", r4)
else:
    print("here are your restaurant choices :\n", r5)
