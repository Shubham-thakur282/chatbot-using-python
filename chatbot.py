from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

Jordan = ChatBot("Jordan")

chatbot = ChatBot(
    'Jordan',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

train_data_normal = open('normalchat.txt').read().splitlines()

train_data_cr = open('crime.txt').read().splitlines()

train_data_crm = open('morecrime.txt').read().splitlines()

train_data = train_data_normal + train_data_cr + train_data_crm

trainer = ListTrainer(Jordan)

trainer.train(
    "chatterbot.corpus.english",
)

trainer.train(
    "chatterbot.corpus.english.greetings",
)

trainer.train(
    "chatterbot.corpus.english.conversations"
)

trainer.train(train_data)

name = input('Enter your name:- ')
while True:
    request = input(name + ': ')
    if request == 'Ok' or request == 'ok':
        response = Jordan.get_response(request)
        print('Jordan: ', response)
        break
    else:
        response = Jordan.get_response(request)
        print('Jordan: ', response)
