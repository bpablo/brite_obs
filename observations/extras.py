""" Extra functions for dealing with data """

import csv, io
from .models import ObsRecords, Satellite
from astropy.time import Time


def cal_to_jd(dates):
    dates = dates+'T00:00:00'
    times = Time(dates).jd
    return times

# @todo add som more cleaning to this 
def obs_to_db(file, obsfield):
    """ parse log file and place in observations table """

    # decode data
    data = file.read().decode('UTF-8')
    io_string = io.StringIO(data)
    header = next(io_string)

    for column in csv.reader(io_string, delimiter=','):
        # make sure  we have the right field
        field = column[5].split('-')[0]
        print("Field comp", field, obsfield.field_no)
        if int(field) == obsfield.field_no:
            
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
            # print(
            #     'hd_num', str(hd_num)+'\n',
            #     'v_mag', str(v_mag)+'\n',
            #     'sptype', str(sptype)+'\n',
            #     'name', str(name)+'\n',
            #     'sat', str(sat)+'\n',
            #     'tstart', str(tstart)+'\n',
            #     'tend',  str(tend)+'\n',
            #     'nred', str(nred)+'\n',
            #     'norg', str(norg)+'\n',
            #     'exptime', str(exptime)+'\n',
            #     'nstack', str(nstack)+'\n',
            #     'xpos', str(xpos)+'\n',
            #     'ypos', str(ypos)+'\n',
            #     'xsize', str(xsize)+'\n',
            #     'ysize', str(ysize)+'\n',
            #     'obsmode', str(obsmode)+'\n',
            # )
            _, created = ObsRecords.objects.update_or_create(
                field_no = obsfield,
                hd_num = int(hd_num),
                v_mag = float(v_mag),
                sp_type = str(sptype),
                star_name = str(name),
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
                obs_mode = str(obsmode)
            )

            message = "Observation Field uploaded successfully"

        else:

            message = " Could Not upload Observation Field. Field Number Doesn't Match log file."

    return message