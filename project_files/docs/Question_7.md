# 7. `PART 1` Provide the necessary steps and technologies for developing a sample software product on a choosen platform. Describe the benefits and difficulties of the platform, the implementation steps, and the most widely used current technologies. `PART 2` Implementation of control structures in assembly (control program flow, branching, looping)

## Part 1

Software is planned, created, tested, and deployed, this cycle is called a Software Development Life Cycle or SDLC. Various SDLC methodologies were popular in a certain time frame and were slowly replaced by the next one.

### Waterfall Model

The waterfall model is broken down into sequential phases. In this model, each phase must be completed before the next phase can begin and there is no overlapping in the phases. The outcome of one phase acts as the input for the next phase sequentially.
This model has 6 phases:

1. Requirement gathering and analysis
2. System Design
3. Implementation
4. Integration and Testing
5. Deployment of system
6. Maintenance

---

- Advantages: This model is simple and easy to understand and easy to manage due to its rigidity. All phases are processed one at a time which means it has very well-defined stages with deliverables that can be easily assessed.
- Disadvantages: There is no working software until the end of the life cycle. This introduces lots of risk and uncertainty. This model can get overwhelming for complex projects or long-term projects. This type of model is also not suited for projects which have a risk of changing their requirements. It is difficult to measure progress within the stages.

### Iterative Model

In this model, we start with a simple implementation of a small set of software requirements and iteratively enhance versions until the complete system is implemented and ready to be deployed. We do not require a full specification of requirements to start. On each iteration, the project is reviewed, and modifications are made on the next iteration. Each iteration flows through the design and development, testing, and implementation phases.

- Advantages: A working software can be developed early in the life cycle. Results are obtained early, and progress is easy to measure. This type of model is cheaper to change the requirements for. The testing phase is simpler as it is only concerned with the changes in the current iteration. It is easier to analyze risk since risks can be identified on each iteration.
- Disadvantages: This type of model requires more resources, even though the cost to change the requirements is less, more resources are required to execute the many iterations. This is not suitable for smaller projects. The end of the project is not clearly defined which is a risk.

### Spiral Model

This model is a combination of iterative models and takes aspects of the sequential flow like in the waterfall model. This model has four phases, a software project is repeatedly passed through these phases in iterations called spirals. These phases are:

1. Identification – This involves gathering the business requirements in the initial spiral. In subsequent spirals, the subsystem requirements are identified in each iteration.
2. Design – This phase starts with conceptual design in the initial spiral. In subsequent spirals, it involves architecture design, logic design, product, and final design.
3. Constructor builds – This is where the actual software development happens. In the initial spiral, the software is simply a proof of concept or POC. In subsequent spirals, it is developed further.
4. Evaluation and risk analysis – This phase includes identifying, estimating, and monitoring risks such as schedule slippage or cost overrun. The customer provides feedback on every iteration of this phase.

---

- Advantages: It’s easy to change the requirements. This model allows for quick iterations of software early in the life cycle. Development can be divided into smaller parts and riskier parts can be developed in later spirals.
- Disadvantages: Management for such a model is more complex and the end of the project is not clearly defined. This is not suitable for small-scale projects. Since there are many intermediate stages, it requires extensive documentation.

### Agile Model

This model breaks the product into small incremental builds. These builds are provided in iteration where each iteration typically lasts from one to three weeks. Every iteration includes cross functioning teams working on areas like:

1. Planning
2. Requirement analysis
3. Design
4. Coding
5. Unit testing
6. Acceptance testing

At the end of the iteration, a working product is displayed to the customer.
In Agile, tasks are divided into time boxes to deliver specific features for a release. Each build is incremental in terms of features and the final build contains all features required by the customer. This is the most popular model used in SDLC today. Agile has 4 main principles:

1. Individuals and interactions – Self-organization and motivation are important as well as co-location and pair programming.
2. Working software – There must be a demo working software that best communicates to the customer to give updates and understand new requirements instead of simply documentation.
3. Customer collaboration – Continuous customer interaction is very important since all the requirements are not established at the very start, these evolve with the input of the customer.
4. Responding to change – Agile development is focused on quick responses to change and continuous development.

---

- Advantages: It is a very realistic approach and promotes teamwork and cross-training. Functionality can be developed rapidly and demonstrated. This works for both fixed and changing requirements. There is a working software early in the life cycle. This model is easy to manage and gives flexibility to developers.
- Disadvantages: This model requires a plan, an agile leader, and an agile project manager. Depends heavily on customer interaction, which means if the customer is not clear then the project can become slow or hard to materialize. Transfer of technology to new team members might be difficult due to a lack of extensive documentation.

There are some famous agile frameworks like SCRUM where a product owner will dictate some requirements which are put in the product backlog which is managed by a scrum master. Some sprints can last from one or two weeks with daily scrum meetings to give small updates and talk about roadblocks. At the end of a sprint, a version is delivered which is showcased to the customer. We also have Kanban which is a scheduling system like Jira which includes 4 main columns which are to-do, in progress, testing, and done. Tickets are created and tasks are moved from left to right as they are done. This is completely transparent to the team and the customer.

## Part 2

### Control structures

Control structures are a way to specify the flow of control in programs. They analyze and choose the direction in which a program flows based on certain parameters or conditions. The three basic control structures are Sequence, which is the default control structure where instructions are executed one after the other. The next basic type is conditional control structures, which allow the program to follow many options of paths depending on a given condition. The last type of control structure is iterative where instructions are executed in the body of a loop. Assembly language low-level control structures make extensive use of labels. These control structures usually transfer control between two points in the program. We specify the destination of such a transfer using a statement label, a label consists of a valid identifier and a colon. The three basic types of control structures are present in the assembly and are:

### Sequential

In assembly, these are basic arithmetic, logical, and bit operations where data is moved and copied. An example would be ‘MOV EAX, EBX’ where we move the 4 bytes in memory at address ebx into eax.

### Conditional or branching

In assembly these structures consist of direct and indirect jumps. Here we choose between two or more alternative paths, in assembly, this is done by using two types of instructions: a compare instruction like CMP which compares the two values, this is simply a subtract instruction internally. This is followed by a jump statement which will go to the instruction label which satisfies the given condition. There are two types of jumps, conditional jump instruction like jump if equal JE will go to the label if the two values are equal, which means the output of the compare instruction must be zero. The other type of jump instruction is an unconditional jump. This is performed by the JMP instruction. This type of jump instruction is used to jump on a particular location unconditionally, that is there is no need to satisfy any condition for the jump to take place. Some examples of conditional jump instructions are JNE or jump if not equal, JG or jump if greater, JGE, jump if equal or greater, JL or jump if lower, JLE or jump if lower. An unconditional jump example could be JMP followed by the label which is a direct jump or It can be followed by a register or a memory address. An example of conditional jump instruction can be that we have two registers AH and CH and we have moved a value into them. Next, we can compare these two with the CMP instruction followed by AH and then CH. We can then define some conditional jump instructions like JE followed by a label like L1, this instruction will be executed if the value in AH and CH are equal, we can also have an instruction like JL followed by a label like L2, we will jump to L2 if AH is less than CH. Both L1 and L2 will point to code blocks where we can execute whatever logic we need to.

### Iterative or looping

In assembly, these are looping structures like WHILE, DO WHILE, and FOR. They can be implemented using the JMP instruction. These loops must have an exit or break statement to avoid infinite loops. Infinite loops are usually a programmer’s error, but event loops and task schedulers are examples of an infinite loop. Processors also have a newer LOOP instruction to execute loops more conveniently. An example of a loop that will execute a block for a fixed number of times with JMP instruction could be if we move the value 5 to the register AL. Then we will define a label for example L1, inside this code block we will decrease the value of AL by one using the DEC instruction on each loop iteration. Next, we can use a conditional jump statement like JNZ followed by L1, this code will run 5 times, when AL reached 0, we will not go back into the loop but exit it. We can also use the LOOP instruction to create a loop. An example could be if we move the value 5 in the ECX register and define a loop L1. This loop can simply have the instruction LOOP followed by L1 or the label we want to iterate over. The LOOP instruction decrements the value of ECX and compares it with zero, if the value in ECX is equal to zero, the program jumps to the L1 label, otherwise, it exits the loop.
