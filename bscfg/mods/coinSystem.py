import settings
import bs
import bsUI
import os
import bsInternal
import json
from threading import Timer
from random import randrange
from datetime import datetime
from settings import *
import logger
correctAnswer = None
answeredBy = None
bankfile = logger.bank
customer = logger.customers


def _customer():
    if os.path.exists(customer):
        with open(customer) as f:
            custom = json.loads(f.read())
            return custom
    else:
        return


def commit_custom(e):
    if os.path.exists(customer):
        with open(customer, 'w') as f:
            f.write(json.dumps(e, indent=4))
            f.close()


def checkExpiredItems():
    customers = _customer()
    flag = 0
    for i in bsInternal._getForegroundHostActivity().players:
        accountID = i.get_account_id()
        custom = customers[accountID]
        if (accountID is None) and (not accountID in customers):
            pass

        for k, v in custom["effects"].items():
            now = datetime.now()
            expiry = datetime.strptime(v, '%d-%m-%Y %H:%M:%S')
            if expiry < now:
                print 'expired item found'
                flag = 1
                customers.pop(k)
                break
    if flag == 1:
        commit_custom(customers)


def askQuestion():
    global answeredBy
    global correctAnswer
    keys = []
    for x in questionsList:
        keys.append(x)

    question = keys[randrange(len(keys))]
    correctAnswer = questionsList[question]
    if question == 'add':
        a = randrange(100, 999)
        b = randrange(10, 99)
        correctAnswer = str(a + b)
        question = 'What is ' + str(a) + ' + ' + str(b) + '?'
    elif question == 'multiply':
        a = randrange(100, 999)
        availableB = [0, 1, 10, 5]
        b = availableB[randrange(4)]
        correctAnswer = str(a * b)
        question = 'What is ' + str(a) + ' x ' + str(b) + '?'
    bsInternal._chatMessage(question)
    answeredBy = None
    checkExpiredItems()
    return


def checkAnswer(msg, clientID):
    global answeredBy
    if True:  # msg.lower() == correctAnswer:
        if answeredBy is not None:
            bsInternal._chatMessage('Already awarded to ' + answeredBy)
        else:
            for i in bsInternal._getForegroundHostActivity().players:
                if i.getInputDevice().getClientID() == clientID:
                    answeredBy = i.getName()
                    accountID = i.get_account_id()
                    bs.screenMessage(answeredBy + ': ' + msg,
                                     color=(0, 0.6, 0.2), transient=True)
            try:
                bsInternal._chatMessage(
                    'Congratulations ' + answeredBy + '! You won ' + bs.getSpecialChar('ticket') + '10.')
                addCoins(accountID, 10)
            except:
                pass

    '''else:
        bs.screenMessage('Wrong', color=(1, 0, 0), transient=True, clients=[clientID])'''
    return


def addCoins(accountID, amount):
    if os.path.exists(bankfile):
        with open(bankfile) as f:
            bank = json.loads(f.read())
    else:
        bank = {}
    if accountID not in bank:
        bank[accountID] = 0
    bank[accountID] += amount
    with open(bankfile, 'w') as f:
        f.write(json.dumps(bank))
    if amount > 0:
        bs.playSound(bs.getSound('cashRegister'))
    print 'Transaction successful'


def getCoins(accountID):
    if os.path.exists(bankfile):
        with open(bankfile, 'r') as f:
            coins = json.loads(f.read())
            if accountID in coins:
                return coins[accountID]
    return 0


if settings.enableCoinSystem:
    timer = bs.Timer(questionDelay * 1000, askQuestion,
                     timeType='real', repeat=True)
    print 'Coin system loaded...'
