You are to write a program that supports the following operations on order-statistic trees. Anorder-statistic treeis a red-black tree withsizeinformation stored in
each node. We maintain a dynamic set of integers in an order-statistic tree. Assume that integers are in the range of [1..9999] and initially treeTis empty.  

OS-Insert(T, x) returns x if integer x is not already in order-statistic treeT (i.e., x is inserted); 0 otherwise.  
OS-Delete(T, x) returnsxif integerxis inT (i.e.,xis deleted); 0 otherwise.  
OS-Select(T, i) returns the i-th smallest integer in T if the number of integers in T is ≥ i; 0 otherwise.  
OS-Rank(T, x) returns the rank of xamong the integers in T if xis in T; 0 otherwise.  

An input file contains a sequence of operations. In the input file OS-Insert(T,17) is denoted by I 17, OS-Delete(T,8) by D 8, OS-Select(T,5) by S 5, and OS-Rank(T,9) by R 9. Put a space between two operations.

Your program should proceed as follows.  
(1) Read an input sequence and print it.  
(2) Run your program on the input sequence. Print the output sequence.  
(3) Check the correctness of your program by a checker program. Print the result of checking. A checker program gets the input and output sequences as its input and checks whether the output sequence is correct or not. Write a checker program by using an arrayA[1..9999].  

◦ Explain how your checker program works in your report.  
◦ Hand in your report, programs, and an example running (with two input sequences).  
◦ Write down the environment you run your program and how to run your program  in your report. 
◦ Write comments appropriately in your program.  
