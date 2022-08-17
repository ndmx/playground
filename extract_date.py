#code to extract birth year, month or day from a birthdate
import calendar

# take second element for sort
def elem_num(elem):
    return elem[-4:]

def extractDate(birthdate):
    birthdate.sort(key=elem_num)
    year_day=""
    year_month=""
    year_year = ""
    result = ""

    for number, birthday in enumerate(birthdate):
        dates = birthday.split(".")
        for num, days in enumerate(dates):
            if num == 0:
                year_day += days
            elif num == 1:
                year_month += (days)
            elif num == 2:
                year_year += days

        i = (int(str(year_month)))
        monthname = calendar.month_name[(i)]
        if number == 0:
            abrv = "st"
        elif number == 1:
            abrv = "nd"
        elif number == 2:
            abrv = "rd"
        else:
            abrv = "th"
        result += "The {0:0>2d}{1:2s} Person has a birthday on the {2:0>2s}{3:2s} of {4:^.3s}, {5:6s}\n".format(number+1, abrv, year_day, abrv, monthname, year_year)

        year_day=""
        year_month=""
        year_year = ""
        
        #for n in [int(n) for n in str(dates)]:
        # print(n)   
    return result
    
highest_paid_actors_birthdate = ["25.9.1968","6.4.1969","13.6.1981","9.9.1966","5.1.1975","7.4.1954","9.9.1967","4.4.1965","11.8.1983","2.5.1972"]
print(extractDate(highest_paid_actors_birthdate))