string = input().lower()
b="aeiouy"
notvowl = ".".join([c for c in string if not c in b])

print ("." + notvowl)