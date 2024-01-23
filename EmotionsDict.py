dic1 = { "sad":":(", "disouraged":":-(", "happy":":)","glad":":-)","blenk":";)"}
words = input("Enter your status")
word = words.split(' ')
output = ""
for w in word:
    output += dic1.get(w.lower(),w) + ' '
print(output)