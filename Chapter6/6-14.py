muisc_media = [45]
print muisc_media

muisc_media.insert(0,'compact disc')

print muisc_media

muisc_media.append('long playing record')

print muisc_media

muisc_media.insert(2, '8-track-tape')

print muisc_media

print 'cassette' in muisc_media

print 'compact disc'in muisc_media

print muisc_media.index(45)

print muisc_media.index('8-track-tape')

for eachMediaType in (45,'8-track tape','cassette'):
    if(eachMediaType in muisc_media):
        print muisc_media.index(eachMediaType)
muisc_media.sort()
print muisc_media
muisc_media.reverse()
print muisc_media


new_media = ['24/96 digital audio disc', 'DVD audio disc', 'Super audio CD']
muisc_media.extend(new_media)


