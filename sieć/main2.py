import main
import time

input_neurons = 1024
output_neurons = 65

learning_rate = 0.5
weights = main.read_weights()


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
    f = open("vectors.txt", "r")
    for x in f:
        input_vector = main.string_to_vector(x)
        output_vector2 = main.calculate_euclidean_distance(input_vector, weights)
        winner = main.choose_winning_neuron(output_vector2)
        main.update_weights(weights, winner, learning_rate, input_vector)
        print(winner)


start = time.time()
for x in range(10):
    function(weights)
end = time.time()
print(end - start)
main.save_weights(weights)
f = open("a.txt", "w")
for x in weights:
    f.write(str(x) + "\n")
f.close()
