from ipywidgets import widgets
from .quiz import Quiz

class FreeTextTest(Quiz):
    def __init__(self, description="", answer="", show_answer=False):
        super().__init__(description, answer, show_answer)
        self.answer = answer
        self.entered = None
        self._entry = widgets.Textarea(
            value=None,
            placeholder='Type something',
        )

        self._box = widgets.VBox(
            [
                self._description,
                self._entry,
                self._submit,
                self._response,
                self._output

            ]
        )

    def _submit_answer(self, change):
        self.entered = self._entry.value.strip()
        self._validate_answer()

    def _validate_answer(self):
        # If there's already a response, remove it
        if self.entered == self.answer:
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