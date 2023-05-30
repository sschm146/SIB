from otree.api import *
import pandas as pd
import datetime
from pathlib import Path
import string
import re

c = Currency

doc = """
Payout
"""

class Constants(BaseConstants):
    name_in_url = 'Payout'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    total_payoff = models.FloatField()
    iban = models.StringField()
    surname = models.StringField()
    name = models.StringField()
    safety_question = models.StringField(choices=[
        ["Haustier", "Wie lautete der Name Ihres ersten Haustiers?"],
        ["Schule", "Wie hieß Ihre erste Schule?"],
        ["Spitzname", "Wie lautete als Kind Ihr Spitzname?"],
        ["StadtEltern", "In welcher Stadt bzw. welchem Ort haben sich Ihre Eltern kennengelernt?"],
        ["VornameGeschwister", "Wie lautet der zweite Vorname Ihrer ältesten Schwester bzw. Ihres ältesten Bruders?"],
        ["Geburtsort", "In welcher Stadt bzw. an welchem Ort wurden Sie geboren?"]],
        label="Bitte wählen Sie hier Ihre Sicherheitsfrage."
    )
    safety_answer = models.StringField()


# PAGES
class PayoutWaitPage(WaitPage):
    wait_for_all_groups = True


class Anon_Pay(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'anon_pay'


def anon_pay(subsession: Subsession):
    players = subsession.get_players()

    session_code = []
    total_payoff = []
    name = []
    surname = []
    iban = []
    safety_question = []
    safety_answer = []
    date = []
    import time
    for p in players:
        participant = p.participant
        p.total_payoff = float(participant.payoff_plus_participation_fee())
        session_code.append(p.session.code)
        total_payoff.append(p.total_payoff)
        name.append(p.name)
        surname.append(p.surname)
        iban.append(p.iban.replace(" ", ""))
        safety_question.append(p.safety_question)
        safety_answer.append(p.safety_answer)
        date.append(datetime.datetime.fromtimestamp(time.time()).strftime('%x %X'))

    # Gather all info anonymously
    df = pd.DataFrame({'session': session_code, 'date': date, 'name': name, 'surname': surname, 'payoff': total_payoff, 'iban': iban, 'safety_question': safety_question,
                        'safety_answer': safety_answer})
    # Shuffle all info
    df.sample(frac=1)
    # Save info
    session_code = subsession.session.code
    name = "".join([str(session_code), "_payout_data.xlsx"])
    name1 = "".join([str(session_code), "_payout_data1.xlsx"])

    place = Path(__file__).resolve().parent

    df.to_excel(name, index=False)  # Saving to current working directory
    df.to_excel("".join([str(place), "/", name1]), index=False)  # Saving to Payout-App folder

    for p in players:
        p.iban = '[REDACTED]'
        p.name = '[REDACTED]'
        p.surname = '[REDACTED]'

class IBAN(Page):
    form_model = 'player'
    form_fields = ['iban', 'name', 'surname', 'safety_question', 'safety_answer']


def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


_LETTERS = chain(enumerate(string.digits + string.ascii_uppercase),
                 enumerate(string.ascii_lowercase, 10))
LETTERS = {ord(d): str(i) for i, d in _LETTERS}


def _number_iban(iban):
    # Filter out any special characters from input and replacing them with empty string (i.e. removing them)
    #iban = re.sub(r'[^a-zA-Z0-9]', '', iban)
    return (iban[4:] + iban[:4]).translate(LETTERS)


def generate_iban_check_digits(iban):
    number_iban = _number_iban(iban[:2] + '00' + iban[4:])
    return '{:0>2}'.format(98 - (int(number_iban) % 97))


def valid_iban(iban):
    return int(_number_iban(iban)) % 97 == 1


def iban_error_message(player, my_iban):
    my_iban = my_iban.replace(" ", "")
    pattern = r'[^a-zA-Z0-9]'
    if re.search(pattern, my_iban):
        return 'Geben sie bitte eine gültige IBAN ein'
    elif (generate_iban_check_digits(my_iban) == my_iban[2:4] and valid_iban(my_iban)) or my_iban == "invalid":
        pass
    else:
        return 'Geben sie bitte eine gültige IBAN ein'


class Payout(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

        SIM_payoff = participant.SIM_payoff
        GuessingTask_payoff = participant.GuessingTask_payoff

        if participant.Role == 'sender' or participant.Role == 'prior_sender':
            return dict(
                part_fee=player.session.config['participation_fee'],
                SIM_payoff=cu(SIM_payoff),
                GuessingTask_payoff=cu(GuessingTask_payoff),
                Questionnaire_payoff=cu(player.session.config['Questionnaire_payoff']),
                total_payoff=cu(participant.total_payoff + player.session.config['participation_fee']),
                payoff_ball=participant.chosen_payoff,
                role=participant.Role
            )
        if participant.Role == 'receiver':
            Trust_payoff = participant.Trust_payoff
            return dict(
                part_fee=player.session.config['participation_fee'],
                SIM_payoff=cu(SIM_payoff),
                GuessingTask_payoff=cu(GuessingTask_payoff),
                Trust_payoff=cu(Trust_payoff),
                Questionnaire_payoff=cu(player.session.config['Questionnaire_payoff']),
                total_payoff=cu(participant.total_payoff + player.session.config['participation_fee']),
                payoff_ball=participant.chosen_payoff,
                role=participant.Role
            )


class Payout_hidden(Page):
    pass


page_sequence = [PayoutWaitPage, IBAN, Anon_Pay, Payout, Payout_hidden]
