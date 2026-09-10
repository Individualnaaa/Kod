word = "Python"
# print(word)
# word[0] = "J"
# to nie zadziała, ze względu na to, że stringi są niezmienne (immutable)

copy_word = print(word[:]) 
copy_word1 = word[:] # kopiowanie stringa
print(copy_word1) # idealna kopia, nawet id te samo

print(id(word))
print(id(copy_word1)) # różne miejsca w pamięci, bo to kopia

copy_word1 = copy_word1 + " jest super" # tworzymy nowy string, bo stringi są niezmienne
print(id(copy_word1))

copy_word1 = copy_word1.upper()
print(copy_word1) # tworzymy nowy string, bo stringi są niezmienne