# -*- coding: utf-8 -*-
import bs
import settings
import bsGame
print 'Nigth Mode: ', settings.nightMode

# ajust max players

bsGame.Session.maxPlayers = 13
bs.getConfig()['Free-for-All Max Players'] = 13


def night():
    try:
        # print 'Nigth Mode: ', settings.nightMode
        if settings.nightMode:
            bs.getSharedObject('globals').tint = (0.5, 0.7, 1.0)
    except:
        pass


def main():
    night()
