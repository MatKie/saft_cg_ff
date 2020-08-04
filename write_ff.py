from mkutils.gromacs_writer import FFWriter
import json, os

ff_file = 'saft_parameters.json'

if not os.path.isfile(ff_file):
    with open(ff_file, 'w') as f:
        _dict = {'atomtypes': {}, 'crossints': {}}       
        json.dump(_dict, f)

ff = FFWriter(ff_file)

ff.add_atomtype('cgw_ift_25', 8., 6., 305.21, 0.29016, 18.015028, 10)

ff.add_atomtype('C_T', 15.947, 6., 358.37, 0.45012, 43.08698, 25)

ff.add_atomtype('C_M', 16.433, 6., 377.14, 0.4184, 42.07914, 24)

ff.add_atomtype('Na+', 8., 6., 48.24, 0.204, 22.989769, 11)

ff.add_atomtype('Cl-', 8., 6., 49.35, 0.362 , 35.453, 17)

ff.add_crossint('cgw_ift_25', 'C_T', k=0.31)
ff.add_crossint('cgw_ift_25', 'C_M', k=0.34)
ff.add_crossint('cgw_ift_25', 'Na+', eps_mix=623.381266818)
ff.add_crossint('cgw_ift_25', 'Cl-', eps_mix=31.6660976139)

ff.add_crossint('C_T', 'C_M', eps_mix=345.72)
ff.add_crossint('C_T', 'Na+', eps_mix=212.4)
ff.add_crossint('C_T', 'Cl-', eps_mix=212.4)

ff.add_crossint('C_M', 'Na+', eps_mix=213.01)
ff.add_crossint('C_M', 'Cl-', eps_mix=213.01)

ff.add_crossint('Na+', 'Cl-', eps_mix=19.65)

ff.write_forcefield(outfile='ffnonbonded_new.itp')


