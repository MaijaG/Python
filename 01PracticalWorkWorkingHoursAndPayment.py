# 1.1


def workingHorus () :
    ivalHours = 0
    ivalRate = 0
    workedHours = input ('Insert round worked hours: ')
    ivalHours = int(workedHours)
    rate = input ('Insert hourly rate: ')
    ivalRate = float(rate)
    print('Total salary' + str(ivalHours*ivalRate))

def workingAboveHours() :
    ivalHours =0
    ivalRate = 0
    normHours = 40
    overTimeRate = 1.75

    workedHours = input ('Insert round worked hours: ')
    ivalHours = int(workedHours)
    rate = input ('Insert hourly rate: ')
    ivalRate = float(rate)
  
    if  ivalHours > normHours :
        print('Total salary ' +  str((ivalHours - normHours)*overTimeRate*ivalRate+ normHours*ivalRate))
    else :
        print('Total salary ' + str(ivalHours*ivalRate))

def pay ()  :
    ivalHours =0
    ivalRate = 0
    normHours = 40
    overTimeRate = 1.75

    workedHours = input ('Insert round worked hours: ')
    try :
        ivalHours = int(workedHours)
    except:
        ivalHours = 0
    rate = input ('Insert hourly rate: ')
    try :
        ivalRate = float(rate)
    except:
        ivalRate = 0

    if ivalHours == 0 or ivalRate == 0 :
        print ('Error. Please enter numeric input - Round working hours and Hourly rate')
    elif  ivalHours > normHours :
        print('Total salary ' +  str((ivalHours - normHours)*overTimeRate*ivalRate+ normHours*ivalRate))
    else :
        print('Total salary ' + str(ivalHours*ivalRate))

workingHorus()
workingAboveHours()
pay()
