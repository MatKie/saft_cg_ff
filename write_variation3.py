from mkutils.gromacs_writer import FFWriter
import json, os

ff_file = 'saft_variation3.json'

if not os.path.isfile(ff_file):
    with open(ff_file, 'w') as f:
        _dict = {'atomtypes': {}, 'crossints': {}}       
        json.dump(_dict, f)

ff = FFWriter(ff_file)

ff.add_atomtype('Wift25', 8., 6., 305.21, 0.29016, 18.015028, 10)

ff.add_atomtype('CT', 15.947, 6., 358.37, 0.45012, 43.08698, 25)

ff.add_atomtype('CM', 16.433, 6., 377.14, 0.4184, 42.07914, 24)

ff.add_atomtype('Na+', 8., 6., 48.24, 0.204, 22.989769, 11)

ff.add_atomtype('Cl-', 8., 6., 49.35, 0.362 , 35.453, 17)

ff.add_crossint('Wift25', 'CT', k=0.31)
ff.add_crossint('Wift25', 'CM', k=0.34)
ff.add_crossint('Wift25', 'Na+', eps_mix=623.381266818)
ff.add_crossint('Wift25', 'Cl-', eps_mix=31.6660976139)

ff.add_crossint('CT', 'CM', eps_mix=345.72)

ff.add_crossint('Na+', 'Cl-', eps_mix=19.65)

ff.add_atomtype('SO4v6', 8., 6., 57.72, 0.412, 96.06, 48)
ff.add_atomtype('SO4v9', 8., 6., 57.72, 0.412, 96.06, 48)

ff.add_crossint('SO4v6', 'Wift25', eps_mix=69.1829688535) 
ff.add_crossint('SO4v6', 'Na+', eps_mix=21.14)
ff.add_crossint('SO4v6', 'CM', k=0.6)
ff.add_crossint('SO4v6', 'CT', k=0.6)
#ff.add_crossint('Na+', 'CM', k=0.6)
#ff.add_crossint('Na+', 'CT', k=0.6)
#ff.add_crossint('Cl-', 'CM', k=0.6)
#ff.add_crossint('Cl-', 'CT', k=0.6)

ff.add_crossint('SO4v9', 'Wift25', eps_mix=87.4734785037) 
ff.add_crossint('SO4v9', 'Na+',  eps_mix=21.14)
ff.add_crossint('SO4v9', 'CM', k=0.6)
ff.add_crossint('SO4v9', 'CT', k=0.6)



ff.write_forcefield(outfile='ffnonbonded_variation3.itp')


