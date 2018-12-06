import pandas as pd
from datetime import datetime

def load_data(option):
    today = str(datetime.now())[0:10]    
    data  = pd.read_csv(today + '-' + option + '.csv', sep=';')
    return data

def get_by_pos(data, pos):
    by_pos = data[data['Pos'] == pos]
    return by_pos

def split_into_pos(data):
    #players who play one position
    point_guards    = get_by_pos(data, 1)
    shooting_guards = get_by_pos(data, 2)
    small_forwards  = get_by_pos(data, 3)
    power_forwards  = get_by_pos(data, 4)
    centers         = get_by_pos(data, 5)

    #players who play two poisitions
    pg_sg           = get_by_pos(data, 12)
    sg_sf           = get_by_pos(data, 23)
    sf_pf           = get_by_pos(data, 34)
    pf_c            = get_by_pos(data, 45)

    point_guards    = point_guards.append(pg_sg)

    shooting_guards = shooting_guards.append(pg_sg)
    shooting_guards = shooting_guards.append(sg_sf)

    small_forwards  = small_forwards.append(sg_sf)
    small_forwards  = small_forwards.append(sf_pf)
    
    power_forwards  = power_forwards.append(sf_pf)
    power_forwards  = power_forwards.append(pf_c)

    centers         = centers.append(pf_c)

    return (point_guards, shooting_guards, small_forwards, power_forwards, centers)

print(split_into_pos(load_data('dk'))[2])
