# -*- coding: utf-8 -*-
"""
Rabbits and Recurrence Relations

problem

A sequence is an ordered collection of objects (usually numbers), which are
allowed to repeat. Sequences can be finite or infinite. Two examples are the
finite sequence (pi,−sqrt(2),0,pi) and the infinite sequence of odd numbers
(1,3,5,7,9,...). We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect
to the values of previous terms. In the case of Fibonacci's rabbits from the
introduction, any given month will contain the rabbits that were alive the
previous month, plus any new offspring. A key observation is that the number of
offspring in any month is equal to the  number of rabbits that were alive two
months prior. As a result, if Fn represents the number  of rabbit pairs alive
after the n-th month, then we obtain the Fibonacci sequence having terms  Fn
that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to
initiate the sequence).  Although the sequence bears Fibonacci's name, it was
known to Indian mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we
can simply use the recurrence relation to generate terms for progressively
larger values of n. This problem introduces us to the computational technique of
dynamic programming, which successively builds up solutions by using the answers
to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months if
we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample Dataset:
5 3 

Sample Output:
19 
"""


import sys
# Define a main() function that prints a little greeting.
def main():
 [n,k]= (open(sys.argv[1]).readline().strip().split(' '))
 Time=int(n)
 Offspring=int(k)
 Immature_Num=1
 Mature_Num=0 
 for gen in range(Time-1):
 	New_Offsring=Mature_Num*Offspring
 	Mature_Num+=Immature_Num
 	Immature_Num=New_Offsring
 with open('Ex8_Output.txt', 'a') as f:
	f.write('Time (n): '+ str(Time) +'\n')
	f.write('Offspring Rate (k): '+k +'\n')
	f.write('Mature Rabbits: '+str(Mature_Num) +'\n')
	f.write('New Born Rabbits: '+str(Immature_Num) +'\n')
	f.write('Total Rabbits: '+str(Mature_Num+Immature_Num) +'\n')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
