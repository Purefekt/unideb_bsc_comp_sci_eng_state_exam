# 2. `PART 1` Synthesis of continuous time control systems. The gain and phase margin. Linear systems and their description in time- and frequency domains. Signal transfer in control systems.`PART 2` Explain the data elements of TCP and UDP transport layer protocols, and the differences between their mechanisms.

## Part 1

### Control Systems

A control system is a system that provides the desired response by controlling the output. The input is varied by some mechanism. The traffic lights control system is an example of a control system. A sequence of input signals is applied, and the output is one of the three lights that stay on for some duration of time. Based on the traffic data at a particular junction, the on and off times of the lights can be determined. The input signal controls the output, and it operates on a time basis. Control systems can be classified on the type of signal. A system that deals with continuous-time signals is called a continuous-time system; its opposite is the discrete-time system which uses discrete-time signals. Continuous-time systems view variables as having a particular value for potentially only an infinitesimally short amount of time. The variable time ranges over the entire real number line. Its domain is a continuum, that is the function's domain is an uncountable set.

### Gain and Phase Margin

Gain and Phase margin can be derived from a Bode plot. A bode plot is a graph that is used to determine the stability of a control system. It maps the frequency response of the system through two graphs – the bode magnitude plot (expressing the magnitude in decibels) and the bode phase plot (expressing the phase shift in degrees).
The Gain Margin (GM) is the amount of gain which can be increased or decreased without making the system unstable. It is expressed as a magnitude in decibels. The greater the gain margin, the greater the stability of a system. GM can be read directly from a bode plot, this is done by calculating the vertical distance between the magnitude curve and the x-axis at the frequency, this point is known as the phase crossover frequency. The gain margin is the negative of gain. If the gain is 20 then the gain margin is -20 decibels.
Phase Margin (PM) is the amount of phase which can be increased or decreased without making the system unstable. It is expressed as the phase in degrees. The greater the phase margin, the greater the stability of the system. We can read the phase margin directly from a bode plot. This is done by calculating the vertical distance between the phase curve and the x-axis at the frequency. This point is known as the gain crossover frequency. Phase margin is the phase lag plus 180 degrees. If the phase lag is -189 degrees, then the phase margin is -9 degrees.

### Linear Systems

Linear systems are systems whose outputs for a linear combination of inputs are the same as a linear combination of individual responses to those inputs. Linear systems can be time-invariant which are linear systems where the output does not depend on when input was applied. So, if we apply an input to a system now or T seconds from now, the output will be identical except for a time delay of T seconds. Linear systems in frequency domains refer to the analysis of these systems with respect to frequency. A frequency-domain graph shows how much of the signal lies within each given frequency band over a range of frequencies. To change a linear system from a time domain to a frequency domain, we apply a Laplace transform function of the impulse response. In the frequency domain, the output is the product of the transfer function with the transformed input.
Linear control systems use negative feedback to produce a control signal to maintain the controlled PV at the desired SP. There are several types of linear control systems with different capabilities.

### Transfer Function

Transfer function represents the relationship between the output signal of a control system and the input signal for all possible input values. For any control system, there is a reference input known as excitation which operates through a transfer function to produce a controlled output. The transfer function of a control system is defined as the ratio of the Laplace transform of the output variable to the Laplace transform of the input variable assuming all initial conditions to be zero. It is not necessary that the output and input of a control system are of the same category. For example, in electric motors, the input is an electrical signal whereas the output is a mechanical signal since electrical energy is required to rotate the motors. Similarly in an electric generator, the input is a mechanical signal, and the output is an electrical signal since mechanical energy is required to produce electricity in a generator. But for mathematical analysis of a system, all kinds of signals should be represented in a similar form. This is done by transforming all kinds of signals to their Laplace form. Transfer functions can be obtained using a Block diagram method or a signal flow graph. The Block diagram method is when the transfer function of each element of a control system is represented by a block diagram. A modified form of a block diagram is a signal flow graph which further shortens the representation of a control system. Poles of a transfer function are defined as those values in the ratio whose substitution in the denominator makes the transfer function infinite. Zeros of transfer function have to do with the numerator. Those values of the ratio that when substituted make the transfer function zero is the zeros of the transfer function. The steps to calculate the transfer function are as follows:

- The time-domain equations of the system must be written after considering different required variables in the system.
- Consider the initial conditions as 0, write the Laplace transform of the time domain equations of the system.
  Determine the input as well as the output variables from the frequency domain equations.
- Remove the initially considered variables and write the resultant equations in the form of input and output variables.
- The ratio of Laplace transform of output and input must be determined to have the transfer function of the overall system.

## Part 2

### TCP

TCP stands for Transmission Control Protocol, which is a communications standard that enables applications, programs, and computing devices to exchange messages over a network. It is designed to send packets across the internet and ensure the successful delivery of data and messages over networks. TCP guarantees the integrity of the data being communicated over a network. High-level protocols like File Transfer Protocol (FTP), Secure Shell (SSH), Telnet, Internet Message Access Protocol (IMAP), and Simple Mail Transfer Protocol (SMTP) all use TCP. TCP is an expensive protocol since a connection is established between the server and the client. Three-way handshake and error detection add to reliability but increase latency.
TCP accepts data from a data stream, divides it into chunks, and adds a TCP header creating a TCP segment. The TCP segment is then encapsulated into an Internet Protocol datagram and exchanged with peers. A TCP segment consists of a segment header and a data section. The segment header contains 10 mandatory fields and an optional extension field. The data sections follow the header and are the actual data carried for the application. The sections are:
Source port (16 bits) – The client’s port number.
Destination port (16 bits) – The server’s port number.
Sequence number (32 bits) – A sequence number used for guaranteeing packet order.
Acknowledgment Number (32 bits) – An acknowledge number notifying senders of the receipt of TCP segments.
Data offset (4 bits) – The size of the TCP header.
Reserved (3 bits) – Set to zero, reserved for future use.
Flags (9 bits) – Flags set TCP control options used to alter the connection.
Window (16 bits) – The receive window. The number of bytes that the sender of this segment is willing to receive.
Checksum (16 bits) – A 16-bit checksum used for error-checking.
Urgent pointer (16 bits) – If the sender sets the URG flag, then this 16-bit field is an offset from the sequence number indicating the last urgent data byte.
Options (0-320 bits [divisible by 32])
Padding (0-320 bits [divisible by 32]) - Zeros, ensures that the TCP header ends, and data begins on a 32-bit boundary.
Data (variable) – The payload data for this TCP segment.

TCP uses a three-way handshake to establish the connection. First, the client will generate a random number and set it as the sequence number and set the SYN or synchronization bit on, and send this to the server. The server will send a message back to the client, the SYN bit will be on and the ACK or acknowledge bit will be set to the sequence number the client sent plus one. The server will generate its sequence number and send it as well. In the last step, the client sends a message to the server, this time the SYN bit is 0, the acknowledgment number is the sequence number of the server plus one and the sequence number is the acknowledgment number sent by the server in the last step which is the sequence number of the client in the first step plus one. After the handshake is complete, a client can start sending data packets immediately. TCP segments are exchanged between the client and the server. To guard against the unreliable network, TCP uses sequence numbers to verify the correct delivery and ordering of TCP segments. The sequence number is included on each transmitted packet and acknowledged by the opposite host as an acknowledgment number to inform the sending host that the transmitted data was received successfully. Flow control can be managed by the window field, if a sender is under heavy load, then it sets the window to a low value to decrease pressure and vice versa.

### UDP

UDP is User Datagram Protocol is a communication protocol that is primarily used to establish low-latency and loss tolerating connections between applications on the internet. UDP speeds up transmissions by enabling the transfer of data before an agreement is provided by the receiver. As a result, UDP is good for time-sensitive communication like voice over IP (VoIP) and domain name system DNS lookup. UDP sends messages as datagrams and doesn’t provide any guarantee that the data will be delivered or checked for dropped data. UDP allows for packets to be dropped and received in a different order than they were transmitted, making it have low latency. It can be used where many clients are connected, and real-time error correction isn’t necessary such as gaming.
UDP header has 4 fields, each of 2 bytes:
Source port number – the port number of the sender.
Destination port number – the destination port number.
Length – the length in bytes of the UDP header and any encapsulated data.
Checksum – used for error checking, it is required in IPv6 and optional in IPv4.

### Differences between UDP and TCP

- UDP is a connectionless protocol whereas TCP is a connection-oriented protocol.
- UDP is used for VoIP, gaming, live broadcasts whereas TCP is used for most data protocols on the internet.
- UDP is faster and uses fewer resources whereas TCP has higher latency and is resource-intensive.
- The packets in UDP don’t necessarily arrive in order, whereas the TCP ensures packet order so they can be stitched back together.
- UDP allows for missing packets, the sender is unable to know whether a packet was successfully received or not, whereas TCP guarantees no missing packets, and all sent data makes it to the intended recipient.
- There is basic error checking mechanisms in UDP whereas there is extensive error checking and acknowledgment of data in TCP.
- UDP supports broadcasting whereas TCP does not.
- UDP is better suited for time-sensitive applications whereas TCP is better suited for applications that need data reliability and are not as time sensitive.
- UDP has a smaller header than TCP.
