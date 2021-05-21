Problem 2 may look a bit odd at first so let me explain.
We first build enough paths for phi_obv that any number 
0-127 is correctly classified as a power of 2 or not. 
We also add the constraint that k(x) results in either
x + ?? or x - ??. We then give Z3 the hint that ?? is 
less than 0 (I also tried giving the hint that ?? is 
greater than 0). We then check that for all x,y 
phi_obv == phi_smart. This would mean that they are 
equivalent programs. Note that I ignore the cases where
x >= 128 because this creates overflow problems. We can
see that Z3 returns that k(x) = 129 + x. Which is an odd
answer. But notice that 129 in binary is 10000001. This 
is simply -1 when encoded in two's complement. This means
that Z3 is correctly telling us that k(x) = x - 1.
