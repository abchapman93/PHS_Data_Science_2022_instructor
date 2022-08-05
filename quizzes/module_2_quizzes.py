from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

quiz_helpers_code = FreeTextTest(answer="from quizzes.module_2_quizzes import *")
quiz_helpers_code_mc = MultipleChoiceQuiz(answer="Imports a the contents of module_2_quizzes", options=["Imports a module called module_2_quizzes",
                                                                                "It is there for decoration."])

def validate_np_sd(func):
    import numpy
    try:
        assert func is numpy.std
        print("That is correct!")
    except AssertionError:
        print("That is incorrect. Check your sd function.")
test_np_sd = FunctionTest(validation_func=validate_np_sd)

quiz_shape_matrix = MultipleChoiceQuiz(answer="(2, 10)", options=["(10, 2)", "(2,)"])

quiz_data_type_matrix = MultipleChoiceQuiz(answer="numpy.ndarray", options=["numpy.matrix", "list", "tuple"])

quiz_shape_matrix_t = MultipleChoiceQuiz(answer="(10, 2)", options=["(2, 10)", "(10,)"])

test_matrix_first_row_all_cols = SelectMultipleQuiz(answer=["matrix[0 , :]", "matrix[0, 0: ]"], options=["matrix[0][:]", "matrix[0, 0: ]", "matrix[0:]"], shuffle_answer=False)


def test_severity_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.Series):
        print(f"Incorrect. Expected an object with type pd.Series, not {type(actual)}")
        return
    if actual.name != "severity":
        print(f"Incorrect. The column should be named 'severity', not '{actual.name}'")
        return
    expected_values = [40, 10, 20, 15, 50]
    if list(actual.values) != expected_values:
        print(f"Incorrect values. Expected {expected_values}, got {list(actual.values)}")
        return
    print("That is correct!")


test_severity = ValueTest(validation_func=test_severity_validation_func)

hint_severity_below_30= QuizHint(
    hints=[
        widgets.HTML("""Your output should look like this:</br>
        <img src="./media/output_filtered_severity.png" width="45%"></img>"""),
    ]
)
