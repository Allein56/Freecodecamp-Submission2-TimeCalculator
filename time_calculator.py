def add_time(start, duration, day_start=None):
    time_start = start
    dur = duration
    try:
        day = day_start.capitalize()
    except AttributeError:
        day = day_start

    # Turning duration to minutes
    if ':' in dur:
        minutes_dur_str = dur.split(':')
        minutes_dur = int(minutes_dur_str[0]) * 60 + int(minutes_dur_str[1])
    else:
        minutes_dur = int(dur)

    # Breaking down time start into its elements
    colon_pos = time_start.find(':')
    if 'PM' in time_start:
        time_format = time_start.find('PM')
    elif 'AM' in time_start:
        time_format = time_start.find('AM')
    else:
        return 'Error: Time Format must be in AM/PM'

    hour = int(time_start[0:colon_pos])
    minutes = int(time_start[colon_pos + 1:time_format - 1])
    _format = time_start[time_format:len(time_start)]

    # Creating Time Calculator
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    total_days = 0
    while minutes_dur > 0:
        if hour == 11 and minutes == 59:
            # Changing days
            if _format == 'PM':
                minutes_dur -= 1
                hour += 1
                minutes = 0
                _format = 'AM'
                total_days += 1
            # Changing to PM after midday
            elif _format == 'AM':
                minutes_dur -= 1
                hour += 1
                minutes = 0
                _format = 'PM'
        # Formating from 12:59 to 01:00
        elif hour == 12 and minutes == 59:
            minutes_dur -= 1
            hour = 1
            minutes = 0
        elif minutes == 59:
            minutes_dur -= 1
            hour += 1
            minutes = 0
        else:
            minutes_dur -= 1
            minutes += 1

    # Determining the day at the end of the time period
    day_remaining = total_days % 7
    if day is not None:
        day_index = days.index(day)
        while day_remaining > 0:
            if day == 'Sunday':
                day_index = 0
                day = days[day_index]
                day_remaining -= 1
            else:
                day_index += 1
                day = days[day_index]
                day_remaining -= 1
    else:
        pass

    # Formating the output
    if hour == 0:
        hour = str(hour).zfill(2)
    minutes = str(minutes).zfill(2)
    if day is not None:
        if total_days == 0:
            new_time = '{}:{} {}, {}'.format(hour, minutes, _format, day)
        elif total_days == 1:
            new_time = '{}:{} {}, {} (next day)'.format(hour, minutes, _format, day)
        else:
            new_time = '{}:{} {}, {} ({} days later)'.format(hour, minutes, _format, day, total_days)
    else:
        if total_days == 0:
            new_time = '{}:{} {}'.format(hour, minutes, _format)
        elif total_days == 1:
            new_time = '{}:{} {} (next day)'.format(hour, minutes, _format)
        else:
            new_time = '{}:{} {} ({} days later)'.format(hour, minutes, _format, total_days)

    return new_time
