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
    true_state = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    sd = 3


class Subsession(BaseSubsession):
    x = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Role = models.StringField()
    sent_signal = models.IntegerField()  # signal sent by the sender
    estimate = models.IntegerField()  # the estimate sent by the estimation device which is observed by senders
    posterior = models.FloatField()  # the posterior belief of the receiver
    true_state = models.IntegerField()
    received_signal_1 = models.IntegerField()
    received_signal_2 = models.IntegerField()
    received_signal_3 = models.IntegerField()
    received_signal_4 = models.IntegerField()
    received_signal_5 = models.IntegerField()
    received_signal_6 = models.IntegerField()
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
    comprq3_noCN = models.IntegerField(
        choices=[[1, 'I will observe an estimate of 1 randomly drawn estimation device.'],
                 [2, 'I will observe the estimates of 2 randomly drawn estimation devices.'],
                 [3, 'I will observe the estimates of 3 randomly drawn estimation devices.']],
        widget=widgets.RadioSelect,
        label='')
    comprq4_noCN = models.IntegerField(
        choices=[[1, 'A randomly drawn estimation device shows me an estimate of 490.'],
                 [2, 'A randomly drawn estimation device shows me an estimate of 541.'],
                 [3, 'A randomly drawn estimation device shows me an estimate of 555.']],
        widget=widgets.RadioSelect,
        label='')
    comprq5_noCN = models.IntegerField(choices=[[1, '9'],
                                                [2, '18'],
                                                [3, '19'],
                                                [4, '24']],
                                       widget=widgets.RadioSelect,
                                       label='')
    comprq3_CN = models.IntegerField(
        choices=[[1, 'I will observe the average estimate of 2 randomly drawn estimation devices.'],
                 [2, 'I will observe the estimates of 3 randomly drawn estimation device.'],
                 [3, 'I will observe the actual number x and the estimate of 1 randomly drawn estimation device.']],
        widget=widgets.RadioSelect,
        label='')
    comprq4_CN = models.IntegerField(
        choices=[[1, 'The average estimate of the two randomly drawn estimation devices I observe is 490.'],
                 [2, 'The average estimate of the two randomly drawn estimation devices I observe is 541.'],
                 [3, 'The average estimate of the two randomly drawn estimation devices I observe is 555.']],
        widget=widgets.RadioSelect,
        label='')
    comprq5_CN = models.IntegerField(choices=[[1, '9'],
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
                                           [2, 'Senders A and B observed an estimate of 1 randomly drawn estimation device. '
                                               'Senders C, D, E, and F observed an average estimate of two estimation devices: '
                                               'one estimation device was randomly drawn for each of the two senders, and the other estimation device was the same device assigned to Sender B'],
                                           [3, 'Senders A, B, C, and D observed an estimate of 1 randomly drawn estimation device. '
                                               'Senders E and F observed an average estimate of two estimation devices: '
                                               'one estimation device was randomly drawn for each of the senders, and the other estimation device was the same device assigned to Sender D.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq8 = models.IntegerField(choices=[[1, '307'],
                                           [2, '310'],
                                           [3, '311'],
                                           [4, '312']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq9 = models.IntegerField(choices=[[1, 'I will observe an estimate of 1 randomly drawn estimation device.'],
                                           [2, 'I will observe an estimate of 6 randomly drawn estimation devices.'],
                                           [3, 'I will observe the estimates of 6 senders. The senders will not be identified with names.'],
                                           [4, 'I will observe the estimates of 6 senders. The senders will be identified with names: Sender A, Sender B, Sender C, Sender D, Sender E, and Sender F.']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq10 = models.IntegerField(choices=[[1, 'The estimate of a randomly drawn estimation device is equally likely to be the correct number x or any other number.'],
                                           [2, 'The estimate of a randomly drawn estimation device is less likely to be the correct number x than any other number, and the further one moves away from x, the more likely it is that an estimation device reports such a number.'],
                                           [3, 'The estimate of a randomly drawn estimation device is more likely to be the correct number x than any other number, and the further one moves away from x, the less likely it is that an estimation device reports such a number']],
                                  widget=widgets.RadioSelect,
                                  label='')
    comprq11 = models.IntegerField(choices=[[1, 'The average of estimates of all the estimation devices can be any number with equal probability.'],
                                           [2, 'The average of estimates of all the estimation devices corresponds exactly (or almost exactly) to number x.'],
                                           [3, 'The average of estimates of all the estimation devices will always be larger than number x.'],
                                            [4, 'The average of estimates of all the estimation devices will always be smaller than number x.']],
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
    comprq14 = models.IntegerField(choices=[[1, '1490'],
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
                 [5, ""], ],
        widget=widgets.RadioSelect, label=''
    )
    q4 = models.IntegerField(
        choices=[[0, ""],
                 [1, ""],
                 [2, ""],
                 [3, ""],
                 [4, ""],
                 [5, ""], ],
        widget=widgets.RadioSelect, label=''
    )
    q5 = models.IntegerField(
        choices=[[0, "Weiblich"],
                 [1, "Mänlich"],
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
        choices=[[1, "Poor"],
                 [2, "Average"],
                 [3, "Good"],
                 [4, "Excellent"]],
        widget=widgets.RadioSelect, label=''
    )
    q11 = models.IntegerField(
        choices=[[1, "Poor"],
                 [2, "Average"],
                 [3, "Good"],
                 [4, "Excellent"]],
        widget=widgets.RadioSelect, label=''
    )
    q12 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
    )
    q13 = models.IntegerField(
        choices=[[1, "I’ve always known how to budget"],
                 [2, "I’ve had to learn to budget whilst at University"],
                 [3, "I struggle to purchase necessities"],
                 [4, "I can afford everything but I don’t budget"]],
        widget=widgets.RadioSelect, label=''
    )
    q14 = models.IntegerField(
        choices=[[1, "Not budgeting"],
                 [2, "Cost of necessities too expensive"],
                 [3, "Too care-free with money"],
                 [4, "Other priorities such as shopping & nightlife take a priority"],
                 [5, "I don’t struggle"],
                 [6, " I’m good with budgeting"],
                 [7, " I have no idea"]],
        widget=widgets.RadioSelect, label=''
    )
    q15 = models.StringField(label='')
    q16 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
    )
    q17 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
    )
    q18 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
    )
    q19 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
    )
    q20 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
    )
    q21 = models.IntegerField(
        choices=[[1, "Yes"],
                 [2, "No"]],
        widget=widgets.RadioSelect, label=''
    )
    q22 = models.IntegerField(
        choices=[[1, "Student Union"],
                 [2, "Parents"],
                 [3, "Friends"],
                 [4, "Bank"],
                 [5, "Financial adviser"],
                 [6, "Other"]],
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
    estimates = np.random.normal(Constants.true_state[subsession.round_number - 1], Constants.sd, Constants.num_senders)
    estimates = np.rint(estimates)
    for p in players: #Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.Role = participant.Role
        if p.Role == "sender":
            if p.id_in_group == Constants.num_senders:
                p.estimate = (estimates[Constants.num_senders - 1 - 2] + estimates[Constants.num_senders - 1]) / 2
            elif p.id_in_group == Constants.num_senders - 1:
                p.estimate = (estimates[Constants.num_senders - 1 - 2] + estimates[Constants.num_senders - 1 - 1]) / 2
            else:
                p.estimate = estimates[p.id_in_group - 1]
        if p.round_number <= Constants.num_rounds / 2:
            p.true_state = Constants.true_state[subsession.round_number - 1]
        else:
            p.true_state = Constants.true_state[int(subsession.round_number - Constants.num_rounds / 2) - 1]


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


class Instructions_GT_senders_CN(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1 and (
                    player.id_in_group in [Constants.num_senders, Constants.num_senders - 1])

    form_model = "player"
    form_fields = ["comprq1", "comprq2", "comprq3_CN", "comprq4_CN", "comprq5_CN", "comprq6"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq1=3,
            comprq2=2,
            comprq3_CN=1,
            comprq4_CN=2,
            comprq5_CN=3,
            comprq6=3,
        )

        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[
                    field_name] = 'Falsche Antwort - Bitte korrigiere deine Angabe oder hebe deine Hand zur Klärung mit dem Laborpersonal.'

        return error_messages



class Instructions_GT_senders_noCN(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "sender" and player.round_number == 1 and (
                    player.id_in_group not in [Constants.num_senders, Constants.num_senders - 1])


    form_model = "player"
    form_fields = ["comprq1", "comprq2", "comprq3_noCN", "comprq4_noCN", "comprq5_noCN", "comprq6"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq1=3,
            comprq2=2,
            comprq3_noCN=1,
            comprq4_noCN=2,
            comprq5_noCN=3,
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
    form_fields = ["comprq7", "comprq8", "comprq9", "comprq10", "comprq11", "comprq12", "comprq13", "comprq14"]

    @staticmethod
    def error_message(player, values):
        solutions = dict(
            comprq7=3,
            comprq8=3,
            comprq9=4,
            comprq10=3,
            comprq11=2,
            comprq12=2,
            comprq13=2,
            comprq14=4,
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

    @staticmethod
    def is_displayed(player):
        return player.round_number == (Constants.num_rounds / 2) + 1

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
        current_round = player.round_number
        prev_player = player.in_round(current_round - Constants.num_rounds/2)
        prev_players = prev_player.group.get_players()
        signals = [p.sent_signal for p in prev_players if p.Role =='sender']
        if player.Role == "receiver":
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
                round=current_round-10
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
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff
        if p.Role == "receiver":
            i = random.randint(int(Constants.num_rounds / 2) + 1, Constants.num_rounds)
            prev_player = p.in_round(i)
            participant = p.participant
            participant.GuessingTask_payoff = prev_player.payoff


page_sequence = [Instructions_GT_senders_CN, Instructions_GT_senders_noCN, StartWaitPage, Signals, Filler_Task,Instructions_GT_receivers,
                 Guess, SecondWaitPage]
