Dining Philosophers Problem in Distributed Systems
--------------------------------------------------

This program demonstrates a solution to Dining Philosophers's Problem in Distributed Systems by not using shared memory. Message Passing is the only means of communication.

## What is Dining Philosopher Problem?

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed between each pair of adjacent philosophers. 

Each philosopher must alternately think and eat. However, a philosopher can only eat spaghetti when they have both left and right forks. Each fork can be held by only one philosopher and so a philosopher can use the fork only if it is not being used by another philosopher. After an individual philosopher finishes eating, they need to put down both forks so that the forks become available to others. A philosopher can take the fork on their right or the one on their left as they become available, but cannot start eating before getting both forks.

Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite supply and an infinite demand are assumed.

The problem is how to design a discipline of behavior (a concurrent algorithm) such that no philosopher will starve; i.e., each can forever continue to alternate between eating and thinking, assuming that no philosopher can know when others may want to eat or think.

For more details on the problem, read [this Wikipedia article](https://en.wikipedia.org/wiki/Dining_philosophers_problem).

## Program Description

1.	Creates five child processes for philosophers, and five child processes for forks. The parent process does nothing but creates ten child processes. The requests for granting and releasing forks are done by each child process through the communication with the two corresponding fork processes. The philosophers change their states among "thinking," "waiting" (for forks), and "eating," until all philosophers fulfill their eating requirements (90 seconds total eating time).

2. 	Uses the socket to do IPC. The connection-oriented type of sockets are initiated for each connection between a philosopher process and its corresponding fork processes. The datagram type of sockets are initiated for each connection between the parent and child processes.

3. 	Avoids a possible deadlock. "Hold and Wait" is restricted to break all possible deadlocks; i.e., a philosopher gives up the fork (if he/she is currently holding one) if his/her request for another fork is rejected by the server.

4. The status of each philosopher is printed whenever there is a change in the status (see the sample output on next page). The printing isn't done in individual philosopher processes. A single process handles all the printing. The datagram type of sockets are initiated for each connection between the printing process and philosopher processes.

5. Properly handles socket closing and cleanup. Avoids memory leakage and over-usage of system's resources. Zombie processes are killed when application terminates.

6. The program honors correctness, generality, and efficiency.

## Requirements
Python 3

## Running the Program
```sh
$ python dining_philosopher.py
```

## Acknowledgement
I would like to thank [Dr. Lawrence J. Osborne](https://www.lamar.edu/arts-sciences/computer-science/people/faculty-members/lawrence_osborne.html) for assigning this project to me. It was because of his lectures and guidance that I was able to complete this assignment. I would also like to acknowledge my partner Shelby LeBlanc who collaborated with me on this project.
