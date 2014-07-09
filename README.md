Sum of Sines
============

This is some very barebones code designed to allow an Arduino board to send step commands to a stepper indexer and have that stepper motor generate a sum of sines motion.

Usage
-----
sumfosines.py uses data from sumofsines.csv to generate timings for step commands to the indexer, producing sumofsines.h. In the sumofsines sketch folder, sumofsines.ino includes this header and provides a very basic sketch to send these timing outputs to the stepper indexer. Note that for large header files, you'll either want an Arduino Due or to modify the code to store the stimulus on an SD card.
