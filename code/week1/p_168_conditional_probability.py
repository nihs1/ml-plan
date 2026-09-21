"""
#168 Calculate Conditional Probability from Data
Суть: определить вероятность события А, при условии что событие Б уже произошло

"""

def conditional_probability(data, x, y):
    x_ct = 0
    x_n_y_ct = 0

    for i in range(len(data)):
      if x in data[i] and y in data[i]:
        x_n_y_ct += 1
      for el in data[i]:
        if x == el:
          x_ct += 1

    if x_ct == 0:
      return 0.0

    prob = x_n_y_ct / x_ct
    
    return prob