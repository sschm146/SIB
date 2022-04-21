from otree.api import *
import numpy as np
import random


c = Currency

doc = """
GuessingTask_noSI
"""


class Constants(BaseConstants):
    name_in_url = "Trust_SI"
    num_rounds = 1
    players_per_group = None
    num_senders = 6
    payoff_trust = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    identity = models.StringField()  # the identity from the previous apps
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

#roles allocation and mu_signals (true) simulation for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:  # Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.identity = participant.identity
        p.Role = participant.Role


# PAGES

# wait for all senders to send a signal
class StartWaitPage(WaitPage):
    wait_for_all_groups = True


class SecondWaitPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"


class ThirdWaitPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

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
        participant = player.participant

        return dict(
            signals_round_1=participant.signals_all_rounds[0:6],
            signals_round_2=participant.signals_all_rounds[6:12],
            signals_round_3=participant.signals_all_rounds[12:18],
            signals_round_4=participant.signals_all_rounds[18:24],
            signals_round_5=participant.signals_all_rounds[24:30],
            signals_round_6=participant.signals_all_rounds[30:36],
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:31:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:32:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:33:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:34:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:35:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:36:6].count('-'),
        )


    @staticmethod
    def error_message(player, values):
        participant = player.participant
        if values['trust_sender_1'] > 10 - participant.signals_all_rounds[0:31:6].count('-'):
            return 'Error for Sender F: Please enter a number between 0 and ' + str(
                10 - participant.signals_all_rounds[5:36:6].count('-')) + ' (amount of received signals Sender F)!'
        if values['trust_sender_2'] > 10 - participant.signals_all_rounds[1:32:6].count('-'):
            return 'Error for Sender F: Please enter a number between 0 and ' + str(
                10 - participant.signals_all_rounds[5:36:6].count('-')) + ' (amount of received signals Sender F)!'
        if values['trust_sender_3'] > 10 - participant.signals_all_rounds[2:33:6].count('-'):
            return 'Error for Sender F: Please enter a number between 0 and ' + str(
                10 - participant.signals_all_rounds[5:36:6].count('-')) + ' (amount of received signals Sender F)!'
        if values['trust_sender_4'] > 10 - participant.signals_all_rounds[3:34:6].count('-'):
            return 'Error for Sender F: Please enter a number between 0 and ' + str(
                10 - participant.signals_all_rounds[5:36:6].count('-')) + ' (amount of received signals Sender F)!'
        if values['trust_sender_5'] > 10 - participant.signals_all_rounds[4:35:6].count('-'):
            return 'Error for Sender F: Please enter a number between 0 and ' + str(
                10 - participant.signals_all_rounds[5:36:6].count('-')) + ' (amount of received signals Sender F)!'
        if values['trust_sender_6'] > 10 - participant.signals_all_rounds[5:36:6].count('-'):
            return 'Error for Sender F: Please enter a number between 0 and ' + str(
                10 - participant.signals_all_rounds[5:36:6].count('-')) + ' (amount of received signals Sender F)!'


    form_model = "player"
    form_fields = ["trust_sender_1", "trust_sender_2", "trust_sender_3", "trust_sender_4", "trust_sender_5", "trust_sender_6"]

class Confidence_1_all10(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_3 + player.trust_sender_4 +\
               player.trust_sender_5 + player.trust_sender_6 == 60


class Confidence_1_notall10(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_3 + player.trust_sender_4 + \
               player.trust_sender_5 + player.trust_sender_6 < 60


class Confidence_2(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return dict(
            signals_round_1=participant.signals_all_rounds[0:6],
            signals_round_2=participant.signals_all_rounds[6:12],
            signals_round_3=participant.signals_all_rounds[12:18],
            signals_round_4=participant.signals_all_rounds[18:24],
            signals_round_5=participant.signals_all_rounds[24:30],
            signals_round_6=participant.signals_all_rounds[30:36],
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:31:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:32:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:33:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:34:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:35:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:36:6].count('-'),
        )

    @staticmethod
    def js_vars(player: Player):
        participant = player.participant
        return dict(
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:31:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:32:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:33:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:34:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:35:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:36:6].count('-'),
        )

    form_model = "player"
    form_fields = ["trust_sender_1_conf", "trust_sender_2_conf", "trust_sender_3_conf", "trust_sender_4_conf", "trust_sender_5_conf", "trust_sender_6_conf"]


class Confidence_3(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_3 + player.trust_sender_4 + \
               player.trust_sender_5 + player.trust_sender_6 < 60

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return dict(
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            mistrust_sender_1=10 - participant.signals_all_rounds[0:31:6].count('-') - player.trust_sender_1,
            mistrust_sender_2=10 - participant.signals_all_rounds[1:32:6].count('-') - player.trust_sender_2,
            mistrust_sender_3=10 - participant.signals_all_rounds[2:33:6].count('-') - player.trust_sender_3,
            mistrust_sender_4=10 - participant.signals_all_rounds[3:34:6].count('-') - player.trust_sender_4,
            mistrust_sender_5=10 - participant.signals_all_rounds[4:35:6].count('-') - player.trust_sender_5,
            mistrust_sender_6=10 - participant.signals_all_rounds[5:36:6].count('-') - player.trust_sender_6,
        )

class Confidence_4(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_3 + player.trust_sender_4 + \
               player.trust_sender_5 + player.trust_sender_6 < 60

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return dict(
            signals_round_1=participant.signals_all_rounds[0:6],
            signals_round_2=participant.signals_all_rounds[6:12],
            signals_round_3=participant.signals_all_rounds[12:18],
            signals_round_4=participant.signals_all_rounds[18:24],
            signals_round_5=participant.signals_all_rounds[24:30],
            signals_round_6=participant.signals_all_rounds[30:36],
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            mistrust_sender_1=10 - participant.signals_all_rounds[0:31:6].count('-') - player.trust_sender_1,
            mistrust_sender_2=10 - participant.signals_all_rounds[1:32:6].count('-') - player.trust_sender_2,
            mistrust_sender_3=10 - participant.signals_all_rounds[2:33:6].count('-') - player.trust_sender_3,
            mistrust_sender_4=10 - participant.signals_all_rounds[3:34:6].count('-') - player.trust_sender_4,
            mistrust_sender_5=10 - participant.signals_all_rounds[4:35:6].count('-') - player.trust_sender_5,
            mistrust_sender_6=10 - participant.signals_all_rounds[5:36:6].count('-') - player.trust_sender_6,
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:31:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:32:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:33:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:34:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:35:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:36:6].count('-'),
        )

    @staticmethod
    def js_vars(player: Player):
        participant = player.participant
        rec_signals_sender_4 = participant.signals_all_rounds[3:34:6]
        censored_signals_sender_4 = []
        for i in range(len(rec_signals_sender_4)):
            if rec_signals_sender_4[i] == '-':
                censored_signals_sender_4.append(i)
        rec_signals_sender_5 = participant.signals_all_rounds[4:35:6]
        censored_signals_sender_5 = []
        for i in range(len(rec_signals_sender_5)):
            if rec_signals_sender_5[i] == '-':
                censored_signals_sender_5.append(i)
        rec_signals_sender_6 = participant.signals_all_rounds[5:36:6]
        censored_signals_sender_6 = []
        for i in range(len(rec_signals_sender_6)):
            if rec_signals_sender_6[i] == '-':
                censored_signals_sender_6.append(i)
        return dict(
            mistrust_sender_1=10 - participant.signals_all_rounds[0:31:6].count('-') - player.trust_sender_1,
            mistrust_sender_2=10 - participant.signals_all_rounds[1:32:6].count('-') - player.trust_sender_2,
            mistrust_sender_3=10 - participant.signals_all_rounds[2:33:6].count('-') - player.trust_sender_3,
            mistrust_sender_4=10 - participant.signals_all_rounds[3:34:6].count('-') - player.trust_sender_4,
            mistrust_sender_5=10 - participant.signals_all_rounds[4:35:6].count('-') - player.trust_sender_5,
            mistrust_sender_6=10 - participant.signals_all_rounds[5:36:6].count('-') - player.trust_sender_6,
            num_senders=Constants.num_senders,
            censored_signals_sender_4=censored_signals_sender_4,
            censored_signals_sender_5=censored_signals_sender_5,
            censored_signals_sender_6=censored_signals_sender_6
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


def payout_calc(subsession: Subsession):
    players = subsession.get_players()

    for p in players:
        participant = p.participant
        if p.Role == "sender":
            p.payoff = 0
        if p.Role == "receiver":
            participant = p.participant
            congruent_report = [0, 0, 0, 0, 0, 0]
            temp = [0, 0, 0, 0, 0, 0]
            trust_sender = [p.trust_sender_1, p.trust_sender_2, p.trust_sender_3, p.trust_sender_4, p.trust_sender_5, p.trust_sender_6]
            signals_all_rounds = participant.signals_all_rounds
            estimates_all_rounds = participant.estimates_all_rounds
            for i in list(range(Constants.num_rounds)):
                for j in list(range(0, 6)):
                    temp_signal = signals_all_rounds[i + j]
                    temp_estimate = estimates_all_rounds[i + j]
                    if temp_signal == temp_estimate:
                        congruent_report[j] += 1
                    if congruent_report[j] == trust_sender[j]:
                        temp[j] = Constants.payoff_trust
            p.payoff = random.choice(temp)
        participant.Trust_payoff = p.payoff




page_sequence = [StartWaitPage, Instructions_Trust_in_Senders, Trust_in_Senders, Confidence_1_all10,
                 Confidence_1_notall10, Confidence_2, Confidence_3, Confidence_4, ThirdWaitPage, Payout_calc]
