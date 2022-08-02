from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

test_day_of_week = MultipleChoiceQuiz(description="<strong>1.Multiple choice</strong> </br>What day of the week is it?",
                   answer=datetime.now().strftime('%A'),
                  options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                  show_answer=True)

test_state = FreeTextTest(description="<strong>1. Free text</strong> </br>What state are we in? (No abbreviations!)",
             answer="Utah")

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

test_max = FunctionTest(args=([1,2,3],), expected=3)

test_x_equals_3 = ValueTest(3, show_answer=True)

test_square_2 = ValueTest(4, show_answer=True)

test_add_3_5 = ValueTest(8, show_answer=True)

test_square_add_3_5 = ValueTest(64, show_answer=True)


def test_add_validation_func(add_submitted):
    import random
    pairs = zip(random.sample(range(0, 100), 10), random.sample(range(0, 100), 10))
    for (x, y) in pairs:
        actual = add_submitted(x, y)
        expected = x + y
        if actual != expected:
            print(f"Incorrect value. Expected {x} + {y} = {expected}, got {actual}")
            return
    print("Correct!")


test_add_function = FunctionTest(validation_func=test_add_validation_func)

ethnicity_descr_hint = QuizHint(hints=[
    widgets.HTML(
        """Your plot should look something like:</br>
        <img src="media/ethnicity_descr_counts.png"></img>
        """
    )
])

age_at_discharge_mc_quiz = MultipleChoiceQuiz("What are the mean and median ages at discharge?",
                                              answer="70.29; 73.41",
                                              options=["73.41; 70.29", "61.14; 105.42"],

                                              )

hint_2_2 = QuizHint(description="Visualization hints",
        hints=[
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_hist.png"></img>
            """),
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_boxplot.png"></img>
            """),
        ]
        )