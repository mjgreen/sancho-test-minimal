import random
mytasks = ["control", "reward", "valence"]
random.shuffle(mytasks)

if mytasks[0] == "control":

    possible_labels=['air', 'earth', 'sky']
    random.shuffle(possible_labels)
    Label1_type = possible_labels[0]
    Label2_type = possible_labels[1]
    Label3_type = possible_labels[2]

    indices=[0,1,2]
    random.shuffle(indices)
    #[1,0,2]
    possible_file_names =  ['Triangle.bmp', 'Square.bmp', 'Circle.bmp']
    possible_shape_names = ['Triangle',     'Square',     'Circle']

    Shape1_shape_name = possible_shape_names[indices[0]] # possible_shape_names[1]  label='Square'
    Shape1_file_name = possible_file_names[indices[0]] # possible_file_names[1] filename is 'Square.bmp'

    Shape2_shape_name = possible_shape_names[indices[1]]
    Shape2_file_name = possible_file_names[indices[1]]

    Shape1_shape_name = possible_shape_names[indices[2]]
    Shape1_file_name = possible_file_names[indices[2]]

elif mytasks[0] == "reward":
    # then 
     possible_labels=['high', 'medium', 'none']
     random.shuffle(possible_labels)
     Label1_type = possible_labels[0]
     Label2_type = possible_labels[1]
     Label3_type = possible_labels[2]

     indices=[0,1,2]
     random.shuffle(indices)
     # [2,0,1]
     possible_file_names =  ['Pentagon.bmp', 'Diamond.bmp', 'Oval.bmp']
     possible_shape_names = ['Pentagon',     'Diamond',     'Oval']

     Shape1_shape_name = possible_shape_names[indices[0]] # possible_shape_names[1]  label='Oval'
     Shape1_file_name = possible_file_names[indices[0]] # possible_file_names[1] filename is 'Oval.bmp'

     Shape2_shape_name = possible_shape_names[indices[1]]
     Shape2_file_name = possible_file_names[indices[1]]

     Shape1_shape_name = possible_shape_names[indices[2]]
     Shape1_file_name = possible_file_names[indices[2]]

elif mytasks[0] == "valence":
    # then 
     possible_labels=['happy', 'neutral', 'sad']
     random.shuffle(possible_labels)
     Label1_type = possible_labels[0]
     Label2_type = possible_labels[1]
     Label3_type = possible_labels[2]

     indices=[0,1,2]
     random.shuffle(indices)
     # [0,2,1]
     possible_file_names =  ['Hexagon.bmp', 'Rectangle.bmp', 'Star.bmp']
     possible_shape_names = ['Hexagon',     'Rectangle',     'Star']

     Shape1_shape_name = possible_shape_names[indices[0]] # possible_shape_names[1]  label='Hexagon'
     Shape1_file_name = possible_file_names[indices[0]] # possible_file_names[1] filename is 'Hexagon.bmp'

     Shape2_shape_name = possible_shape_names[indices[1]]
     Shape2_file_name = possible_file_names[indices[1]]

     Shape1_shape_name = possible_shape_names[indices[2]]
     Shape1_file_name = possible_file_names[indices[2]]
