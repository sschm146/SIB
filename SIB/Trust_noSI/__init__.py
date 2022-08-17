from otree.api import *
import numpy as np
import random

import settings

c = Currency

doc = """
GuessingTask_noSI
"""


class Constants(BaseConstants):
    name_in_url = "Trust_noSI"
    num_rounds = 1
    num_senders = 6
    players_per_group = None


class Subsession(BaseSubsession):
    x = models.IntegerField()


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
    subsession.x = random.randint(0, 50)
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
        return player.round_number == Constants.num_rounds and player.Role == "receiver" and \
               player.trust_sender_1 + player.trust_sender_2 + player.trust_sender_3 + player.trust_sender_4 + \
               player.trust_sender_5 + player.trust_sender_6 < 60

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
            trust_sender_1=player.trust_sender_1,
            trust_sender_2=player.trust_sender_2,
            trust_sender_3=player.trust_sender_3,
            trust_sender_4=player.trust_sender_4,
            trust_sender_5=player.trust_sender_5,
            trust_sender_6=player.trust_sender_6,
            mistrust_sender_1=10 - participant.signals_all_rounds[0:56:6].count('-') - player.trust_sender_1,
            mistrust_sender_2=10 - participant.signals_all_rounds[1:56:6].count('-') - player.trust_sender_2,
            mistrust_sender_3=10 - participant.signals_all_rounds[2:57:6].count('-') - player.trust_sender_3,
            mistrust_sender_4=10 - participant.signals_all_rounds[3:58:6].count('-') - player.trust_sender_4,
            mistrust_sender_5=10 - participant.signals_all_rounds[4:59:6].count('-') - player.trust_sender_5,
            mistrust_sender_6=10 - participant.signals_all_rounds[5:60:6].count('-') - player.trust_sender_6,
            mistrust = 60- participant.signals_all_rounds.count('-') - player.trust_sender_1 - player.trust_sender_2 - player.trust_sender_3 - player.trust_sender_4 - player.trust_sender_5 - player.trust_sender_6,
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
            mistrust_sender_1=10 - participant.signals_all_rounds[0:56:6].count('-') - player.trust_sender_1,
            mistrust_sender_2=10 - participant.signals_all_rounds[1:56:6].count('-') - player.trust_sender_2,
            mistrust_sender_3=10 - participant.signals_all_rounds[2:57:6].count('-') - player.trust_sender_3,
            mistrust_sender_4=10 - participant.signals_all_rounds[3:58:6].count('-') - player.trust_sender_4,
            mistrust_sender_5=10 - participant.signals_all_rounds[4:59:6].count('-') - player.trust_sender_5,
            mistrust_sender_6=10 - participant.signals_all_rounds[5:60:6].count('-') - player.trust_sender_6,
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
            participant = p.participant
            congruent_report = [0, 0, 0, 0, 0, 0]
            temp = [0, 0, 0, 0, 0, 0]
            trust_sender = [p.trust_sender_1, p.trust_sender_2, p.trust_sender_3, p.trust_sender_4, p.trust_sender_5, p.trust_sender_6]
            signals_all_rounds = participant.signals_all_rounds
            estimates_all_rounds = participant.estimates_all_rounds
            for i in list(range(0,10)): #Amount of rounds
                for j in list(range(0, 6)): #Amount of senders
                    temp_signal = signals_all_rounds[i*6 + j]
                    temp_estimate = estimates_all_rounds[i*6 + j]
                    if temp_signal == temp_estimate:
                        congruent_report[j] += 1
            for j in list(range(0, 6)): #Amount of senders
                if congruent_report[j] == trust_sender[j]:
                    temp[j] = subsession.session.config['Trust_payoff_1']

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


            def findall(element, matrix):
                result = []
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        if matrix[i][j] == element:
                            result.append((i, j))
                return result
            urn = findall(1, corrections)
            if any(urn):
                ball = random.choice(urn)
                #sender = ball[0]
                #round = ball[1]
                actual_signal = subsession.session.config['Signals'][ball[0]][ball[1]]
                sent_signal = participant.signals_all_rounds[ball[1]*6 + ball[0]]
                if actual_signal != sent_signal:
                    correction_payoff = subsession.session.config['Trust_payoff_3']
                else:
                    correction_payoff = 0
            else:
                correction_payoff = 0
                # participants get rewards for precision in TiS (temp) + fixed payment for Confidence_2 + rewards for precision in Confidence_4
            p.chosen_sender = random.choice(list(range(1, 7)))
            p.payoff = temp[p.chosen_sender - 1] + subsession.session.config['Trust_payoff_2'] + correction_payoff
            participant.Trust_payoff = p.payoff

page_sequence = [Instructions_Trust_in_Senders, Trust_in_Senders, Confidence, ThirdWaitPage, Payout_calc]

