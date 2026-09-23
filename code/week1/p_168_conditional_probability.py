"""
#168 Calculate Conditional Probability from Data
Суть: определить вероятность события А, при условии что событие Б уже произошло

"""

def conditional_probability(data, x, y):
    x_ct = 0
    x_n_y_ct = data.count((x, y))

    for tup in data:
      if tup[0] == x:
        x_ct += 1

    if x_ct == 0:
      return 0.0

    prob = x_n_y_ct / x_ct

    return prob