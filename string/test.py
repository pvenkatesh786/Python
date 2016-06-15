from string import maketrans

i = "aeiou"
o = "12345"
trantab = maketrans(o,i)

str = "Hi this is venky"
print str.translate(trantab)
