import ipywidgets as widgets
from random import shuffle
class MultipleChoiceQuiz:
    def __init__(self, description="", answer="True", options=("True", "False")):
        self._output = widgets.Output()
        if answer not in options:
            raise ValueError(f"Invalid answer {answer}. Options = {options}")
        shuffle(options)
        self.description = description
        self._description = widgets.HTML(value=self.description)
        self.options = options
        self._options = widgets.RadioButtons(
            options=self.options
        )
        self.answer = answer
        self.submitted = None

        self._submit = widgets.Button(description="Submit")
        self._submit.on_click(self._submit_answer)

        self.response = ""
        self._response = self._response = widgets.HTML(
            value=self.response
        )

        self._box = widgets.VBox(
            [
                self._description,
                self._options,
                self._submit,
                self._response,
                self._output

            ]
        )



    def _submit_answer(self, change):
        self.submitted = self._options.value
        self._validate_answer()

    def _validate_answer(self):
        # If there's already a response, remove it
        if self.submitted == self.answer:
            self.response = "That is correct!"
        else:
            self.response = "That is incorrect."
        self._response.value = self.response

    def display(self):
        """Display the Box widget in the current IPython cell."""
        from IPython.display import display as ipydisplay
        self._output.clear_output()

        ipydisplay(self._box)

    def __repr__(self):
        self.display()
        return ""