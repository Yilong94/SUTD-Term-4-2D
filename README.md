# SUTD-Term-4-2D

##Part 1: 32-bit adder optimization

optimized1.jsim contains the optimized 32-bit adder. It is optimized via:
  *Carry-select and carry-lookahead adder architecture
  *Using inverting logic to increase speed
  *Use buffers to reduce load-dependent delays
  *Minimize delays along critical paths

Timing:**2.23ns**

##Part 2: Translating netlist to CNF

This is the general flow: 
1. Write a python script to generate boolean expression in BC file format
   *$ python optimized1_bcgen.py* 
2. Convert the BC file into CNF file using bc2cnf in BCpackage-0.40
   *$ ./BCpackage-0.40/bc2cnf ./optimized1.bc ./optimized1.cnf*
3. Run findsolssat to solve for unsatisfiability
   *$ java -jar ./findsolssat/findsolssat.jar ./optimized1.cnf*
