from collections import Counter
string = "This is a common question for interview"
dictionary = dict(Counter(string))
a = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)
print(a)
