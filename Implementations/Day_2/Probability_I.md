# Probability and Compound Events

**Question 1:**
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

*Thought process:*
Determine total number of possible dice rolls: 36 <br />
Determine total number of possible dice rolls with value 9 or less: 30

**Answer: 30/36 -> 5/6**
<br />


**Question 2:**
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

*Thought process:*
Determine total number of possible dice rolls: 36 <br />
Determine total number of possible dice rolls with value 6 but also different (1-5,2-4,4-2,5-1: 4

**Answer: 4/36 -> 1/9**
<br />

**Question 3:**
There are 3 urns labeled X, Y, and Z.
<ul>
    <li>Urn X contains 4 red balls and 3 black balls.
    <li>Urn Y contains 5 red balls and 4 black balls.
    <li>Urn Z contains 4 red balls and 4 black balls.
</ul>
One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

*Thought process:*
Find probability of drawing one red or black ball from each urn:
<ul>
  <li>X: red -> 4/7, black -> 3/7
  <li>Y: red -> 5/9, black -> 4/9
  <li>Z: red -> 4/8, black -> 4/8
</ul>

Consider combination of 2 reds and 1 black from the three urns:
<ul>
  <li>1) X,Y -> 2 red, Z -> 1 black: 4/7 * 5/9 * 4/8 = 80/504
  <li>2) X,Z -> 2 red, Y -> 1 black: 4/7 * 4/8 * 4/9 = 64/504
  <li>3) Y,Z -> 2 red, X -> 1 black: 5/9 * 4/8 * 3/7 = 60/504
</ul>

Sum 1,2 and 3: 80/504 + 64/504 + 60/504 = 204/504

**Answer: 204/504 -> 17/42**
  
