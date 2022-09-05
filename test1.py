print("Preis: %10.2f Euro" % (12.535423423))

#########################################

print("Hallo %s, dein Preis beträgt %5.2f Euro." % ("Peter"))

#print("Hallo {0:s}, dein Preis beträgt {1:<8.2f} EUR.".format("Peter", 13.23143))

zahl = int(input ("Geben Sie eine Zahl ein."))
zahl = zahl + 2
print(zahl)

#########################################

from decimal import *
a = 1.1
a2 = Decimal("1.2")
b = True
c = 20
d = 'Hello'
e = [1, 2, 3]
f = (1, 2, 3)
print(a, b, c, d, e, f, sep="\n")
print(type(a), type(a2), type(b), type(c), type(d), type(e), type(f), sep="\n")

#########################################

from decimal import *
z1 = 0.1 + 0.1 + 0.1
print(z1)
z2 = Decimal("0.1") + Decimal("0.1") + Decimal("0.1")
print(z2)

#########################################

eine_zahl : int = 2 #richtiger Huso Move :^) 
eine_zahl = "Hallo"
print(eine_zahl)

#########################################

# Arithmethische Operatoren
#``+, -, *, /, %, **, ...``

# Logische Operatoren
#and, or, not, &, |

# Vergleichsoperatoren
#``< <= > >= != = ``

#########################################

