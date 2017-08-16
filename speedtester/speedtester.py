import datetime
import speedtest

# Formatting function
# taken from https://github.com/jputman-testing/python-speedtest-with-tweet-functionality
def FormatSpeed(speed):
    units = ['bps', 'Kbps', 'Mbps', 'Gbps']
    unit = 0
    while speed >= 1024:
        speed /= 1024
        unit += 1
    return '%0.3f %s' % (speed, units[unit])

print('Running speed test . . .')
time = datetime.datetime.now()
speed = speedtest.Speedtest()
speed.get_best_server()
speed.download()
speed.upload()

formattedDown = FormatSpeed(speed.results.download)
formattedUp = FormatSpeed(speed.results.upload)

print('Download: %s\nUpload: %s\nPing: %0.0f' % (formattedDown, formattedUp, speed.results.ping))

print('Outputting results to log . . .')
file = open("speed-log.csv", "a+")
file.write('%s,%0.0f,%s,%s\n' % (time, speed.results.ping, speed.results.download, speed.results.upload))
file.close()

print('Done!')