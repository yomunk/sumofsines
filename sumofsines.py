import numpy as np

# We assume that the supplied csv file will have two columns, containing time in
# the first column and position in the second. Position should be normalized
# position, i.e. ranging between [-1,1]
filename='sumofsines.csv'

# Desired output amplitude of motor motion, in degrees
amplitude=20
# Stepper motor step resolution (standard is 1.8 for 200 deg/rev, if
# microstepping is enabled this becomes, e.g.,  0.18)
step_resolution=0.18

# Load record array from file
ss = np.loadtxt(filename, delimiter=',', dtype=[('t', 'f4'), ('pos', 'f4')])

# Convert position into step number, where step 0 is the origin.
bin_pos = np.floor((amplitude*ss['pos'] + 0.5*step_resolution) / step_resolution)

# Now find where the motor actually needs to produce a step, i.e. where the
# change in bin_pos is not zero.

steps = np.diff(bin_pos)

time = ss['t'][np.argwhere(steps!=0)].flatten()

# step directions are -1 and +1, so renormalize so that direction is either 0 or
# 1 (i.e. low/high)
direction = (0.5*(steps[np.argwhere(steps!=0)].flatten() + 1)).astype(int)

# Now produce a file for inclusion into an arduino project.

f = open('sumofsines.h', 'w')
f.write('num_steps = {};\n'.format(len(time)))
f.write('step_time = { ')
for t in time[:-1]:
    f.write('{:.3f}, '.format(t))
f.write('{:.3f} }};\n'.format(time[-1]))

f.write('step_direction = { ')
for d in direction[:-1]:
    f.write('{:d}, '.format(d))
f.write('{:d} }};\n'.format(direction[-1]))

f.close()
