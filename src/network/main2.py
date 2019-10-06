import network.main as main
import network.symbols as symbols

input_neurons = 1024
output_neurons = 94

learning_rate = 0.5
weights = main.read_weights("C:/Users/PRECISION MX800/Desktop/OPTICAL-CHARACTER-RECOGNITION/src/network/vectors-15-50")
# weights = main.set_random_weights(input_neurons, output_neurons)

print("8=================================D~~")


def function(weights, filename):
    ff = open(str(filename), "r")
    counter = 0
    for xx in ff:
        input_vector = main.string_to_vector(xx)
        # output_vector2 = main.calculate_euclidean_distance(input_vector, weights)
        winner = counter
        # winner = main.choose_winning_neuron(output_vector2)
        main.update_weights(weights, winner, learning_rate, input_vector)
        counter += 1
        if counter >= 93:
            counter = 0

# rangee = 15
#
# weights = main.set_random_weights(input_neurons, output_neurons)
#
# for x in range(rangee):
#      function(weights, "C:/Users/PRECISION MX800/Desktop/vol 1/0001.txt")
#      print(x)
#
#
# nazwa = "vectors-" + str(rangee) + "-"+str(int(learning_rate*100))
# main.save_weights(weights, nazwa)


def function2(vector):
    list = []
    for xx in vector:
        # input_vector = main.string_to_vector(xx)
        output_vector2 = main.calculate_euclidean_distance(xx, weights)
        winner = main.choose_winning_neuron(output_vector2)
        list.append(symbols.select_symbol(winner))
    return list


#print(function2([3.4, 5.5]))
