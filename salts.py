from mkutils.gromacs_writer import FFWriter
import json, os

ff_file = 'nacl.json'

if not os.path.isfile(ff_file):
    with open(ff_file, 'w') as f:
        _dict = {'atomtypes': {}, 'crossints': {}}       
        json.dump(_dict, f)

ff = FFWriter(ff_file)

# Add common interactions
ff.add_atomtype('Wift25', 8., 6., 305.21, 0.29016, 18.015028, 10)
ff.add_atomtype('Na+', 8., 6., 48.24, 0.204, 22.989769, 11)
ff.add_atomtype('Cl-', 8., 6., 49.35, 0.362 , 35.453, 17)
ff.add_crossint('Na+', 'Cl-', eps_mix=19.65)

# Add version 1
ff.add_crossint('Wift25', 'Na+', eps_mix=623.381266818)
ff.add_crossint('Wift25', 'Cl-', eps_mix=31.6660976139)

ff.write_forcefield(outfile='nacl_1.itp')

# Add version 2
ff.add_crossint('Wift25', 'Na+', eps_mix=200.52, update=True)
ff.add_crossint('Wift25', 'Cl-', eps_mix=217.65, update=True)

ff.write_forcefield(outfile='nacl_2.itp')

# Add version 3
ff.add_crossint('Wift25', 'Na+', eps_mix=50.82, update=True)
ff.add_crossint('Wift25', 'Cl-', eps_mix=282.36, update=True)

ff.write_forcefield(outfile='nacl_3.itp')

# Add version 4
ff.add_crossint('Wift25', 'Na+', eps_mix=351.51, update=True)
ff.add_crossint('Wift25', 'Cl-', eps_mix=150.07, update=True)

ff.write_forcefield(outfile='nacl_4.itp')

# Add version 5
ff.add_crossint('Wift25', 'Na+', eps_mix=494.8, update=True)
ff.add_crossint('Wift25', 'Cl-', eps_mix=85.35, update=True)

ff.write_forcefield(outfile='nacl_5.itp')
