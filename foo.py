#Changing the different labels...
if Task == 'Control':
    #random_indices = [0,1,2].shufffle
    possible_labels=['sky', 'earth', 'air']
    possible_shapes.shuffle
    Label1_type = possible_shapes[0]
    Label2_type = possible_shapes[1]
    Label3_type = possible_shapes[2]
    #Label1_type = 'sky'
    #Label2_type = 'earth'
    #Label3_type = 'air'
    possible_shapes = ['Triangle', 'Square', 'Circle']
    possible_shapes.shuffle
    Shape1_type = possible_shapes[0]
    Shape2_type = possible_shapes[1]
    Shape3_type = possible_shapes[2]
    #Shape1_type = 'Triangle'
    #Shape2_type = 'Square'
    #Shape3_type = 'Circle'
elif Task == 'Reward':
    Label1_type = 'HighReward'
    Label2_type = 'MediumReward'
    Label3_type = 'LowReward'
    Shape1_type = 'Pentagon'
    Shape2_type = 'Diamond'
    Shape3_type = 'Oval'
elif Task == 'Valence':
    Label1_type = 'Happy'
    Label2_type = 'Neutral'
    Label3_type = 'Sad'
    Shape1_type = 'Hexagon'
    Shape2_type = 'Rectangle'
    Shape3_type = 'Star'
