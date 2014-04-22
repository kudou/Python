def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return (data.strip().split(','))
    except IOError as ioerr:
        print("File error: " + str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

james = get_coach_data("james.txt")
julie = get_coach_data("julie.txt")
mikey = get_coach_data("mikey.txt")
sarah = get_coach_data("sarah.txt")

clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_sarah = [sanitize(each_t) for each_t in sarah]


print(sorted(set(clean_james))[0:3])
print(sorted(set(clean_julie))[0:3])
print(sorted(set(clean_mikey))[0:3])
print(sorted(set(clean_sarah))[0:3])

