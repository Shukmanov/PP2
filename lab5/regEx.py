import re

#1

stri = input()

print(re.match(r'ab{0,5}',stri))

#2

print(re.match(r'ab{2,3}', stri))

#3

print(re.match(r'\w+(_\w+)*', stri))

# \w+ значит любые буквы,символы "1 или более раз"
# * значит "0 или более раз"(типа повторяется)

#print(re.match(r'[a-z]{0,26}_[a-z]{0,26}', stri))

#4

print(re.match(r'[A-Z]([a-z])*', "Check"))

# "Check" нужен для того чтобы окончательно дать понять каким именно должен выглядеть шаблон
# для исключения "Test848esdhfue" ситуации

#5

print(re.match(r'a\w+b', stri))

#6

print(re.sub(r'._\s', ':', stri))

#7

print(re.sub(r'[a-z]_[a-z]', '[A-Z][A-Z]', stri))