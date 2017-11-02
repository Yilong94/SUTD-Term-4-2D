import math

bcfile = open('optimized1.bc','w')
bcfile.write('BC1.1\n')


#to insert the 32 bit adder code
import adder32bit_bcgen
adder32bit_bcgen.adder32bit_gen(bcfile)

bcfile.write('\n\n\n\n\n')

layer = int((math.log(32))/(math.log(2)))
#print layer
count = 32

#layer 1: 32
#bcfile.write('Layer 1: 32 boxA\n')
for each_box1 in range(count):
	current_P = 'P0_{0} := NOT(NOT(OR(A{0},B{0})));\n'.format(each_box1)
	current_G = 'G0_{0} := NOT(NOT(AND(A{0},B{0})));\n'.format(each_box1)
	current_SUM = 'S_optimized{0} := ODD(A{0},B{0},C_optimized{0});\n'.format(each_box1)
	bcfile.write(current_P + current_G + current_SUM)
	bcfile.write('\n')
bcfile.write('\n\n\n')

count=count/2
#layer 2: 16
#bcfile.write('Layer 2: 16 boxB\n')
for each_box2 in range(count):
	current_P = 'P1_{0} := NOT(NOT(AND(P0_{1},P0_{2})));\n'.format(each_box2, each_box2*2, each_box2*2+1)
	current_G = 'G1_{0} := NOT(AND(NOT(G0_{2}),NOT(AND(G0_{1},P0_{2}))));\n'.format(each_box2, each_box2*2, each_box2*2+1)
	nextC = 'C_optimized{1} := NOT(AND(NOT(G0_{2}), NOT(AND(P0_{2},C_optimized{0}))));\n'.format(each_box2*2, each_box2*2+1, each_box2*2)
	bcfile.write(current_P + current_G + nextC)
	bcfile.write('\n')
bcfile.write('\n\n\n')

count=count/2
#layer 3: 8
#bcfile.write('Layer 3: 8 boxB\n')
for each_box2 in range(count):
	current_P = 'P2_{0} := NOT(NOT(AND(P1_{1},P1_{2})));\n'.format(each_box2, each_box2*2, each_box2*2+1)
	current_G = 'G2_{0} := NOT(AND(NOT(G1_{2}),NOT(AND(G1_{1},P1_{2}))));\n'.format(each_box2, each_box2*2, each_box2*2+1)	
	nextC = 'C_optimized{1} := NOT(AND(NOT(G1_{2}), NOT(AND(P1_{2}, C_optimized{0}))));\n'.format(each_box2*4, each_box2*4+2, each_box2*2)
	bcfile.write(current_P + current_G + nextC)
	bcfile.write('\n')
bcfile.write('\n\n\n')

count = count/2
#layer 4: 4
#bcfile.write('Layer 4: 4 boxB\n')
for each_box2 in range(count):
	current_P = 'P3_{0} := NOT(NOT(AND(P2_{1},P2_{2})));\n'.format(each_box2, each_box2*2, each_box2*2+1)
	current_G = 'G3_{0} := NOT(AND(NOT(G2_{2}),NOT(AND(G2_{1},P2_{2}))));\n'.format(each_box2, each_box2*2, each_box2*2+1)
	nextC = 'C_optimized{1} := NOT(AND(NOT(G2_{2}), NOT(AND(P2_{2}, C_optimized{0}))));\n'.format(each_box2*8, each_box2*8+4, each_box2*2)
	bcfile.write(current_P + current_G + nextC)
	bcfile.write('\n')
bcfile.write('\n\n\n')

count = count/2
#layer 5: 2
#bcfile.write('Layer 5: 2 boxB\n')
for each_box2 in range(count):
	current_P = 'P4_{0} := NOT(NOT(AND(P3_{1},P3_{2})));\n'.format(each_box2, each_box2*2, each_box2*2+1)
	current_G = 'G4_{0} := NOT(AND(NOT(G3_{2}),NOT(AND(G3_{1},P3_{2}))));\n'.format(each_box2, each_box2*2, each_box2*2+1)
	nextC = 'C_optimized{1} := NOT(AND(NOT(G3_{2}), NOT(AND(P3_{2}, C_optimized{0}))));\n'.format(each_box2*16, each_box2*16+8, each_box2*2)
	bcfile.write(current_P + current_G + nextC)
	bcfile.write('\n')
bcfile.write('\n\n\n')

count = count/2
#layer 6: 1
#bcfile.write('Layer 6: 1 boxB\n')
current_P = 'P5_0 := NOT(NOT(AND(P4_0,P4_1)));\n'	#.format(each#_box2, each_box2*2, each_box2*2+1)
current_G = 'G5_0 := NOT(AND(NOT(G4_1),NOT(AND(G4_0,P4_1))));\n'	#.format(each_box2, each_box2*2, each_box2*2+1)
nextC = 'C_optimized16 := NOT(AND(NOT(G4_0), NOT(AND(P4_0,OP0))));\n'		#.format(each_box2*2, each_box2*2+1)
bcfile.write(current_P + current_G + nextC)
bcfile.write('\n\n\n')

#connects op0 to the C_optimized0 node 
bcfile.write('C_optimized0 := (OP0);\n\n\n')

#to verify that the bits from the two circuits are the same by CEC
bcfile.write('Z := ODD(S31, S_optimized31);\n')
bcfile.write('ASSIGN Z;')


bcfile.close()