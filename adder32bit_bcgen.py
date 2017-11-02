def adder32bit_gen(file_handler):
	# example
	# bit1
	# S0 := ODD(A0,B0,OP0);
	# C0 := OR(AND(A0,B0),AND(OP0,A0),AND(OP0,B0));

	# bit2
	# S1 := ODD(A1,B1,C0);
	# C1 := OR(AND(A1,B1),AND(C0,A1),AND(C0,A1));

	# bit3
	# S2 := ODD(A2,B2,C0);
	# C2 := OR(AND(A2,B2),AND(C1,A2),AND(C1,A2));

	file_handler.write('B0 := ODD(b0,OP0);\n')
	file_handler.write('S0 := ODD(A0,B0,OP0);\n')
	file_handler.write('C1 := OR(AND(A0,B0),AND(OP0,A0),AND(OP0,B0));\n')
	#file_handler.write('C0 := (OP0);\n')
	file_handler.write('\n')

	for i in range(1, 32):
		currentXB = 'B{0} := ODD(b{0},OP0);\n'.format(i)
		#currentSum = 'S{0} := ODD(A{0},B{0},C{1});\n'.format(i, i-1)
		currentSum = 'S{0} := ODD(A{0},B{0},C{1});\n'.format(i, i)
		#currentCarryOut = 'C{0} := OR(AND(A{0},B{0}),AND(C{1},A{0}),AND(C{1},B{0}));\n'.format(i, i-1)
		currentCarryOut = 'C{1} := OR(AND(A{0},B{0}),AND(C{0},A{0}),AND(C{0},B{0}));\n'.format(i, i+1)
		file_handler.write(currentXB + currentSum + currentCarryOut + '\n')




if __name__=='__main__':
	bcfile = open('adder32bit.bc','w')
	bcfile.write('BC1.1\n')
	adder32bit_gen(bcfile)
	bcfile.close()
