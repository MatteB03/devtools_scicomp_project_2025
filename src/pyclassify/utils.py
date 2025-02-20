def distance(point1,point2):
    square_distance=0
    for i in range(len(point1)):
        linear_distance=point1[i]-point2[i]
        square_distance=square_distance+(linear_distance*linear_distance)
    return square_distance**0.5

def majority_vote(neighbors):
    label_dict=dict()
    for label in neighbors:
        if label not in label_dict.keys():
            label_dict[label]=1
        else:
            label_dict[label]=label_dict[label]+1
    keys=list(label_dict.keys())
    values=list(label_dict.values())
    return keys[values.index(max(values))]

def read_config(file):
   filepath = os.path.abspath(f'{file}.yaml')
   with open(filepath, 'r') as stream:
      kwargs = yaml.safe_load(stream)
   return kwargs
