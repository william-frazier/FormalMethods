
The code for both problems 1 and 2 can be run through
__main__.py. The code itself is in zune.py. From __main__
just use either run(fc, k, lbl1, lbl2) or run_full(fc, k).

Examples: run(zune_fc, 5, "3", "6"), run_full(zune_fc_S, 8)

For the purposes of full paths, I assume that label "1" is
the initial node and that the final node ends a triplet but 
does not start one such as ('2', '(not (r x1 c2))', '10') in
zune_fc_S with respect to label "10". I believe that my only 
other assumption is that each instruction in a path is written
(label1, instruction, label2).

My solution to problem 3 remains buggy and so I have not 
included the code for it.