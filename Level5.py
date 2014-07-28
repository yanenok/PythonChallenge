import pickle

with open('Level5-source.txt', 'rb') as f:
    data = pickle.load(f)

    for j in data:
        print "".join([i[0] * i[1] for i in j])