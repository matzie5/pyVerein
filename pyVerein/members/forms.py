from django import forms
from .models import Member, Division, Subscription


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('salutation', 'last_name', 'first_name', 'street', 'zipcode', 'city', 'birthday', 'phone', 'mobile', 'fax', 'email', 'membership_number', 'division', 'joined_at', 'terminated_at', 'payment_method', 'subscription', 'iban', 'bic', 'debit_mandate_at', 'debit_reference', 'field_1', 'field_2', 'field_3', 'field_4', 'field_5')
        widgets = {
            'salutation': forms.RadioSelect(attrs={'class':'mdc-radio__native-control'}),
            'subscription': forms.CheckboxSelectMultiple(attrs={'class': 'mdc-checkbox__native-control'})
        }

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['division'].empty_label = ""

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('name', 'income_account', 'debitor_account', 'cost_center', 'cost_object')
        widgets = {
            'income_account': forms.TextInput(),
            'debitor_account': forms.TextInput(),
            'cost_center': forms.TextInput(),
            'cost_object': forms.TextInput(),
        }

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('name', 'amount', 'payment_frequency')
        widgets = {
            'amount': forms.TextInput(),
            'payment_frequency': forms.RadioSelect(attrs={'class':'mdc-radio__native-control'})
        }