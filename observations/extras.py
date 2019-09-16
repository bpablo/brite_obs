""" Extra functions for dealing with data """

import csv, io
from .models import ObsRecords, Satellite, PrincInv, Stars
from astropy.time import Time
from astroquery.simbad import Simbad


def find_hd_num(name):
    result_table = Simbad.query_objectids(name)
    for x in result_table:
        name = x[0]
        if 'HD' in name:
            hd_num = name.split(' ')[-1]
            return hd_num
    name = ''
    return name
  
def cal_to_jd(dates):
    dates = dates+'T00:00:00'
    times = Time(dates).jd
    return times

# @todo add som more cleaning to this 
def obs_to_db(file, obsfield):
    """ parse log file and place in observations table """
    print(obsfield.id)
    # decode data
    data = file.read().decode('UTF-8')
    io_string = io.StringIO(data)
    header = next(io_string)

    for column in csv.reader(io_string, delimiter=','):
        # make sure  we have the right field
        field = column[5].split('-')[0]
  #      print("Field comp", field, obsfield.field_no)
        if int(field) == obsfield.field_no:
            # determine release by splitting filename (this should probably be it's own column)
            print(column[0])
            rel = column[0].split('_')[-1][:-4]
            
#            print("release number", rel)

            # change columns before inserting into db
            hd_num = column[1].strip('HD')
            v_mag = column[2]
            sptype = column[3]
            name = column[4]
            sat = Satellite.objects.get(sat_id=column[6]) 
            setup = column[7].strip('setup')
            tstart = cal_to_jd(column[8])
            tend = cal_to_jd(column[9])
            nred = column[11]
            norg = column[12]
            exptime = column[14]
            nstack = column[15]
            xpos = column[16]
            ypos = column[17]
            xsize = column[18]
            ysize = column[19]
            obsmode = column[20]
            pi_last_name = column[22]
            
            #create star record 
            #check to make sure it doesn't exist:
            if Stars.objects.filter(hd_num=int(hd_num), field=obsfield):
                print("the star already exists")
                star = Stars.objects.get(hd_num=int(hd_num), field=obsfield)
            else:
#                print("Star Name Length", len(name), name+" this is the name")
#                print("PI Name", pi_last_name)
                if pi_last_name == 'none':
                    pi = None
                else:
                    pi = PrincInv.objects.get(last_name = pi_last_name)
                if len(name) <= 1:
#                    print("there is no spoon")
                    _, created = Stars.objects.update_or_create(
                        hd_num = int(hd_num),
                        v_mag = float(v_mag),
                        sp_type = str(sptype),
                        pi = pi,
                        field = obsfield,
                    )
                else:           
                    _, created = Stars.objects.update_or_create(
                        hd_num = int(hd_num),
                        v_mag = float(v_mag),
                        sp_type = str(sptype),
                        star_name = str(name),
                        pi = pi,
                        field = obsfield,
                    )
     #           print("I created the damn star")
                star = Stars.objects.get(hd_num =int(hd_num), field=obsfield)
     #           print("I found the damn star")

            _, created = ObsRecords.objects.update_or_create(
#                field = obsfield,
                star = star,
                # hd_num = int(hd_num),
                # v_mag = float(v_mag),
                # sp_type = str(sptype),
                # star_name = str(name),
                sat = sat,
                setup = str(setup),
                obs_start = float(tstart),
                obs_end = float(tend),
                nred = int(nred),
                norg = int(norg),
                exptime = int(exptime),
                nstack = int(nstack),
                xpos = int(xpos),
                ypos = int(ypos),
                xsize = int(xsize),
                ysize = int(ysize),
                obs_mode = str(obsmode),
                data_release = str(rel),

            )

            message = "Observation Field uploaded successfully"

        else:

            message = " Could Not upload Observation Field. Field Number Doesn't Match log file."

    return message