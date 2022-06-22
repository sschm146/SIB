from otree.api import *

c = Currency

doc = """
Welcome & Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'Intro_SI_all'
    players_per_group = None
    num_rounds = 1
    num_senders = 6


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identity = models.StringField()
    Role = models.StringField()


#FUNCTIONS
def creating_session(subsession: Subsession):
    import itertools
    identity = itertools.cycle(["Blau", "Gelb"])
    for player in subsession.get_players():
        participant = player.participant
        if player.session.config['prior_sender']:
            if player.id_in_group == Constants.num_senders + 1:
                participant.identity = "neutral"
                player.identity = participant.identity
            if player.id_in_group > Constants.num_senders + 1:
                participant.identity = next(identity)
                player.identity = participant.identity
            if player.id_in_group <= Constants.num_senders/2:
                participant.identity = "Blau"
                player.identity = participant.identity
            if player.id_in_group > Constants.num_senders/2 and player.id_in_group <= Constants.num_senders:
                participant.identity = "Gelb"
                player.identity = participant.identity
        else:
            if player.id_in_group > Constants.num_senders:
                participant.identity = next(identity)
                player.identity = participant.identity
            if player.id_in_group <= Constants.num_senders / 2:
                participant.identity = "Blau"
                player.identity = participant.identity
            if player.id_in_group > Constants.num_senders / 2 and player.id_in_group <= Constants.num_senders:
                participant.identity = "Gelb"
                player.identity = participant.identity

    for p in subsession.get_players():  # Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        if p.id_in_group in list(range(1, Constants.num_senders + 1)):
            participant.Role = "sender"
            p.Role = participant.Role
        elif p.session.config['prior_sender'] and p.id_in_group in list(range(Constants.num_senders + 1, Constants.num_senders + 2)):
            participant.Role = "prior_sender"
            p.Role = participant.Role
        else:
            participant.Role = "receiver"
            p.Role = participant.Role


# PAGES
class Instructions_all(Page):

    @staticmethod
    def vars_for_template(player: Player):
        part_fee = player.session.config['participation_fee']
        return dict(
            part_fee=part_fee
        )

class Instructions_sender(Page):
    @staticmethod
    def is_displayed(player):
            return player.Role == "sender" or player.Role == "prior_sender"

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        identity = participant.identity
        return dict(
            identity=identity
        )

class Instructions_receiver(Page):
    @staticmethod
    def is_displayed(player):
        return player.Role == "receiver"

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        identity = participant.identity
        return dict(
            identity=identity
        )



page_sequence = [Instructions_all, Instructions_sender, Instructions_receiver]
