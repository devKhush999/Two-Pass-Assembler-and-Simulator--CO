import instructions
V = 0
LGE = 0
flags = {'FLAGS': '111'}
binary_of_registers = {'R0': ['000',0], 'R1':['001',0],'R2': ['010',0], 'R3':['011',0], 'R4': ['100',0], 'R5':['101',0], 'R6':['110',0]}


def typeA_fun(instruction_entered) :
    op_code = instructions.type_A_instructions[instruction_entered[0]]

    #taking register's binary value from the dictionaries
    register1_binary = binary_of_registers[instruction_entered[1]][0]
    register2_binary= binary_of_registers[instruction_entered[2]][0]
    register3_binary= binary_of_registers[instruction_entered[3]][0]
    ml= op_code+"00"+register1_binary+register2_binary+register3_binary #converted into machine code 

    #add function
    if (ml[:5]=="00000"):
        binary_of_registers[instruction_entered[1]][1] = binary_of_registers[instruction_entered[2]][1]+ binary_of_registers[instruction_entered[3]][1]
        if binary_of_registers[instruction_entered[1]][1]> 65535: #overflow:when the answer is more than 255
            V=1
            binary_of_registers[instruction_entered[1]][1] -= 65536      # remove this and set lower 16 bits values into Reg1

    #subtraction function
    elif (ml[:5]=="00001"):
        binary_of_registers[instruction_entered[1]][1]= binary_of_registers[instruction_entered[2]][1]- binary_of_registers[instruction_entered[3]][1]
        if binary_of_registers[instruction_entered[1]][1]<0:      # overflow : when the sub is less than 0
            V=1
            binary_of_registers[instruction_entered[1]][1]=0


    #multiplication function
    elif (ml[:5]=="00110"):
        binary_of_registers[instruction_entered[1]][1] = binary_of_registers[instruction_entered[2]][1]* binary_of_registers[instruction_entered[3]][1]
        if binary_of_registers[instruction_entered[1]][1]> 65535: #overflow:when the answer is more than 255
            V=1
            binary_of_registers[instruction_entered[1]][1] -= 65536  # remove this and set lower 16 bits values into Reg1

    #bitwise XOR
    elif(ml[:5]=="01010"):
        binary_of_registers[instruction_entered[1]][1]= binary_of_registers[instruction_entered[2]][1]^ binary_of_registers[instruction_entered[3]][1]

    #bitwise OR
    elif(ml[:5]=="01011"):
        binary_of_registers[instruction_entered[1]][1] = binary_of_registers[instruction_entered[2]][1] | binary_of_registers[instruction_entered[3]][1]

    #bitwise AND
    elif (ml[:5]=="01100"):
        binary_of_registers[instruction_entered[1]][1]= binary_of_registers[instruction_entered[2]][1] & binary_of_registers[instruction_entered[3]][1]
    print(ml)


