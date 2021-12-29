# 6. `PART 1` Sequential logical: Latches and Flip-Flops. Counters. Shift registers. Memories. `PART 2` New elements of HTML5. New features of CSS3. Control structures in web scripts. Sensor through a web page. Providing remote management systems through a web page.

## Part 1

Sequential logic is a form of binary circuit design that has one or more inputs and one or more outputs, whose states are dependent in part on the previous states. Sequential logic circuits have some form of inherent memory built-in. Sequential logic circuits remember the conditions and stay fixed in their current state until the next clock signal changes one of the states.

Latches are basic storage elements that operate with signal levels. Latches are level-sensitive devices and are useful for the design of asynchronous sequential circuits. There are two basic latches called the SR latch and the D latch.
SR latch is a circuit with two cross-coupled NOR gates or two cross-coupled NAND gates with two inputs labeled S for set and R for a reset with two outputs Q and Q prime. This latch has two useful states. When the output Q is 1 and Q prime is 0, the latch is said to be inset state. When Q is 0 and Q prime is 1, then it is in a reset state. Normally the outputs Q and Q prime complement each other. An SR Nor latch has these states:

1. When S is 0 and R is 1, then the output Q is 0 and Q prime is 1. This is the reset condition. Now if R goes back to 0, the reset state remains, now S and R are 0 but the previous output has been stored as memory.
2. When S is 1 and R is 0, then Q prime is 0 and Q is 1. This is the set state. Now if S goes back to 0, the circuit remains in the set state.
3. When S and R are both 1, then Q and Q prime become 0, this violates that both outputs must complement each other, this condition is avoided by making sure that 1s are not applied to both inputs simultaneously, this is the invalid state.
   To fix the drawback of the invalid state where both inputs are 1, we use the D latch, which has a single input D by sending the same signal to both S and R but placing an inverter in front of either one of them. This ensures that the input to one is always the opposite of the input to the other.

Flip-Flops are just edge-triggered latches, it only changes state when a control signal goes from high to low or low to high. This makes using flip-flops with clock signals possible. We have SR flip-flops and D flip-flops which are the same as the latches. We have other flip-flops like JK flip-flop and T flip-flop.

Counters are devices that store the number of times a particular event or process has occurred, often in relationship to a clock. A 4-bit ripple counter will count from 0000 or 0 to 1111 or 15. This can be made by chaining 4 T flip-flops together. Each clock pulse causes a change that ripples through the chain of flip flops with a delay. We also have synchronous counters which use the same clock signal on all flip-flops, this uses more circuitry but has no delay. There are also ring counters which are composed of flip-flops connected into a shift register, with the output of the last flip-flop fed to the input of the first, making a circular or ring structure. There are two types of ring counters, a straight ring counter connects the output of the last shift register to the first shift register input, this circulates a single one or zero bit around the ring. A twisted ring counter connects the complement of the output of the last shift register to the input of the first register and circulates a stream of ones followed by zeros around the ring.

Flip-flops can be used to store a single bit of binary data. To store multiple bits of data, we need multiple flip-flops, N flip-flops connected to store n bits of data are called registers. A shift register is a type of digital circuit using a cascade of flip-flops where the output of one flip-flop is connected to the input of the next. They share a single clock signal which causes the data stores in the system to shift from one location to the next. By connecting the last flip-flop back to the first, the data can cycle within the shifters for extended periods and in this form, they are used as a form of computer memory. The registers which shift the bits to the left are called shift left registers and the registers which will shift the bits to the right are called shift right registers. We have 4 basic types of shift registers:

1. Serial in serial out – these allow serial input and produce serial output.
2. Serial in parallel out – these allow serial input and produce a parallel output.
3. Parallel in serial out – these allow parallel input and produce a serial output.
4. Parallel in parallel out – these allow parallel input and produce a parallel output.

System memory is like a human brain. It is used to store data and instructions. Computer memory is the storage space in computers where data to be processed and instructions required for processing are stored. The memory is divided into a large number of small parts. Each part is called a cell and each location or cell has a unique address that varies from zero to memory size minus one. Memory is primarily of two types, internal memory like cache memory and primary memory, and external memory like magnetic disk, optical disk, or flash storage.

## Part 2

HTML 5 introduced the following new elements:

1. Article – represents an independent piece of content of a document, such as a block entry or newspaper article.
2. Aside – Represents a piece of content that is only slightly related to the rest of the page.
3. Audio – defines an audio file.
4. Canvas – This is used for rendering dynamic bitmap graphics on the fly, such as graphs or games.
5. Command – Represents a command the user can invoke.
6. Datalist – Together with the new list attribute for input, can be used to make combo boxes.
7. Details – Represents additional information or controls which the user can obtain on demand.
8. Embed – Defines external interactive content or plugin.
9. Figure – Represents a piece of self-contained flow content, typically referenced as a single unit from the main flow of the document.
10. Footer – Represents a footer for a section and can contain information about the author, copyright information, etc.
11. Header – Represents a group of introductory or navigational aids.
12. Group – represents the header of a section.
13. Keygen – Represents a control for key pair generation.
14. Mark – Represents a run of text in one document marked or highlighted for reference purposes.
15. Meter – Represents a measurement such as a disk usage.
16. Nav – Represents a section of the document intended for navigation.
17. Output – Represents some type of output, such as from a calculation done through scripting.
18. Progress – Represents a completion of a task, such as downloading or when performing a series of expensive operations.
19. Ruby – Together with rt and RP allows for marking up ruby annotations.
20. Section – Represents a generic document or application section.
21. Time – Represents a date or time.
22. Video – Defines a video file.
23. Wbr – Represents a line break opportunity.

New features of CSS3 are as follows:

1.  Advanced animations – We can utilize both transition and animation when it is required to change a component starting with one state moving onto the next. With transitions, a user can make float or mouse down effects or trigger the animation by changing the style of a component with JavaScript.
2.  Multiple backgrounds and gradient – With multiple backgrounds, creators can stack various pictures as backgrounds of a component. Each picture or layer can be moved and animated with ease. CSS3 also allows for gradients as backgrounds.
3.  Multiple column layouts – This feature enables web designers to display their content in multiple sections with alternatives like column-width, column-gap, etc.
4.  Opacity – This property can make components more transparent. The opacity ranges from 0 which is transparent to 1 which is opaque.
5.  Rounded corner – This feature is very famous among social media giants. Rounded corners can make a site look tidier.
6.  Selectors – these are patterns or elements and other terms that tell the browser which HTML elements should be selected to have the CSS property values inside the rule applied to them. The elements selected by the selector are called the subject of the selector.

Control structures are programming constructs that determine which statements or procedures are executed at a given point in a program, either based on the evaluation of one or more variables or in response to some external input. In the absence of control structures, program statements will execute sequentially or in the order in which they appear in the code. There are two basic kinds of control structures – conditional and iterative.
A conditional control structure typically defines a sequence of one or more program statements that will be executed if a particular condition is met.
An iterative control structure loops through or iterates a sequence of program statements repeatedly until some predetermined exit condition is met. Program loops can be for example a counting loop that iterates a fixed number of times and then exits the loop. The number of iterations is determined by the value of a counter variable.
In web scripts we have some basic types of control structures:

1. If-else – This evaluates a condition as a true or false value, if the value is true, the block following if statement is executed, if this is false then the block following else is executed. We can only execute one of the two blocks for a given expression.
2. Switch – The switch statement allows us to make multiple if-else constructs more elegantly. We have a statement that might have multiple outputs, for each discrete output we have a different switch case. We also have a default case for when none of the given cases are met. For a given expression only one case can be executed at a time.
3. For loop – This control structure has a counter variable and will run a block of code for a specified number of times, specified by the counter variable. Once this number has been reached, the program exits the loop.
4. For in – This control structure iterates through the enumerable properties of a JavaScript object.
5. While loop – This loop executes a block of code over and over until a certain condition is met. This condition is defined outside the loop and can be changed within the loop. Once this condition is met, the loop exits.
6. Try catch – The try-catch block is used to handle exceptions. The code is first sent to the try block, if it doesn’t throw an error, the next catch block is ignored, and program flow continues. If the try block throws an error, the control is transferred to the catch block which will execute the given exception handler.

Sensor data is used by many web apps to enable immersive gaming, fitness tracking, and augmented reality applications. The Generic Sensor API is a set of interfaces that expose sensor devices to the web platform. The API has a base sensor interface and a set of sensor classes built on top. There are sensors like accelerometer, gyroscope, gravity sensor for motion, and ambient light sensors for the environment.

Remote Management is managing a computer or a network from a remote location. It involves installing software and managing all activities on the systems/network, workstations, servers, or endpoints of a client, from a remote location. Remote administration refers to any method of controlling a computer from a remote location. Software that allows remote administration is becoming increasingly common and is often used when it is difficult or impractical to be physically near a system to use it.
