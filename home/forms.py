from django import forms

from .models import Profile


class add_staffForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email_address": "Email Address",
            "phone_number": "Phone Number",
            "address": "Home address",
            "gender": "Gender",
            "management_level": "Management Level",
            "entry_date": "Date of entry",
            "termination_date": "Date of termination",
            "position_held": "Position held",
            "basic_salary": "Basic Salary",
        }

        self.fields["first_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "gender" and field != "management_level":
                self.fields[field].widget.attrs["placeholder"] = placeholders[field]

            else:
                self.fields[field].widget.attrs[
                    "class"
                ] = "border-dark m-1 rounded-0 mx-auto add_staff-form-input"

            # self.fields[field].label = False