import main
import symbols

input_neurons = 1024
output_neurons = 94

learning_rate = 0.5
# weights = main.read_weights("C:/Users/mietek/PycharmProjects/ocr3/venv/petla_100_learning_rate_0.5")
weights = main.set_random_weights(input_neurons, output_neurons)

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

# for x in range(1):
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/1.txt")
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/2.txt")
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/3.txt")
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/4.txt")
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/5.txt")
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/6.txt")
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/7.txt")
#     function(weights, "C:/Users/mietek/PycharmProjects/ocr3/venv/8.txt")
#
# main.save_weights(weights, "vectors")


def function2(filename):
    weights = main.read_weights("C:/Users/mietek/PycharmProjects/ocr3/vectors")
    ff = open(str(filename), "r")
    list = []
    for xx in ff:
        input_vector = main.string_to_vector(xx)
        output_vector2 = main.calculate_euclidean_distance(input_vector, weights)
        winner = main.choose_winning_neuron(output_vector2)
        list.append(symbols.select_symbol(winner))
    return list


print(function2("C:/Users/mietek/PycharmProjects/ocr3/venv/1.txt"))