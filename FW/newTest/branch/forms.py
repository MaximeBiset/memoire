from django import forms
from django.utils.translation import ugettext as _
from bootstrap3_datetime.widgets import DateTimePicker
from multiselectfield import MultiSelectField

from branch.models import Branch, Demand, Offer, OfferObj, DemandObj, Comment, DemandProposition, SuccessDemand, \
                            DemandPropositionObj, SuccessDemandObj, SuccessOfferObj, DemandPropositionOObj

from django.utils import timezone
from datetime import timedelta
from django.utils import formats
from branch.widgets import OneJobSelect

# =====================
# FEATURE BEGIN : MONEY
# =====================
class FWMoneyForm(forms.ModelForm):
    """
    def clean_estimated_time(self):
        est = self.cleaned_data.get('estimated_time')
        if not est :
            raise forms.ValidationError(_("Indiquez une estimation."))
        if est <= 0:
            raise forms.ValidationError(_("Le temps estimé doit être plus grand que 0 minutes."))
        return est
    """

def FWAddMoney():
    return [] #['estimated_time']
# ===================
# FEATURE END : MONEY
# ===================

class CreateBranchForm(forms.ModelForm):
    """ Form for creating a branch """
    class Meta:
        model = Branch
        fields = ['name', 'location', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
        }

    def clean(self):
        if not 'latitude' in self.cleaned_data or not 'longitude' in self.cleaned_data:
            raise forms.ValidationError(_("Veuillez choisir une adresse"))
        if not 'location' in self.cleaned_data or not self.cleaned_data['location']:
            raise forms.ValidationError(_("Veuillez choisir une adresse"))
        super(CreateBranchForm, self).clean()

class ChooseBranchForm(forms.Form):
    """ Form for choosing a branch """
    id = forms.IntegerField(widget=forms.HiddenInput)

    def clean(self):
        id = self.cleaned_data.get('id')
        try:
            Branch.objects.get(pk=id)
        except Branch.DoesNotExist:
            raise forms.ValidationError(_("Veuillez choisir un point sur la carte"))
        super(ChooseBranchForm, self).clean()

    class Meta:
        fields = ['id']

class CommentForm(forms.ModelForm):
    """ Form for making a comment """ 
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
          'comment': forms.Textarea(attrs={'rows':3,}),
        }
# ============================
# FEATURE BEGIN : TRANSACTIONS
# ============================
class NeedHelpForm(FWMoneyForm):
    """ Form for asking help """
    category = MultiSelectField(verbose_name=_("Categorie"), max_choices=1)

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now() - timezone.timedelta(hours=24):
            raise forms.ValidationError(_("Veuillez choisir une date dans le futur."))
        return date

    def clean(self):
        if not self.cleaned_data['latitude'] and not self.cleaned_data['longitude']:
            raise forms.ValidationError(_("Veuillez choisir une adresse"))
        super(NeedHelpForm, self).clean()

    class Meta:
        model = Demand
        fields = ['description', 'category', 'date', 'time', 'location', 'latitude', 'longitude', 'title', 'receive_help_from_who'] + FWAddMoney()
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
            'date': DateTimePicker(options={"pickTime": False,}),
            'category': OneJobSelect,
        }

class OfferHelpForm(forms.ModelForm):
    """ Form for offering help """
    category = MultiSelectField(verbose_name=_("Categorie"))

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now() + timezone.timedelta(hours=-24):
            raise forms.ValidationError(_("Veuillez choisir une date dans le futur."))
        return date

    class Meta:
        model = Offer
        fields = ['category', 'date', 'time', 'receive_help_from_who',]
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
            'date' : DateTimePicker(options={"pickTime": False,}),
        }

class TakeOfferForm(NeedHelpForm):

    class Meta:
        model = Demand
        fields = ['description', 'category', 'time', 'location', 'latitude', 'longitude', 'title', 'receive_help_from_who'] + FWAddMoney()
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
            'date': DateTimePicker(options={"pickTime": False,}),
            'category': OneJobSelect,
        }

class UpdateNeedHelpForm(NeedHelpForm):
    class Meta:
        model = Demand
        fields = ['description', 'date', 'time', 'location', 'latitude', 'longitude', 'title', 'receive_help_from_who'] + FWAddMoney()
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
            'date': DateTimePicker(options={"pickTime": False,}),
            'category': OneJobSelect,
        }


class DemandObjForm(FWMoneyForm):
    """ Form for asking object """

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now() - timezone.timedelta(hours=24):
            raise forms.ValidationError(_("Veuillez choisir une date dans le futur."))
        return date

    def clean(self):
        if not self.cleaned_data['latitude'] and not self.cleaned_data['longitude']:
            raise forms.ValidationError(_("Veuillez choisir une adresse"))
        super(DemandObjForm, self).clean()

    class Meta:
        model = DemandObj
        fields = ['description', 'date', 'location', 'latitude', 'longitude', 'title', 'receive_help_from_who'] + FWAddMoney()
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
            'date': DateTimePicker(options={"pickTime": False,})
        }

class UpdateDemandObjForm(NeedHelpForm):
    class Meta:
        model = Demand
        fields = ['description', 'date', 'location', 'latitude', 'longitude', 'title', 'receive_help_from_who'] + FWAddMoney()
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
            'date': DateTimePicker(options={"pickTime": False,}),
        }

class OfferObjForm(FWMoneyForm):
    """ Form for asking object """

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now() - timezone.timedelta(hours=24):
            raise forms.ValidationError(_("Veuillez choisir une date dans le futur."))
        return date

    def clean(self):
        if not self.cleaned_data['latitude'] and not self.cleaned_data['longitude']:
            raise forms.ValidationError(_("Veuillez choisir une adresse"))
        super(OfferObjForm, self).clean()

    class Meta:
        model = OfferObj
        fields = ['title', 'description', 'date', 'location', 'latitude', 'longitude', 'receive_help_from_who'] + FWAddMoney()
        widgets = {
            'latitude': forms.HiddenInput,
            'longitude': forms.HiddenInput,
            'location': forms.HiddenInput,
            'date': DateTimePicker(options={"pickTime": False,})
        }

# ==========================
# FEATURE END : TRANSACTIONS
# ==========================
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = DemandProposition
        fields = ['comment', 'km', 'time',]
        widgets = {
            'km' : forms.HiddenInput,
        }

class ForceVolunteerForm(forms.ModelForm):
    class Meta:
        model = DemandProposition
        fields = ['user', 'comment', 'km', 'time',]

class SuccessDemandForm(forms.ModelForm):
    class Meta:
        model = SuccessDemand
        fields = ['comment'] + FWAddMoney()

class SuccessDemandObjForm(forms.ModelForm):
    class Meta:
        model = SuccessDemandObj
        fields = ['comment'] + FWAddMoney()

class SuccessOfferObjForm(forms.ModelForm):
    class Meta:
        model = SuccessOfferObj
        fields = ['comment'] + FWAddMoney()

class CommentConfirmForm(forms.Form):
    comment = forms.CharField(required=False, widget=forms.Textarea, label = _("Commentaire"))

class VolunteerObjForm(forms.ModelForm):
    class Meta:
        model = DemandPropositionObj
        fields = ['comment', 'km']
        widgets = {
            'km' : forms.HiddenInput,
        }

class VolunteerOObjForm(forms.ModelForm):
    class Meta:
        model = DemandPropositionOObj
        fields = ['comment', 'km']
        widgets = {
            'km' : forms.HiddenInput,
        }

class ForceVolunteerObjForm(forms.ModelForm):
    class Meta:
        model = DemandPropositionObj
        fields = ['user', 'comment', 'km']

class ForceVolunteerOObjForm(forms.ModelForm):
    class Meta:
        model = DemandPropositionOObj
        fields = ['user', 'comment', 'km']

