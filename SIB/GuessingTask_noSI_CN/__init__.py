from otree.api import *
import numpy as np
import random

c = Currency

doc = """
GuessingTask_noSI_CN
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_noSI_CN"
    num_rounds = 20
    players_per_group = None
    num_senders = 6



class Subsession(BaseSubsession):
    x = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    sent_signal = models.IntegerField(min=0, max=10000)  # signal sent by the sender
    estimate = models.IntegerField()  # the estimate sent by the estimation device which is observed by senders
    posterior = models.FloatField(min=0, max=10000)  # the posterior belief of the receiver
    true_state = models.IntegerField()
    signal_order = models.IntegerField()
    chosen_round = models.IntegerField()
    received_signal_1 = models.IntegerField()
    received_signal_2 = models.IntegerField()
    received_signal_3 = models.IntegerField()
    received_signal_4 = models.IntegerField()
    received_signal_5 = models.IntegerField()
    received_signal_6 = models.IntegerField()
    comprq1 = models.IntegerField(choices=[[1,
                                            'Die Schätzung eines zufällig gezogenen Schätzgeräts kann mit gleicher Wahrscheinlichkeit der Zahl x oder einer andere Zahl entsprechen.'],
                                           [2,
                                            'Die Schätzung eines zufällig gezogenen Schätzgeräts entspricht mit geringerer Wahrscheinlichkeit der Zahl x als jeder anderen Zahl. '
                                            'Je weiter man sich von der Zahl x entfernt, desto wahrscheinlicher ist es, dass ein Schätzgerät eine solche Schätzung angibt.'],
                                           [3,
                                            'Die Schätzung eines zufällig gezogenen Schätzgeräts entspricht mit größerer Wahrscheinlichkeit der Zahl x als jeder anderen Zahl. '
                                            'Je weiter man sich von der Zahl x entfernt, desto unwahrscheinlicher ist es, dass ein Schätzgerät eine solche Schätzung angibt.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq2 = models.IntegerField(choices=[
        [1,
         'Der Durchschnitt der Schätzungen aller Schätzgeräte entspricht mit gleicher Wahrscheinlichkeit entweder der Zahl x oder jeder beliebigen anderen Zahl.'],
        [2, 'Der Durchschnitt der Schätzungen aller Schätzgeräte entspricht genau (oder fast genau) der Zahl x.'],
        [3, 'Der Durchschnitt der Schätzungen aller Schätzgeräte ist immer größer als die Zahl x.'],
        [4, 'Der Durchschnitt der Schätzungen aller Schätzgeräte ist immer kleiner als die Zahl x.']],
        widget=widgets.RadioSelect,
        label='')
    comprq3_CN = models.IntegerField(
        choices=[[1, 'Ich werde den Durchschnitt der Schätzungen von 2 zufällig gezogenen Schätzgeräten beobachten.'],
                 [2, 'Ich werde den Durchschnitt der Schätzungen von 3 zufällig gezogenen Schätzgeräten beobachten.'],
                 [3, 'Ich werde die Schätzungen von 2 zufällig gezogenen Schätzgeräten beobachten.']],
        widget=widgets.RadioSelect,
        label='')
    comprq3 = models.IntegerField(
        choices=[[1, 'Ich werde die Schätzung von 1 zufällig gezogenen Schätzgerät beobachten.'],
                 [2, 'Ich werde die Schätzungen von 2 zufällig gezogenen Schätzgeräten beobachten.'],
                 [3, 'Ich werde die Schätzungen von 3 zufällig gezogenen Schätzgeräten beobachten.']],
        widget=widgets.RadioSelect,
        label='')
    comprq5 = models.IntegerField(label='')
    comprq4_CN = models.IntegerField(
        choices=[[1, 'The average estimate of the two randomly drawn estimation devices I observe is 490.'],
                 [2, 'The average estimate of the two randomly drawn estimation devices I observe is 541.'],
                 [3, 'The average estimate of the two randomly drawn estimation devices I observe is 555.']],
        widget=widgets.RadioSelect,
        label='')
    comprq5_CN = models.IntegerField(label='')
    comprq6_CN = models.IntegerField(choices=[[1, 'Meine Chancen auf die zusätzliche Auszahlung von 13€ sind so am höchsten. '],
                                              [2, 'Dies hat keinen Einfluss auf meine Auszahlung.'],
                                              [3, 'Meine Chancen auf die zusätzliche Auszahlung von 13€ sind sehr gering.']],
                                     widget=widgets.RadioSelect,
                                     label='')
    comprq6 = models.IntegerField(choices=[[1, 'Meine Chancen auf die zusätzliche Auszahlung von 13€ sind so am höchsten. '],
                                              [2, 'Dies hat keinen Einfluss auf meine Auszahlung.'],
                                              [3, 'Meine Chancen auf die zusätzliche Auszahlung von 13€ sind sehr gering.']],
                                     widget=widgets.RadioSelect,
                                     label='')
    comprq7 = models.IntegerField(choices=[[1, 'Jeder Sender hat die Schätzung von 1 zufällig gezogenen Schätzgerät beobachtet.'],
                                           [2, 'Die Sender A und B beobachteten die Schätzung von jeweils 1 zufällig gezogenen Schätzgerät. '
                                               'Die Sender C, D, E und F beobachteten den Durchschnitt der Schätzungen von zwei Schätzgeräten: '
                                               'Die Schätzung des jeweils ihnen zugeordneten Schätzgerätes und die Schätzung des Schätzgerätes von Sender B'],
                                           [3, 'Die Sender A, B, C und D beobachteten die Schätzung von jeweils 1 zufällig gezogenen Schätzgerät. '
                                               'Die Sender E und F beobachteten den Durchschnitt der Schätzungen von zwei Schätzgeräten: '
                                               'Die Schätzung des jeweils ihnen zugeordneten Schätzgerätes und die Schätzung des Schätzgerätes von Sender D.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq8 = models.IntegerField(choices=[[1, '307'],
                                           [2, '310'],
                                           [3, '311'],
                                           [4, '312']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq9 = models.IntegerField(choices=[[1, 'Ich werde die Schätzung von 1 zufällig gezogenen Schätzgerät beobachten.'],
                                           [2, 'Ich werde die Schätzungen von 6 zufällig gezogenen Schätzgeräten beobachten.'],
                                           [3, 'Ich werde die Schätzungen von 6 Sendern beobachten: Sender A, Sender B, Sender C, Sender D, Sender E, und Sender F.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq10 = models.IntegerField(choices=[[1, 'Die Schätzung eines zufällig gezogenen Schätzgeräts ist mit gleicher Wahrscheinlichkeit die tatsächliche Zahl x oder eine andere Zahl.'],
                                           [2, 'Die Schätzung eines zufällig gezogenen Schätzgeräts entspricht mit geringerer Wahrscheinlichkeit der tatsächlichen Zahl x als jeder anderen Zahl. '
                                               'Je weiter man sich von Zahl x entfernt, desto wahrscheinlicher ist es, dass ein Schätzgerät eine solche Schätzung meldet.'],
                                           [3, 'Die Schätzung eines zufällig gezogenen Schätzgeräts entspricht mit größerer Wahrscheinlichkeit der tatsächlichen Zahl x als jeder anderen Zahl. '
                                               'Je weiter man sich von Zahl x entfernt, desto unwahrscheinlicher ist es, dass ein Schätzgerät eine solche Schätzung meldet.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq11 = models.IntegerField(choices=[[1, 'Der Durchschnitt der Schätzungen aller Schätzgeräte kann mit gleicher Wahrscheinlichkeit eine beliebige Zahl sein.'],
                                           [2, 'Der Durchschnitt der Schätzungen aller Schätzgeräte entspricht genau (oder fast genau) der Zahl x.'],
                                           [3, 'Der Durchschnitt der Schätzungen aller Schätzgeräte ist immer größer als die Zahl x.'],
                                            [4, 'Der Durchschnitt der Schätzungen aller Schätzgeräte ist immer kleiner als die Zahl x.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq12 = models.IntegerField(choices=[[1, 'Sender B’s randomly drawn estimation device showed an estimate of 490.'],
                                           [2, 'Sender B’s randomly drawn estimation device showed an estimate of  541.'],
                                           [3, 'Sender B’s randomly drawn estimation device showed an estimate of  555.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq13 = models.IntegerField(choices=[[1, 'Sender A: 20, Sender C: 22, Sender F: 28'],
                                           [2, 'Sender A: 19, Sender C: 20, Sender F: 22'],
                                           [3, 'Sender A: 19, Sender C: 19, Sender F: 22'],
                                            [4, 'Sender A: 20, Sender C: 20, Sender F: 20']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq14 = models.IntegerField(choices=[[1, '0%'],
                                           [2, '50%'],
                                           [3, '67%'],
                                           [4, '100%']],
                                  widget=widgets.RadioSelect,
                                  label='')

    error_comprq1 = models.IntegerField(initial=0)
    error_comprq2 = models.IntegerField(initial=0)
    error_comprq3 = models.IntegerField(initial=0)
    error_comprq5 = models.IntegerField(initial=0)
    error_comprq6 = models.IntegerField(initial=0)
    error_comprq3_CN = models.IntegerField(initial=0)
    error_comprq5_CN = models.IntegerField(initial=0)
    error_comprq6_CN = models.IntegerField(initial=0)
    error_comprq7 = models.IntegerField(initial=0)
    error_comprq8 = models.IntegerField(initial=0)
    error_comprq9 = models.IntegerField(initial=0)
    error_comprq10 = models.IntegerField(initial=0)
    error_comprq11 = models.IntegerField(initial=0)
    error_comprq13 = models.IntegerField(initial=0)
    error_comprq14 = models.IntegerField(initial=0)
    q1 = models.IntegerField(label='')
    q2 = models.IntegerField(label='')
    q3 = models.IntegerField(
        choices=[[0, ""],
                 [1, ""],
                 [2, ""],
                 [3, ""],
                 [4, ""],
                 [5, ""],
                 [6, ""], ],
        widget=widgets.RadioSelect, label=''
    )
    q4 = models.IntegerField(
        choices=[[0, ""],
                 [1, ""],
                 [2, ""],
                 [3, ""],
                 [4, ""],
                 [5, ""],
                 [6, ""], ],
        widget=widgets.RadioSelect, label=''
    )
    q5 = models.IntegerField(
        choices=[[0, "Weiblich"],
                 [1, "Männlich"],
                 [2, "Divers"]],
        widget=widgets.RadioSelect, label=''
    )
    q6 = models.IntegerField(
        choices=[[0, "Nein"],
                 [1, "Ja"]],
        widget=widgets.RadioSelect, label=''
    )
    q7 = models.StringField(label='', blank=True)
    q8 = models.IntegerField(label='')
    q9 = models.IntegerField(min=0, label='')
    q10 = models.IntegerField(
        choices=[[1, "Schlecht"],
                 [2, "Durchschnittlich"],
                 [3, "Gut"],
                 [4, "Ausgezeichnet"]],
        widget=widgets.RadioSelect, label=''
    )
    q11 = models.IntegerField(
        choices=[[1, "Schlecht"],
                 [2, "Durchschnittlich"],
                 [3, "Gut"],
                 [4, "Ausgezeichnet"]],
        widget=widgets.RadioSelect, label=''
    )
    q12 = models.IntegerField(
        choices=[[1, "Ja"],
                 [2, "Nein"]],
        widget=widgets.RadioSelect, label=''
    )
    q13 = models.IntegerField(
        choices=[[1, "Ich habe schon immer gewusst, wie man haushaltet."],
                 [2, "Ich musste während meines Studiums lernen, mit Geld umzugehen."],
                 [3, "Ich habe Mühe, lebensnotwendige Dinge zu kaufen"],
                 [4, "Ich kann mir alles leisten, ich haushalte nicht."]],
        widget=widgets.RadioSelect, label=''
    )
    q14 = models.IntegerField(
        choices=[[1, "Ich habe keine Schwierigkeiten"],
                 [2, "Keine Haushaltsplanung"],
                 [3, "Kosten für lebensnotwendige Dinge zu hoch"],
                 [4, "Zu sorglos mit Geld"],
                 [5, "Andere Prioritäten wie Shopping und Nachtleben haben Vorrang"],
                 [6, "Ich bin gut im Haushalten"],
                 [7, "Ich weiß es nicht"]],
        widget=widgets.RadioSelect, label=''
    )
    q15 = models.LongStringField(label='')
    q16 = models.IntegerField(
        choices=[[1, "Ja"],
                 [2, "Nein"]],
        widget=widgets.RadioSelect, label=''
    )
    q17 = models.IntegerField(
        choices=[[1, "Ja"],
                 [2, "Nein"]],
        widget=widgets.RadioSelect, label=''
    )
    q18 = models.IntegerField(
        choices=[[1, "Ja"],
                 [2, "Nein"]],
        widget=widgets.RadioSelect, label=''
    )
    q19 = models.IntegerField(
        choices=[[1, "Ja"],
                 [2, "Nein"]],
        widget=widgets.RadioSelect, label=''
    )
    q20 = models.IntegerField(
        choices=[[1, "Ja"],
                 [2, "Nein"]],
        widget=widgets.RadioSelect, label=''
    )
    q21 = models.IntegerField(
        choices=[[1, "Ja"],
                 [2, "Nein"]],
        widget=widgets.RadioSelect, label=''
    )
    q22 = models.IntegerField(
        choices=[[1, "Studentenwerk"],
                 [2, "Eltern"],
                 [3, "Freunde"],
                 [4, "Bank"],
                 [5, "Finanzberatung"],
                 [6, "Sonstige"]],
        widget=widgets.RadioSelect, label=''
    )
    q23 = models.LongStringField(label='', blank=True)
    q24 = models.LongStringField(label='')
    q25 = models.LongStringField(label='')

# FUNCTIONS

#roles allocation and mu_signals (true) simulaion for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        subsession.x = random.randint(0, p.session.config['QSR_cutoff']) #Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.Role = participant.Role
        if p.Role == "sender":
            if p.round_number <= Constants.num_rounds / 2:
                if p.id_in_group == Constants.num_senders:
                    p.estimate = int((p.session.config['Signals'][p.id_in_group - 1 - 2][p.round_number - 1] + p.session.config['Signals'][p.id_in_group - 1][p.round_number - 1]) / 2)
                elif p.id_in_group == Constants.num_senders - 1:
                    p.estimate = int((p.session.config['Signals'][p.id_in_group - 1 - 1][p.round_number - 1] + p.session.config['Signals'][p.id_in_group - 1][p.round_number - 1]) / 2)
                else:
                    p.estimate = p.session.config['Signals'][p.id_in_group - 1][p.round_number - 1]
                p.true_state = p.session.config['True_state'][p.round_number - 1]

# PAGES

# senders see estimate and send signal
class Signals(Page):
    form_model = "player"
    form_fields = ["sent_signal"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((player.true_state  - player.sent_signal), 2)
        if diff <= player.subsession.x:
            player.payoff = player.session.config['GT_sender_payoff']
        else:
            player.payoff = 0

    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number <= Constants.num_rounds/2

    @staticmethod
    def vars_for_template(player: Player):
        estimate = player.estimate
        round = player.round_number
        return dict(
            estimate=estimate,
            round=round,
            border=player.session.config['entry_warning_border'],
            GT_sender_payoff=player.session.config['GT_sender_payoff']
        )

    @staticmethod
    def js_vars(player: Player):
        estimate = player.estimate
        return dict(
            round=player.round_number,
            estimate=estimate,
            entry_warning_border=player.session.config['entry_warning_border']
        )


class Instructions_GT_senders_CN(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1 and (
                    player.id_in_group in [Constants.num_senders, Constants.num_senders - 1])

    form_model = "player"
    form_fields = ["comprq1", "comprq2", "comprq3_CN", "comprq5_CN", "comprq6_CN"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            GT_receiver_payoff=player.session.config['GT_receiver_payoff'],
            GT_sender_payoff=player.session.config['GT_sender_payoff']
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq1=3,
            comprq2=2,
            comprq3_CN=1,
            comprq5_CN=3,
            comprq6_CN=3,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigieren Sie Ihre Angabe oder heben Sie Ihre Hand zur Klärung mit dem Laborpersonal.'
                if field_name == "comprq1":
                    player.error_comprq1 += 1
                if field_name == "comprq2":
                    player.error_comprq2 += 1
                if field_name == "comprq3_CN":
                    player.error_comprq3_CN += 1
                if field_name == "comprq5_CN":
                    player.error_comprq5_CN += 1
                if field_name == "comprq6_CN":
                    player.error_comprq6_CN += 1
        return error_messages



class Instructions_GT_senders_noCN(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1 and (
                    player.id_in_group not in [Constants.num_senders, Constants.num_senders - 1])

    form_model = "player"
    form_fields = ["comprq1", "comprq2", "comprq3", "comprq5", "comprq6"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            GT_receiver_payoff=player.session.config['GT_receiver_payoff'],
            GT_sender_payoff=player.session.config['GT_sender_payoff']
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq1=3,
            comprq2=2,
            comprq3=1,
            comprq5=3,
            comprq6=3,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigieren Sie Ihre Angabe oder heben Sie Ihre Hand zur Klärung mit dem Laborpersonal.'
                if field_name == "comprq1":
                    player.error_comprq1 += 1
                if field_name == "comprq2":
                    player.error_comprq2 += 1
                if field_name == "comprq3":
                    player.error_comprq3 += 1
                if field_name == "comprq5":
                    player.error_comprq5 += 1
                if field_name == "comprq6":
                    player.error_comprq6 += 1
        return error_messages



class Instructions_GT_receivers(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number == (Constants.num_rounds / 2) + 1

    form_model = "player"
    form_fields = ["comprq7", "comprq8", "comprq9", "comprq10", "comprq11", "comprq13", "comprq14"]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            GT_receiver_payoff=player.session.config['GT_receiver_payoff'],
            GT_sender_payoff=player.session.config['GT_sender_payoff']
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq7=3,
            comprq8=3,
            comprq9=3,
            comprq10=3,
            comprq11=2,
            comprq13=2,
            comprq14=4,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigieren Sie Ihre Angabe oder heben Sie Ihre Hand zur Klärung mit dem Laborpersonal.'
                if field_name == "comprq7":
                    player.error_comprq7 += 1
                if field_name == "comprq8":
                    player.error_comprq8 += 1
                if field_name == "comprq9":
                    player.error_comprq9 += 1
                if field_name == "comprq10":
                    player.error_comprq10 += 1
                if field_name == "comprq11":
                    player.error_comprq12 += 1
                if field_name == "comprq13":
                    player.error_comprq13 += 1
                if field_name == "comprq14":
                    player.error_comprq14 += 1
        return error_messages


# wait for all senders to send a signal
class StartWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_signals'

    @staticmethod
    def is_displayed(player):
        return player.round_number == (Constants.num_rounds / 2)

def set_signals(subsession: Subsession):
    players = subsession.get_players()

    if subsession.round_number == Constants.num_rounds / 2:
        all = [0,0,0,0,0,0]
        for i in list(range(1, 11, 1)):
            all_signals = []
            all_senders = []
            for p in players:
                prev_player = p.in_round(i)
                prev_players = prev_player.group.get_players()
                all_signals = [prev.sent_signal for prev in prev_players if prev.Role == 'sender']
                all_senders = [prev.id_in_group for prev in prev_players if prev.Role == 'sender']
            all = np.vstack([all, all_signals])
            all = np.vstack([all, all_senders])
            if i == 1:
                all = np.delete(all, 0, 0)
        for p in players:
            if p.Role == "receiver":
                orders = [p.session.config['signal_order_1'], p.session.config['signal_order_2'],
                          p.session.config['signal_order_3']]
                temp = [1, 2, 3] * 100
                p.signal_order = temp[p.id_in_group - 1]
                signal_order = orders[p.signal_order - 1]
                for i in list(range(0, 10, 1)):
                    fut_player = p.in_round(Constants.num_rounds/2 + i + 1)
                    fut_player.signal_order = p.signal_order
                    fut_player.received_signal_1 = int(all[2 * signal_order[i]][0])
                    fut_player.received_signal_2 = int(all[2 * signal_order[i]][1])
                    fut_player.received_signal_3 = int(all[2 * signal_order[i]][2])
                    fut_player.received_signal_4 = int(all[2 * signal_order[i]][3])
                    fut_player.received_signal_5 = int(((all[2 * signal_order[i]][4]) + fut_player.received_signal_4)/2)
                    fut_player.received_signal_6 = int(((all[2 * signal_order[i]][5]) + fut_player.received_signal_4)/2)
                    fut_player.true_state = p.session.config['True_state'][signal_order[i]]


class Filler_Task(Page):
    form_model = "player"
    form_fields = ["q"+str(i) for i in range(1, 26)]


    @staticmethod
    def is_displayed(player):
        return (player.Role == "receiver" and player.round_number == 1) or (player.Role == "sender" and player.round_number == Constants.num_rounds/2 + 1)






# the receiver observes all the signals sent by senders and states a guess/posterior
# Receivers see signals sent by senders in a random order and with known group identity
class Guess(Page):
    timeout_seconds = 240
    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((player.true_state  - player.posterior), 2)
        if diff <= player.subsession.x:
            player.payoff = player.session.config['GT_receiver_payoff']
        else:
            player.payoff = 0

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            signal_1=player.received_signal_1,
            signal_2=player.received_signal_2,
            signal_3=player.received_signal_3,
            signal_4=player.received_signal_4,
            signal_5=player.received_signal_5,
            signal_6=player.received_signal_6,
            round=player.round_number - 10
        )


    form_model = "player"
    form_fields = ["posterior"]

    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number > Constants.num_rounds/2

    @staticmethod
    def js_vars(player: Player):
        return dict(
            round=player.round_number - Constants.num_rounds/2,
        )

class SecondWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'save_signals_payoff'
    @staticmethod
    def is_displayed(player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if player.Role == "receiver":
            return upcoming_apps[1]


def save_signals_payoff(subsession: Subsession):
    players = subsession.get_players()
    signals_all_rounds = []
    estimates_all_rounds = []

    for i in list(range(0, int(Constants.num_rounds / 2))):
        for p in players:
            if p.Role == 'sender':
                prev_player = p.in_round(i + 1)
                signals_all_rounds.append(prev_player.field_maybe_none('sent_signal'))
                estimates_all_rounds.append(prev_player.estimate)
    # Payoff calculation
    for p in players:
        participant = p.participant
        participant.estimates_all_rounds = estimates_all_rounds
        participant.signals_all_rounds = signals_all_rounds
        if p.Role == "sender":
            i = random.randint(1, int(Constants.num_rounds / 2))
            p.chosen_round = i
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff
        if p.Role == "receiver":
            i = random.randint(int(Constants.num_rounds / 2) + 1, Constants.num_rounds)
            p.chosen_round = i
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff


page_sequence = [Instructions_GT_senders_CN, Instructions_GT_senders_noCN, Signals, Filler_Task,
                 Instructions_GT_receivers, StartWaitPage, Guess, SecondWaitPage]
