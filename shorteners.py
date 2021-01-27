import pyshorteners

s = pyshorteners.Shortener()
original_url = input()
print(s.tinyurl.short(original_url))

