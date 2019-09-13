from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ObsField, ObsRecords, Stars
from .forms import ObsForm, SearchForm
from .extras import obs_to_db, find_hd_num



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
        return render(request, self.template_name,{'form':form})


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

    def get(self, request, fieldno, fieldname):

        field = ObsField.objects.get(field_no=fieldno, field_name=fieldname)
        #stars = field.order_by('hd_num').values('hd_num').distinct()
        stars = Stars.objects.filter(field=field)
        #field_records = ObsRecords.objects.filter(field=field)
        #star_ids = field_records.values_list('star', flat=True).distinct() 
        #stars = Stars.objects.filter(id__in=star_ids).order_by('hd_num')

        #same for all stars
        dr = ObsRecords.objects.filter(star=stars[0])[0].data_release
        obsbystar = []
        url = "https://brite.camk.edu.pl/pub/LC_pub/"+str(fieldno)+"-"+str(fieldname)+"_D"+str(dr)+"/"#21-CetEri-I-2016_DR5/"
        # for x in range(len(stars)):
        #     starobs = field_records.filter(**stars[x])
        # #    url = "https://brite.camk.edu.pl/pub/LC_pub/"+str(fieldno)+str(field)+"_"+/"#21-CetEri-I-2016_DR5/"
        #     star_dict = {
        #         "hd_num" : starobs[0].hd_num,
        #         "star_name": starobs[0].star_name,
        #         "v_mag" : starobs[0].v_mag,
        #         "sp_type" : starobs[0].sp_type,
        #         "availability" : starobs[0].availability,
        #         "url"     : url,
        #     }
        #     obsbystar.append(star_dict)
        
        sats = ObsRecords.objects.filter(star__in=stars).values('sat_id').distinct()
        print(sats[0])

        context = {
            'fieldno' : fieldno,
            'fieldname' : fieldname,
        #    'field_records' : field_records,
            'obsbystar' : stars,
            'url' : url,
            'sats' : sats,

        }

        return render(request, self.template_name, context)

class StarView(TemplateView):  
     template_name = "observations/starpage.html"
     def get(self, request, fieldno, fieldname, star_id):

        field = ObsField.objects.get(field_no=fieldno, field_name=fieldname)
        star = Stars.objects.get(field=field, id=star_id)
        print(star.hd_num, star.sp_type)
        records = ObsRecords.objects.filter(star=star)

        context = {
            'star' : star,
            'field' : field,
            'records' : records,
        }

        return render(request, self.template_name, context)   

class SearchView(TemplateView):

    template_name = 'observations/obs_search.html'

    def get(self, request):
        
        form = SearchForm()

        return render(request, self.template_name, {'form' : form}) 

    def post(self, request):    

        form = SearchForm(request.POST)
        
        star = form['starsearch']
        #TODO add cleaning function for input
        print(form['starsearch'])
        # find star name in simbad and return HD number
        name = star.value()
  #      print(name)
  #      hd_num = find_hd_num(name)
  #      print(hd_num)        
        try:
            hd_num = find_hd_num(name)
            print(hd_num)
        except:
            print('i errored out ')
            error = '{} was not recognized by Simbad'.format(name)
            context = {
                'form': form,
                'error': error,
            }
            Observations= None
            return render(request, self.template_name, context)
        #print(hd_num) 
        if hd_num == '':
            error = 'No records found for {}'.format(name)
            Observations = None
        #If something is actually found do database query
        else: 
            Observations = Stars.objects.filter(hd_num = hd_num)
            if len(Observations) == 0:
                error = 'No records found for {}'.format(name)
            else:
                error = None
        context ={
            'form': form,
            'error': error ,
            'Observations': Observations,
        }    
        print(Observations)
        return render(request, self.template_name, context)