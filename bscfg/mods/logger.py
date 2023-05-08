# -*- coding: utf-8 -*-
import bs
import os
import json

env = bs.getEnvironment()['userScriptsDirectory']
path = os.path.join(env, 'data')
stats = os.path.join(path, 'stats.json')
pStats = os.path.join(path, 'pStats.json')
bank = os.path.join(path, 'banks.json')
customers = os.path.join(path, 'effectCustomers.json')
roles = os.path.join(path, 'roles.json')


class storage:
    customers = {}
    roles = {}


# creamos una lista con todos los archivos
myfiles = [stats, pStats, bank, roles, customers]

# creamos este diccionario vacio para poder guardar los archivos
empty = {}

# creamos el directorio
if not os.path.exists(path):
    os.mkdir(path)


def create(files):
    for file in files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                f.write(json.dumps(empty, indent=4))
                f.close()


create(myfiles)
