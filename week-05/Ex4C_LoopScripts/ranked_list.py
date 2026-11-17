cities = ["Venice", "Mexico City", "Paris", "Politano", "Lisbon"]

for index, item in enumerate(reversed(cities), start=1):
    print(f"{index}. {item}")

    if index == 1:
        print(f"<- top pick!")