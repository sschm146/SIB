from otree.api import *
import numpy as np
import random

c = Currency

doc = """
GuessingTask_noSI_SB
"""


class Constants(BaseConstants):
    name_in_url = "GuessingTask_noSI_SB"
    num_rounds = 20
    players_per_group = None
    num_senders = 6
    true_state = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sd = 3


class Subsession(BaseSubsession):
    x = models.IntegerField()
    censored_signal = models.StringField()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    sent_signal = models.IntegerField()  # signal sent by the sender
    estimate = models.IntegerField()  # the estimate sent by the estimation device which is observed by senders
    posterior = models.FloatField()  # the posterior belief of the receiver
    true_state = models.IntegerField()
    SB_sender_4 = models.StringField()
    signal_order = models.IntegerField()
    SB_received_signal_1 = models.IntegerField()  # saving received signals across rounds for analyses
    SB_received_signal_2 = models.IntegerField()  # saving received signals across rounds for analyses
    SB_received_signal_3 = models.IntegerField()  # saving received signals across rounds for analyses
    SB_received_signal_4 = models.IntegerField()  # saving received signals across rounds for analyses
    comprq1 = models.IntegerField(choices=[[1,
                                            'The estimate of a randomly drawn estimation device is equally likely to be the correct number x or any other number.'],
                                           [2,
                                            'The estimate of a randomly drawn estimation device is less likely to be '
                                            'the correct number x than any other number, and the further one moves away '
                                            'from x, the more likely it is that an estimation device reports such a number.'],
                                           [3,
                                            'The estimate of a randomly drawn estimation device is more likely to be '
                                            'the correct number x than any other number, and the further one moves away '
                                            'from x, the less likely it is that an estimation device reports such a number.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq2 = models.IntegerField(choices=[
        [1, 'The average of estimates of all the estimation devices can be any number with equal probability.'],
        [2,
         'The average of estimates of all the estimation devices corresponds exactly (or almost exactly) to number x'],
        [3, 'The average of estimates of all the estimation devices will always be larger than number x.'],
        [4, 'The average of estimates of all the estimation devices will always be smaller than number x.']],
        widget=widgets.RadioSelect,
        label='')
    comprq3 = models.IntegerField(choices=[[1, 'I will observe an estimate of 1 randomly drawn estimation device.'],
                                           [2, 'I will observe the estimates of 3 randomly drawn estimation devices.'],
                                           [3,
                                            'I will observe the actual number x and the estimate of 1 randomly drawn estimation device.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq4 = models.IntegerField(choices=[[1, 'A randomly drawn estimation device shows me an estimate of 490.'],
                                           [2, 'A randomly drawn estimation device shows me an estimate of 541.'],
                                           [3, 'A randomly drawn estimation device shows me an estimate of 555.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq5 = models.IntegerField(choices=[[1, '9'],
                                           [2, '18'],
                                           [3, '19'],
                                           [4, '24']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq6 = models.IntegerField(
        choices=[[1, 'All parts of the experiment in which additional money can be earned will be paid out.'],
                 [2,
                  'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. '
                  'If it happens that part 2 is chosen, then the earnings from each of the 10 estimation tasks will be paid out.'],
                 [3,
                  'Only one of the parts in which additional money can be earned will be randomly chosen and paid out. '
                  'If it happens that part 2 is chosen, then one of the 10 estimation tasks will be randomly chosen, and my additional payment will depend only on my precision on that particular estimation task.']],
        widget=widgets.RadioSelect,
        label='')
    comprq7 = models.IntegerField(choices=[[1, 'Each sender observed an estimate of 1 randomly drawn estimation device.'],
                                           [2, 'Each sender observed an estimate of 3 randomly drawn estimation devices.'],
                                           [3, 'Each sender observed an estimate of an actual number x and the estimate of 1 randomly drawn estimation device.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq8 = models.IntegerField(choices=[[1, 'I will observe the estimates of 6 senders. The senders’ names will not be shown.'],
                                           [2, 'I will observe the estimates of 5 senders.This includes Sender A, Sender B, Sender C, and 2 out of the following 3 senders: '
                                               'Sender D, Sender E, and Sender F. '
                                               'The senders’ names and group affiliation will be shown. '
                                               'From senders D, E, and F, I will always observe the two lowest estimates. '
                                               'The highest of those 3 estimates is on average y higher than the second highest estimates.'],
                                           [3, 'I will observe the estimates of 5 senders.This includes Sender A, Sender B, Sender C, and 2 out of the following 3 senders: '
                                               'Sender D, Sender E, and Sender F. '
                                               'The senders’ names and group affiliation will be shown. '
                                               'From senders D, E, and F, I will always observe the two highest estimates. '
                                               'The lowest of those 3 estimates is on average y-2 lower than the second lowest estimate.'],
                                           [4, 'I will observe the estimates of 5 senders. '
                                               'This includes Sender A, Sender B, Sender C, and 2 out of the following 3 senders: '
                                               'Sender D, Sender E, and Sender F. The senders’ names and group affiliation will be shown. '
                                               'From senders D, E, and F, I will always observe the two lowest estimates. '
                                               'The highest of those 3 estimates is on average y higher than the second highest estimates.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq9 = models.IntegerField(choices=[[1, 'The estimate of a randomly drawn estimation device is equally likely to be the correct number x or any other number'],
                                           [2, 'The estimate of a randomly drawn estimation device is less likely to be the correct number x than any other number, and the further one moves away from x, the more likely it is that an estimation device reports such a number'],
                                           [3, 'The estimate of a randomly drawn estimation device is more likely to be the correct number x than any other number, and the further one moves away from x, the less likely it is that an estimation device reports such a number']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq10 = models.IntegerField(choices=[[1, 'The average of estimates of all the estimation devices can be any number with equal probability.'],
                                           [2, 'The average of estimates of all the estimation devices corresponds exactly (or almost exactly) to number x.'],
                                           [3, 'The average of estimates of all the estimation devices will always be larger than number x.'],
                                           [4, 'The average of estimates of all the estimation devices will always be smaller than number x.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq11 = models.IntegerField(choices=[[1, 'A sender’s randomly drawn estimation device showed an estimate of 490.'],
                                           [2, 'A sender’s randomly drawn estimation device showed an estimate of 541.'],
                                           [3, 'A sender’s randomly drawn estimation device showed an estimate of 555.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq12 = models.IntegerField(choices=[[1, '9'],
                                           [2, '18'],
                                           [3, '19'],
                                           [4, '24']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq13 = models.IntegerField(choices=[[1, '1490'],
                                           [2, '1520'],
                                           [3, '1521'],
                                           [4, '1525']],
                                  widget=widgets.RadioSelect,
                                  label='')

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
    q9 = models.IntegerField(label='')
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
                 [2, "Ich musste während meines Studiums lernen, mit dem Geld umzugehen.."],
                 [3, "Ich habe Mühe, das lebensnotwendige Dinge zu kaufen"],
                 [4, "Ich kann mir alles leisten, aber ich haushalte nicht."]],
        widget=widgets.RadioSelect, label=''
    )
    q14 = models.IntegerField(
        choices=[[1, "Keine Haushaltsplanung"],
                 [2, "Kosten für lebensnotwendige Dinge zu hoch"],
                 [3, "Zu sorglos mit Geld"],
                 [4, "Andere Prioritäten wie Shopping und Nachtleben haben Vorrang"],
                 [5, "Ich habe keine Schwierigkeiten"],
                 [6, "Ich bin gut im Haushalten"],
                 [7, "Ich wei? es nicht"]],
        widget=widgets.RadioSelect, label=''
    )
    q15 = models.StringField(label='')
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
    q23 = models.StringField(label='', blank=True)
    q24 = models.StringField(label='')
    q25 = models.StringField(label='')



# FUNCTIONS

#roles allocation and mu_signals (true) simulaion for each sender
def creating_session(subsession: Subsession):
    players = subsession.get_players()
    subsession.x = random.randint(0, 50)
    for p in players: #Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.Role = participant.Role
        if p.Role == "sender":
            if p.round_number <= Constants.num_rounds / 2:
                p.estimate = p.session.config['Signals'][p.id_in_group - 1][p.round_number - 1]
                p.true_state = p.session.config['True_state'][p.round_number - 1]
            else:
                p.true_state = p.session.config['True_state'][int(p.round_number - Constants.num_rounds / 2) - 1]



# PAGES

# senders see estimate and send signal
class Signals(Page):
    form_model = "player"
    form_fields = ["sent_signal"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((Constants.true_state[int(player.round_number) - 1] - player.sent_signal), 2)
        if diff <= player.subsession.x:
            player.payoff = player.session.config['GT_receiver_payoff']
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
            round=round
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            round=player.round_number,
        )


class Instructions_GT_senders(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1


    form_model = "player"
    form_fields = ["comprq1", "comprq2", "comprq3", "comprq4", "comprq5", "comprq6"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq1=3,
            comprq2=2,
            comprq3=1,
            comprq4=2,
            comprq5=3,
            comprq6=3,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigiere deine Angabe oder hebe deine Hand zur Klärung mit dem Laborpersonal.'

        return error_messages


class Instructions_GT_receivers(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver" and player.round_number == (Constants.num_rounds / 2) + 1


    form_model = "player"
    form_fields = ["comprq7", "comprq8", "comprq9", "comprq10", "comprq11", "comprq12", "comprq13"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq7=1,
            comprq8=3,
            comprq9=2,
            comprq10=2,
            comprq11=2,
            comprq12=3,
            comprq13=2,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigiere deine Angabe oder hebe deine Hand zur Klärung mit dem Laborpersonal.'

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
                orders = [p.session.config['signal_order_1'], p.session.config['signal_order_2'], p.session.config['signal_order_3']]
                p.signal_order = random.choice(range(len(orders)))
                signal_order = orders[p.signal_order]
                for i in list(range(0, 10, 1)):
                    fut_player = p.in_round(Constants.num_rounds/2 + i + 1)
                    fut_player.signal_order = p.signal_order
                    fut_player.SB_received_signal_1 = int(all[2 * signal_order[i]][0])
                    fut_player.SB_received_signal_2 = int(all[2 * signal_order[i]][1])
                    fut_player.SB_received_signal_3 = int(all[2 * signal_order[i]][2])
                    SB_list = [int(all[2 * signal_order[i]][3]), int(all[2 * signal_order[i]][4]), int(all[2 * signal_order[i]][5])]
                    fut_player.SB_received_signal_4 = max(SB_list)
                    fut_player.SB_sender_4 = all[2 * signal_order[i] + 1][SB_list.index(fut_player.SB_received_signal_4)]
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
    @staticmethod
    def before_next_page(player, timeout_happened):
        diff = pow((Constants.true_state[int(player.round_number - Constants.num_rounds / 2) - 1] - player.posterior), 2)
        if diff <= player.subsession.x:
            player.payoff = player.session.config['GT_receiver_payoff']
        else:
            player.payoff = 0

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
                signal_1=player.SB_received_signal_1,
                signal_2=player.SB_received_signal_2,
                signal_3=player.SB_received_signal_3,
                signal_4=player.SB_received_signal_4,
                sender_4=player.SB_sender_4,
                round=player.round_number-10
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
    for i in list(range(1, 11, 1)):
        for p in players:
            prev_player = p.in_round(i)
            prev_players = prev_player.group.get_players()
        signals_1_3 = [prev.sent_signal for prev in prev_players if prev.Role == 'sender' and prev.id_in_group <= 3]
        pre_signals_4_6 = [prev.sent_signal for prev in prev_players if prev.Role == 'sender' and prev.id_in_group > 3]
        max_signal = max(pre_signals_4_6)
        max_index = pre_signals_4_6.index(max_signal)
        signals_4_6 = ['-', '-', '-']
        signals_4_6[max_index] = pre_signals_4_6[max_index]
        pre = signals_1_3 + signals_4_6
        signals_all_rounds.extend(pre)
        estimates_all_rounds.append(prev_player.field_maybe_none('estimate'))
    # Payoff calculation
    for p in players:
        participant = p.participant
        participant.estimates_all_rounds = estimates_all_rounds
        participant.signals_all_rounds = signals_all_rounds
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


page_sequence = [Instructions_GT_senders, Signals, Filler_Task, Instructions_GT_receivers, StartWaitPage,
                 Guess, SecondWaitPage]
