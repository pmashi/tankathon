import random as rand

probabilities = [
    [14, 14, 14, 12.5, 10.5, 9, 7.5, 6, 4.5, 3, 2, 1.5, 1, 0.5], 
    [13.42, 13.42, 13.42, 12.23, 10.54, 9.20, 7.80, 6.34, 4.83, 3.27, 2.20, 1.66, 1.11, 0.56],
    [12.75, 12.75, 12.75, 11.89, 10.56, 9.41, 8.14, 6.74, 5.23, 3.60, 2.45, 1.86, 1.25, 0.63],
    [11.97, 11.97, 11.97, 11.46, 10.53, 9.62, 8.52, 7.22, 5.71, 4.01, 2.76, 2.10, 1.43, 0.72],
    [47.86, 27.84, 14.84, 7.24, 2.22], 
    [20.02, 26.00, 25.74, 19.61, 8.62], 
    [7.02, 16.74, 26.74, 29.77, 19.72], 
    [2.19, 8.68, 20.55, 34.11, 34.47], 
    [0.62, 3.68, 12.88, 32.10, 50.72], 
    [0.15, 1.30, 6.75, 25.90, 65.90], 
    [0.03, 0.38, 3.01, 18.99, 77.59],
    [0.01, 0.09, 1.20, 12.60, 86.10], 
    [0.01, 0.02, 0.40, 6.70, 92.88], 
    [0.01, 0.01, 0.07, 2.34, 97.57] 
]

def list_sum(list): 
    sum = 0
    for i in list:
        sum+=i
    return sum

def print_2d_array(arr): 
    for i in arr: 
        print(i)

prob_counter = []

for i in range(len(probabilities)): 
    prob_counter.append([])
    for j in range(len(probabilities[i])):
        try:
            prob_counter[i].append(probabilities[i] + prob_counter[i][j-1])
        except: 
            prob_counter[i].append(probabilities[i])

print_2d_array(prob_counter)

def getRollSelection(probs): 
    selection = rand.randint(1, 1400)
    print(selection)

    return selection_index

# print(probabilities)

for arr in probabilities: 
    sum = 0
    for i in arr: 
        sum += i
    # print(str(sum) + str(round(sum)))

for i in range(len(probabilities)): 
    for j in range(len(probabilities[i])): 
        probabilities[i][j] *= 100

for arr in probabilities: 
    sum = 0
    for i in arr: 
        sum += i
    # print(str(sum) + "  " + str(round(sum, -4)))
