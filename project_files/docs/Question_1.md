# 1. `PART 1` The processor implementation options: Processor technology, implementation techniques and design technologies. Typically peripherals for embedded systems. Communication protocols. `PART 2` Program units. Subprograms. Parameter evaluation. Parameter passing methods. Block. Scoping, accessibility. Abstract data type. Generic programming. I/O tools of programming languages, file handling. Exception handling. Parallel programming.

## Part 1

### Processor technology

Processor – A processor or a central processing unit is the electronic circuit that executes instructions in a computer program. The processor performs basic arithmetic, logic control, and input/output operations specified by the instructions in a program. Principal components of a CPU include the arithmetic logic unit (ALU) that performs arithmetic and logic operations, processor registers that supply operands to the ALU and store the results of ALU operations, and a control unit that performs the fetch, decode, and execution cycle.

All processors execute a sequence of stored instructions which is called a program. These instructions are kept in the computer memory. The instructions cycle typically comprises fetch, decode, and execute. Fetch involves retrieving the instruction from program memory, which is determined by the program counter. Next comes decode, here the instruction is converted into a signal. Finally, the instruction is executed as a single action or sequence of actions. The results are usually written to the very fast registers on the CPU but sometimes can be written to the slower but much bigger computer memory. Modern CPUs also have cache, which is super-fast memory stored on the CPU, this is much smaller than the main memory, but can be used extremely quickly and thus reduces the time and energy to access data from the main memory. Cache has a hierarchy of where the data is organized called L1, L2, L3, etc. in decreasing speeds and increasing sizes. Most CPUs are synchronous circuits which means they use a clock signal to pace sequential operations. This clock signal is produced by an external oscillator circuit that generates a consistent number of pulses each second in the form of a periodic square wave. The frequency of the clock pulses determines the rate at which a CPU executes instructions, the faster the clock, the more instructions the CPU will execute each second.

### Microprocessor

Microprocessor – This is a computer processor where the data processing logic and control are included on a single integrated circuit. The microprocessor uses Very-Large-scale Integration to integrate the entire CPU onto a single IC, this greatly reduces the cost of processing power. The first commercially available microprocessor was the intel 4004. Microprocessors are very popular in almost all desktops and some laptops with modern processors like Intel’s alder lake and AMD’s ryzen 5000 using the x86-64 instruction set architecture.

### Microcontroller

Microcontroller – These are microprocessors along with memory and programmable input/output peripherals. Microcontrollers are designed for embedded applications like single-board computers like the raspberry pi. There are more sophisticated chips called System on a chip or SoC which have a microcontroller as a part but also have graphics processing unit and Wi-Fi modules. These SoCs are often seen in smartphones like the Apple A14 chip or the Qualcomm snapdragon 888 seen in most high-end iPhones and android phones.

### Implementation (ISA)

Implementation – An instruction set architecture is an abstract model of a computer. A device that executes instructions described by that ISA, such as a central processing unit, is called an implementation. Different ISAs vary in performance, efficiency, size, etc. ISA serves as the interface between software and hardware. Software that has been written for an ISA can run on different implementations of the same ISA. This has helped lower the costs of computers and increase their applicability. There are 3 popular ISAs today, x86-64 which was developed by Intel and then AMD. These are complex instruction set computer CISC architecture, which means a single instruction can execute several low-level operations. These are most prevalent on desktops, servers, and laptops. The other very popular ISA is ARM which is developed by Arm Ltd. These are reduced instruction set computer RISC architectures where a given task requires more instructions as compared to CISC, but the individual instructions are simpler and executed faster. ARM chips are also substantially more power-efficient and thus are the primary chips used in smartphones and single-board computers like the raspberry pi. They are also slowly being used for laptops due to their battery performance. The third most popular architecture is RISC-V which in contrast to x86-64 and ARM is open source. This means anyone can use this ISA without any royalties or licensing fees. This is also a RISC-based architecture.

### Embedded systems & Peripherals

Embedded systems are computer systems comprising of a processor, memory, and input/output peripheral devices that have a dedicated function within a larger system. Embedded systems range from simple microcontroller boards like Arduino to more complex systems which use multiple peripherals and networking equipment to communicate with other systems. Typical peripherals for embedded systems are:

1. Serial Communication Interfaces (SCI) – These are relatively slow, asynchronous communication ports that are used to communicate with other embedded systems and devices.
2. Inter-Integrated Circuit(I2C) – These are widely used for attaching lower-speed peripheral integrated circuits to processors and microcontrollers in short-distance communication.
3. Universal Serial Bus (USB) – USB is an industry-standard that allows for connection, communication, and power supply. Embedded systems can use it to power, transfer data, or connect to input devices like keyboards and mice.
4. Multimedia Cards (SD cards) – These are used to store the data, and, in most cases, they host the operating system for the embedded system.
5. Network (Ethernet) – Ethernet ports are a family of wired computer networking technologies used to connect multiple devices physically.
6. General Purpose Input/Output (GPIO) – GPIO is an uncommitted digital signal pin or multiple pins on embedded systems that can be used as an input or output or both and are controlled by the user at runtime. In the case of raspberry pi, we have multiple HATs (hardware attached on top) which connect to the GPIO pins. These can be temperature detection HAT, LED HATs, etc.

### Communication protocols in embedded systems

Communication protocols in embedded systems can be of two kinds – Inter system protocol and Intra system protocol.

1. Inter System Protocol - This is the communication between two communication devices, for example, a PC and an embedded system. Here communication is achieved through inter bus system.
   ● USB – Universal Serial Bus, this is a two-wired serial communication protocol. USB sends and receives the data serially between the host and an external peripheral device. Data is sent as packets.
   ● UART – Universal Asynchronous Receiver/Transmitter is a physical piece of hardware that converts parallel data into serial data. Its main purpose is to transmit and receive data serially.
   ● USART – Universal Synchronous Asynchronous Receiver/Transmitter is identical to UART with added synchronous functionality.
2. Intra System Protocol – This establishes communication between components within the circuit board.
   ● I2C – Inter-Integrated Circuit is a serial communication protocol. It allows connecting peripheral chips with a microcontroller.
   ● SPI - Serial Peripheral Interface is a serial communication protocol. It is used for short-distance communication in embedded systems.
   ● CAN – Controller Area Network is a serial communication protocol and is based on a message-oriented communication protocol. It is primarily used for communication in embedded systems in vehicles.

## Part 2

### Program Unit

The program unit is a sequence of one or more lines, organized as statements, comments, and includes directives. A program unit can be the main program, a module, a block data program unit, an external function subprogram, or an external subroutine subprogram.

### Subprogram

A subprogram is a sequence of instructions whose execution is invoked from one or more remote locations in a program, with the expectation that when the subprogram execution is complete, execution resumes at the instruction after the one that invoked the subprogram in high-level languages, subprograms are also called subroutines, procedures, and functions. In object-oriented languages, they are usually called methods or constructors. In most modern high-level languages, subprograms can have parameters, local variables, and returned values. A procedure just executes a set of instructions while a function will return a value when it has finished executing. Writing subprograms makes the code more readable and reusable as the code is broken into smaller sections.

### Parameter Evalaution

Parameter evaluation is the process of mapping formal and actual parameters when a subprogram is called. Formal parameters are defined in the specification of the subprogram, they are declared only once. Actual parameters (arguments) are specified in the calls themselves. Thus, the formal parameter list is determinative to parameter evaluation. There are three issues related to parameter evaluation:

1. Assigning actual parameter to formal parameter – The actual parameters are assigned to formal parameters based on their relative order in the parameter list, the first argument is assigned to the first formal parameter, second to second, and so on. We can also supply the name of the formal parameter and assign it to the actual parameter, here the order is irrelevant.
2. Number of actual parameters passed to the subprogram call – The number of formal parameters is fixed; in this case, the number of actual parameters must equal the number of formal parameters, or the number of actual parameters can be less than the number of formal parameters in which case the formal parameters did not assign an actual parameter during the subprogram call will be assigned default values which are pre-defined by the programmer.
3. Relationship between types of formal and actual parameters – In some programming languages the type of the actual parameter must be exactly as the type of the formal parameter. In other languages, the actual parameter is converted to the type of the corresponding formal parameter.

Parameter passing is the action of passing the actual parameters to the formal parameters when a function or subroutine is called. There are various methods to pass parameters:

1. Pass by value – Here the value of the actual parameters is copied to formal parameters. These two different parameters store the values in separate memory locations. Here we are passing the value and not the variable.
2. Pass by reference – Here both actual and formal parameters refer to the same memory location. Thus, the changes made to the formal parameters in the subroutine call will cause changes to the actual parameter. Here we are not passing the value but the memory address.

### Block

Block or code block is a structure of source code that is grouped. Blocks contain one or more declarations and statements. They allow us to group statements so they can be treated as one statement and to define scopes for variables to distinguish them from the same name used elsewhere.

### Scope

The scope is where an item like variable, constant, function, etc that has an identifier name is recognized and be used. These examples use a variable as the item. Global scope is when a variable is defined outside a function, when the program is compiled, this variable is assigned memory space at initialization. This variable can be used for all functions in the source code and even other modules which are linked to the code. Global variables are always defined at the very top before any function definitions, so they are available to all functions. Local scope occurs when a variable is defined inside a function or a code block like an if statement. When the code is compiled, these variables are assigned to the stack in the computer memory, this exists until the function is complete. These variables are assigned at the top inside of the function or code block, making them available to everything inside the function. If a local variable has the same name identifier as a global variable, then that variable will get the local variable value inside the function call.

### Abstract Data Types

Abstract Data Types or ADT are objects whose behavior is defined by a set of values and a set of operations. ADT only mentions what operations are to be performed but not how these operations will be implemented. It does not specify how data will be organized in memory and what algorithms will be used for implementing the operations. It is called abstract because it gives an implementation-independent view. There are many ADTs like list, stack, and queue, all of these have different implementations in different programming languages.

### Generic Programming

Generic programming is a style of programming where algorithms and functions are written in terms of types so that they work on all data types and not just one. We can have a placeholder data type which is a general data type, this can be replaced with different data types and work with all of them.

### I/O tools and file handling

Computer stores data in files like plain text, image data, etc. Files can be accessed, updated, and created using programming languages. When data is written into a file, that is called input and when data is read from a file, that is called output. Files can be handled in separate ways, read-only mode allows for only getting data from the file. Write only mode allows the programming language to only write data to the file and not read it. Read and write mode allows for both getting data from the file and writing data to the file. Append mode allows for writing the file without overwriting the existing data on the file. All programming languages first initialize an object of the type of file, which contains all the information to control the stream, we also must specify the mode such as read-only, write-only, etc. Once functions associated with the file are done, the file must be closed. Once this is done, the memory allocated for handling the file is freed up. In python a file is opened using the open() function, it can be read using read(), written to using write(), and closed using close() functions of the file object.

### Exception handling

Exception handling is the process of responding to the occurrence of exceptions or errors during the execution of a program. An exception breaks the normal flow of execution and executes a pre-registered exception handler. Exception handling attempts to handle these situations so that a program does not crash. In python, there are some built-in exception handlers, we can also define custom exception handlers using the ‘try – except’ blocks. The program first attempts the try block, if it throws an exception, then we execute the except block, and the program flow is maintained instead of crashing.

### Parallel programming

Parallel programming is when we use multiple processors or threads to execute parts of a program at the same time. The program is broken down into smaller steps, these are then executed simultaneously on multiple threads. The output of these steps mustn't influence each other. This is very advantageous since all modern processors are multi-core with SMT or Simultaneous multithreading enabled which means a single core can perform 2 virtual threads at the same time. This type of programming is hard to learn and to a large extent must be enforced by the programmer during programming.
