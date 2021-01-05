import time

Puzzle1Text = open("Puzzle1Text.txt","r")
Puzzle2Text = open("Puzzle2Text.txt","r")
Puzzle3Text = open("Puzzle3Text.txt","r")
Puzzle4Text = open("Puzzle4Text.txt","r")


def Puzzle1(a_file):
    x = []
    answer1 = 0
    answer2 = 0
    for line in a_file:
        y = line.strip()
        x.append(int(y))

    for num1 in x:
        for num2 in x:
            if num1 + num2 == 2020:
                answer1 = num1*num2
            for num3 in x:
                if num1 + num2 + num3 == 2020:
                    answer2 = num1*num2*num3
    return answer1,answer2

def Puzzle2_a(a_file):
    x = []
    for line in a_file:
        y = line.strip()
        x.append(y)

    sections = []

    count = 0

    for y in x:
        sections = y.split()

        min = 0
        max = 0

        for i in range(0,len(sections[0])):
            if sections[0][i] == '-':
                min = int(sections[0][0:i])
                max = int(sections[0][i+1:len(sections[0])]) 
        
        char = None

        for j in range(0,len(sections[1])):
            if sections[1][j] == ':':
                char = sections[1][j-1]

        subcount = 0

        for n in sections[2]:
            if n == char:
                subcount += 1
            
        if subcount <= max and subcount >= min:
            count += 1
    
    return count

def Puzzle2_b(a_file):
    x = []
    for line in a_file:
        y = line.strip()
        x.append(y)

    sections = []

    count = 0

    for y in x:
        sections = y.split()

        first = 0
        second = 0

        for i in range(0,len(sections[0])):
            if sections[0][i] == '-':
                first = int(sections[0][0:i]) -1
                second = int(sections[0][i+1:len(sections[0])]) -1
        
        char = None

        for j in range(0,len(sections[1])):
            if sections[1][j] == ':':
                char = sections[1][j-1]
            
        if (sections[2][first] == char and sections[2][second] != char) or (sections[2][first] != char and sections[2][second] == char):
            count += 1
    
    return count

def Puzzle3_a(a_file):
    x = []

    for line in a_file:
        y = line.strip()
        x.append(y)

    line_len = len(x[0])

    curr = 0

    trees = 0

    for line in x:
        if line[curr] == '#':
            trees += 1
        curr = (curr+3) % line_len
    
    return trees

def Puzzle3_b(a_file):
    x = []

    for line in a_file:
        y = line.strip()
        x.append(y)

    line_len = len(x[0])

    curr = [0,0,0,0,0]

    trees = [0,0,0,0,0]

    for j in range(0,len(x)):
        if x[j][curr[0]] == '#':
            trees[0] += 1
        curr[0] = (curr[0]+1) % line_len

        if x[j][curr[1]] == '#':
            trees[1] += 1
        curr[1] = (curr[1]+3) % line_len

        if x[j][curr[2]] == '#':
            trees[2] += 1
        curr[2] = (curr[2]+5) % line_len

        if x[j][curr[3]] == '#':
            trees[3] += 1
        curr[3] = (curr[3]+7) % line_len

        if j%2 == 0:
            if x[j][curr[4]] == '#':
                trees[4] += 1
            curr[4] = (curr[4]+1) % line_len

    result = 1

    for m in trees:
        result *= m
    
    return result

def Puzzle4_a(a_file):
    x = a_file.read().split('\n\n')
    
    x = [y.replace("\n", " ") for y in x]
    
    passports = []
    tags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for person in x:
        passports.append(dict(item.split(":") for item in person.split(" ")))
    
    count = 0

    for check in passports:
        subcount = 0
        if all(tag in check for tag in tags):

            if int(check['byr']) <= 2020 and int(check['byr']) >= 1920:
                subcount += 1

            if int(check['iyr']) <= 2020 and int(check['iyr']) >= 2010:
                subcount += 1

            if int(check['eyr']) <= 2030 and int(check['eyr']) >= 2020:
                subcount += 1

            if 'cm' in check['hgt']:
                if int(check['hgt'][:-2]) >= 150 and int(check['hgt'][:-2]) <= 193:
                    subcount += 1
                    
            elif 'in' in check['hgt']:
                if int(check['hgt'][:-2]) >= 59 and int(check['hgt'][:-2]) <= 76:
                    subcount += 1 

            if len(check['hcl']) == 7:                  
                if all(char in 'abcdef0123456789#' for char in check['hcl']):
                    subcount += 1

            req = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            c = 0
            for n in req:
                if n == check['ecl']:
                    c += 1
            if c == 1:
                subcount += 1

            if len(check['pid']) and all(char in '0123456789' for char in check['pid']):
                subcount += 1
        
            if subcount >= 7:
                count += 1

    return count



# answer1 = Puzzle1(Puzzle1Text)
# print(answer1)

# answer2_a = Puzzle2_a(Puzzle2Text)
# print(answer2_a)

# answer2_b = Puzzle2_b(Puzzle2Text)
# print(answer2_b)

# answer3_a = Puzzle3_a(Puzzle3Text)
# print(answer3_a)

# answer3_b = Puzzle3_b(Puzzle3Text)
# print(answer3_b)

answer4_a = Puzzle4_a(Puzzle4Text)
print(answer4_a)