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
    
    def post(self, request):
        print("POST request", request.POST)
        print("FILE request", request.FILES)
 #       obsfile = request.FILES['obsfile']
        form = ObsForm(request.POST, request.FILES)
        print("THIS IS A DAMN Form", form)
        obsfile = form.cleaned_data['obsfile']
        field = form.cleaned_data['field']
#   #      print("request files", request.FILES)
#   #      print(obsfile.name)
#   #      obsfile.read().decode('UTF-8')
#         print("this is a field", field)
#         print("this is a file", obsfile)
        data = obsfile.read().decode('UTF-8')

        return render(request, self.template_name)

    
            
    # obsfile = request.FILES['file']

    # if not obsfile.name.endswith('.csv'):
    #     messages.error(request, "Observation must be a .csv file")

    # data_set = obsfile.read().decode('UTF-8')
    # io_string = io.STRINGIO(data_set)
