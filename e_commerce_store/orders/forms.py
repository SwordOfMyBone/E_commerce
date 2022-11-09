from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-horizontal'
        self.helper.label_class = "col-auto col-sm-2 m-10 font-weight-bold"
        self.helper.field_class = "col ml-auto m-10"
        self.helper.form_method = "POST"
        self.helper.add_input(
            Submit("submit", "Continue", css_class="btn btn-lg btn-block mt-20")
        )

    class Meta:
        model = Order
        fields = ["address", "postal_code", "city"]
