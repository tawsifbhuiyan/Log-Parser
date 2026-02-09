from datetime import datetime, timedelta
import calendar



def find_lines_with_query(file_path, query_string):
    matched_lines = []

    with open(file_path, 'r', errors='ignore') as file:
        for line in file:
            if query_string in line:
                matched_lines.append(line.strip())

    
    print("\nMATCHED LINES:")
    for line in matched_lines:
        print(line)

    return matched_lines



def extract_datetime_strings(lines_list):
    datetime_strings = [line[:23] for line in lines_list]

    
    print("\nEXTRACTED DATE-TIME STRINGS:")
    for dt in datetime_strings:
        print(dt)

    return datetime_strings



def convert_to_datetime_objects(datetime_strings):
    
    return [
        datetime.strptime(dt, "%Y-%m-%d %H:%M:%S.%f")
        for dt in datetime_strings
    ]


#Just for demonstration!
def add_years(datetime_objects, years_to_add):
    
    result = []

    for dt in datetime_objects:
        try:
            new_dt = dt.replace(year=dt.year + years_to_add)
        except ValueError:
            # Leap year safety(Feb 29 to Feb 28)
            new_dt = dt.replace(month=2, day=28, year=dt.year + years_to_add)

        result.append(new_dt)

    return result



def add_months(datetime_objects, months_to_add):
    result = []
    for dt in datetime_objects:
        month = dt.month - 1 + months_to_add
        year = dt.year + month // 12
        month = month % 12 + 1
        # I am Making sure the day is valid for the new month
        day = min(dt.day, calendar.monthrange(year, month)[1])
        new_dt = dt.replace(year=year, month=month, day=day)
        result.append(new_dt)
    return result


def add_days(datetime_objects, days_to_add):
    result = []
    for dt in datetime_objects:
        new_dt = dt + timedelta(days=days_to_add)
        result.append(new_dt)
    return result


def add_hours(datetime_objects, hours_to_add):
    result = []
    for dt in datetime_objects:
        new_dt = dt + timedelta(hours=hours_to_add)
        result.append(new_dt)
    return result


def add_minutes(datetime_objects, minutes_to_add):
    result = []
    for dt in datetime_objects:
        new_dt = dt + timedelta(minutes=minutes_to_add)
        result.append(new_dt)
    return result



def main():
    log_file = "sample_log.txt"
    query = "App Close Requested"

    
    lines = find_lines_with_query(log_file, query)

    
    dt_strings = extract_datetime_strings(lines)

    
    dt_objects = convert_to_datetime_objects(dt_strings)

    print("\nDATETIME OBJECTS (AFTER CONVERSION):")
    # for dt in dt_objects:
    #     print(dt)  #to print with last zeroes
    for dt in dt_objects:
     print(dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])  #to print without last zeroes
    
    # (Just for demonstration!)
    dt_after_200_years = add_years(dt_objects, 200)
    dt_after_3_months = add_months(dt_objects, 3)
    dt_after_10_days = add_days(dt_objects, 10)
    dt_after_5_hours = add_hours(dt_objects, 5)
    dt_after_30_minutes = add_minutes(dt_objects, 30)

    print("\nDATETIME OBJECTS (AFTER +200 YEARS):")
    for dt in dt_after_200_years:
        #print(dt)
        print(dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

    print("\nDATETIME OBJECTS (AFTER +3 MONTHS):")
    for dt in dt_after_3_months:
       # print(dt)
       print(dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

    print("\nDATETIME OBJECTS (AFTER +10 DAYS):")
    for dt in dt_after_10_days:
        #print(dt)
        print(dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

    print("\nDATETIME OBJECTS (AFTER +5 HOURS):")
    for dt in dt_after_5_hours:
        #print(dt)
        print(dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

    print("\nDATETIME OBJECTS (AFTER +30 MINUTES):")
    for dt in dt_after_30_minutes:
       #print(dt)
       print(dt.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


if __name__ == "__main__":
    main()