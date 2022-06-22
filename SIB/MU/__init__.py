from otree.api import *
import random as random


class Constants(BaseConstants):
    name_in_url = 'MU'
    players_per_group = None
    tasks = ['Altruism', 'Trust']
    num_rounds = len(tasks)
    endowment = 100

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    altruism_domestic = models.IntegerField(min=0, max=Constants.endowment, blank=True)
    altruism_foreign = models.IntegerField(min=0, max=Constants.endowment, blank=True)
    altruism_global = models.IntegerField(min=0, max=Constants.endowment, blank=True)
    trust_domestic = models.IntegerField(min=0, max=Constants.endowment, blank=True)
    trust_foreign = models.IntegerField(min=0, max=Constants.endowment, blank=True)
    trust_global = models.IntegerField(min=0, max=Constants.endowment, blank=True)


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            p.participant.task_rounds = dict(zip(Constants.tasks, round_numbers))


# PAGES
class Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Instructions_altruism(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Altruism']


class Altruism_domestic(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Altruism']

    @staticmethod
    def error_message(player, values):
        if values['altruism_domestic'] is None:
            error_message = 'Bitte klicken Sie auf den grauen Balken und treffen Sie eine Auswahl über den Schieberegler.'
            return error_message

    form_model = 'player'
    form_fields = ['altruism_domestic']


class Altruism_foreign(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Altruism']

    @staticmethod
    def error_message(player, values):
        if values['altruism_foreign'] is None:
            error_message = 'Bitte klicken Sie auf den grauen Balken und treffen Sie eine Auswahl über den Schieberegler.'
            return error_message

    form_model = 'player'
    form_fields = ['altruism_foreign']


class Altruism_global(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Altruism']

    @staticmethod
    def error_message(player, values):
        if values['altruism_global'] is None:
            error_message = 'Bitte klicken Sie auf den grauen Balken und treffen Sie eine Auswahl über den Schieberegler.'
            return error_message

    form_model = 'player'
    form_fields = ['altruism_global']


class Trust_domestic(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Trust']

    @staticmethod
    def error_message(player, values):
        if values['trust_domestic'] is None:
            error_message = 'Bitte klicken Sie auf den grauen Balken und treffen Sie eine Auswahl über den Schieberegler.'
            return error_message

    form_model = 'player'
    form_fields = ['trust_domestic']


class Trust_foreign(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Trust']

    @staticmethod
    def error_message(player, values):
        if values['trust_foreign'] is None:
            error_message = 'Bitte klicken Sie auf den grauen Balken und treffen Sie eine Auswahl über den Schieberegler.'
            return error_message

    form_model = 'player'
    form_fields = ['trust_foreign']


class Trust_global(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Trust']

    @staticmethod
    def error_message(player, values):
        if values['trust_global'] is None:
            error_message = 'Bitte klicken Sie auf den grauen Balken und treffen Sie eine Auswahl über den Schieberegler.'
            return error_message

    form_model = 'player'
    form_fields = ['trust_global']


class Instructions_trust(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['Trust']

class FinalWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'data_saving'

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


def data_saving(subsession: Subsession):
    for player in subsession.get_players():
        prev_player = player.in_round(1)
        if player.field_maybe_none('altruism_domestic') is None:
            player.altruism_domestic = prev_player.altruism_domestic
            prev_player.trust_domestic = player.trust_domestic
        if player.field_maybe_none('altruism_foreign') is None:
            player.altruism_foreign = prev_player.altruism_foreign
            prev_player.trust_foreign = player.trust_foreign
        if player.field_maybe_none('altruism_global') is None:
            player.altruism_global = prev_player.altruism_global
            prev_player.trust_global= player.trust_global
        if player.field_maybe_none('trust_domestic') is None:
            player.trust_domestic = prev_player.trust_domestic
            prev_player.altruism_domestic = player.altruism_domestic
        if player.field_maybe_none('trust_foreign') is None:
            player.trust_foreign = prev_player.trust_foreign
            prev_player.altruism_foreign = player.altruism_foreign
        if player.field_maybe_none('trust_global') is None:
            player.trust_global = prev_player.trust_global
            prev_player.altruism_global = player.altruism_global





page_sequence = [Instructions, Instructions_altruism, Altruism_domestic, Altruism_foreign, Altruism_global,
                 Instructions_trust, Trust_domestic, Trust_foreign, Trust_global, FinalWaitPage]
