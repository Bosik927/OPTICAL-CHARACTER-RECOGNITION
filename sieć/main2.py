import main
import time

input_neurons = 1024
output_neurons = 94

learning_rate = 0.5
weights = main.read_weights()
# weights = main.set_random_weights(input_neurons, output_neurons)

#
# output_vector = main.calculate_euclidean_distance(main.set_random_vector(input_neurons), weights)
# print(weights)
# print(output_vector)
# winner = main.choose_winning_neuron(output_vector)
# print(winner)
# main.update_weights(weights, winner, learning_rate, main.set_random_vector(input_neurons))
# print(weights)
print("8=================================D~~")


def function(weights):
    ff = open("vectors.txt", "r")
    counter = 0
    for xx in ff:
        input_vector = main.string_to_vector(xx)
        output_vector2 = main.calculate_euclidean_distance(input_vector, weights)
        #winner = counter
        winner = main.choose_winning_neuron(output_vector2)
        main.update_weights(weights, winner, learning_rate, input_vector)
        if counter >= 93:
            counter = 0
        else:
            counter += 1
        print(winner)

start = time.time()
for x in range(100):
    function(weights)
    print(x+1)
end = time.time()
print(end - start)
main.save_weights(weights)

f = open("a.txt", "w")
for x in weights:
    f.write(str(x) + "\n")
f.close()
