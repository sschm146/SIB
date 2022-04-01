from otree.api import *

c = Currency

doc = """
Welcome & Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'Intro_noSI_all'
    players_per_group = None
    num_rounds = 1
    num_senders = 6


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()

def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:  # Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        if p.id_in_group in list(range(1, Constants.num_senders + 1)):
            p.Role = 'sender'
        else:
            p.Role = 'receiver'

# PAGES
class Instructions_all(Page):
    pass

class Instructions_sender(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender"

class Instructions_receiver(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver"



page_sequence = [Instructions_all, Instructions_sender, Instructions_receiver]
