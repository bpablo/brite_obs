from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ObsField, ObsRecords
from .forms import ObsForm
from .extras import obs_to_db
# Create your views here.

class obs_submission(TemplateView):
    
    template_name = "observations/obs_submission.html"

    def get(self, request):
        
        form = ObsForm()

        return render(request, self.template_name, {'form' : form})
    
    def post(self, request):
        print("POST request", request.POST)
        print("FILE request", request.FILES)
        form = ObsForm(request.POST, request.FILES)
        print("THIS IS A DAMN Form", form)
        obsfile = form.cleaned_data['obsfile']
        field = form.cleaned_data['field']
        field_no = field.field_no
        print("FIELD", field.field_no)

        status_message = obs_to_db(obsfile, field)
        print(status_message)
        return render(request, self.template_name)


class Observations(TemplateView):

    template_name = "observations/observations.html"

    def get(self, request):

        Obsfields  = ObsField.objects.all()
        context = {
            'Obsfields': Obsfields
        }

        return render(request, self.template_name, context)


class ObservationField(TemplateView):

    template_name = "observations/observation_field.html"

    def get(self, request, fieldname='default'):

        context = {
            'fieldname' : fieldname
        }

        return render(request, self.template_name, context)