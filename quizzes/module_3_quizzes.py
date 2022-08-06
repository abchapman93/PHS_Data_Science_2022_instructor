from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

quiz_relational_columns1 = SelectMultipleQuiz(
    description="The ID's of all patients who have had Covid-19.", shuffle_answer=False,
    answer=["subject_id", "diagnosis",],
    options=["subject_id", "diagnosis", "diagnosis.date", "encounter.date", "encounter_type"]
)

quiz_relational_columns2 = SelectMultipleQuiz(
    description="The number of outpatient encounters between January and May of 2022.",
    answer=["encounter_type", "encounter.date",],
    options=["subject_id", "diagnosis", "diagnosis.date", "encounter.date", "encounter_type"],
    shuffle_answer=False
)

quiz_relational_columns3 = SelectMultipleQuiz(
    description="The age at time of diagnosis for patients with cancer.",
    answer=["subject_id", "diagnosis", "diagnosis.date", "encounter_id", "encounter.date",],
    options=["subject_id", "diagnosis", "diagnosis.date", "encounter_id", "encounter.date",],
    shuffle_answer=False
)

quiz_simple_query_parts = SelectMultipleQuiz(
    shuffle_answer=False,
    description="Which clauses were included in the example query we ran?",
    answer=[
        "'SELECT' clause",
        "'FROM' clause",
        "'WHERE' clause",
        "'LIMIT' clause",
    ],
    options=[
        "'SELECT' clause",
        "'FROM' clause",
        "'JOIN' clause",
        "'WHERE' clause",
        "'ORDER' clause",
        "'LIMIT' clause",
    ]
)

quiz_tables_in_query = SelectMultipleQuiz(description="Which tables are used in the query above?",
                  answer=["d_patients", "admissions"],
                  options=["subject_id", "hospital_expire_flag", "dod"])

quiz_order_by_column = MultipleChoiceQuiz(
    "Which column is used in the query to sort the data?",
    answer="dod",
    options=["subject_id", "dob", "hospital_expire_flg"]
)


def test_query_result1_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 25:
        print(f"Incorrect. df should have 25 rows. Your dataframe had {len(actual)}.")
        return

    if set(actual.columns) != {'hadm_id', 'subject_id', 'admit_dt', 'disch_dt'}:
        print(f"Incorrect. Your dataframe should have columns ['hadm_id', 'subject_id', 'admit_dt', 'disch_dt'], not {actual.columns}")
        return
    print("That is correct!")


test_query_result1 = ValueTest(validation_func=test_query_result1_validation_func)

quiz_fix_where_ambiguity = MultipleChoiceQuiz(options=["a", "b", "c", "a and b", "a, b, and c"], answer="a and b", shuffle_answer=False)


def test_fixed_where_ambiguity_validation_func(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 1:
        print(f"Incorrect. df should have 1 rows. Your dataframe had {len(actual)}.")
        return
    if set(actual.columns) != {'subject_id', 'dob', 'dod', 'admission_type_descr'}:
        print(
            f"Incorrect. Your dataframe should have columns ['subject_id', 'dob', 'dod', 'admission_type_descr'], not {actual.columns}")
        return
    if set(actual["subject_id"]) != {78}:
        print(f"Incorrect. Your dataframe should have one subject_id 78, not {actual.iloc[0]['subject_id']}")
        return
    print("That is correct!")


test_fixed_where_ambiguity = ValueTest(validation_func=test_fixed_where_ambiguity_validation_func)


def test_query_dob_descending(actual):
    import pandas as pd
    if not isinstance(actual, pd.DataFrame):
        print(f"Incorrect. df should be a pandas DataFrame, not {type(actual)}")
        return
    if len(actual) != 3:
        print(f"Incorrect. df should have 3 rows. Your dataframe had {len(actual)}.")
        return
    if set(actual.columns) != {'subject_id', 'sex', 'dob', 'dod', 'hospital_expire_flg'}:
        print(
            f"Incorrect. Your dataframe should have columns ['subject_id', 'sex', 'dob', 'dod', 'hospital_expire_flg'], not {list(actual.columns)}")
        return
    if set(actual["subject_id"]) != {37, 78, 56}:
        print(f"Incorrect. Your dataframe should have subject_id's (37, 78, 56), not {tuple(actual['subject_id'])}")
        return
    if tuple(actual["subject_id"]) != (37, 78, 56):
        print(
            f"Incorrect. Your dataframe should have subject ids in the order (37, 78, 56), not {tuple(actual['subject_id'])}")

    print("That is correct!")


test_query_dob_descending = ValueTest(validation_func=test_query_dob_descending)