import datetime
import calendar

def meetup_date(year, month):
    '''Returns the 4th wednesday of the month'''
    week_1, week_2, week_3, week_4, week_5,*rest = calendar.monthcalendar(year, month)
    
    if week_1[calendar.THURSDAY] == 0:
        return datetime.date(year, month, week_5[calendar.THURSDAY])
    else:
        return datetime.date(year, month, week_4[calendar.THURSDAY])


if __name__ == "__main__":
    print(meetup_date(2013, 5)) 
    print(meetup_date(2015, 8))

