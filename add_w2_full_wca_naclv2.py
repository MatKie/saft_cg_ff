from mkutils.gromacs_writer import FFWriter                                 
import json, os
                                          
ff_file = 'saft_wca_v2.json'                         
                                                  
ff = FFWriter(ff_file)                               
    
ff.add_atomtype('W2', 8., 6., 400., 0.37467, 36.03056, 20)
                                                  
ff.add_crossint('W2', 'CT', k=0.32)                  
ff.add_crossint('W2', 'CM', k=0.33)               
                                                     
ff.add_crossint('W2', 'Na+', eps_mix=195.578331625)  
ff.add_crossint('W2', 'Cl-', eps_mix=210.384356863)
ff.add_crossint('W2', 'SO4v6', eps_mix=292.003438537)
ff.add_crossint('W2', 'SO4v9', eps_mix=341.23241767) 
                                                  
ff.write_tables(shift=True, cutoff=2.0)              
ff.write_forcefield(outfile='ffnonbonded_wca_v2.itp')
