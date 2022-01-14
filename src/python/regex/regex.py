# https://regex101.com/
import re
import string

# Find one number
p = re.compile("[0-9]")
print(p.findall("Find the number 1"))
print(p.findall("Find the number 12"))

# Find following number
p = re.compile("[0-9]+")
print(p.findall("Find the number 12"))

# Find pytest failed count
print(re.search(".{3}(?:failed)", "=== 1 failed ==="))

# Email check
p = re.compile("[a-zA-Z0-9\+]+@[a-zA-Z0-9]+\.[\.a-zA-Z0-9]+")
sentences = [
    "Filter for my email@adress.com",
    "@me dont filter this email@adress.com.de", ]

for sentence in sentences:
    print(p.search(sentence))

# Remove punctuation
samples = [' The cant sat on the mat.', 'The dog! ate my homework:']
print(samples[1].translate(str.maketrans('', '', string.punctuation)))



regexp = 'burrito'
string = 'boorrito'
result = re.match(regexp, string)

# . represents every charackter exept \n
regexp = 'string .'
re.match(regexp, 'string x')

# ? previous character can occur once or 0 times
regexp = '..? points? to gryffindor'
re.match(regexp, '50 points to gryffindor')

# r'' avoids backslash plague

# [] defines set of charackters
template = '[ax][le]'
print(re.match(template, 'ae'))

re.match('ja[a-z].', 'jaaa')
re.match('[A-Z]merica', 'Kmerica')
re.match('[0-9]', '1')   # match

# ^ excludes
print(re.match('Al[^qea-z]', 'Alex'))

# + means one or n times
template = "nicu+"
re.match(template, "nicuuuuuuuuuuuuuuu")

# * is like + just plus 0
template = "go*d"
re.match(template, "nic")

# {} is a number of repetitions
# \w is every letter big/small and number
template = "\w{4}"
re.match(template, "alex")

template = "\d{0,10}"
re.match(template, "12345")
