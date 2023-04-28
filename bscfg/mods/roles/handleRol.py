# -*- coding: utf-8 -*-
import os
import json
import random
import logger
roles = logger.roles


def ver_roles():
    if os.path.exists(roles):
        with open(roles) as f:
            rol = json.loads(f.read())
            f.close()
    return rol


def commit_roles(d):
    if os.path.exists(roles):
        with open(roles) as f:
            f.write(json.dumps(d, indent=4))
            f.close()
    return


def hasBanned():
    return ver_roles()["banned"]
