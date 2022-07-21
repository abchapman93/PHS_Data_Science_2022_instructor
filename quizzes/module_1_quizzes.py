from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest

quiz1 = MultipleChoiceQuiz(
    description='<strong>1.</strong> What class is x? </br><p style="font-family:courier";>x = 3</p>',
    options=["int", "float", "str", "list"],
    answer="int"
)

quiz2 = MultipleChoiceQuiz(
    description='<strong>2.</strong> What class is x? </br><p style="font-family:courier";>x = 3.0</p>',
    options=["int", "float", "str", "list"],
    answer="float"
)