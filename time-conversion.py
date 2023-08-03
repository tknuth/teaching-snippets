time = "6:75"

def to_minutes(time):
    h, m = time.split(":")
    return 60 * int(h) + int(m)

def to_hh_mm(minutes):
    h = minutes // 60
    m = minutes % 60
    return "{}:{:02d}".format(h, m)

to_hh_mm(to_minutes(time))
