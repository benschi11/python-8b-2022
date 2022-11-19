user_input: str = "";
ects_list: list[float] = [];

while user_input != "e":
    user_input = input("Bitte geben Sie die ECTS Punkte ein:");
    if(user_input != "e"):
        ects_list.append(user_input);


sum: float = 0;
for ects in ects_list:
    sum += float(ects);

av: float = sum / len(ects_list);

lv_count = len(ects_list);

print("Durchschnitt: " + str(av) + " | Summe: " + str(sum) + " | Anzahl LV: " + str(lv_count));


