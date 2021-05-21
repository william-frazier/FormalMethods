############### BEGIN zune_flowchart.py
## Assaf Kfoury
## 6 July 2019

## This is the encoding of the flowchart of the Zune program or, more precisely,
## the Zune program-scheme as a list of triples where each triple has the form
##               (address1, token, address2)
## where "token" is a "test" or an "instruction".
##
## Note carefully the form of an instruction VAR := TERM, where VAR is in 
## {'x1', 'x2', 'x3'}, TERM is built from {f, g, h, c1, c2, c3, x1, x2, x3},
## and there is exactly one blank space between VAR and := and one blank 
## space between := and TERM. In particular, we can retrieve VAR by writing
## "token[0:2]" and retrieve TERM by writing "token[6:]".
##
## Note also that every instruction is of the form VAR := TERM except for 
## one, which is 'skip'.

# ENCODING of zune flowchart (using INFIX notation)
zune_fc = [ ('1', 'x2 := c1', '2'),
            ('2', 'r(x1,c2)', '3'),
            ('2', 'not r(x1,c2)', '10'),
            ('3', 'p(x2)', '4'),
            ('3', 'not p(x2)', '8'),
            ('4', 'r(x1,c3)', '5'),
            ('4', 'not r(x1,c3)', '7'),
            ('5', 'x1 := g(x1,c3)', '6'),
            ('6', 'x2 := f(x2)', '2'),
            ('7', 'skip', '2'),
            ('8', 'x1 := g(x1,c2)', '9'),
            ('9', 'x2 := f(x2)', '2')
            ]

# ENCODING of zune flowchart (using PREFIX notation)
zune_fc_S = [ ('1', 'x2 := c1', '2'),
            ('2', '(r x1 c2)', '3'),
            ('2', '(not (r x1 c2))', '10'),
            ('3', '(p x2)', '4'),
            ('3', '(not (p x2))', '8'),
            ('4', '(r x1 c3)', '5'),
            ('4', '(not (r x1 c3))', '7'),
            ('5', 'x1 := (g x1 c3)', '6'),
            ('6', 'x2 := (f x2)', '2'),
            ('7', 'skip', '2'),
            ('8', 'x1 := (g x1 c2)', '9'),
            ('9', 'x2 := (f x2)', '2')
            ]

###################### END zune_flowchart.py
