import datetime
import pyspeedtest

# Formatting function
# taken from https://github.com/jputman-testing/python-speedtest-with-tweet-functionality
def FormatSpeed(speed):
    units = ['bps', 'Kbps', 'Mbps', 'Gbps']
    unit = 0
    while speed >= 1024:
        speed /= 1024
        unit += 1
    return '%0.3f %s' % (speed, units[unit])

print('starting speed test\n')
speed = pyspeedtest.SpeedTest()
print('running ping test . . .')
ping = speed.ping()
print('running download test . . .')
download = speed.download()
print('running upload test . . .')
upload = speed.upload()

formattedDown = FormatSpeed(download)
formattedUp = FormatSpeed(upload)

print('\nDownload: %s\nUpload: %s\nPing: %0.0f\n' % (formattedDown, formattedUp, ping))

print('Outputting results to log . . .\n')
file = open("speed-log.csv", "a+")
file.write('%s,%0.0f,%s,%s\n' % (datetime.datetime.now(), ping, download, upload))
file.close()

print('Done!')