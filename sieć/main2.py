import main
import time

input_neurons = 1024
output_neurons = 65

learning_rate = 0.1
output_vector = []
weights = main.set_random_weights(input_neurons, output_neurons)

#
# output_vector = main.calculate_euclidean_distance(main.set_random_vector(input_neurons), weights)
# print(weights)
# print(output_vector)
# winner = main.choose_winning_neuron(output_vector)
# print(winner)
# main.update_weights(weights, winner, learning_rate, main.set_random_vector(input_neurons))
# print(weights)
print(":=================================:")
start = time.time()

for x in range(1000):
    input_vector = main.set_random_vector(input_neurons)
    output_vector = main.calculate_euclidean_distance(input_vector, weights)
    winner = main.choose_winning_neuron(output_vector)
    main.update_weights(weights, winner, learning_rate, input_vector)
end = time.time()
print(end - start)