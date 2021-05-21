



from mpe import *


def run(cpts, obs):
    return MPE(cpts,obs)


big_example = [
['x_1', [[[[]],['x_1','0'],0.7],[[[]],['x_1','1'],0.3]]],
['x_2', [[[[]],['x_2','0'],0.8],[[[]],['x_2','1'],0.2]]],
['x_3', [[[[]],['x_3','0'],0.1],[[[]],['x_3','1'],0.9]]],
['x_4', [[[['x_1','0'],['x_2','0']],['x_4','0'],0.4],
         [[['x_1','0'],['x_2','0']],['x_4','1'],0.6],
         [[['x_1','0'],['x_2','1']],['x_4','0'],0.9],
         [[['x_1','0'],['x_2','1']],['x_4','1'],0.1],
         [[['x_1','1'],['x_2','0']],['x_4','0'],0.1],
         [[['x_1','1'],['x_2','0']],['x_4','1'],0.9],
         [[['x_1','1'],['x_2','1']],['x_4','0'],0.8],
         [[['x_1','1'],['x_2','1']],['x_4','1'],0.2]
         ]],
['x_5', [[[['x_2','0'],['x_3','0']],['x_5','0'],0.9],
         [[['x_2','0'],['x_3','0']],['x_5','1'],0.1],
         [[['x_2','0'],['x_3','1']],['x_5','0'],0.7],
         [[['x_2','0'],['x_3','1']],['x_5','1'],0.3],
         [[['x_2','1'],['x_3','0']],['x_5','0'],0.4],
         [[['x_2','1'],['x_3','0']],['x_5','1'],0.6],
         [[['x_2','1'],['x_3','1']],['x_5','0'],0.5],
         [[['x_2','1'],['x_3','1']],['x_5','1'],0.5]
         ]],
['x_6', [[[['x_5','0']],['x_6','0'],0.5],
         [[['x_5','0']],['x_6','1'],0.5],
         [[['x_5','1']],['x_6','0'],0.9],
         [[['x_5','1']],['x_6','1'],0.1]
         ]],
['x_7', [[[['x_4','0']],['x_7','0'],0.6],
         [[['x_4','0']],['x_7','1'],0.4],
         [[['x_4','1']],['x_7','0'],0.3],
         [[['x_4','1']],['x_7','1'],0.7]
         ]],
['x_8', [[[['x_4','0'],['x_5','0']],['x_8','0'],0.3],
         [[['x_4','0'],['x_5','0']],['x_8','1'],0.7],
         [[['x_4','0'],['x_5','1']],['x_8','0'],0.4],
         [[['x_4','0'],['x_5','1']],['x_8','1'],0.6],
         [[['x_4','1'],['x_5','0']],['x_8','0'],0.5],
         [[['x_4','1'],['x_5','0']],['x_8','1'],0.5],
         [[['x_4','1'],['x_5','1']],['x_8','0'],0.6],
         [[['x_4','1'],['x_5','1']],['x_8','1'],0.4]
         ]]
]

instance = [['x_1', [[[[]],['x_1','0'],0.9],[[[]],['x_1','1'],0.1]]], 
            ['x_2', [[[[]],['x_2','0'],0.7],[[[]],['x_2','1'],0.3]]], 
            ['x_3', [[[['x_1','0'],['x_2','0']],['x_3','0'],0.99],
                     [[['x_1','0'],['x_2','0']],['x_3','1'],0.01],
                     [[['x_1','0'],['x_2','1']],['x_3','0'],0.1],
                     [[['x_1','0'],['x_2','1']],['x_3','1'],0.9],
                     [[['x_1','1'],['x_2','0']],['x_3','0'],0.3],
                     [[['x_1','1'],['x_2','0']],['x_3','1'],0.7],
                     [[['x_1','1'],['x_2','1']],['x_3','0'],0.01],
                     [[['x_1','1'],['x_2','1']],['x_3','1'],0.99]
         ]], 
            ['x_4', [[[['x_3','0']],['x_4','0'],0.9],
                     [[['x_3','0']],['x_4','1'],0.1],
                     [[['x_3','1']],['x_4','0'],0.2],
                     [[['x_3','1']],['x_4','1'],0.8]
         ]]]