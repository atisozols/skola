# Dota teksta datne teksts.txt. Izveido programmu, 
# kas saskaita vārdu biežumu datnē dotajā tekstā
# un izvada piecus biežāk minētos vārdus. 
# Atslēgas vārda garums nedrīkst būt īsāks par četriem burtiem.
import string

with open("teksts.txt") as f:
  text = f.read()
  text = text.lower()
  
  pieturzimes = string.punctuation
  
  for pieturzime in pieturzimes:
    text = text.replace(pieturzime, "")
    
  words = text.split(" ")
  # print(words)
  
  freq = {}
  for word in words:
    if len(word) > 3:
      freq[word] = words.count(word)
    # freq.update({word:words.count(word)})
    
  sortedWords = sorted(freq, key=freq.get, reverse=True)
  print(freq)
  print(sortedWords[:5])
  
  
  
  
  
  
  
  
  
  
  