# 4. [PART 1] The SSH protocol, key generation, configuration of user settings [PART 2] The principles of control, feedback control and open loop control. Set point control and reference signal tracking, the role of negative feedback. Requirements for control systems.

## Part 1

SSH protocol or the secure shell protocol is a method for secure remote login from one computer to another. It has a strong authentication system, it maintains the integrity of the data being sent by running on top of the TCP protocol and always listens to the TCP/IP port number 22 by default, and it is secure since it encrypts the data using encryption algorithms like Advanced Encryption Standard AES or Data Encryption Standard DES. It is more secure than other remote login protocols like telnet and it is better at exchanging data than insecure file sharing protocols like File Transfer Protocol FTP. SSH can be used via the command line to connect and issue commands to the remote computer. SSH first establishes a connection between the client and the server in three steps:
Verification of server – The client initiates an SSH connection with the server, the client will authenticate the public key of the server.
Generation of a session key – Once the server is verified, both client and server will negotiate a session key using a Diffie-Hellman algorithm. The generated key is a shared symmetric key that will be used for the encryption and decryption of the data.
Authentication of the client – The client will send an ID for the public-private key pair. The server will check its authorized_keys file and see if the client's ID exists here. If it is found then the server will generate a random number and encrypt it using the public key, this message is sent to the client. If the client has the correct private key, it can decrypt the message and get the random number. This random number is used with the shared session key to create an MD5 hash. This MD5 hash is sent to the server, the server can use the shared session key and the original random number to calculate its MD5 hash. If the MD5 hash generated by the client matches the one generated by the server, the client has been authenticated and then the connection is completed. Instead of MD5, we can also use SHA-2 or secure hash algorithm 2.
SSH is used widely for things like managing routers, server hardware, virtualization platform, remote operating systems, etc.

Key generation is the process of generating keys in cryptography. A key is used to encrypt and decrypt whatever data is being encrypted/decrypted. A device or program used to generate keys is called a key generator or keygen. Modern cryptographic systems include symmetric key algorithms like Data Encryption Standard or DES and Advanced Encryption Standard or AES and public key algorithms like RSA. Symmetric key algorithms use a single shared key; keeping data secret requires keeping this key secret. Public key algorithms use a public key and a private key. The public key is made available to anyone by the means of a digital certificate. A sender encrypts the data with the receiver’s public key and only the holder of this private key can then decrypt the data. The SSH protocol uses a combination of the two key algorithms since public key algorithms tend to be much slower than the symmetric key algorithm. One party receives the other’s public key and encrypts a small piece of data, then the remainder of the connection uses a typically faster symmetric key algorithm for encryption. On a Linux machine, we can simply use the ssh-keygen command to generate a public/private authentication key pair. Authentication keys allow a user to connect to a remote system without supplying a password. Keys must be generated for each user separately. Use the -t option to specify the type of keys like RSA or DSA. The user can also specify a passphrase to encrypt the private key. The shh-key command will generate two keys in the hidden directory .ssh in the home directory of the user. These two files are id_rsa and id_rsa.pub. the id_rsa.pub is the public key, this should be placed in the remote systems authorized_keys directory in its .ssh hidden folder on its home directory, this directory must also have root permissions granted. Now whoever has the corresponding private key can login to this remote computer using ssh protocol.

A user is an entity in Linux that can manipulate files and perform other operations. Each user is assigned a unique ID called the UID or user identifier. When the system is created ID 0 is assigned to the root user and IDs 1 to 999 are assigned to the system users and thus the IDs of local users begin from 1000. On Linux systems, user settings configuration can be done using the command line. A new user can be added using the adduser command followed by a name that has not already been taken. This command will create a new account with a new UID, the user’s information is stored in the /etc/passwd and /etc/shadow files, and create a home directory for this user. The user can set a password for this account using the passwd followed by the name. A user account can be removed using the deluser command. The user configuration file which is the /etc/passwd file can be accessed using a text editor like nano since the data is stored in plaintext. The usermod command with various arguments can be used to make changes like changing the ID of the user, modifying the group ID of the user, changing the user login name, and changing the home directory of the user. The root user has access to all files on the system whereas the normal users have limited access.

## Part 2

Control systems manage commands, direct, or regulates the behavior of other devices or systems using control loops. A control loop is the fundamental building block of industrial control systems. Control loops are systems applied by design engineers to maintain process variables PVs at the desired value or setpoint SP. Control loops are important for maintaining the stability of a system and for consistently producing the desired outcome of a process. A basic example of a control loop is a temperature control loop. These work to maintain the temperatures in our homes and offices. The steps are as follows:
The process to be controlled is established. In the case of the temperature control loop, this refers to the temperature of a substance that is being heated.
Sensors measure the process value PV. In the case of the temperature control loop, the current value of the temperature, the sensor is usually a thermostat in this example.
Sensors feed the measured value of the process value to the controller. In this example the temperature controller. This initiates the control process to achieve the set point or desired temperature in this example.
The final control element receives the manipulated values from the controller. In this example, the temperature is increased or decreased.

The core components of a control loop are:
Sensors and transducers – Sensors are the initial measurement devices in a control loop. They convert the process variable PV into corresponding analog or digital signals which are read by the controllers. Transducers are advanced sensors that further transform the given values through signal conditioning.
Controllers – The controller is the device that interprets the measurements fed by the sensor and determines the control action to take based on a comparison of that to the setpoint SP. PID or proportional integral derivative controllers are the most effective and stable controllers.
Final control elements and actuators – Final control elements are those that receive the control action signals from the controllers. They adjust the process variable PV at the desired parameter. Actuators are an important component within final control elements. These have a direct influence on the control process.

There are two types of control loops, open-loop control, and closed-loop or feedback control loops. An open-loop control system acts completely based on input; the output does not affect the control action. A closed-loop control system looks at the current output and alters it to the desired condition; also known as a feedback system, the control action in these systems is based on the output. Open-loop control is used when low cost is a priority as open control is inexpensive. They are also great when the output rarely changes if at all for example in cooling pumps. They can be used when there is no possibility of quantitative measurement or when the process is erratic, for example, a process with an erratic sensor. Closed-loop or feedback control loops are used when the measurement is feasible, and the process has a degree of predictability; that is when we have a known estimated response to the input control. We also use closed-loop control when the output varies from the desired outcome. Before working with closed-loop control, all parts must be in proper working condition and order and there must be no erratic sensors. This makes closed-loop controls more expensive than open-loop control.

Setpoint in control systems is the target value that an automatic control system, for example, a PID controller will aim to reach. For example, a boiler control system will have a temperature setpoint which is set using a thermostat. This is the temperature the control system aims to attain, and the entire system will modulate the actuators to achieve it. The reference signal is the signal which is external to the control loop, this serves as the reference or the comparison to the controller variable. Reference signal tracking involves keeping track of this value and constantly updating the system to match it.

Feedback loops come in two different kinds: positive and negative. Negative feedback loops are more common and work to keep a system stabilized or at equilibrium. In negative feedback, the effective input is the difference between the reference input and the feedback signal but in positive feedback, the effective input is a summation of the reference input and the feedback signal. This is why the stability of a system increases in negative feedback, but it decreases in positive feedback. Thus, the accuracy of a system also increases in negative feedback. An electronic amplifier is an example of a negative feedback system. We prefer negative feedback to positive feedback since positive feedback tends to lead to instability due to exponential growth or chaotic behavior, on the other hand, negative feedback promotes stability.

Requirements of a good control system:
Sensitivity – The rate of change of a control system with the change in its surroundings is called sensitivity. A good control system should be sensitive to its input only and should not be sensitive to the surrounding parameters.
Accuracy – The tolerance of errors of an instrument is known as accuracy. We can improve the accuracy by using feedback elements like adding an error detector circuit in the control system to increase the accuracy.
Stability – If the input of a system is zero then the output should also be a zero value. If the input changes, the output also changes as per the system function, this is a stable system.
Noise – Undesired signal input due to external sources is known as noise. A good control system should have a high noise tolerance value, so it can reduce the noise level. System performance decreases as noise value increases.
Speed – In control systems, the time taken by the output to be stable is known as speed. High-speed systems are considered good control systems.
Bandwidth – Bandwidth is the range of frequencies of a system. Bandwidth is decided by the operating frequencies. A system having a high bandwidth is considered a good control system.
Oscillation – Oscillation means the fluctuations of the output of a system. These oscillations affect the stability and a higher number of these fluctuations in a system will decrease the stability of a system.