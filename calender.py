class calender:
    def __init__(self, mon,day, yr):
        self.mon = mon
        self.day = day
        self.yr = yr
    def setday(self,day):
        self.day=day
    #Set month
    def setmonth(self,mon):
        self.mon=mon
    #Set year
    def setyear(self,yr):
        self.yr=yr
    #Get day
    def retday(self):
        return self.day
    #***Get month
    def retmonth(self):
        return self.mon
    #***Get year
    def retyear(self):
        return self.yr

    def isleapyr(self, yr):
        leapyear = (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0)
        if leapyear == 0:
            return False
        else:
            return True
    def daysinmonth(self, mon,yr):
        if mon == 4 or mon == 6 or mon == 9 or mon == 11:
            days = 30
        elif mon==2:
            if self.isleapyr(self.yr)== False:
            #leapyear = (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0)
            #if leapyear == 0:
                days = 28
                print("not a leap year")
            else:
                days = 29
                print("leap year")
        else:
            days = 31
        return days
    #adddays
    def adddate(self,adddays,months):
        self.month=[1,3,5,7,8,10,12]
        adddays=self.retday()+adddays
        self.totaldays=self.daysinmonth(self.retmonth(),self.retyear())
        print(self.totaldays)
        if self.totaldays>=adddays:
            self.setday(adddays)
        else:
            adddays=adddays-self.totaldays
            self.setmonth(months[months.index(self.retmonth())+1])
            self.setday(adddays)
         # subtract days
    def subdate(self,subdays,months):
        subdays=self.retday()-subdays
        if subdays <= 0:
            self.setmonth(months[months.index(self.retmonth())-1])
            self.totaldays=self.daysinmonth(self.retmonth(),self.retyear)
            subdays=self.totaldays+subdays
            self.setday(subdays)
        else:
            self.setday(subdays)
    def displaydate(self):
        print("Date :",self.retday(),"-",self.retmonth(),"-",self.retyear())
if __name__ == "__main__":
    month=[1,2,3,4,5,6,7,8,9,10,11,12]
    c1 = calender(2,26,2020)
    print("number of days in month")
    print(c1.daysinmonth(2,2020))
    #print(c1.isleapyr(2020))
    c1.adddate(4,month)
    c1.displaydate()
    c1.subdate(2,month)
    c1.displaydate()
    
 #P.S. I don't know why this code prints 'leap year' after every statement in output
