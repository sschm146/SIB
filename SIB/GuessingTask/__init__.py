from otree.api import *
import yaml
import random

c = Currency

doc = """
GuessingTask
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask"
    players_per_group = 5
    num_rounds = 1
    SENDER1_ROLE = "sender"
    SENDER2_ROLE = "sender"
    SENDER3_ROLE = "sender"
    SENDER4_ROLE = "sender"
    RECEIVER_ROLE = "receiver"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    signals_s = models.StringField()  # all the signal which the senders see
    posterior_belief = models.IntegerField()  # the posterior belief of the receiver
    signal_mu = models.IntegerField()  # the simulated "true" signal observed by senders


class Player(BasePlayer):
    signal_s = models.IntegerField()  # signal observed by the sender


# FUNCTIONS


# collecting all signals sent by the senders in a dictionary
def signals(group: Group):
    players = group.get_players()
    ids = [p.id_in_group for p in players if p.role == "sender"]
    signal_values = [p.signal_s for p in players if p.role == "sender"]
    group.signals_s = str(dict(zip(ids, signal_values)))


# simulating the "true" signals (the same observed by all the senders)
def simulate_signal(group: Group):
    group.signal_mu = random.randint(1, 10)


# PAGES
class Instructions(Page):
    pass


# waiting for all in the group before simulating signal_mu
class MyWaitPage1(WaitPage):
    after_all_players_arrive = simulate_signal


# senders see signal_mu and send signal_s
class Signals(Page):
    form_model = "player"
    form_fields = ["signal_s"]

    @staticmethod
    def is_displayed(player):
        return player.role == "sender"

    def vars_for_template(player: Player):
        group = player.group
        signal_mu = group.signal_mu
        return dict(
            signal_mu=signal_mu,
        )


# wait for all senders to send a signal
class MyWaitPage2(WaitPage):
    after_all_players_arrive = signals


# the receiver observes all the signals sent by senders and makes a guess
class Guess(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        received_signals_s = yaml.load(group.signals_s)
        received_signals_s = ", ".join(str(s) for s in received_signals_s.values())
        if player.role == "receiver":
            return dict(
                received_signals_s=received_signals_s,
            )

    form_model = "group"
    form_fields = ["posterior_belief"]

    @staticmethod
    def is_displayed(player):
        return player.role == "receiver"


page_sequence = [Instructions, MyWaitPage1, Signals, MyWaitPage2, Guess]
