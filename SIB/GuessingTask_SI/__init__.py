from otree.api import *
import numpy as np
import random


c = Currency

doc = """
GuessingTask_noSI
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_SI"
    num_rounds = 22
    players_per_group = None
    num_senders = 6


class Subsession(BaseSubsession):
    x = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    identity = models.StringField()  # the identity from the previous apps
    sent_signal = models.IntegerField(min=0, max=1000)  # signal sent by the sender
    estimate = models.IntegerField()  # the estimate sent by the estimation device which is observed by senders
    posterior = models.FloatField(min=0, max=1000)  # the posterior belief of the receiver
    true_state = models.IntegerField()
    signal_order = models.IntegerField()
    chosen_round = models.IntegerField()
    received_signal_1 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_2 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_3 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_4 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_5 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_6 = models.IntegerField() #saving received signals across rounds for analyses
    received_signal_1_identity = models.StringField() #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_2_identity = models.StringField() #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_3_identity = models.StringField() #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_4_identity = models.StringField() #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_5_identity = models.StringField() #saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
    received_signal_6_identity = models.StringField()#saving senders identity across rounds for analyses - 1 if sender and receiver have same identity
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
    comprq3 = models.IntegerField(
        choices=[[1, 'Ich werde die Schätzung von 1 zufällig gezogenen Schätzgerät beobachten.'],
                 [2, 'Ich werde die Schätzungen von 2 zufällig gezogenen Schätzgeräten beobachten.'],
                 [3, 'Ich werde die Schätzungen von 3 zufällig gezogenen Schätzgeräten beobachten.']],
        widget=widgets.RadioSelect,
        label='')
    comprq4 = models.IntegerField(choices=[[1, 'A randomly drawn estimation device shows me an estimate of 490.'],
                                           [2, 'A randomly drawn estimation device shows me an estimate of 541.'],
                                           [3, 'A randomly drawn estimation device shows me an estimate of 555.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq5 = models.IntegerField(label='')
    comprq6 = models.IntegerField(
        choices=[[1, 'Meine Chancen auf die zusätzliche Auszahlung von 13€ sind so am höchsten. '],
                 [2, 'Dies hat keinen Einfluss auf meine Auszahlung.'],
                 [3, 'Meine Chancen auf die zusätzliche Auszahlung von 13€ sind sehr gering.']],
        widget=widgets.RadioSelect,
        label='')
    comprq7 = models.IntegerField(
        choices=[[1, 'Jeder Sender hat eine Schätzung von 1 zufällig gezogenen Schätzgerät beobachtet.'],
                 [2, 'Jeder Sender hat eine Schätzung von 2 zufällig gezogenen Schätzgeräten beobachtet.'],
                 [3, 'Jeder Sender hat eine Schätzung von 3 zufällig gezogenen Schätzgeräten beobachtet.']],
        widget=widgets.RadioSelect,
        label='')
    comprq8 = models.IntegerField(
        choices=[[1, 'Ich werde die Schätzung von 1 zufällig gezogenen Schätzgerät beobachten.'],
                 [2, 'Ich werde die Schätzungen von 6 zufällig gezogenen Schätzgeräten beobachten.'],
                 [3,
                  'Ich werde die Schätzungen von 6 Sendern beobachten: Sender A, Sender B, Sender C, Sender D, Sender E, und Sender F.']],
        widget=widgets.RadioSelect,
        label='')
    comprq8_2 = models.IntegerField(
        choices=[[1, 'Sender A, Sender E und Sender F sind Mitglieder der Gruppe Blau, während Sender D, Sender B und Sender C Mitglieder der Gruppe Gelb sind.'],
                 [2, 'Sender D, Sender B und Sender F sind Mitglieder der Gruppe Blau, während Sender A, Sender E und Sender C Mitglieder der Gruppe Gelb sind.'],
                 [3, 'Sender A, Sender B und Sender C sind Mitglieder der Gruppe Blau, während Sender D, Sender E und Sender F Mitglieder der Gruppe Gelb sind.']],
        widget=widgets.RadioSelect,
        label='')
    comprq9 = models.IntegerField(choices=[[1, 'Die Schätzung eines zufällig gezogenen Schätzgeräts kann mit gleicher Wahrscheinlichkeit der Zahl x oder einer andere Zahl entsprechen.'],
                                           [2, 'Die Schätzung eines zufällig gezogenen Schätzgeräts entspricht mit geringerer Wahrscheinlichkeit der Zahl x als jeder anderen Zahl. '
                                            'Je weiter man sich von der Zahl x entfernt, desto wahrscheinlicher ist es, dass ein Schätzgerät eine solche Schätzung angibt.'],
                                           [3, 'Die Schätzung eines zufällig gezogenen Schätzgeräts entspricht mit größerer Wahrscheinlichkeit der Zahl x als jeder anderen Zahl. '
                                            'Je weiter man sich von der Zahl x entfernt, desto unwahrscheinlicher ist es, dass ein Schätzgerät eine solche Schätzung angibt.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq10 = models.IntegerField(choices=[[1,
                                             'Der Durchschnitt der Schätzungen aller Schätzgeräte entspricht mit gleicher Wahrscheinlichkeit entweder der Zahl x oder jeder beliebigen anderen Zahl.'],
                                            [2,
                                             'Der Durchschnitt der Schätzungen aller Schätzgeräte entspricht genau (oder fast genau) der Zahl x.'],
                                            [3,
                                             'Der Durchschnitt der Schätzungen aller Schätzgeräte ist immer größer als die Zahl x.'],
                                            [4,
                                             'Der Durchschnitt der Schätzungen aller Schätzgeräte ist immer kleiner als die Zahl x.']],
                                   widget=widgets.RadioSelect,
                                   label='')
    comprq11 = models.IntegerField(
        choices=[[1, 'A sender’s randomly drawn estimation device showed an estimate of 490.'],
                 [2, 'A sender’s randomly drawn estimation device showed an estimate of 541.'],
                 [3, 'A sender’s randomly drawn estimation device showed an estimate of 555.']],
        widget=widgets.RadioSelect,
        label='')
    comprq12 = models.IntegerField(label='')
    comprq13 = models.IntegerField(choices=[[1, '0%'],
                                            [2, '50%'],
                                            [3, '67%'],
                                            [4, '100%']],
                                   widget=widgets.RadioSelect,
                                   label='')
    comprq14 = models.IntegerField(
        choices=[[1, 'All parts of the experiment in which additional money can be earned will be paid out.'],
                 [2,
                  'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. '
                  'If it happens that part 3 is chosen, then the earnings from each of the 10 estimation tasks will be paid out.'],
                 [3,
                  'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. If it happens that part 3 is chosen, then one of the 10 estimation tasks will be randomly chosen, and my additional payment will depend only on my precision on that particular estimation task.']],
        widget=widgets.RadioSelect,
        label='')
    comprq15 = models.IntegerField(
        choices=[[1, 'Die Zahlen aus der aktuellen Schätzaufgaben sind abhängig von allen vorherigen Schätzaufgaben. '
                     'Zahlen aus allen vorherigen Schätzaufgaben sollte ich daher in meinen Entscheidungsprozess miteinfliesen lassen.'],
                 [2, 'Die Zahlen aus der aktuellen Schätzaufgaben sind abhängig von der letzten Schätzaufgabe. '
                     'Zahlen aus der letzten Schätzaufgabe sollte ich daher in meinen Entscheidungsprozess miteinfliesen lassen.'],
                 [3, 'Alle 11 Schätzaufgaben haben zwar die gleiche Struktur, sind aber völlig unabhängig voneinander. '
                     'Das bedeutet, dass die Zahl x, die Schätzungen der Schätzgeräte und die Schätzungen der Sender über die 11 Schätzaufgaben hinweg in keiner Weise miteinander verbunden sind. '
                     'Die Zahl x, die Schätzungen der Schätzgeräte und die Schätzungen der Sender sind ausschließlich für die jeweils aktuelle Schätzaufgabe von Bedeutung.']],
        widget=widgets.RadioSelect,
        label='')
    comprq15_sender = models.IntegerField(
        choices=[[1, 'Die Zahlen aus der aktuellen Schätzaufgaben sind abhängig von allen vorherigen Schätzaufgaben. '
                     'Zahlen aus allen vorherigen Schätzaufgaben sollte ich daher in meinen Entscheidungsprozess miteinfliesen lassen.'],
                 [2, 'Die Zahlen aus der aktuellen Schätzaufgaben sind abhängig von der letzten Schätzaufgabe. '
                     'Zahlen aus der letzten Schätzaufgabe sollte ich daher in meinen Entscheidungsprozess miteinfliesen lassen.'],
                 [3, 'Alle 11 Schätzaufgaben haben zwar die gleiche Struktur, sind aber völlig unabhängig voneinander. '
                     'Das bedeutet, dass die Zahl x und die Schätzungen der Schätzgeräte über die 11 Schätzaufgaben hinweg in keiner Weise miteinander verbunden sind. '
                     'Die Zahl x und die Schätzungen der Schätzgeräte sind ausschließlich für die jeweils aktuelle Schätzaufgabe von Bedeutung.']],
        widget=widgets.RadioSelect,
        label='')
    error_comprq15_sender = models.IntegerField(initial=0)
    error_comprq1 = models.IntegerField(initial=0)
    error_comprq2 = models.IntegerField(initial=0)
    error_comprq3 = models.IntegerField(initial=0)
    error_comprq5 = models.IntegerField(initial=0)
    error_comprq6 = models.IntegerField(initial=0)
    error_comprq7 = models.IntegerField(initial=0)
    error_comprq8 = models.IntegerField(initial=0)
    error_comprq8_2 = models.IntegerField(initial=0)
    error_comprq9 = models.IntegerField(initial=0)
    error_comprq10 = models.IntegerField(initial=0)
    error_comprq12 = models.IntegerField(initial=0)
    error_comprq13 = models.IntegerField(initial=0)
    error_comprq14 = models.IntegerField(initial=0)
    error_comprq15 = models.IntegerField(initial=0)
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
    q24 = models.LongStringField(label='', blank=True)
    q25 = models.LongStringField(label='', blank=True)


# FUNCTIONS

#roles allocation and mu_signals (true) simulation for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        subsession.x = random.randint(0, p.session.config['QSR_cutoff']) #Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.Role = participant.Role
        if p.Role == "sender":
            if p.round_number <= Constants.num_rounds / 2:
                p.estimate = p.session.config['Signals'][p.id_in_group - 1][p.round_number - 1]
                p.true_state = p.session.config['True_state'][p.round_number - 1]
            else:
                p.true_state = p.session.config['True_state'][int(p.round_number - Constants.num_rounds / 2) - 1]
        p.identity = participant.identity


# PAGES

class Next_Round(Page):
    @staticmethod
    def is_displayed(player):
        return (player.Role == "sender" and player.round_number > 1 and player.round_number <= Constants.num_rounds/2) or (player.Role == "receiver" and player.round_number > Constants.num_rounds/2 + 1)

    @staticmethod
    def vars_for_template(player: Player):
        if player.Role == "sender":
            return dict(
                round=player.round_number,
                last_round=player.round_number - 1,
                role=player.Role
            )
        if player.Role == "receiver":
            return dict(
                round=player.round_number - int(Constants.num_rounds/2),
                last_round=player.round_number - 1 - int(Constants.num_rounds/2),
                role=player.Role
            )
# senders see estimate and send signal
class Signals(Page):
    form_model = "player"
    form_fields = ["sent_signal"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((player.true_state - player.sent_signal), 2)
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

class Instructions_GT_senders(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1

    form_model = "player"
    form_fields = ["comprq1", "comprq2", "comprq3", "comprq5", "comprq6", "comprq15_sender"]

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        identity = participant.identity
        return dict(
            identity=identity,
            GT_receiver_payoff=player.session.config['GT_receiver_payoff'],
            GT_sender_payoff=player.session.config['GT_sender_payoff']
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq1=3,
            comprq2=2,
            comprq3=1,
            comprq5=190,
            comprq6=3,
            comprq15_sender=3,
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
                if field_name == "comprq15_sender":
                    player.error_comprq15_sender += 1
        return error_messages


class Instructions_GT_receivers(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number == (Constants.num_rounds / 2) + 1

    form_model = "player"
    form_fields = ["comprq7", "comprq8","comprq8_2", "comprq9", "comprq10",  "comprq12", "comprq13", "comprq15"]

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        identity = participant.identity
        return dict(
            identity=identity,
            GT_receiver_payoff=player.session.config['GT_receiver_payoff'],
            GT_sender_payoff=player.session.config['GT_sender_payoff'],
            GT_guess_time=int(player.session.config['GT_guess_time']/60)
        )

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq7=1,
            comprq8=3,
            comprq8_2=3,
            comprq9=3,
            comprq10=2,
            comprq12=190,
            comprq13=4,
            comprq15=3,
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
                if field_name == "comprq8_2":
                    player.error_comprq8_2 += 1
                if field_name == "comprq9":
                    player.error_comprq9 += 1
                if field_name == "comprq10":
                    player.error_comprq10 += 1
                if field_name == "comprq12":
                    player.error_comprq12 += 1
                if field_name == "comprq13":
                    player.error_comprq13 += 1
                if field_name == "comprq15":
                    player.error_comprq15 += 1
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
        for i in list(range(1, 12, 1)):
            all_signals = []
            all_senders = []
            all_identities = []
            for p in players:
                prev_player = p.in_round(i)
                prev_players = prev_player.group.get_players()
                all_signals = [prev.sent_signal for prev in prev_players if prev.Role == 'sender']
                all_senders = [prev.id_in_group for prev in prev_players if prev.Role == 'sender']
                all_identities = [prev.identity for prev in prev_players if prev.Role == 'sender']
            all = np.vstack([all, all_signals])
            all = np.vstack([all, all_senders])
            all = np.vstack([all, all_identities])
            if i == 1:
                all = np.delete(all, 0, 0)

        for p in players:
            if p.Role == "receiver":
                orders = [p.session.config['signal_order_1'], p.session.config['signal_order_2'],
                          p.session.config['signal_order_3']]
                temp = [1, 2, 3] * 100
                p.signal_order = temp[p.id_in_group - 1]
                signal_order = orders[p.signal_order - 1]
                for i in list(range(0, 11, 1)):
                    fut_player = p.in_round(Constants.num_rounds/2 + i + 1)
                    fut_player.signal_order = p.signal_order
                    fut_player.received_signal_1 = int(all[3 * signal_order[i]][0])
                    fut_player.received_signal_2 = int(all[3 * signal_order[i]][1])
                    fut_player.received_signal_3 = int(all[3 * signal_order[i]][2])
                    fut_player.received_signal_4 = int(all[3 * signal_order[i]][3])
                    fut_player.received_signal_5 = int(all[3 * signal_order[i]][4])
                    fut_player.received_signal_6 = int(all[3 * signal_order[i]][5])
                    fut_player.received_signal_1_identity = all[3 * signal_order[i] + 2][0]
                    fut_player.received_signal_2_identity = all[3 * signal_order[i] + 2][1]
                    fut_player.received_signal_3_identity = all[3 * signal_order[i] + 2][2]
                    fut_player.received_signal_4_identity = all[3 * signal_order[i] + 2][3]
                    fut_player.received_signal_5_identity = all[3 * signal_order[i] + 2][4]
                    fut_player.received_signal_6_identity = all[3 * signal_order[i] + 2][5]
                    fut_player.true_state = p.session.config['True_state'][signal_order[i]]


class Filler_Task(Page):
    form_model = "player"
    form_fields = ["q"+str(i) for i in range(1, 26)]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            Questionnaire_payoff=player.session.config['Questionnaire_payoff']
        )

    @staticmethod
    def is_displayed(player):
        return (player.Role == "receiver" and player.round_number == 1) or (player.Role == "sender" and player.round_number == Constants.num_rounds/2 + 1)


# the receiver observes all the signals sent by senders and states a guess/posterior
# Receivers see signals sent by senders in a random order and with known group identity
class Guess(Page):
    timeout_seconds = 240
    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((player.true_state - player.posterior), 2)
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
                round=player.round_number - int(Constants.num_rounds/2)
            )

    form_model = "player"
    form_fields = ["posterior"]

    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number > Constants.num_rounds/2

    @staticmethod
    def js_vars(player: Player):
        return dict(
            round=player.round_number - Constants.num_rounds / 2,
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
    for p in players:
        for i in list(range(1, int(Constants.num_rounds + 1))):
            prev_player = p.in_round(i)
            prev_player.payoff = 0


page_sequence = [Instructions_GT_senders, Next_Round, Signals, Filler_Task, Instructions_GT_receivers, StartWaitPage,
                 Guess, SecondWaitPage]
