from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ObsField, ObsRecords
from .forms import ObsForm

# Create your views here.

class obs_submission(TemplateView):
    
    template_name = "observations/obs_submission.html"

 #   prompt = {
 #       'order': "@todo"
 #   }

    def get(self, request):
        
        form = ObsForm()

        return render(request, self.template_name, {'form' : form})
    
    # obsfile = request.FILES['file']

    # if not obsfile.name.endswith('.csv'):
    #     messages.error(request, "Observation must be a .csv file")

    # data_set = obsfile.read().decode('UTF-8')
    # io_string = io.STRINGIO(data_set)
