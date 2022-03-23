from otree.api import *
import random

c = Currency

doc = """
GuessingTask_noSI
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_noSI"
    num_rounds = 2
    players_per_group = None
    num_senders = 6


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    signal_s = models.IntegerField()  # signal observed by the sender
    signal_mu = models.IntegerField()  # the simulated "true" signal observed by senders
    posterior_belief = models.IntegerField()  # the posterior belief of the receiver


# FUNCTIONS

#roles allocation and mu_signals (true) simulaion for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        if p.id_in_group in list(range(1, Constants.num_senders + 1)):
            p.Role = 'sender'
            p.signal_mu = random.randint(1, 10)
        else:
            p.Role = 'receiver'



# PAGES
class Instructions_sender(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender"


class Instructions_receiver(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver"


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
class WaitPage(WaitPage):
    pass


# the receiver observes all the signals sent by senders and makes a guess
class Guess(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        players = group.get_players()
        signals = [p.signal_s for p in players if p.Role =='sender']
        #yellow = ", ".join(str(p.signal_s) for p in players if p.Role=='sender' and p.identity=='Yellow')
        #blue = ", ".join(str(p.signal_s) for p in players if p.Role=='sender' and p.identity=='Blue')
        if player.Role == "receiver":
            return dict(
                signal_1=signals[0],
                signal_2=signals[1],
                signal_3=signals[2],
                signal_4=signals[3],
                signal_5=signals[4],
                signal_6=signals[5],
            )

    form_model = "player"
    form_fields = ["posterior_belief"]

    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver"


page_sequence = [Instructions_sender, Instructions_receiver, WaitPage, Signals, WaitPage, Guess, WaitPage]
