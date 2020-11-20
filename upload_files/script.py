import utilities as u

from follow_app import Follow_App
from g6_14_day import G6_14_Day
from g6_adverse_events import G6_Adverse
from reliance_acks_mitigation import Reliance_Acks_Mitigation
from zero_forty_five_categorization_extract import Zero_Forty_Five_Categorization_Extract
from clarity import Clarity

list = [
    Follow_App,
    G6_14_Day,
    G6_Adverse,
    Reliance_Acks_Mitigation,
    Zero_Forty_Five_Categorization_Extract,
    Clarity
]


for script in list:
    script().transform_columns()
