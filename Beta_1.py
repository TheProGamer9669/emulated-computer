import  os, time, json

opcodes = {
	"1000":"add", 
	# add op1, op2, op3 \ adds op1 to op2 and stores the result in op3
	# if op3 is not provied it will default to op1
	# Examples:
	# add a, b, 00x00000001 \ will do a + b and store it in memory location 00x00000001
	# add a, b \ will do a + b and put the result into register a

	"1001":"sub", 
	# sub op1, op2, op3 \ subtracts op2 from op1 and stores the result in op3
	# if op3 is not provied it will default to op1
	# Examples:
	# sub a, b, 00x00000002 \ will do a - b and store the result into memory address 00x00000002
	# sub a, b \ will do a - b and store the result in register a

	"1010":"lda", 
	# lda op1 \ loads into register a the value at the memory address op1
	# Example:
	# lda 00x00000003 \ will load the value of 00x00000003 into register a

	"1011":"ldb", 
	# ldb op1 \ loads into register b the value at the memory address op1
	# Example:
	# ldb 00x00000004 \ loads into register be the value stored at 00x00000004

	"1100":"ld" 
	# ld op1, op2 \ loads op2 into memory at the address of op1,
	# or if op1 is a register thats NOT a or b it will load op2 into that register
	# Examples:
	# ld 00x00000005, 5 \ loads 5 into memory address 00x00000005
	# ld pc, 00x00000005 \ loads 00x00000005 into pc

	"1101":"push", 
	# push op1 \ pushes op1 onto the top of the stack
	# Example:
	# push a \ pushes the value of a onto the stack

	"1110":"pop", 
	# pop op1 \ pops stuff off the top of the stack into op1
	# Example:
	# pop a \ the value at the top of the stack into a

	"1111":"jmp", 
	# jmp op1, x \ jumps to a defined function
	# if the x flag is included it will check if the last result was = x,
	# if it is it will jump if not it will continue with the program without jumping
	# Examples:
	# jmp _start \ jumps to start no matter what the last result was
	# jmp _start, 5 \ jumps to start if the last result was a 5
	# jmp _start, >5 \ jumps to start if the last result was greater than 5
	# jmp _start, <5 \ jumps to start if the last result was less than 5
	# jmp _start, =>5 \ jumps to start if the last result was greater or equal to 5
	# jmp _start, =<5 \ jumps to start if the last result was equal or less than 5
}
registers = {
	"0001":"a", # 16 bit or 2 byte \ register a
	"0010":"b", # 16 bit or 2 byte \ register b
	"0011":"pc", # 32 bit \ the program counter
	"0100":"s1", # 32 bit or 4 byte \ keeps track of the top of the stack
	"0101":"s2", # 32 bit or 4 byte \ keeps track of the bottom of the stack
	"0110":"rt" # 32 bit or 4 byte \ keeps track of the last result
}

def parser(tobeparsed):
	tobeparsed = tobeparsed.split()
	if 3 < len(tobeparsed) or len(tobeparsed) <= 0:
		print("Error: " + str(tobeparsed))
		pass
	else:
		if tobeparsed[0] in opcodes:
			a = opcodes[tobeparsed[0]]
		else:
			print("Error Invalid instruction: \n" + str(tobeparsed))
		if tobeparsed[1] in registers:
			b = registers[tobeparsed[1]]
		else:
			b = int(tobeparsed[1], 2)
		if tobeparsed[2] in registers:
			c = registers[tobeparsed[2]]
		else:
			c = int(tobeparsed[2], 2)
	return str(a) + " " + str(b) + " " + str(c)

def executer(instruction):
	insruction = instruction.split()
	if instruction in opcodes:


