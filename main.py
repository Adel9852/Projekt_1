oddelovac = "-"* 40
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
USERS =dict({
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
    })
username = input("username: ")
password = input("password: ")
print("username: ", username)
print("password: ", password, oddelovac, sep="\n")
registered = False
for user, pwd in USERS.items():
    if username == user and password == pwd:
        registered = True
        break
if not registered:
    print("Invalid login details.")
print(f"Welcome to the app, {username}")
print(f"\nWe have {len(TEXTS)} texts to be analyzed.", oddelovac, sep="\n")
choice = input(f"Enter a number from 1 to {len(TEXTS)} to select: ")
print(oddelovac, sep="\n")
choice = int(choice)
if choice < 1 or choice> len(TEXTS):
    print(f"Your number is not in the list")
    quit

text = TEXTS[choice - 1]
raw_words = text.split()

for raw in raw_words:
    cleaned = ""
    for char in raw:
        if char.isalnum():
            cleaned += char
    if cleaned:
        words.append(cleaned)

word_count = 0
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
number_count = 0
number_sum = 0

for word in words:
    word_count += 1
    if word.istitle():
        titlecase_count += 1
    elif word.isupper():
        uppercase_count += 1
    elif word.islower():
        lowercase_count += 1
    if word.isdigit():
        number_count += 1
        number_sum += int(word)

print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all the numbers {number_sum}.", oddelovac, sep="\n")

words = text.split()
word_lengths = [len(word.strip('.,!?";:()[]{}')) for word in words]
length_counts = {}

for length in word_lengths:
    if length in length_counts:
        length_counts[length] += 1
    else:
        length_counts[length] = 1

print("LEN|  OCCURENCES |  NR.", oddelovac, sep="\n")
for length, count in sorted(length_counts.items()):
    print(f"{length} | {'*' * count}| {count}")
