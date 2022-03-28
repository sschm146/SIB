from otree.api import *
import numpy as np
import random

c = Currency

doc = """
GuessingTask_noSI
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_noSI_CB"
    num_rounds = 4
    players_per_group = None
    num_senders = 6
    true_state = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sd = 3
    payoff_guess = 1


class Subsession(BaseSubsession):
    x = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    sent_signal = models.IntegerField()  # signal sent by the sender
    estimate = models.IntegerField()  # the estimate sent by the estimation device which is observed by senders
    posterior = models.IntegerField()  # the posterior belief of the receiver
    prior = models.IntegerField()
    true_state = models.IntegerField()
    received_signal_1 = models.IntegerField()
    received_signal_2 = models.IntegerField()
    received_signal_3 = models.IntegerField()
    received_signal_4 = models.IntegerField()
    received_signal_5 = models.IntegerField()
    received_signal_6 = models.IntegerField()

# FUNCTIONS

#roles allocation and mu_signals (true) simulaion for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    subsession.x = random.randint(0, 100)
    estimates = np.random.normal(Constants.true_state[subsession.round_number - 1], Constants.sd, 10)
    estimates = np.rint(estimates)
    for p in players: #Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        p.estimate = estimates[p.id_in_group - 1]
        if p.id_in_group in list(range(1, Constants.num_senders + 1)):
            p.Role = 'sender'
        else:
            p.Role = 'receiver'
        if p.round_number <= Constants.num_rounds / 2:
            p.true_state = Constants.true_state[subsession.round_number - 1]
        else:
            p.true_state = Constants.true_state[int(subsession.round_number - Constants.num_rounds / 2) - 1]



# PAGES
class Instructions_sender(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1


class Instructions_receiver(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number == 1


# senders see estimate and send signal
class Signals(Page):
    form_model = "player"
    form_fields = ["sent_signal"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((Constants.true_state[int(player.round_number) - 1] - player.sent_signal), 2)
        if diff <= player.subsession.x:
            player.payoff = Constants.payoff_guess
        else:
            player.payoff = 0

    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number <= Constants.num_rounds/2

    def vars_for_template(player: Player):
        estimate = player.estimate
        return dict(
            estimate=estimate,
        )


class Prior(Page):

    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number == 1

    def vars_for_template(player: Player):
        estimate = player.estimate
        return dict(
            estimate=estimate,
        )

    form_model = "player"
    form_fields = ["prior"]



# wait for all senders to send a signal
class FirstWaitPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class SecondWaitPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds/2 or player.round_number == Constants.num_rounds


# the receiver observes all the signals sent by senders and states a guess/posterior
# Receivers see signals sent by senders in a random order and with known group identity
class Guess(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((Constants.true_state[int(player.round_number - Constants.num_rounds / 2) - 1] - player.posterior), 2)
        if diff <= player.subsession.x:
            player.payoff = Constants.payoff_guess
        else:
            player.payoff = 0


    @staticmethod
    def vars_for_template(player: Player):
        current_round = player.round_number
        prev_player = player.in_round(current_round - Constants.num_rounds/2)
        prev_players = prev_player.group.get_players()
        signals = [p.sent_signal for p in prev_players if p.Role =='sender']
        if player.Role == "receiver":   # Gathering all signals and the resp. sender's identities for analyses -
                                        # this part works but can be improved with a loop or something
            player.received_signal_1 = signals[0]
            player.received_signal_2 = signals[1]
            player.received_signal_3 = signals[2]
            player.received_signal_4 = signals[3]
            player.received_signal_5 = signals[4]
            player.received_signal_6 = signals[5]
            return dict(
                signal_1=signals[0],
                signal_2=signals[1],
                signal_3=signals[2],
                signal_4=signals[3],
                signal_5=signals[4],
                signal_6=signals[5],
            )

    form_model = "player"
    form_fields = ["posterior"]

    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number > Constants.num_rounds/2


class Payout_calc(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'payout_calc'

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


def payout_calc(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        if p.Role == "sender":
            i = random.randint(1, int(Constants.num_rounds / 2))
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff
        if p.Role == "receiver":
            i = random.randint(int(Constants.num_rounds / 2) + 1, Constants.num_rounds)
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff

page_sequence = [Instructions_sender, Instructions_receiver, FirstWaitPage,Prior, Signals, Guess, SecondWaitPage, Payout_calc]
