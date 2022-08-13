from .multiple_choice_quiz import MultipleChoiceQuiz
from .function_test import FunctionTest
from .free_text_test import FreeTextTest
from .select_multiple_quiz import SelectMultipleQuiz
from .value_test import ValueTest
from .quiz_hint import QuizHint
from datetime import datetime
import ipywidgets as widgets

quiz_text_3 = MultipleChoiceQuiz("""<h4>TODO</h4>Using the variable `text` that we defined above, what would be the value of
<p style="font-family:courier";>text[3]</p>""", answer="e",
                  options=["i", "Chi", "e", "E"])

quiz_len_empty = FreeTextTest('What value would be generated by the following code:</br><p style="font-family:courier";>len("")</p> ',
            answer=0)

quiz_split_pna_empty = MultipleChoiceQuiz("""What would happen if you split the string `"pna"` on an empty string?""",
                  answer="['p', 'n', 'a']",
                  options=["An error would be raised.", "You'd get an empty list.", "['pna']"])

hint_tokenize_disch_summ = QuizHint(hints=[
    widgets.HTML("""If 'He' and 'he' both appear in the document, how would you make sure they count as the same token?"""),
    widgets.HTML("""If you wanted to also get counts of tokens, you could use Python's `Counter` class:</br>
    <p style="font-family:courier";>from collections import Counter</br>help(Counter)</p>"""),
])


def test_get_section_name_validation_func(func):
    texts = [
        "Chief Complaint:\n5 days worsening SOB, DOE",
        "History of Present Illness:\nPt is a 63M w/ h/o metastatic carcinoid tumor.",
        "Social History:\nLives alone with two daughters."
    ]
    expected = ["Chief Complaint", "History of Present Illness", "Social History"]
    for text, expected in zip(texts, expected):
        if (actual := func(text)) != expected:
            print(f"Incorrect. Expected {expected}, got {actual} for {text}")
            return
    print("That is correct!")
test_get_section_name = ValueTest(validation_func=test_get_section_name_validation_func)


def test_pneumonia_in_text_validation_func(func):
    pna_strings = [
        "The patient has pneumonia.",
        "INDICATION: EVALUATE FOR PNEUMONIA",
        "Patient shows symptoms concerning for pna.",
        "The chest image found no evidence of pna",
    ]
    for string in pna_strings:
        if (actual := func(string)) is not True:
            print(f"Incorrect. Expected True, got {actual} with string {string}")
            return
    if func("") is True:
        print(f"Incorrect. Expected False, got True with \"\"")
        return
    print("That is correct!")
test_pneumonia_in_text = ValueTest(validation_func=test_pneumonia_in_text_validation_func)

quiz_mc_pneumonia_in_text = MultipleChoiceQuiz("If the function above returns True, that means the note indicates the patient has pneumonia.", answer="False")

hint_generate_chief_complaint = QuizHint(hints=[
    widgets.HTML("""Your output should like like:</br><img src="./media/hint_generate_chief_complaint.png" width="75%"></img>""")
])
