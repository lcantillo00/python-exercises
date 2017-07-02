from test import testEqual
pirate = {'sir':'matey','hotel':'fleabag inn','student':'swabbie','boy':'matey','restaurant':'galley', 'your':'	yer','excuse':'	arr','are':'be'}


sentence = input("Please enter a sentence in English")

translatemsg = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        translatemsg.append(pirate[aword])
    else:
        translatemsg.append(aword)

print(" ".join(translatemsg))
