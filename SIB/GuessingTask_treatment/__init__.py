from otree.api import *
import yaml
import random
import pandas as pd

c = Currency

doc = """
GuessingTask
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_SI"
    num_rounds = 2
    players_per_group = None


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    posterior_belief = models.IntegerField()  # the posterior belief of the receiver


class Player(BasePlayer):
    signal_s = models.IntegerField()  # signal observed by the sender
    signal_mu = models.IntegerField()  # the simulated "true" signal observed by senders
    Role = models.StringField()
    treatment = models.StringField() #the treatment group from the previous apps


# FUNCTIONS

#roles allocation and mu_signals (true) simulaion for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        if p.id_in_group in [1, 2, 3, 4]:
            p.Role = 'sender'
            p.signal_mu = random.randint(1, 10)
        else:
            p.Role = 'receiver'

        participant = p.participant
        p.treatment = participant.treatment




# PAGES
class Instructions(Page):
    pass


# senders see signal_mu and send signal_s
class Signals(Page):
    form_model = "player"
    form_fields = ["signal_s"]

    @staticmethod
    def is_displayed(player):
        return player.Role == "sender"

    def vars_for_template(player: Player):
        signal_mu = player.signal_mu
        return dict(
            signal_mu=signal_mu,
        )


# wait for all senders to send a signal
class MyWaitPage(WaitPage):
    pass


# the receiver observes all the signals sent by senders and makes a guess
class Guess(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        players = group.get_players()
        yellow = ", ".join(str(p.signal_s) for p in players if p.Role=='sender' and p.treatment=='Yellow')
        blue = ", ".join(str(p.signal_s) for p in players if p.Role=='sender' and p.treatment=='Blue')
        if player.Role == "receiver":
            return dict(
                yellow=yellow,
                blue=blue,
            )

    form_model = "group"
    form_fields = ["posterior_belief"]

    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver"


page_sequence = [Instructions, Signals, MyWaitPage, Guess]
