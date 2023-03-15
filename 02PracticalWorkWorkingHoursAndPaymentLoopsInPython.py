
normHours = 40
overTimeRate = 1.75

def insertHours() :
    ivalHours = 0
    while ivalHours == 0 :
        workedHours = input('Insert worked hours: ')
        try :
            ivalHours = int(workedHours)
        except:
            ivalHours = 0
        if ivalHours == 0 :
            print ('Error. Please enter numeric input - Round working hours and Hourly rate')    
    return ivalHours
    
def insertRate () :
    ivalRate = 0
    while ivalRate == 0 :
        hourlyRate = input('Insert hourly rate: ')
        try :
            ivalRate = float(hourlyRate)
        except:
            ivalRate = 0
        if  ivalRate == 0 :print ('Error. Please enter numeric input - Round working hours and Hourly rate')
    return ivalRate

def compute_salary(hours, rate) :
    if hours == 0 or rate == 0 :
        print ('Error. Please enter numeric input - Round working hours and Hourly rate')
    if  hours > normHours :
        print('Total salary ' +  str((hours - normHours)*overTimeRate*rate+ normHours*rate))
    else :
        print('Total salary ' + str(hours*rate))

def rombs () :
    for i in [4, 3, 2, 1, 0, 1, 2, 3, 4] :
        for e in range(0, i):
            print(' ', end = " ")
        for e in range(0,(4-i)*2+1):
            print('^', end = " ")
        print()

def astoni() :

    for i in range (1,12) :
        if i == 1 or i == 6 or i == 11 :
            for e in range(0, 2) :
                print(' ', end = " ")
            for e in range (1,8) :
                print('*', end = " ") 
        if i == 2 or i == 5 or i == 7 or i == 10 :
            for e in range(0,1) :
                print(' ', end = " ")
            for e in range (1, 10) :
                print ('*', end = " ")    
        if i == 3 or i == 4 or i == 8 or i == 9 :
            for e in range(0,4):
                print('*', end = " ")
            for e in range (4,7) :
                print(' ', end = " ") 
            for e in range (7,11) :
                print ('*', end = " ")     
            
        print()

rombs()
astoni()
ivalHours = insertHours () 
ivalRate = insertRate ()
compute_salary(ivalHours, ivalRate)