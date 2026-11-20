def trunc_name(name):
    name = name.strip().lower()
    for i, letter in enumerate(name):
        if letter in "aeiou":
            return name[i:]
    return name


def name_game(name):
    name = name.strip()
    short_name = trunc_name(name)
    first_letter = name[0].lower()
    b_sound = "" if first_letter == "b" else "b"
    f_sound = "" if first_letter == "f" else "f"
    m_sound = "" if first_letter == "m" else "m"
    
    yield f"{name}, {name}, bo-{b_sound}{short_name}"
    yield f"banana fana fo-{f_sound}{short_name}"
    yield f"me my mo-{m_sound}{short_name}"
    yield f"{name}!"


entered_name = input("Enter a name: ").strip()
while not entered_name or not all(word.isalpha() for word in entered_name.split()):
    entered_name = input("Please enter a name using letters and spaces: ").strip()

# print(trunc_name(entered_name))
for name in [entered_name, "Arash", "carly", "CHARLIE", "Aidan", "Braden", "Billy Bob"]:
    if name.lower() in ["bart", "buck", "chuck"]:
        print(f"Skipping {name} because the rhyme may be inappropriate.")
        continue
    for line in name_game(name):
        print(line)
    print()