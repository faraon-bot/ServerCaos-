# -*- coding: utf-8 -*-
import bs
import settings
import bsGame


def night():
    try:
        # print 'Nigth Mode: ', settings.nightMode
        if settings.nightMode:
            bs.getSharedObject("globals").tint = (0.5, 0.7, 1.0)
    except:
        pass


def main():
    night()
