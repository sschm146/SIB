from pickle import FALSE
from otree.api import *
import numpy as np
import random

c = Currency

doc = """
GuessingTask_noSI
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_noSI_CN"
    num_rounds = 4
    players_per_group = None
    num_senders = 6
    true_state = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sd = 100
    payoff_guess = 1
    isRandom = True


class Subsession(BaseSubsession):
    x = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    sent_signal = models.IntegerField()  # signal sent by the sender
    estimate = models.IntegerField()  # the estimate sent by the estimation device which is observed by senders
    posterior = models.IntegerField()  # the posterior belief of the receiver
    true_state = models.IntegerField()
    received_signal_1 = models.IntegerField()
    received_signal_2 = models.IntegerField()
    received_signal_3 = models.IntegerField()
    received_signal_4 = models.IntegerField()
    received_signal_5 = models.IntegerField()
    received_signal_6 = models.IntegerField()
    trust_sender_1 = models.IntegerField(min=0, max=10)
    trust_sender_2 = models.IntegerField(min=0, max=10)
    trust_sender_3 = models.IntegerField(min=0, max=10)
    trust_sender_4 = models.IntegerField(min=0, max=10)
    trust_sender_5 = models.IntegerField(min=0, max=10)
    trust_sender_6 = models.IntegerField(min=0, max=10)
    trust_sender_1_conf = models.IntegerField()
    trust_sender_2_conf = models.IntegerField()
    trust_sender_3_conf = models.IntegerField()
    trust_sender_4_conf = models.IntegerField()
    trust_sender_5_conf = models.IntegerField()
    trust_sender_6_conf = models.IntegerField()
    sender_1_correction_1_inround = models.IntegerField(blank=True)
    sender_1_correction_2_inround = models.IntegerField(blank=True)
    sender_1_correction_3_inround = models.IntegerField(blank=True)
    sender_1_correction_4_inround = models.IntegerField(blank=True)
    sender_1_correction_5_inround = models.IntegerField(blank=True)
    sender_1_correction_6_inround = models.IntegerField(blank=True)
    sender_1_correction_7_inround = models.IntegerField(blank=True)
    sender_1_correction_8_inround = models.IntegerField(blank=True)
    sender_1_correction_9_inround = models.IntegerField(blank=True)
    sender_1_correction_10_inround = models.IntegerField(blank=True)
    sender_1_correction_1_actually = models.IntegerField(blank=True)
    sender_1_correction_2_actually = models.IntegerField(blank=True)
    sender_1_correction_3_actually = models.IntegerField(blank=True)
    sender_1_correction_4_actually = models.IntegerField(blank=True)
    sender_1_correction_5_actually = models.IntegerField(blank=True)
    sender_1_correction_6_actually = models.IntegerField(blank=True)
    sender_1_correction_7_actually = models.IntegerField(blank=True)
    sender_1_correction_8_actually = models.IntegerField(blank=True)
    sender_1_correction_9_actually = models.IntegerField(blank=True)
    sender_1_correction_10_actually = models.IntegerField(blank=True)
    sender_2_correction_1_inround = models.IntegerField(blank=True)
    sender_2_correction_2_inround = models.IntegerField(blank=True)
    sender_2_correction_3_inround = models.IntegerField(blank=True)
    sender_2_correction_4_inround = models.IntegerField(blank=True)
    sender_2_correction_5_inround = models.IntegerField(blank=True)
    sender_2_correction_6_inround = models.IntegerField(blank=True)
    sender_2_correction_7_inround = models.IntegerField(blank=True)
    sender_2_correction_8_inround = models.IntegerField(blank=True)
    sender_2_correction_9_inround = models.IntegerField(blank=True)
    sender_2_correction_10_inround = models.IntegerField(blank=True)
    sender_2_correction_1_actually = models.IntegerField(blank=True)
    sender_2_correction_2_actually = models.IntegerField(blank=True)
    sender_2_correction_3_actually = models.IntegerField(blank=True)
    sender_2_correction_4_actually = models.IntegerField(blank=True)
    sender_2_correction_5_actually = models.IntegerField(blank=True)
    sender_2_correction_6_actually = models.IntegerField(blank=True)
    sender_2_correction_7_actually = models.IntegerField(blank=True)
    sender_2_correction_8_actually = models.IntegerField(blank=True)
    sender_2_correction_9_actually = models.IntegerField(blank=True)
    sender_2_correction_10_actually = models.IntegerField(blank=True)
    sender_3_correction_1_inround = models.IntegerField(blank=True)
    sender_3_correction_2_inround = models.IntegerField(blank=True)
    sender_3_correction_3_inround = models.IntegerField(blank=True)
    sender_3_correction_4_inround = models.IntegerField(blank=True)
    sender_3_correction_5_inround = models.IntegerField(blank=True)
    sender_3_correction_6_inround = models.IntegerField(blank=True)
    sender_3_correction_7_inround = models.IntegerField(blank=True)
    sender_3_correction_8_inround = models.IntegerField(blank=True)
    sender_3_correction_9_inround = models.IntegerField(blank=True)
    sender_3_correction_10_inround = models.IntegerField(blank=True)
    sender_3_correction_1_actually = models.IntegerField(blank=True)
    sender_3_correction_2_actually = models.IntegerField(blank=True)
    sender_3_correction_3_actually = models.IntegerField(blank=True)
    sender_3_correction_4_actually = models.IntegerField(blank=True)
    sender_3_correction_5_actually = models.IntegerField(blank=True)
    sender_3_correction_6_actually = models.IntegerField(blank=True)
    sender_3_correction_7_actually = models.IntegerField(blank=True)
    sender_3_correction_8_actually = models.IntegerField(blank=True)
    sender_3_correction_9_actually = models.IntegerField(blank=True)
    sender_3_correction_10_actually = models.IntegerField(blank=True)
    sender_4_correction_1_inround = models.IntegerField(blank=True)
    sender_4_correction_2_inround = models.IntegerField(blank=True)
    sender_4_correction_3_inround = models.IntegerField(blank=True)
    sender_4_correction_4_inround = models.IntegerField(blank=True)
    sender_4_correction_5_inround = models.IntegerField(blank=True)
    sender_4_correction_6_inround = models.IntegerField(blank=True)
    sender_4_correction_7_inround = models.IntegerField(blank=True)
    sender_4_correction_8_inround = models.IntegerField(blank=True)
    sender_4_correction_9_inround = models.IntegerField(blank=True)
    sender_4_correction_10_inround = models.IntegerField(blank=True)
    sender_4_correction_1_actually = models.IntegerField(blank=True)
    sender_4_correction_2_actually = models.IntegerField(blank=True)
    sender_4_correction_3_actually = models.IntegerField(blank=True)
    sender_4_correction_4_actually = models.IntegerField(blank=True)
    sender_4_correction_5_actually = models.IntegerField(blank=True)
    sender_4_correction_6_actually = models.IntegerField(blank=True)
    sender_4_correction_7_actually = models.IntegerField(blank=True)
    sender_4_correction_8_actually = models.IntegerField(blank=True)
    sender_4_correction_9_actually = models.IntegerField(blank=True)
    sender_4_correction_10_actually = models.IntegerField(blank=True)
    sender_5_correction_1_inround = models.IntegerField(blank=True)
    sender_5_correction_2_inround = models.IntegerField(blank=True)
    sender_5_correction_3_inround = models.IntegerField(blank=True)
    sender_5_correction_4_inround = models.IntegerField(blank=True)
    sender_5_correction_5_inround = models.IntegerField(blank=True)
    sender_5_correction_6_inround = models.IntegerField(blank=True)
    sender_5_correction_7_inround = models.IntegerField(blank=True)
    sender_5_correction_8_inround = models.IntegerField(blank=True)
    sender_5_correction_9_inround = models.IntegerField(blank=True)
    sender_5_correction_10_inround = models.IntegerField(blank=True)
    sender_5_correction_1_actually = models.IntegerField(blank=True)
    sender_5_correction_2_actually = models.IntegerField(blank=True)
    sender_5_correction_3_actually = models.IntegerField(blank=True)
    sender_5_correction_4_actually = models.IntegerField(blank=True)
    sender_5_correction_5_actually = models.IntegerField(blank=True)
    sender_5_correction_6_actually = models.IntegerField(blank=True)
    sender_5_correction_7_actually = models.IntegerField(blank=True)
    sender_5_correction_8_actually = models.IntegerField(blank=True)
    sender_5_correction_9_actually = models.IntegerField(blank=True)
    sender_5_correction_10_actually = models.IntegerField(blank=True)
    sender_6_correction_1_inround = models.IntegerField(blank=True)
    sender_6_correction_2_inround = models.IntegerField(blank=True)
    sender_6_correction_3_inround = models.IntegerField(blank=True)
    sender_6_correction_4_inround = models.IntegerField(blank=True)
    sender_6_correction_5_inround = models.IntegerField(blank=True)
    sender_6_correction_6_inround = models.IntegerField(blank=True)
    sender_6_correction_7_inround = models.IntegerField(blank=True)
    sender_6_correction_8_inround = models.IntegerField(blank=True)
    sender_6_correction_9_inround = models.IntegerField(blank=True)
    sender_6_correction_10_inround = models.IntegerField(blank=True)
    sender_6_correction_1_actually = models.IntegerField(blank=True)
    sender_6_correction_2_actually = models.IntegerField(blank=True)
    sender_6_correction_3_actually = models.IntegerField(blank=True)
    sender_6_correction_4_actually = models.IntegerField(blank=True)
    sender_6_correction_5_actually = models.IntegerField(blank=True)
    sender_6_correction_6_actually = models.IntegerField(blank=True)
    sender_6_correction_7_actually = models.IntegerField(blank=True)
    sender_6_correction_8_actually = models.IntegerField(blank=True)
    sender_6_correction_9_actually = models.IntegerField(blank=True)
    sender_6_correction_10_actually = models.IntegerField(blank=True)


# FUNCTIONS

#roles allocation and mu_signals (true) simulaion for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    subsession.x = random.randint(0, 100)
    estimates = np.random.normal(Constants.true_state[subsession.round_number - 1], Constants.sd, 6)
    estimates = np.rint(estimates)
    receiverCount = 0
    for p in players: #Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        if p.id_in_group in list(range(1, Constants.num_senders + 1)):
            p.Role = 'sender'
            p.estimate = estimates[p.id_in_group-1]
        else:
            p.Role = 'receiver'
            receiverCount = receiverCount + 1
        if p.round_number <= Constants.num_rounds / 2:
            p.true_state = Constants.true_state[subsession.round_number - 1]
        else:
            p.true_state = Constants.true_state[int(subsession.round_number - Constants.num_rounds / 2) - 1]

    if(Constants.isRandom):
        playersTmp = subsession.get_players()
        randomOriginal = random.randint(0, len(players) - (receiverCount + 1))
        randomInt = random.randint(0, len(players) - (receiverCount + 1))  
        while(randomOriginal == randomInt):
            randomOriginal = random.randint(0, len(players) - (receiverCount + 1))
            randomInt = random.randint(0, len(players) - (receiverCount + 1))  
        players[randomOriginal].estimate = int(playersTmp[randomInt].estimate)
    else:
        playersTmp = subsession.get_players()
        randomInt = random.randint(0, len(players) - (receiverCount + 2))
        players[len(players) - (receiverCount + 1)].estimate = int(playersTmp[randomInt].estimate)

# PAGES

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

class Instructions_GT_senders(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1

class Instructions_GT_receivers(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number == 1


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

class ThirdWaitPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


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


class Instructions_Trust_in_Senders(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"


class Trust_in_Senders(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"


    @staticmethod
    def vars_for_template(player: Player):
        signals_all_rounds = []
        for i in range(10): # Amount of rounds
            signals_all_rounds.append([])
            for j in range(6): # Amount of players
                signals_all_rounds[i].append(0)
        for i in list(range(0, int(Constants.num_rounds/2))):
            prev_player = player.in_round(i + 1)
            prev_players = prev_player.group.get_players()
            signals = [p.field_maybe_none('sent_signal') for p in prev_players if p.Role == 'sender']
            signals_all_rounds[i] = signals
        return dict( #The following works but is super, super dirty coded - haven't found a way to easily shorten it
            round_1_sender_1=signals_all_rounds[0][0],
            round_1_sender_2=signals_all_rounds[0][1],
            round_1_sender_3=signals_all_rounds[0][2],
            round_1_sender_4=signals_all_rounds[0][3],
            round_1_sender_5=signals_all_rounds[0][4],
            round_1_sender_6=signals_all_rounds[0][5],
            round_2_sender_1=signals_all_rounds[1][0],
            round_2_sender_2=signals_all_rounds[1][1],
            round_2_sender_3=signals_all_rounds[1][2],
            round_2_sender_4=signals_all_rounds[1][3],
            round_2_sender_5=signals_all_rounds[1][4],
            round_2_sender_6=signals_all_rounds[1][5],
            round_3_sender_1=signals_all_rounds[2][0],
            round_3_sender_2=signals_all_rounds[2][1],
            round_3_sender_3=signals_all_rounds[2][2],
            round_3_sender_4=signals_all_rounds[2][3],
            round_3_sender_5=signals_all_rounds[2][4],
            round_3_sender_6=signals_all_rounds[2][5],
            round_4_sender_1=signals_all_rounds[3][0],
            round_4_sender_2=signals_all_rounds[3][1],
            round_4_sender_3=signals_all_rounds[3][2],
            round_4_sender_4=signals_all_rounds[3][3],
            round_4_sender_5=signals_all_rounds[3][4],
            round_4_sender_6=signals_all_rounds[3][5],
            round_5_sender_1=signals_all_rounds[4][0],
            round_5_sender_2=signals_all_rounds[4][1],
            round_5_sender_3=signals_all_rounds[4][2],
            round_5_sender_4=signals_all_rounds[4][3],
            round_5_sender_5=signals_all_rounds[4][4],
            round_5_sender_6=signals_all_rounds[4][5],
            round_6_sender_1=signals_all_rounds[5][0],
            round_6_sender_2=signals_all_rounds[5][1],
            round_6_sender_3=signals_all_rounds[5][2],
            round_6_sender_4=signals_all_rounds[5][3],
            round_6_sender_5=signals_all_rounds[5][4],
            round_6_sender_6=signals_all_rounds[5][5],
            round_7_sender_1=signals_all_rounds[6][0],
            round_7_sender_2=signals_all_rounds[6][1],
            round_7_sender_3=signals_all_rounds[6][2],
            round_7_sender_4=signals_all_rounds[6][3],
            round_7_sender_5=signals_all_rounds[6][4],
            round_7_sender_6=signals_all_rounds[6][5],
            round_8_sender_1=signals_all_rounds[7][0],
            round_8_sender_2=signals_all_rounds[7][1],
            round_8_sender_3=signals_all_rounds[7][2],
            round_8_sender_4=signals_all_rounds[7][3],
            round_8_sender_5=signals_all_rounds[7][4],
            round_8_sender_6=signals_all_rounds[7][5],
            round_9_sender_1=signals_all_rounds[8][0],
            round_9_sender_2=signals_all_rounds[8][1],
            round_9_sender_3=signals_all_rounds[8][2],
            round_9_sender_4=signals_all_rounds[8][3],
            round_9_sender_5=signals_all_rounds[8][4],
            round_9_sender_6=signals_all_rounds[8][5],
            round_10_sender_1=signals_all_rounds[9][0],
            round_10_sender_2=signals_all_rounds[9][1],
            round_10_sender_3=signals_all_rounds[9][2],
            round_10_sender_4=signals_all_rounds[9][3],
            round_10_sender_5=signals_all_rounds[9][4],
            round_10_sender_6=signals_all_rounds[9][5],
            )

    form_model = "player"
    form_fields = ["trust_sender_1", "trust_sender_2", "trust_sender_3", "trust_sender_4", "trust_sender_5", "trust_sender_6"]

class Confidence_1_all10(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_2 + player.trust_sender_2 +\
               player.trust_sender_2 + player.trust_sender_2 == 100


class Confidence_1_notall10(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_2 + player.trust_sender_2 +\
               player.trust_sender_2 + player.trust_sender_2 < 100

class Confidence_2(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"

    @staticmethod
    def vars_for_template(player: Player):
        signals_all_rounds = []
        for i in range(10):  # Amount of rounds
            signals_all_rounds.append([])
            for j in range(6):  # Amount of players
                signals_all_rounds[i].append(0)
        for i in list(range(0, int(Constants.num_rounds / 2))):
            prev_player = player.in_round(i + 1)
            prev_players = prev_player.group.get_players()
            signals = [p.sent_signal for p in prev_players if p.Role == 'sender']
            signals_all_rounds[i] = signals
        return dict(  # The following works but is super, super dirty coded - haven't found a way to easily shorten it
            round_1_sender_1=signals_all_rounds[0][0],
            round_1_sender_2=signals_all_rounds[0][1],
            round_1_sender_3=signals_all_rounds[0][2],
            round_1_sender_4=signals_all_rounds[0][3],
            round_1_sender_5=signals_all_rounds[0][4],
            round_1_sender_6=signals_all_rounds[0][5],
            round_2_sender_1=signals_all_rounds[1][0],
            round_2_sender_2=signals_all_rounds[1][1],
            round_2_sender_3=signals_all_rounds[1][2],
            round_2_sender_4=signals_all_rounds[1][3],
            round_2_sender_5=signals_all_rounds[1][4],
            round_2_sender_6=signals_all_rounds[1][5],
            round_3_sender_1=signals_all_rounds[2][0],
            round_3_sender_2=signals_all_rounds[2][1],
            round_3_sender_3=signals_all_rounds[2][2],
            round_3_sender_4=signals_all_rounds[2][3],
            round_3_sender_5=signals_all_rounds[2][4],
            round_3_sender_6=signals_all_rounds[2][5],
            round_4_sender_1=signals_all_rounds[3][0],
            round_4_sender_2=signals_all_rounds[3][1],
            round_4_sender_3=signals_all_rounds[3][2],
            round_4_sender_4=signals_all_rounds[3][3],
            round_4_sender_5=signals_all_rounds[3][4],
            round_4_sender_6=signals_all_rounds[3][5],
            round_5_sender_1=signals_all_rounds[4][0],
            round_5_sender_2=signals_all_rounds[4][1],
            round_5_sender_3=signals_all_rounds[4][2],
            round_5_sender_4=signals_all_rounds[4][3],
            round_5_sender_5=signals_all_rounds[4][4],
            round_5_sender_6=signals_all_rounds[4][5],
            round_6_sender_1=signals_all_rounds[5][0],
            round_6_sender_2=signals_all_rounds[5][1],
            round_6_sender_3=signals_all_rounds[5][2],
            round_6_sender_4=signals_all_rounds[5][3],
            round_6_sender_5=signals_all_rounds[5][4],
            round_6_sender_6=signals_all_rounds[5][5],
            round_7_sender_1=signals_all_rounds[6][0],
            round_7_sender_2=signals_all_rounds[6][1],
            round_7_sender_3=signals_all_rounds[6][2],
            round_7_sender_4=signals_all_rounds[6][3],
            round_7_sender_5=signals_all_rounds[6][4],
            round_7_sender_6=signals_all_rounds[6][5],
            round_8_sender_1=signals_all_rounds[7][0],
            round_8_sender_2=signals_all_rounds[7][1],
            round_8_sender_3=signals_all_rounds[7][2],
            round_8_sender_4=signals_all_rounds[7][3],
            round_8_sender_5=signals_all_rounds[7][4],
            round_8_sender_6=signals_all_rounds[7][5],
            round_9_sender_1=signals_all_rounds[8][0],
            round_9_sender_2=signals_all_rounds[8][1],
            round_9_sender_3=signals_all_rounds[8][2],
            round_9_sender_4=signals_all_rounds[8][3],
            round_9_sender_5=signals_all_rounds[8][4],
            round_9_sender_6=signals_all_rounds[8][5],
            round_10_sender_1=signals_all_rounds[9][0],
            round_10_sender_2=signals_all_rounds[9][1],
            round_10_sender_3=signals_all_rounds[9][2],
            round_10_sender_4=signals_all_rounds[9][3],
            round_10_sender_5=signals_all_rounds[9][4],
            round_10_sender_6=signals_all_rounds[9][5],
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
        )

    form_model = "player"
    form_fields = ["trust_sender_1_conf", "trust_sender_2_conf", "trust_sender_3_conf", "trust_sender_4_conf", "trust_sender_5_conf", "trust_sender_6_conf"]


class Confidence_3(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_2 + player.trust_sender_2 +\
               player.trust_sender_2 + player.trust_sender_2 < 100

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            mistrust_sender_1=10 - player.trust_sender_1,
            mistrust_sender_2=10 - player.trust_sender_2,
            mistrust_sender_3=10 - player.trust_sender_3,
            mistrust_sender_4=10 - player.trust_sender_4,
            mistrust_sender_5=10 - player.trust_sender_5,
            mistrust_sender_6=10 - player.trust_sender_6,
        )

class Confidence_4(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_2 + player.trust_sender_2 +\
               player.trust_sender_2 + player.trust_sender_2 < 100

    @staticmethod
    def vars_for_template(player: Player):
        signals_all_rounds = []
        for i in range(10):  # Amount of rounds
            signals_all_rounds.append([])
            for j in range(6):  # Amount of players
                signals_all_rounds[i].append(0)
        for i in list(range(0, int(Constants.num_rounds / 2))):
            prev_player = player.in_round(i + 1)
            prev_players = prev_player.group.get_players()
            signals = [p.sent_signal for p in prev_players if p.Role == 'sender']
            signals_all_rounds[i] = signals
        return dict(  # The following works but is super, super dirty coded - haven't found a way to easily shorten it
            round_1_sender_1=signals_all_rounds[0][0],
            round_1_sender_2=signals_all_rounds[0][1],
            round_1_sender_3=signals_all_rounds[0][2],
            round_1_sender_4=signals_all_rounds[0][3],
            round_1_sender_5=signals_all_rounds[0][4],
            round_1_sender_6=signals_all_rounds[0][5],
            round_2_sender_1=signals_all_rounds[1][0],
            round_2_sender_2=signals_all_rounds[1][1],
            round_2_sender_3=signals_all_rounds[1][2],
            round_2_sender_4=signals_all_rounds[1][3],
            round_2_sender_5=signals_all_rounds[1][4],
            round_2_sender_6=signals_all_rounds[1][5],
            round_3_sender_1=signals_all_rounds[2][0],
            round_3_sender_2=signals_all_rounds[2][1],
            round_3_sender_3=signals_all_rounds[2][2],
            round_3_sender_4=signals_all_rounds[2][3],
            round_3_sender_5=signals_all_rounds[2][4],
            round_3_sender_6=signals_all_rounds[2][5],
            round_4_sender_1=signals_all_rounds[3][0],
            round_4_sender_2=signals_all_rounds[3][1],
            round_4_sender_3=signals_all_rounds[3][2],
            round_4_sender_4=signals_all_rounds[3][3],
            round_4_sender_5=signals_all_rounds[3][4],
            round_4_sender_6=signals_all_rounds[3][5],
            round_5_sender_1=signals_all_rounds[4][0],
            round_5_sender_2=signals_all_rounds[4][1],
            round_5_sender_3=signals_all_rounds[4][2],
            round_5_sender_4=signals_all_rounds[4][3],
            round_5_sender_5=signals_all_rounds[4][4],
            round_5_sender_6=signals_all_rounds[4][5],
            round_6_sender_1=signals_all_rounds[5][0],
            round_6_sender_2=signals_all_rounds[5][1],
            round_6_sender_3=signals_all_rounds[5][2],
            round_6_sender_4=signals_all_rounds[5][3],
            round_6_sender_5=signals_all_rounds[5][4],
            round_6_sender_6=signals_all_rounds[5][5],
            round_7_sender_1=signals_all_rounds[6][0],
            round_7_sender_2=signals_all_rounds[6][1],
            round_7_sender_3=signals_all_rounds[6][2],
            round_7_sender_4=signals_all_rounds[6][3],
            round_7_sender_5=signals_all_rounds[6][4],
            round_7_sender_6=signals_all_rounds[6][5],
            round_8_sender_1=signals_all_rounds[7][0],
            round_8_sender_2=signals_all_rounds[7][1],
            round_8_sender_3=signals_all_rounds[7][2],
            round_8_sender_4=signals_all_rounds[7][3],
            round_8_sender_5=signals_all_rounds[7][4],
            round_8_sender_6=signals_all_rounds[7][5],
            round_9_sender_1=signals_all_rounds[8][0],
            round_9_sender_2=signals_all_rounds[8][1],
            round_9_sender_3=signals_all_rounds[8][2],
            round_9_sender_4=signals_all_rounds[8][3],
            round_9_sender_5=signals_all_rounds[8][4],
            round_9_sender_6=signals_all_rounds[8][5],
            round_10_sender_1=signals_all_rounds[9][0],
            round_10_sender_2=signals_all_rounds[9][1],
            round_10_sender_3=signals_all_rounds[9][2],
            round_10_sender_4=signals_all_rounds[9][3],
            round_10_sender_5=signals_all_rounds[9][4],
            round_10_sender_6=signals_all_rounds[9][5],
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            mistrust_sender_1=10 - player.trust_sender_1,
            mistrust_sender_2=10 - player.trust_sender_2,
            mistrust_sender_3=10 - player.trust_sender_3,
            mistrust_sender_4=10 - player.trust_sender_4,
            mistrust_sender_5=10 - player.trust_sender_5,
            mistrust_sender_6=10 - player.trust_sender_6,
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            mistrust_sender_1=10 - player.trust_sender_1,
            mistrust_sender_2=10 - player.trust_sender_2,
            mistrust_sender_3=10 - player.trust_sender_3,
            mistrust_sender_4=10 - player.trust_sender_4,
            mistrust_sender_5=10 - player.trust_sender_5,
            mistrust_sender_6=10 - player.trust_sender_6,
        )
    form_model = "player"
    form_fields = ["sender_1_correction_1_inround", "sender_1_correction_2_inround", "sender_1_correction_3_inround",
                   "sender_1_correction_4_inround", "sender_1_correction_5_inround",
                   "sender_1_correction_6_inround", "sender_1_correction_7_inround", "sender_1_correction_8_inround",
                   "sender_1_correction_9_inround", "sender_1_correction_10_inround",
                   "sender_1_correction_1_actually", "sender_1_correction_2_actually", "sender_1_correction_3_actually",
                   "sender_1_correction_4_actually", "sender_1_correction_5_actually",
                   "sender_1_correction_6_actually", "sender_1_correction_7_actually", "sender_1_correction_8_actually",
                   "sender_1_correction_9_actually", "sender_1_correction_10_actually",
                   "sender_2_correction_1_inround", "sender_2_correction_2_inround", "sender_2_correction_3_inround",
                   "sender_2_correction_4_inround", "sender_2_correction_5_inround",
                   "sender_2_correction_6_inround", "sender_2_correction_7_inround", "sender_2_correction_8_inround",
                   "sender_2_correction_9_inround", "sender_2_correction_10_inround",
                   "sender_2_correction_1_actually", "sender_2_correction_2_actually", "sender_2_correction_3_actually",
                   "sender_2_correction_4_actually", "sender_2_correction_5_actually",
                   "sender_2_correction_6_actually", "sender_2_correction_7_actually", "sender_2_correction_8_actually",
                   "sender_2_correction_9_actually", "sender_2_correction_10_actually",
                   "sender_3_correction_1_inround", "sender_3_correction_2_inround", "sender_3_correction_3_inround",
                   "sender_3_correction_4_inround", "sender_3_correction_5_inround",
                   "sender_3_correction_6_inround", "sender_3_correction_7_inround", "sender_3_correction_8_inround",
                   "sender_3_correction_9_inround", "sender_3_correction_10_inround",
                   "sender_3_correction_1_actually", "sender_3_correction_2_actually", "sender_3_correction_3_actually",
                   "sender_3_correction_4_actually", "sender_3_correction_5_actually",
                   "sender_3_correction_6_actually", "sender_3_correction_7_actually", "sender_3_correction_8_actually",
                   "sender_3_correction_9_actually", "sender_3_correction_10_actually",
                   "sender_4_correction_1_inround", "sender_4_correction_2_inround", "sender_4_correction_3_inround",
                   "sender_4_correction_4_inround", "sender_4_correction_5_inround",
                   "sender_4_correction_6_inround", "sender_4_correction_7_inround", "sender_4_correction_8_inround",
                   "sender_4_correction_9_inround", "sender_4_correction_10_inround",
                   "sender_4_correction_1_actually", "sender_4_correction_2_actually", "sender_4_correction_3_actually",
                   "sender_4_correction_4_actually", "sender_4_correction_5_actually",
                   "sender_4_correction_6_actually", "sender_4_correction_7_actually", "sender_4_correction_8_actually",
                   "sender_4_correction_9_actually", "sender_4_correction_10_actually",
                   "sender_5_correction_1_inround", "sender_5_correction_2_inround", "sender_5_correction_3_inround",
                   "sender_5_correction_4_inround", "sender_5_correction_5_inround",
                   "sender_5_correction_6_inround", "sender_5_correction_7_inround", "sender_5_correction_8_inround",
                   "sender_5_correction_9_inround", "sender_5_correction_10_inround",
                   "sender_5_correction_1_actually", "sender_5_correction_2_actually", "sender_5_correction_3_actually",
                   "sender_5_correction_4_actually", "sender_5_correction_5_actually",
                   "sender_5_correction_6_actually", "sender_5_correction_7_actually", "sender_5_correction_8_actually",
                   "sender_5_correction_9_actually", "sender_5_correction_10_actually",
                   "sender_6_correction_1_inround", "sender_6_correction_2_inround", "sender_6_correction_3_inround",
                   "sender_6_correction_4_inround", "sender_6_correction_5_inround",
                   "sender_6_correction_6_inround", "sender_6_correction_7_inround", "sender_6_correction_8_inround",
                   "sender_6_correction_9_inround", "sender_6_correction_10_inround",
                   "sender_6_correction_1_actually", "sender_6_correction_2_actually", "sender_6_correction_3_actually",
                   "sender_6_correction_4_actually", "sender_6_correction_5_actually",
                   "sender_6_correction_6_actually", "sender_6_correction_7_actually", "sender_6_correction_8_actually",
                   "sender_6_correction_9_actually", "sender_6_correction_10_actually",
                   ]


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

page_sequence = [Instructions_GT_senders, Signals, FirstWaitPage, Instructions_GT_receivers, Guess, SecondWaitPage,
                 Instructions_Trust_in_Senders, Trust_in_Senders, Confidence_1_all10, Confidence_1_notall10, Confidence_2, Confidence_3, Confidence_4, ThirdWaitPage, Payout_calc]
