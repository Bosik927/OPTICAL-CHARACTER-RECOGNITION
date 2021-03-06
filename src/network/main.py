import random
import pickle


def set_random_weights(input_neurons, output_neurons):
    weights = []
    for x in range(output_neurons):
        pom = []
        for y in range(input_neurons):
            pom.insert(y, random.uniform(0, 1))
        weights.insert(x, pom)
    return weights


def save_weights(weights, filename):
    file = open(str(filename), "wb")
    pickle.dump(weights, file)
    file.close()


def read_weights(filename):
    file = open(filename, "rb")
    data = pickle.load(file)
    file.close()
    return data


def calculate_euclidean_distance(input_vector, weights):
    pom = []
    for x in range(len(weights)):
        e = 0
        for y in range(len(input_vector)):
            d = (weights[x][y] - input_vector[y])
            e = e + d * d
        pom.append(e)
    return pom


def choose_winning_neuron(output_vector):
    pom = output_vector[0]
    for x in range(len(output_vector)):
        if output_vector[x] < pom:
            pom = output_vector[x]
    return output_vector.index(pom)


def update_weights(weights, winner, learnin_rate, input_neurons):
    for x in range(len(weights[winner])):
        weights[winner][x] = weights[winner][x] + learnin_rate * (input_neurons[x] - weights[winner][x])
   

def set_random_vector(n):
    pom = []
    for x in range(n):
        pom.insert(x, random.randint(0, 1))
    return pom


def string_to_vector(string):
    # string = string.replace('[', '')
    # string = string.replace(']', '')
    # vector = string.split(', ')
    pom = string.strip('\n')
    vector1 = []
    for x in pom:
        vector1.append(int(x))
    return vector1
