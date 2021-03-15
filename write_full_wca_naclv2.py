from mkutils.gromacs_writer import FFWriter
import json, os

ff_file = 'saft_wca_v2.json'

if not os.path.isfile(ff_file):
    with open(ff_file, 'w') as f:
        _dict = {'atomtypes': {}, 'crossints': {}}       
        json.dump(_dict, f)

ff = FFWriter(ff_file)

# Always named W
ff.add_cgw_ift(298.15)

ff.add_atomtype('CT', 15.947, 6., 358.37, 0.45012, 43.08698, 25)

ff.add_atomtype('CM', 16.433, 6., 377.14, 0.4184, 42.07914, 24)

ff.add_atomtype('Na+', 8., 6., 48.24, 0.204, 22.989769, 11)

ff.add_atomtype('Cl-', 8., 6., 49.35, 0.362 , 35.453, 17)

ff.add_crossint('W', 'CT', k=0.31)
ff.add_crossint('W', 'CM', k=0.34)
ff.add_crossint('W', 'Na+', eps_mix=200.52)
ff.add_crossint('W', 'Cl-', eps_mix=217.65)

ff.add_crossint('CT', 'CM', eps_mix=345.72)

ff.add_crossint('Na+', 'Cl-', eps_mix=19.65)

ff.add_atomtype('SO4v6', 8., 6., 57.72, 0.412, 96.06, 48)
ff.add_atomtype('SO4v9', 8., 6., 57.72, 0.412, 96.06, 48)

ff.add_crossint('SO4v6', 'W', eps_mix=222.734) 
ff.add_crossint('SO4v6', 'Na+', eps_mix=21.14)
ff.add_crossint('SO4v6', 'CM', wca=True)
ff.add_crossint('SO4v6', 'CT', wca=True)
ff.add_crossint('Na+', 'CM', wca=True)
ff.add_crossint('Na+', 'CT', wca=True)
ff.add_crossint('Cl-', 'CM', wca=True)
ff.add_crossint('Cl-', 'CT', wca=True)

ff.add_crossint('SO4v9', 'W', eps_mix=241.03) 
ff.add_crossint('SO4v9', 'Na+',  eps_mix=21.14)
ff.add_crossint('SO4v9', 'CM', wca=True)
ff.add_crossint('SO4v9', 'CT', wca=True)

ff.add_atomtype('W2', 8., 6., 400., 0.37467, 36.03056, 20)
                                                  
ff.add_crossint('W2', 'CT', k=0.32)                  
ff.add_crossint('W2', 'CM', k=0.33)               
                                                     
ff.add_crossint('W2', 'Na+', eps_mix=195.578331625)  
ff.add_crossint('W2', 'Cl-', eps_mix=210.384356863)
ff.add_crossint('W2', 'SO4v6', eps_mix=292.003438537)
ff.add_crossint('W2', 'SO4v9', eps_mix=341.23241767) 

ff.write_tables(shift=True, cutoff=2.0)
ff.write_forcefield(outfile='ffnonbonded_wca_v2.itp')

ff.add_cgw_ift(303.15, update=True)
ff.write_forcefield(outfile='ffnonbonded_wca_v2_303K.itp')
ff.add_cgw_ift(298.15, update=True)

ff.add_crossint('W2', 'Na+', eps_mix=605.223253179, update=True)  
ff.add_crossint('W2', 'Cl-', eps_mix=23.6661799151, update=True)
ff.add_crossint('W2', 'SO4v6', eps_mix=126.644442036, update=True)
ff.add_crossint('W2', 'SO4v9', eps_mix=175.625078068, update=True) 
 
ff.write_forcefield(outfile='ffnonbonded_wca_bio_v2.itp')
