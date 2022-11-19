
numbers:list = list(range(10000,100000)); #geniere alle möglichen Zahlen

numbers_copy = numbers.copy(); # deep copy - alle Daten werden kopiert

a:int = 1234;

number:int;
for number in numbers:

    if "5" in str(number):
        numbers_copy.remove(number);
        continue;
    
    if "3" not in str(number) or "6" not in str(number):
        numbers_copy.remove(number);
        continue;

    if int(str(number)[0]) % 2 == 0:
        numbers_copy.remove(number);
        continue;
    
    descend = 0; 
    for i in range(0,len(str(number))-1):
        if int(str(number)[i]) > int(str(number)[i+1]):
            descend += 1;
    if descend > 1:
        numbers_copy.remove(number);
        continue;

print(len(numbers_copy)*3/120);
