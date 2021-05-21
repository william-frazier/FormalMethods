For this file, I mostly just added a couple new
tests and changed a few things around to make
them easier for me to work with. Running the code
multiple times returns different answers (I am 
assuming this has to do with the length of the
bitvecs but I'm not sure). The two most common
answers it returns appear to be:
h1 = 8, h2 = 16, h3 = 4
h1 = 11, h2 = 8, h3 = 4

As far as I can tell, both work for integers of
this size. From this, I conclude that there are
in fact three numbers for which this program works
correctly. With the caveat that this trick may not 
work for numbers of any size but rather only the
integers up to a certain point.