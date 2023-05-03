# -*- coding: utf-8 -*-
import bs
import settings
print 'Nigth Mode: ', settings.nightMode

config = bs.getConfig()
config['Coop Game Max Players'] = 999
config['Team Game Max Players'] = 999
config['Free-for-All Max Players'] = 999
bs.writeConfig()

def night():
    try:
        # print 'Nigth Mode: ', settings.nightMode
        if settings.nightMode:
            bs.getSharedObject('globals').tint = (0.5, 0.7, 1.0)
    except:
        pass


def main():
    night()
