# 10. `PART 1` Configuration of a web server using SSL, the OpenSSL cryptographic library: authentication, encryption. `PART 2` The instruction set architecture (ISA) of Intel X86 processors (registers, addressing, instructions, memory architecture, interrupt system)

## Part 1

### SSL

SSL is a secure sockets layer which is the standard technology for keeping an internet connection secure and safeguarding any sensitive data that is being sent between two systems, preventing criminals from reading and modifying any information transferred, including potential personal details. A handshake protocol is used between the client and server to negotiate the secret key to be used for encrypting the messages. The handshake protocol follows these steps, step 1 is client hello, here the client will send a message to the server about its SSL version, cryptographic algorithms, and data compressing methods. Step 2 is server hello, server will send the cryptographic algorithms it chose from the client’s list, a session ID, its digital certificate, and its public key. In step 3, the client will verify the server’s digital certificate using the certificate authority to confirm the authenticity of the server. In step 4 the client has authenticated the server and it will send a shared secret key in an encrypted format which has been encrypted using the server’s public key, this key can be decrypted by the server since it has the corresponding private key, this shared secret key is stored and will be used for encryption and decryption of the data. In step 5, the client will send a finish message encrypted with the shared secret key. SSL certificate is a digital certificate that can be used for authentication of a website, we can use this for SSL. When a certificate is installed, it makes the website from HTTP to HTTPS. The SSL certificate has two keys, one is public and the other one is private. Data is encrypted with the public key and can be decrypted with a private key only. The web server with a private key can understand the data. Google made the HTTPS everywhere campaign which gave a search engine optimization boost to websites with a digital certificate and later marked all websites not using HTTPS to be insecure, this has pushed everyone to have a digital certificate.

### OpenSSL

OpenSSL is the open-source implementation of SSL. OpenSSL is a cryptographic software library or toolkit. The OpenSSL program is a command-line tool for using various cryptography functions of OpenSSL’s library. OpenSSL can be used to apply for a digital certificate and install the SSL files on the server. A certificate signing request or a CSR code is generated using OpenSSL. CSR is a block of encoded text with data about the website and the company. The owner must submit this CSR to the certificate authority for approval. The certificate request requires a private key from which the public key is created. To generate the private key, we need to specify a key algorithm, the key size, and an optional passphrase. The standard key algorithm is RSA, and the size is usually 2048 bits since this makes it very secure, a higher value can be used but it comes with a performance penalty. We use the OpenSSL command followed by genrsa, the -out argument and the name of the key, and the key size value. This creates the key with the chosen name in the current directory, this key is in the PEM format. The next step is to extract the public key from the private key, this can be done using the OpenSSL RSA command and using the private key as the -in argument and the public key name as the -out argument along with the -pubout argument. Since we have the private key and public key, we can create the CSR using the OpenSSL req command with the -new and -key arguments specifying the name of the private key for the -key argument and a given name for the CSR using the -out argument. OpenSSL will ask a few questions like country name, organization name, email address, etc. This CSR can be sent to the certification authority and then added to the website for a Digital certificate.

### SSL authentication

SSL authentication is intended for the client. The client or the browser verifies the identity of the server, if it finds the server and its certificate are legitimate, then it goes ahead and established a connection.

### SSL encryption

Encryption is a way to encode a message so that its contents are protected from unauthorized access. Secret-key or symmetric encryption is when a variable in cryptography is used what an algorithm to encrypt or decrypt code. Secret keys are only shared with the key’s generator. Public-key or asymmetric encryption is a cryptographic system that uses pairs of keys, the public key is known to others who can use it to encrypt the data, this data can only be decrypted by using the private key which is only available to the owner.

## Part 2

### Instruction set architecture

Instruction set architecture or ISA is an abstract model of a computer. A device executes instructions described by that ISA; a central processing unit is called an implementation. In general, an ISA defines the supported instructions, data types, registers, the hardware support for managing main memory, fundamental features such as memory consistency addressing modes and virtual memory, and the input/output model of the ISA. Intel created the x86 ISA which was based on the intel 8086 microprocessor. This is a proprietary ISA and it is not licensed to others like ARM’s ISA. x86 ISA started as 16-bit and later a 32-bit version was developed. AMD is the only other company that has access to this ISA, and AMD created the 64-bit version which is now called x86-64 or amd64. Even though both Intel and AMD use the same ISA to make their processors, they both have different products since the microarchitecture they use is different. When we talk about x86 ISA, we are referring to the 32-bit model.

### x86 registers

x86 registers are the main tools to write programs in assembly. The registers are like variables built in the processor. Registers are much faster than accessing the memory and it makes the process fast and cleaner, but there is only a small number of registers thus for many elaborate programs, we must keep storing register values to memory and take values from the memory to store in the registers. We have 4 general 32-bit registers, EAX, EBX, ECX, and EDX. We have 6 segment registers, CS, DS, ES, FS, GS, and SS. We have5 index and pointer registers ESI, EDI, EBP, EIP and ESP, and an EFLAGS register. The general registers can be broken down into 16-bit registers which are AX, BX, CX, and DX, and can be further broken down into 8 bits, AH, AL, BH, BL, CH, CL, DH, and DL. The H and L suffix on the 8-bit registers stand for high byte and low byte. These 4 general-purpose registers have some main use, A series registers are called the accumulator register and they are mainly used for I/O port access, arithmetic, and interrupt calls. The B series registers are called the base register, it is used as a base pointer for memory access and can get some interrupt return values. The C series registers are called the counter register, they are used for loop counters, and shifts, they too get some interrupt values. The D series registers are called data registers and they are used for I/O port access, arithmetic, and some interrupt calls. Segment registers hold the segment address of various items. The indexes and pointer registers have the following uses, EDI is used as destination index register ESI is used as a source index register, EBP is used as stack base pointer, ESP is used as a stack pointer, and EIP is used as an index pointer. The EFLAGS register is a 32-bit register that holds the state of the processor, and it is used for comparing parameters, conditional loops, and conditional jumps. There are various flag bits like carry flag, parity flag, zero flag, sign flag, etc.

### x86 addresses

x86 systems can address up to 232 bytes of memory, which means the memory addresses are 32-bits wide. In an assembly instruction where we require two operands, the first operand is generally the destination, which contains the data in a register or memory location and the second operand is the source. Source contains either the data to be delivered or the address of the data, generally, the source data remains unaltered after the operation. There are three basic modes of addressing:

- Register addressing – In this addressing mode, a register contains the operand. Depending upon the instruction, the register may be the first operand, the second, or both. Since this type of processing doesn’t involve memory, it is very fast.
- Immediate addressing – An immediate operand has a constant value or an expression. When an instruction with two operands uses immediate addressing, the first operand may be a register or memory location, and the second operand is an immediate constant. The first operand defines the length of the data.
- Direct memory addressing – When operands are specified in memory addressing mode, direct access to main memory is required. This way of addressing results in slower processing of data. To locate the exact location of data in memory, we need the segment start address, which is typically found in the DS register, and an offset value, this offset value is also called effective address. In direct addressing mode, the offset value is specified directly as part of the instruction, indicated by a variable name. In direct memory addressing, one of the operands refers to a memory location, and the other operand references a register.

### x86 intructions

Some basic instructions in x86 ISA are:

- Mov – The MOV instruction copies the data item referred to by its second operand into the locations referred to by its first operand.
- Push – The push instruction places its operand on top of the hardware-supported stack in memory. First push decrements ESP by 4, then places its operand into the contents of the 32-bit location at the address. The stack-pointed ESP is decremented by push since the x86 stack grows down, from high addresses to lower addresses.
- Pop – The pop instruction removes the 4-byte data elements from the top of the hardware supported stack into the specified operand.
- Add – This instruction adds its two operands, storing the result in the first operand.
- Sub – This instruction subtracts its two operands, storing the result in the first operand.
- Inc, dec – The inc instruction increments the contents of its operand by one. The dec instruction decrements the contents of its operand by one.
- Imul – This instruction will multiply its two operands and store the result in the first operand. There is a three-operand version where it will multiply the second and third operand and store the result in the first operand.
- Idiv – This instruction divides the contents of the 64-bit register which is a combination of EDX:EAX registers in x86 where EDX is the most significant 32 bits and EAX is the least significant 32 bits. The quotient result is stored in EAX while the remained is placed in EDX.
- And, or, xor – These instructions perform the specified logical operation on their operands, storing the result in the first operand.
- Not – This is the logical not and flips all bit values in the operand.
- Shl, shr – These instructions shift the bits in the contents of the first operand left or right.
- Jmp – This instruction transfers program control flow to the instruction at the memory location instructed by the operand.
- Jcondition – This can be je, jle, jg, or other variations and these are conditional jumps based on the status of the condition.
- Cmp – This compares the value of the two operands. This is basically the sub instruction, except the result of the subtraction is discarded.
- Call, ret – These instructions implement a subroutine call and return.

### x86 memory

x86 ISA is a 32-bit model, which means the memory addresses are of the width 32. The memory is called a stack, the stack has a width of 32 bits and it grows downwards. When we add something to the top of the stack, the ESP, or stack pointer gets decremented. When we start a program, the ESP stack pointer is at the top of the stack, when we issue a push command which will push data to the top of the memory stack, this will cause the ESP to be decremented.

### Interupts

An interrupt is an alert to the processor and serves as a request for the processor to interrupt the currently executing code. There are three types of interrupts:

- Hardware interrupts – These are triggered by hardware devices like a special key being pressed on the keyboard. Hardware interrupts are typically asynchronous, their occurrence is unrelated to the instructions being executed at the time they are raised.
- Software interrupts – There are a series of software interrupts that are used to transfer control to a function in the operating system kernel. Software interrupts are triggered by the instruction INT. For example, INT 14H triggers interrupt 0x14, the processor stops the current program and jumps to the code to handle interrupt 14.
- Exceptions – Exceptions are caused by exceptional conditions in the code which is executing. For example, an attempt to divide by zero or accessing a protected memory area. The processor will detect this problem and transfer control to a handler to handle this exception.
