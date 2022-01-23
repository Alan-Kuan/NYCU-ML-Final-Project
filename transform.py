#! /usr/bin/env python3
import json
import csv

def filter(val):
    if val is None: raise
    return val

total_count = 0
elim_count = 0

with open('neo.csv', 'w', newline='') as f_out:
    writer = csv.writer(f_out)

    writer.writerow([
        'id',
        'name',
        'abs_mag',
        'est_dia_min',
        'est_dia_max',
        'epoch',
        'min_orb_inter',
        'jup_tisser',
        'e',
        'a',
        'i',
        'asc_node_long',
        'peri_arg',
        'orb_period',
        'peri_dist',
        'ap_dist',
        'mean_ano',
        'mean_mot',
        'hazard'
    ])

    for page in range(0, 600):
        with open(f'data/page{ page }.json') as f_in:
            objs = json.load(f_in)
            rows = []

            for idx, obj in enumerate(objs):
                total_count += 1
                try:
                    est_d = obj['estimated_diameter']['kilometers']
                    orbital_data = obj['orbital_data']
                    row = []

                    row.append(filter(obj['id']))
                    row.append(filter(obj['name']))
                    row.append(filter(obj['absolute_magnitude_h']))
                    row.append(filter(est_d['estimated_diameter_min']))
                    row.append(filter(est_d['estimated_diameter_max']))
                    row.append(filter(orbital_data['epoch_osculation']))
                    row.append(filter(orbital_data['minimum_orbit_intersection']))
                    row.append(filter(orbital_data['jupiter_tisserand_invariant']))
                    row.append(filter(orbital_data['eccentricity']))
                    row.append(filter(orbital_data['semi_major_axis']))
                    row.append(filter(orbital_data['inclination']))
                    row.append(filter(orbital_data['ascending_node_longitude']))
                    row.append(filter(orbital_data['perihelion_argument']))
                    row.append(filter(orbital_data['orbital_period']))
                    row.append(filter(orbital_data['perihelion_distance']))
                    row.append(filter(orbital_data['aphelion_distance']))
                    row.append(filter(orbital_data['mean_anomaly']))
                    row.append(filter(orbital_data['mean_motion']))
                    row.append(1 if filter(obj['is_potentially_hazardous_asteroid']) else 0)

                    rows.append(row)
                
                except:
                    print(f'skip instance #{ idx } in page { page }.')
                    elim_count += 1

            writer.writerows(rows)

        print(f'page{ page } dumpped.')

print(f'Total { total_count } instances. { elim_count } were eliminated.')
