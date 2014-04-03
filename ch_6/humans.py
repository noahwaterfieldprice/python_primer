# Exercise 6.14
infile = open('human_evolution.txt', 'r')
lines = infile.readlines()[3:10]
humans = {}
for line in lines:
    species = line[:21].strip()
    lived_when = line[21:37].strip()
    height = line[37:50].strip()
    mass = line[50:62].strip()
    brain_vol = line[61:].strip()
    humans['homo' + species[2:]] = {'when': lived_when,
                                    'height': height,
                                    'mass': mass,
                                    'brain volume': brain_vol}

print '%-22s %-16s %-13s %-12s %-25s' % ('Species',
                                         'Lived when',
                                         'Adult',
                                         'Adult',
                                         'Brain volume')
print '%-22s %-16s %-13s %-12s %-25s' % ('',
                                         '(mill. yrs)',
                                         'height (m)',
                                         'mass (kg',
                                         '(cm**3)')
print '-' * 79
for species in humans:
    print '%-22s %-16s %-13s %-12s %-25s' % (species,
                                             humans[species]['when'],
                                             humans[species]['height'],
                                             humans[species]['mass'],
                                             humans[species]['brain volume'])
print '-' * 79

"""
Sample run:
python humans.py
Species                Lived when       Adult         Adult        Brain volume
                       (mill. yrs)      height (m)    mass (kg     (cm**3)
-------------------------------------------------------------------------------
homo erectus           1.4 - 0.2        1.8           60           850 (early) - 1100 (late)
homo heidelbergensis   0.6 - 0.35       1.8           60           1100 - 1400
homo ergaster          1.9 - 1.4        1.9                        700 - 850
homo neanderthalensis  0.35 - 0.03      1.6           55 - 70      1200 - 1700
homo sapiens sapiens   0.2 - present    1.4 - 1.9     50 - 100     1000 - 1850
homo habilis           2.2 - 1.6        1.0 - 1.5     33 - 55      660
homo floresiensis      0.10 - 0.012     1.0           25           400
-------------------------------------------------------------------------------
"""
