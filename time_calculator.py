def add_time(start, end, dow=None):
    elems = start.split(' ')
    elem = elems[0].split(':')
    dur = end.split(':')

    minutes = int(elem[1]) + int(dur [1])
    hours = int(elem[0]) + int(dur[0]) + minutes // 60

    minute = minutes if minutes >= 10 and minutes <= 59 else "0" + str(minutes % 60)
    nd_hours = hours if elems[1] == "AM" else hours + 12
    nd = nd_hours // 24

    if hours >= 12:
        hour = hours % 12
        hour = hour if hour != 0 else 12
        if elems[1] == "PM":
            meridiem = "AM"
        else:
            meridiem = "PM"
    else:
        hour = hours
        meridiem = elems[1]

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    if dow and nd == 0:
        print(f'{hour}:{minute} {meridiem}, {dow}')
    elif dow and nd == 1:
        for x, y in enumerate(days):
            if y.lower() == dow.lower():
                print(f'{hour}:{minute} {meridiem}, {days[(x + nd) % 7]} (next day)')
    elif dow and nd >= 2:
        for x, y in enumerate(days):
            if y.lower() == dow.lower():
                print(f'{hour}:{minute} {meridiem}, {days[(x + nd) % 7]} ({nd} days later)')
    elif nd == 1: print(f'{hour}:{minute} {meridiem} (next day)')
    elif nd >= 2: print(f'{hour}:{minute} {meridiem} ({nd} days later)')
    else: print(f'{hour}:{minute} {meridiem}')

def main():
    add_time("3:00 PM", "3:10")
    # Returns: 6:10 PM
    add_time("11:30 AM", "2:32", "Monday")
    # # Returns: 2:02 PM, Monday
    add_time("11:43 AM", "00:20")
    # # Returns: 12:03 PM
    add_time("10:10 PM", "3:30")
    # # Returns: 1:40 AM (next day)
    add_time("11:43 PM", "24:20", "tueSday")
    # # Returns: 12:03 AM, Thursday (2 days later)

if __name__ == '__main__':
    main()
