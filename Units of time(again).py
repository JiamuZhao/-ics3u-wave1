def time_calculation(t):
    days = t // 86400
    t = t % 86400
    hours = t // 3600
    t = t % 3600
    minutes = t // 60
    t = t % 60
    second = t
    print(f'{days}:{"%02d" % hours}:{"%02d" % minutes}:{"%02d" % second}')


seconds = int(input('Please enter the total time in second >'))
time_calculation(seconds)