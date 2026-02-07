
td = int(input('enter a digit: '))

match td:
    case 0 :
        print('this is a zero')
    case n if n>0:
        print('this number is positive')
    case n if n<0:
        print('this number is negative')
    case _ :
        print('invalid input')
        


''' 
Exercise 2: Day of the Week

Input a number 1–7:

1 → Monday

2 → Tuesday
…

7 → Sunday
Anything else → "Invalid day"

'''
day_no = int(input('enter a number from 1-7 to know what day of the week it is: '))

match day_no:
    case n if n == 1:
        print('monday')
    case n if n == 2:
        print('tuesday')
    case n if n == 3:
        print('wednesday')
    case n if n == 4:
        print('thursday')
    case n if n == 5:
        print('friday')
    case n if n == 6:
        print('saturday')
    case n if n == 7:
        print('sunday')
    case_:
        print('digit not in range 1-7')
        
        
        
'''
LEVEL 2 — Ranges & Guards
Exercise 3: Grading System

Input a score 0–100:

90–100 → A

80–89 → B

70–79 → C

60–69 → D

0–59 → F

Anything else → "Invalid score"'''


grade = int(input('enter thescore to determine the grade: '))

match grade:
    case n if n>89:
        print('A')
    case n if n>79 and n<90:
        print('B')
    case n if n>69 and n<80:
        print('C')
    case n if n>59 and n<70:
        print('D')
    case n if n<60:
        print('F')
    case _: 
        print('the score {grade} is not in range of 0-100')
        
        
       
'''
Exercise 4: Temperature Status

Input temperature in °C:

< 0 → "Freezing"

0–15 → "Cold"

16–25 → "Warm"

> 25 → "Hot"
'''

temp = int(input('enter the temperature: '))

match temp:
    case n if n == 0:
        print('freezing')
    case n if n in range(0,15):
        print('cold')
    case n if n in range(16,25):
        print('warm')
    case n if n >25:
        print('hot')
    case _:
        print('invalid input')



'''
LEVEL 3 — Multiple Values in One Case
Exercise 5: Vowel or Consonant

Input a single letter:

Vowel → "vowel"

Consonant → "consonant"

Anything else → "invalid input"

💡 Hint:

case 'a' | 'e' | 'i' | 'o' | 'u':

'''

test_letter= input('enter a letter to test whether it is a vowel or a consonant: ')
test_letter.strip()

match test_letter:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print('vowel')
    case 'b'|'c'|'d'|'y'|'f'|'x'|'j'|'k'|'l'|'m'|'n'|'w'|'p'|'q'|'r'|'s'|'t'|'v'| 'z':
        print("consonant")
    case _:

        print('invalid')
