from otree.api import *

c = Currency

doc = """
Final Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Big5'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def create_B_field():
    field = models.IntegerField(choices=[1, 2, 3, 4, 5],
                                widget=widgets.RadioSelectHorizontal, label="")
    return field

class Player(BasePlayer):
    identity = models.StringField()
    B_1 = create_B_field()
    B_2 = create_B_field()
    B_3 = create_B_field()
    B_4 = create_B_field()
    B_5 = create_B_field()
    B_6 = create_B_field()
    B_7 = create_B_field()
    B_8 = create_B_field()
    B_9 = create_B_field()
    B_10 = create_B_field()
    B_11 = create_B_field()
    B_12 = create_B_field()

    B_13 = create_B_field()
    B_14 = create_B_field()
    B_15 = create_B_field()
    B_16 = create_B_field()
    B_17 = create_B_field()
    B_18 = create_B_field()
    B_19 = create_B_field()
    B_20 = create_B_field()
    B_21 = create_B_field()
    B_22 = create_B_field()
    B_23 = create_B_field()
    B_24 = create_B_field()

    B_25 = create_B_field()
    B_26 = create_B_field()
    B_27 = create_B_field()
    B_28 = create_B_field()
    B_29 = create_B_field()
    B_30 = create_B_field()
    B_31 = create_B_field()
    B_32 = create_B_field()
    B_33 = create_B_field()
    B_34 = create_B_field()
    B_35 = create_B_field()
    B_36 = create_B_field()

    B_37 = create_B_field()
    B_38 = create_B_field()
    B_39 = create_B_field()
    B_40 = create_B_field()
    B_41 = create_B_field()
    B_42 = create_B_field()
    B_43 = create_B_field()
    B_44 = create_B_field()


# PAGES

class Big5_1(Page):
    form_model = 'player'
    form_fields = ['B_1','B_2','B_3','B_4','B_5','B_6','B_7','B_8','B_9','B_10','B_11','B_12']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            Questionnaire_payoff=player.session.config['Questionnaire_payoff']
        )

class Big5_2(Page):
    form_model = 'player'
    form_fields = ['B_13','B_14','B_15','B_16','B_17','B_18','B_19','B_20','B_21','B_22','B_23','B_24']


class Big5_3(Page):
    form_model = 'player'
    form_fields = ['B_25','B_26','B_27','B_28','B_29','B_30','B_31','B_32','B_33','B_34','B_35','B_36']


class Big5_4(Page):
    form_model = 'player'
    form_fields = ['B_37','B_38','B_39','B_40','B_41','B_42','B_43','B_44']





page_sequence = [Big5_1, Big5_2, Big5_3, Big5_4]
