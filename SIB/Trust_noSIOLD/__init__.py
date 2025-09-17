from otree.api import *
import numpy as np
import random

import settings

c = Currency

doc = """
Trust_noSIOLD
"""


class Constants(BaseConstants):
    name_in_url = "Trust_noSIOLD"
    num_rounds = 1
    num_senders = 6
    players_per_group = None


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    chosen_round = models.IntegerField()
    chosen_sender = models.IntegerField()
    trust_sender_1 = models.IntegerField(min=0, max=10)
    trust_sender_2 = models.IntegerField(min=0, max=10)
    trust_sender_3 = models.IntegerField(min=0, max=10)
    trust_sender_4 = models.IntegerField(min=0, max=10)
    trust_sender_5 = models.IntegerField(min=0, max=10)
    trust_sender_6 = models.IntegerField(min=0, max=10)
    trust_sender_1_1 = models.IntegerField(min=0, max=1)
    trust_sender_1_2 = models.IntegerField(min=0, max=1)
    trust_sender_1_3 = models.IntegerField(min=0, max=1)
    trust_sender_1_4 = models.IntegerField(min=0, max=1)
    trust_sender_1_5 = models.IntegerField(min=0, max=1)
    trust_sender_1_6 = models.IntegerField(min=0, max=1)
    trust_sender_2_1 = models.IntegerField(min=0, max=1)
    trust_sender_2_2 = models.IntegerField(min=0, max=1)
    trust_sender_2_3 = models.IntegerField(min=0, max=1)
    trust_sender_2_4 = models.IntegerField(min=0, max=1)
    trust_sender_2_5 = models.IntegerField(min=0, max=1)
    trust_sender_2_6 = models.IntegerField(min=0, max=1)
    trust_sender_3_1 = models.IntegerField(min=0, max=1)
    trust_sender_3_2 = models.IntegerField(min=0, max=1)
    trust_sender_3_3 = models.IntegerField(min=0, max=1)
    trust_sender_3_4 = models.IntegerField(min=0, max=1)
    trust_sender_3_5 = models.IntegerField(min=0, max=1)
    trust_sender_3_6 = models.IntegerField(min=0, max=1)
    trust_sender_4_1 = models.IntegerField(min=0, max=1)
    trust_sender_4_2 = models.IntegerField(min=0, max=1)
    trust_sender_4_3 = models.IntegerField(min=0, max=1)
    trust_sender_4_4 = models.IntegerField(min=0, max=1)
    trust_sender_4_5 = models.IntegerField(min=0, max=1)
    trust_sender_4_6 = models.IntegerField(min=0, max=1)
    trust_sender_5_1 = models.IntegerField(min=0, max=1)
    trust_sender_5_2 = models.IntegerField(min=0, max=1)
    trust_sender_5_3 = models.IntegerField(min=0, max=1)
    trust_sender_5_4 = models.IntegerField(min=0, max=1)
    trust_sender_5_5 = models.IntegerField(min=0, max=1)
    trust_sender_5_6 = models.IntegerField(min=0, max=1)
    trust_sender_6_1 = models.IntegerField(min=0, max=1)
    trust_sender_6_2 = models.IntegerField(min=0, max=1)
    trust_sender_6_3 = models.IntegerField(min=0, max=1)
    trust_sender_6_4 = models.IntegerField(min=0, max=1)
    trust_sender_6_5 = models.IntegerField(min=0, max=1)
    trust_sender_6_6 = models.IntegerField(min=0, max=1)
    trust_sender_7_1 = models.IntegerField(min=0, max=1)
    trust_sender_7_2 = models.IntegerField(min=0, max=1)
    trust_sender_7_3 = models.IntegerField(min=0, max=1)
    trust_sender_7_4 = models.IntegerField(min=0, max=1)
    trust_sender_7_5 = models.IntegerField(min=0, max=1)
    trust_sender_7_6 = models.IntegerField(min=0, max=1)
    trust_sender_8_1 = models.IntegerField(min=0, max=1)
    trust_sender_8_2 = models.IntegerField(min=0, max=1)
    trust_sender_8_3 = models.IntegerField(min=0, max=1)
    trust_sender_8_4 = models.IntegerField(min=0, max=1)
    trust_sender_8_5 = models.IntegerField(min=0, max=1)
    trust_sender_8_6 = models.IntegerField(min=0, max=1)
    trust_sender_9_1 = models.IntegerField(min=0, max=1)
    trust_sender_9_2 = models.IntegerField(min=0, max=1)
    trust_sender_9_3 = models.IntegerField(min=0, max=1)
    trust_sender_9_4 = models.IntegerField(min=0, max=1)
    trust_sender_9_5 = models.IntegerField(min=0, max=1)
    trust_sender_9_6 = models.IntegerField(min=0, max=1)
    trust_sender_10_1 = models.IntegerField(min=0, max=1)
    trust_sender_10_2 = models.IntegerField(min=0, max=1)
    trust_sender_10_3 = models.IntegerField(min=0, max=1)
    trust_sender_10_4 = models.IntegerField(min=0, max=1)
    trust_sender_10_5 = models.IntegerField(min=0, max=1)
    trust_sender_10_6 = models.IntegerField(min=0, max=1)
    trust_sender_1_conf = models.IntegerField()
    trust_sender_2_conf = models.IntegerField()
    trust_sender_3_conf = models.IntegerField()
    trust_sender_4_conf = models.IntegerField()## adjust to blank=True for old Confidence_2 version
    trust_sender_5_conf = models.IntegerField()## adjust to blank=True for old Confidence_2 version
    trust_sender_6_conf = models.IntegerField()## adjust to blank=True for old Confidence_2 version


# FUNCTIONs
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:  # Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.Role = participant.Role

# PAGES


# wait for all senders to send a signal

class ThirdWaitPage(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds


class Instructions_Trust_in_Senders(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"

    @staticmethod
    def vars_for_template(player: Player):
        CN_treatment = False
        if "correlation" in player.session.config['name']:
            CN_treatment = True
        return dict(
            CN_treatment=CN_treatment
        )

class Confidence(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        CN_treatment = False
        player.trust_sender_1 = player.trust_sender_1_1 + player.trust_sender_2_1 + player.trust_sender_3_1 + player.trust_sender_4_1 + player.trust_sender_5_1 + player.trust_sender_6_1 + player.trust_sender_7_1 + player.trust_sender_8_1 + player.trust_sender_9_1 + player.trust_sender_10_1
        player.trust_sender_2 = player.trust_sender_1_2 + player.trust_sender_2_2 + player.trust_sender_3_2 + player.trust_sender_4_2 + player.trust_sender_5_2 + player.trust_sender_6_2 + player.trust_sender_7_2 + player.trust_sender_8_2 + player.trust_sender_9_2 + player.trust_sender_10_2
        player.trust_sender_3 = player.trust_sender_1_3 + player.trust_sender_2_3 + player.trust_sender_3_3 + player.trust_sender_4_3 + player.trust_sender_5_3 + player.trust_sender_6_3 + player.trust_sender_7_3 + player.trust_sender_8_3 + player.trust_sender_9_3 + player.trust_sender_10_3
        player.trust_sender_4 = player.trust_sender_1_4 + player.trust_sender_2_4 + player.trust_sender_3_4 + player.trust_sender_4_4 + player.trust_sender_5_4 + player.trust_sender_6_4 + player.trust_sender_7_4 + player.trust_sender_8_4 + player.trust_sender_9_4 + player.trust_sender_10_4
        player.trust_sender_5 = player.trust_sender_1_5 + player.trust_sender_2_5 + player.trust_sender_3_5 + player.trust_sender_4_5 + player.trust_sender_5_5 + player.trust_sender_6_5 + player.trust_sender_7_5 + player.trust_sender_8_5 + player.trust_sender_9_5 + player.trust_sender_10_5
        player.trust_sender_6 = player.trust_sender_1_6 + player.trust_sender_2_6 + player.trust_sender_3_6 + player.trust_sender_4_6 + player.trust_sender_5_6 + player.trust_sender_6_6 + player.trust_sender_7_6 + player.trust_sender_8_6 + player.trust_sender_9_6 + player.trust_sender_10_6

        if "correlation" in player.session.config['name']:
            CN_treatment = True
        return dict(
            signals_round_1=participant.signals_all_rounds[0:6],
            signals_round_2=participant.signals_all_rounds[6:12],
            signals_round_3=participant.signals_all_rounds[12:18],
            signals_round_4=participant.signals_all_rounds[18:24],
            signals_round_5=participant.signals_all_rounds[24:30],
            signals_round_6=participant.signals_all_rounds[30:36],
            signals_round_7=participant.signals_all_rounds[36:42],
            signals_round_8=participant.signals_all_rounds[42:48],
            signals_round_9=participant.signals_all_rounds[48:54],
            signals_round_10=participant.signals_all_rounds[54:60],
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            mistrust_sender_1=10 - participant.signals_all_rounds[0:55:6].count('-') - player.trust_sender_1,
            mistrust_sender_2=10 - participant.signals_all_rounds[1:56:6].count('-') - player.trust_sender_2,
            mistrust_sender_3=10 - participant.signals_all_rounds[2:57:6].count('-') - player.trust_sender_3,
            mistrust_sender_4=10 - participant.signals_all_rounds[3:58:6].count('-') - player.trust_sender_4,
            mistrust_sender_5=10 - participant.signals_all_rounds[4:59:6].count('-') - player.trust_sender_5,
            mistrust_sender_6=10 - participant.signals_all_rounds[5:60:6].count('-') - player.trust_sender_6,
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:55:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:56:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:57:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:58:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:59:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:60:6].count('-'),
            CN_treatment=CN_treatment
        )

    @staticmethod
    def js_vars(player: Player):
        participant = player.participant
        return dict(
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:55:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:56:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:57:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:58:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:59:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:60:6].count('-'),
        )

    form_model = "player"
    form_fields = ["trust_sender_1_conf", "trust_sender_2_conf", "trust_sender_3_conf", "trust_sender_4_conf", "trust_sender_5_conf", "trust_sender_6_conf"]

class Trust_in_Senders(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds and player.Role == "receiver"

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        CN_treatment = False
        if "correlation" in player.session.config['name']:
            CN_treatment = True
        return dict(
            signals_round_1=participant.signals_all_rounds[0:6],
            signals_round_2=participant.signals_all_rounds[6:12],
            signals_round_3=participant.signals_all_rounds[12:18],
            signals_round_4=participant.signals_all_rounds[18:24],
            signals_round_5=participant.signals_all_rounds[24:30],
            signals_round_6=participant.signals_all_rounds[30:36],
            signals_round_7=participant.signals_all_rounds[36:42],
            signals_round_8=participant.signals_all_rounds[42:48],
            signals_round_9=participant.signals_all_rounds[48:54],
            signals_round_10=participant.signals_all_rounds[54:60],
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:55:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:56:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:57:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:58:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:59:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:60:6].count('-'),
            CN_treatment=CN_treatment
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
            num_senders=Constants.num_senders,
            censored_signals_sender_4=censored_signals_sender_4,
            censored_signals_sender_5=censored_signals_sender_5,
            censored_signals_sender_6=censored_signals_sender_6,
            signals_round_1=participant.signals_all_rounds[0:6],
            signals_round_2=participant.signals_all_rounds[6:12],
            signals_round_3=participant.signals_all_rounds[12:18],
            signals_round_4=participant.signals_all_rounds[18:24],
            signals_round_5=participant.signals_all_rounds[24:30],
            signals_round_6=participant.signals_all_rounds[30:36],
            signals_round_7=participant.signals_all_rounds[36:42],
            signals_round_8=participant.signals_all_rounds[42:48],
            signals_round_9=participant.signals_all_rounds[48:54],
            signals_round_10=participant.signals_all_rounds[54:60],
            n_rec_signals_sender_1=10 - participant.signals_all_rounds[0:55:6].count('-'),
            n_rec_signals_sender_2=10 - participant.signals_all_rounds[1:56:6].count('-'),
            n_rec_signals_sender_3=10 - participant.signals_all_rounds[2:57:6].count('-'),
            n_rec_signals_sender_4=10 - participant.signals_all_rounds[3:58:6].count('-'),
            n_rec_signals_sender_5=10 - participant.signals_all_rounds[4:59:6].count('-'),
            n_rec_signals_sender_6=10 - participant.signals_all_rounds[5:60:6].count('-'),
        )

    form_model = "player"
    form_fields = ["trust_sender_1_1", "trust_sender_1_2", "trust_sender_1_3",
                   "trust_sender_1_4", "trust_sender_1_5", "trust_sender_1_6",
                   "trust_sender_2_1", "trust_sender_2_2", "trust_sender_2_3",
                   "trust_sender_2_4", "trust_sender_2_5", "trust_sender_2_6",
                   "trust_sender_3_1", "trust_sender_3_2", "trust_sender_3_3",
                   "trust_sender_3_4", "trust_sender_3_5", "trust_sender_3_6",
                   "trust_sender_4_1", "trust_sender_4_2", "trust_sender_4_3",
                   "trust_sender_4_4", "trust_sender_4_5", "trust_sender_4_6",
                   "trust_sender_5_1", "trust_sender_5_2", "trust_sender_5_3",
                   "trust_sender_5_4", "trust_sender_5_5", "trust_sender_5_6",
                   "trust_sender_6_1", "trust_sender_6_2", "trust_sender_6_3",
                   "trust_sender_6_4", "trust_sender_6_5", "trust_sender_6_6",
                   "trust_sender_7_1", "trust_sender_7_2", "trust_sender_7_3",
                   "trust_sender_7_4", "trust_sender_7_5", "trust_sender_7_6",
                   "trust_sender_8_1", "trust_sender_8_2", "trust_sender_8_3",
                   "trust_sender_8_4", "trust_sender_8_5", "trust_sender_8_6",
                   "trust_sender_9_1", "trust_sender_9_2", "trust_sender_9_3",
                   "trust_sender_9_4", "trust_sender_9_5", "trust_sender_9_6",
                   "trust_sender_10_1", "trust_sender_10_2", "trust_sender_10_3",
                   "trust_sender_10_4", "trust_sender_10_5", "trust_sender_10_6",
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
            corrections_1 = [p.field_maybe_none('trust_sender_1_1'), p.field_maybe_none('trust_sender_2_1'),
                             p.field_maybe_none('trust_sender_3_1'), p.field_maybe_none('trust_sender_4_1'),
                             p.field_maybe_none('trust_sender_5_1'), p.field_maybe_none('trust_sender_6_1'),
                             p.field_maybe_none('trust_sender_7_1'), p.field_maybe_none('trust_sender_8_1'),
                             p.field_maybe_none('trust_sender_9_1'), p.field_maybe_none('trust_sender_10_1')]
            corrections_2 = [p.field_maybe_none('trust_sender_1_2'), p.field_maybe_none('trust_sender_2_2'),
                             p.field_maybe_none('trust_sender_3_2'), p.field_maybe_none('trust_sender_4_2'),
                             p.field_maybe_none('trust_sender_5_2'), p.field_maybe_none('trust_sender_6_2'),
                             p.field_maybe_none('trust_sender_7_2'), p.field_maybe_none('trust_sender_8_2'),
                             p.field_maybe_none('trust_sender_9_2'), p.field_maybe_none('trust_sender_10_2')]
            corrections_3 = [p.field_maybe_none('trust_sender_1_3'), p.field_maybe_none('trust_sender_2_3'),
                             p.field_maybe_none('trust_sender_3_3'), p.field_maybe_none('trust_sender_4_3'),
                             p.field_maybe_none('trust_sender_5_3'), p.field_maybe_none('trust_sender_6_3'),
                             p.field_maybe_none('trust_sender_7_3'), p.field_maybe_none('trust_sender_8_3'),
                             p.field_maybe_none('trust_sender_9_3'), p.field_maybe_none('trust_sender_10_3')]
            corrections_4 = [p.field_maybe_none('trust_sender_1_4'), p.field_maybe_none('trust_sender_2_4'),
                             p.field_maybe_none('trust_sender_3_4'), p.field_maybe_none('trust_sender_4_4'),
                             p.field_maybe_none('trust_sender_5_4'), p.field_maybe_none('trust_sender_6_4'),
                             p.field_maybe_none('trust_sender_7_4'), p.field_maybe_none('trust_sender_8_4'),
                             p.field_maybe_none('trust_sender_9_4'), p.field_maybe_none('trust_sender_10_4')]
            corrections_5 = [p.field_maybe_none('trust_sender_1_5'), p.field_maybe_none('trust_sender_2_5'),
                             p.field_maybe_none('trust_sender_3_5'), p.field_maybe_none('trust_sender_4_5'),
                             p.field_maybe_none('trust_sender_5_5'), p.field_maybe_none('trust_sender_6_5'),
                             p.field_maybe_none('trust_sender_7_5'), p.field_maybe_none('trust_sender_8_5'),
                             p.field_maybe_none('trust_sender_9_5'), p.field_maybe_none('trust_sender_10_5')]
            corrections_6 = [p.field_maybe_none('trust_sender_1_6'), p.field_maybe_none('trust_sender_2_6'),
                             p.field_maybe_none('trust_sender_3_6'), p.field_maybe_none('trust_sender_4_6'),
                             p.field_maybe_none('trust_sender_5_6'), p.field_maybe_none('trust_sender_6_6'),
                             p.field_maybe_none('trust_sender_7_6'), p.field_maybe_none('trust_sender_8_6'),
                             p.field_maybe_none('trust_sender_9_6'), p.field_maybe_none('trust_sender_10_6')]
            corrections = [corrections_1, corrections_2, corrections_3, corrections_4, corrections_5, corrections_6]

            i = random.randint(0, 5)  # random sender
            p.chosen_sender = i + 1
            j = random.randint(0, 9)  # random round
            p.chosen_round = j + 1
            if corrections[i][j] == 1:
                actual_signal = subsession.session.config['Signals'][i][j]
                sent_signal = participant.signals_all_rounds[i * 6 + j]
                if actual_signal != sent_signal:
                    correction_payoff = subsession.session.config['Trust_in_Senders_payoff']
                else:
                    correction_payoff = 0
            if corrections[i][j] == 0:
                actual_signal = subsession.session.config['Signals'][i][j]
                sent_signal = participant.signals_all_rounds[i * 6 + j]
                if actual_signal != sent_signal:
                    correction_payoff = 0
                else:
                    correction_payoff = subsession.session.config['Trust_in_Senders_payoff']

            p.payoff = subsession.session.config['Confidence_payoff'] + correction_payoff
            participant.Trust_payoff = p.payoff

page_sequence = [Instructions_Trust_in_Senders, Trust_in_Senders, Confidence, ThirdWaitPage, Payout_calc]

