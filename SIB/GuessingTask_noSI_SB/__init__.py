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
    SB_sender_5 = models.StringField()
    SB_received_signal_1 = models.IntegerField()  # saving received signals across rounds for analyses
    SB_received_signal_2 = models.IntegerField()  # saving received signals across rounds for analyses
    SB_received_signal_3 = models.IntegerField()  # saving received signals across rounds for analyses
    SB_received_signal_4 = models.IntegerField()  # saving received signals across rounds for analyses
    SB_received_signal_5 = models.IntegerField()  # saving received signals across rounds for analyses
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
    q3 = models.StringField(label='')
    q4 = models.StringField(label='')
    q5 = models.IntegerField(
        choices=[[0, "Weiblich"],
                 [1, "Mänlich"],
                  [2, "Divers"]],
        widget=widgets.RadioSelect, label=''
        )
    q6 = models.StringField(label='')
    q7 = models.IntegerField(label='')
    q8 = models.IntegerField(label='')
    q9 = models.IntegerField(label='')
    q10 = models.IntegerField(
        choices=[[1, "Poor"],
                 [2, "Average"],
                  [3, "Good"],
                 [4, "Excellent"]],
        widget=widgets.RadioSelect, label=''
        )
    q11 =  models.IntegerField(
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
    q13 =  models.IntegerField(
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
    q23 = models.StringField(label='')
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
            p.estimate = estimates[p.id_in_group-1]
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

    def vars_for_template(player: Player):
        estimate = player.estimate
        return dict(
            estimate=estimate,
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
        return player.round_number >= (Constants.num_rounds / 2) + 1

def set_signals(subsession: Subsession):
    players = subsession.get_players()
    if subsession.round_number > Constants.num_rounds / 2:
        temp = []
        for p in players:
            prev_player = p.in_round(subsession.round_number - Constants.num_rounds / 2)
        prev_players = prev_player.group.get_players()
        signals = [prev.sent_signal for prev in prev_players if prev.Role == 'sender']
        senders = [prev.id_in_group for prev in prev_players if prev.Role == 'sender']
        for i in list(range(Constants.num_senders - 3, Constants.num_senders)):
            temp.append([signals[i], senders[i]])
        random.shuffle(temp) #important to solve ties at random
        temp = sorted(temp, key=lambda x: int(x[0]))
        #temp.sort(reverse=True) #alternative is to sort first at signal size and then by id_in_group to preserve order at ties:
                                    # temp = sorted(temp, key=lambda x:(int(x[0]), x[1]))
        subsession.censored_signal = str(temp[0])
        del temp[0]
        temp = sorted(temp, key=lambda x: int(x[1]))
        for i in list(range(0, 2)):
            if temp[i][1] == 4:
                temp[i][1] = 'D'
            if temp[i][1] == 5:
                temp[i][1] = 'E'
            if temp[i][1] == 6:
                temp[i][1] = 'F'
        for p in players:
            if p.Role == "receiver":
                p.SB_sender_4 = temp[0][1]
                p.SB_sender_5 = temp[1][1]
                p.SB_received_signal_1 = signals[0]
                p.SB_received_signal_2 = signals[1]
                p.SB_received_signal_3 = signals[2]
                p.SB_received_signal_4 = temp[0][0]
                p.SB_received_signal_5 = temp[1][0]



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
        prev_player = player.in_round(current_round - Constants.num_rounds / 2)
        prev_players = prev_player.group.get_players()
        return dict(
                signal_1=player.SB_received_signal_1,
                signal_2=player.SB_received_signal_2,
                signal_3=player.SB_received_signal_3,
                signal_4=player.SB_received_signal_4,
                signal_5=player.SB_received_signal_5,
                sender_4=player.SB_sender_4,
                sender_5=player.SB_sender_5,
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


def save_signals_payoff(subsession: Subsession):
    players = subsession.get_players()
    signals_all_rounds = []
    estimates_all_rounds = []

    for i in list(range(0, int(Constants.num_rounds / 2))):
        for p in players:
            if p.Role == 'sender':
                prev_player = p.in_round(i + 1)
                prev_subsession = subsession.in_round(i + int(Constants.num_rounds / 2) + 1)
                if prev_player.id_in_group != int(prev_subsession.censored_signal[4]): #indexing of "censored signal" is no as in "4th element of list" but as in "4th element of string object"
                    signals_all_rounds.append(prev_player.field_maybe_none('sent_signal'))
                else:
                    signals_all_rounds.append('-')
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


page_sequence = [Instructions_GT_senders, StartWaitPage, Signals, Filler_Task, Instructions_GT_receivers,
                 Guess, SecondWaitPage]
