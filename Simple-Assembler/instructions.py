import registers


instructions = ["add","sub","mov","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
opcode = ["00000","00001","00010","00011","00100","00101","00110","00111","01000","01001","01010","01011","01100","01101","01110","01111","10000"]
type = ["A","A","B","C","D","D","A","C","B","B","A","A","A","C","C","E","E","E","E","F"]
operands = [3,3,2,2,2,2,3,2,2,2,3,3,3,2,2,1,1,1,1,0]
type_A_instructions = {'add':'00000','sub':'00001','mul':'00110','xor':'01010','or':'01011','and':'01100'}
type_B_instructions = {'mov':'00010','rs':'01000','ls':'01001'}
type_C_instructions = {'mov':'00011','div':'00111','not':'01101','cmp':'01110'}
type_D_instructions = {'ld':'00100','st':'00101'}
type_E_instructions = {'jmp':'01111','jlt':'10000','jgt':'10001','je':'10010'}
type_F_instructions = {'hlt':'10011'}


def typeB_fun(instruction_entered):
    op_code = type_B_instructions[instruction_entered[0]]
    register_binary = registers.binary_of_registers[instruction_entered[1]][0]
    register_value = registers.binary_of_registers[instruction_entered[1]][1]
    register_name = instruction_entered[1]
    imm_string='{0:08b}'.format(int(instruction_entered[2][1:]))    #converting value stored in register

    if(instruction_entered[0]=="rs"):
        registers.binary_of_registers[register_name][1]= register_value >> int(instruction_entered[2][1:])
    elif(instruction_entered[0]=="ls"):
        registers.binary_of_registers[register_name][1]= register_value << int(instruction_entered[2][1:]) #place overflow check
    elif(instruction_entered[0]=="mov"):
        registers.binary_of_registers[register_name][1] = int(instruction_entered[2][1:])
    ml= op_code+register_binary+imm_string #converted into machine code
    print(ml)


def typeC_fun(instruction_entered):
    if instruction_entered[0]=="mov" and instruction_entered[2] =='FLAGS':
        op_code = type_C_instructions[instruction_entered[0]]
        register1_binary= registers.binary_of_registers[instruction_entered[1]][0]
        flags_value =  str(registers.V) + '{0:03b}'.format(registers.LGE)
        ml = op_code + '00000' + register1_binary + '111'
        print(ml)
        registers.binary_of_registers[instruction_entered[1]][1] = int(flags_value,2)
        return
    
    op_code = type_C_instructions[instruction_entered[0]]
    register1_binary= registers.binary_of_registers[instruction_entered[1]][0]
    register2_binary= registers.binary_of_registers[instruction_entered[2]][0]
    if(instruction_entered[0]=="mov"):
        registers.binary_of_registers[instruction_entered[1]][1] = registers.binary_of_registers[instruction_entered[2]][1]
    elif instruction_entered[0] =='div':
        if registers.binary_of_registers[instruction_entered[2]][1] ==0:
            print("Zero Division Error: Cannot divide by zero")
            return
        registers.binary_of_registers['R0'][1] = registers.binary_of_registers[instruction_entered[1]][1] // registers.binary_of_registers[instruction_entered[2]][1]
        registers.binary_of_registers['R1'][1] = registers.binary_of_registers[instruction_entered[1]][1] % registers.binary_of_registers[instruction_entered[2]][1]
    elif(instruction_entered[0]=="not"):
        binary_str_2nd_param = '{0:016b}'.format(registers.binary_of_registers[instruction_entered[2]][1])
        inverted_str =''
        for i in binary_str_2nd_param:
            if i == '0':
                inverted_str += '1'
            else:
                inverted_str += '0'
        registers.binary_of_registers[instruction_entered[1]][1] = int(inverted_str,2)  # bitwise not
    elif(instruction_entered[0]=="cmp"):
        if(registers.binary_of_registers[instruction_entered[1]][1]== registers.binary_of_registers[instruction_entered[2]][1]):
            registers.LGE=1
        elif(registers.binary_of_registers[instruction_entered[1]][1] < registers.binary_of_registers[instruction_entered[2]][1]):
            registers.LGE=4
        elif(registers.binary_of_registers[instruction_entered[1]][1] > registers.binary_of_registers[instruction_entered[2]][1]):
            registers.LGE=2
    ml= op_code+"00000"+register1_binary+register2_binary #converted into machine code
    print(ml)


def typeF_fun(instruction_entered):
    op_code = instructions.type_F_instructions[instruction_entered[0]]
    ml=op_code+"00000000000"
    print(ml)

