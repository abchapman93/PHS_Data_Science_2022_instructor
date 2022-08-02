from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

test_day_of_week = MultipleChoiceQuiz(description="What day of the week is it?",
                   answer=datetime.now().strftime('%A'),
                  options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                  show_answer=True)

test_state = FreeTextTest(description="What state are we in? (No abbreviations!)",
             answer="Utah")

prime_mc = SelectMultipleQuiz("Which of the following numbers are prime? (Select all that apply.)",
                   answer=[2, 3, 5],
                  options=[2, 3, 4, 5, 6],
                  shuffle_answer=False)

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

x_y_changing_var_quiz = MultipleChoiceQuiz(description='What is the value of: <p style="font-family:courier";>add(x,y)</p>',
                   options=[11, 12, 4, 9], answer=11)

test_r_equals_2 = ValueTest(2, True)
test_pi_equals = ValueTest(3.14, True)

quiz_data_type_2_pi_r = MultipleChoiceQuiz(description='What data type is: <p style="font-family:courier";>2*r*pi</p>', answer="float",
                  options=["int", "float", "variable", "other"])

quiz_2_pi_r_part2 = MultipleChoiceQuiz(description='How about: <p style="font-family:courier";>int(2*float(r)*int(pi))</p>',
                   answer="int",
                  options=["int", "float", "variable", "other"])

quiz_y_gt_z = FreeTextTest(description="What code would test whether y is greater than z?",
                          answer=["y>z", "z<y"],
                          preprocessor=lambda x:x.replace(" ", ""))

quiz_y_lte_z = FreeTextTest(description="What code would test whether z less than or equal to y?",
                          answer=["z<=y", "y>=z"],
                          preprocessor=lambda x:x.replace(" ", ""))

quiz_y_ne_z = FreeTextTest(description="What code would test whether z is not equal to y?",
                          answer=["z!=y", "y!=z"],
                          preprocessor=lambda x:x.replace(" ", ""))

test_add_function = FunctionTest(validation_func=test_add_validation_func)

quiz_select_all_true = SelectMultipleQuiz(description="""
    Which of the following lines of code would evaluate as True?
    Use the values y = 10 and z = 5.
    """,
                                          answer=[
                                              "not (True & False)",
                                              "(not True) or (not False)",
                                              "True or False",
                                              "(y == 10) or (z < 5)",

                                          ],
                                          options=[
                                              "not ((y != 10) & z >= 5)",
                                              "y == z"
                                          ]
                                          )

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

ethnicity_descr_hint = QuizHint(hints=[
    widgets.HTML(
        """Your plot should look something like:</br>
        <img src="media/ethnicity_descr_counts.png"></img>
        """
    )
])

age_at_discharge_mc = MultipleChoiceQuiz("What are the mean and median ages at discharge?",
                                         answer="70.29; 73.41",
                                         options=["73.41; 70.29", "61.14; 105.42"],

                                         )

age_at_discharge_viz_hint = QuizHint(description="Visualization hints",
        hints=[
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_hist.png"></img>
            """),
            widgets.HTML("""One option is a histogram:</br>
            <img src="./media/age_at_discharge_boxplot.png"></img>
            """),
        ]
        )

prop_pt_mortality_quiz = MultipleChoiceQuiz(description="What proportion of patients died in the hospital?",
            answer=0.33, options=[0.66, 0.43, 0.1])

age_at_discharge_mortality_hint = QuizHint(description="Visualization hints",
        hints=[
            widgets.HTML("""Your plot should look something like:</br>
            <img src="./media/age_at_discharge_proportions.png"></img>
            """)
        ]
        )

mortality_cols_quiz = SelectMultipleQuiz(answer=("time_discharge_to_death", "disch_dt", "dod"),
                  options=('subject_id', 'hadm_id', 'disch_dt', 'dod', 'sex', 'ethnicity_descr',
       'age_at_discharge', 'age_at_discharge_binned', 'pna',
       'time_discharge_to_death', 'mortality_30_day'), shuffle_answer=False)

in_hospital_mortality_hint = QuizHint(
    hints=[
        widgets.HTML("You could either represent this variable as an integer (0 or 1) or a boolean (True or False)."),
        widgets.HTML("If you have a Series and run `series1 == value`, you'll get back a Series of booleans indicating whether that row has that value."),
    ]
)

def test_in_hospital_mortality_validation_func(actual_df):
    import pandas as pd
    import numpy as np
    # Check that it's a Series
    if not isinstance(actual_df, pd.DataFrame):
        print(f"Incorrect value passed in. Data type should be pd.DataFrame, got {type(actual_df)}")
        return

    # Check that it has a column
    try:
        actual = actual_df["in_hospital_mortality"]
    except KeyError:
        print("Your DataFrame doesn't have a column named 'in_hospital_mortality'")
        return

    # Check that the column contains an acceptable datatype
    if actual.dtype not in ("int64", "float64", "bool"):
        print(f"Incorrect. 'in_hospital_mortality' should contain int, float, or bool, not {str(actual.dtype)}")
        return

    if len(actual_df) != 5074:
        print(f"Expected 5074 rows, got {len(actual_df)}")
        return

    # Check that the mean value is expected
    actual_mean = np.round(actual.mean(), 4)
    if actual_mean != 0.3285:
        print(f"Mean value of 'in_hospital_mortality' wasn't what was expected. Expected 0.3285, got {actual_mean}")
        return

    print("That is correct!")


age_at_discharge_mortality_quiz = SelectMultipleQuiz("What are the two age groups wwith the highest proportion of in-hospital mortality?",
                   answer=("<18", "91+"),
                   options=('<18', '18-35', '36-65', '66-90', '91+',),
                   shuffle_answer=False
                  )

test_in_hospital_mortality = ValueTest(validation_func=test_in_hospital_mortality_validation_func)

pna_prop = MultipleChoiceQuiz("What is the proportion of patients had pneumonia? Round to 4 decimal points.",
            answer=0.2, options=[0.8, 0.33, 0.66])

time_to_death_viz_hint = QuizHint(description="Some hints for visualizing time to death.",
    hints=[
        widgets.HTML("""One option is a boxplot</br>:
    <img src="./media/time_discharge_to_death_boxplot.png"></img>
    """),
        widgets.HTML("""Another option is a histogram:</br>:
    <img src="./media/time_to_death_hist.png"></img>
    """)
          ]
)

time_to_death_mean_quiz = MultipleChoiceQuiz("What are the mean number of days from discharge to death for pneumonia positive and negative patients?",
             answer="254.1; 398.9",
             options=["398.9; 254.1", "35.0; 113.5", "113.5; 35.0"]
            )

in_hospital_mortality_rr_quiz = FreeTextTest(
    "What is the relative risk of in-hospital mortality for pneumonia positive vs pneumonia negative patients?</br>Round to 2 decimals.",
    answer=1.27

)

in_hospital_mortality_rr_interpretation_quiz = MultipleChoiceQuiz("The interpretation of the relative risk is:</br>Patients with pneumonia are ___ ___ than patients without pneumonia to die in the hospital.",
                   answer=" 1.27 times more likely",
                   options=["1.27 times less likely", "Similarly likely"]
                  )
