def main():
    input = read_data()
    print("Solution to task1: ", task1(input))
    print("Solution to task2: ", task2(input))


def task2(input):
    most_common_variants = input
    n_bits = len(input[0][1])
    for bit_position in range(n_bits):
        if len(most_common_variants) <= 1:
            break
        zero_numbers = []
        one_numbers = []
        for number in most_common_variants:
            nth_bit = number[0] >> (n_bits-bit_position-1) & 1
            if nth_bit:
                one_numbers.append(number)
            else:
                zero_numbers.append(number)
        if len(one_numbers) >= len(zero_numbers):
             most_common_variants = one_numbers
        else: 
            most_common_variants = zero_numbers
    
    least_common_variants = input
    for bit_position in range(n_bits):
        if len(least_common_variants) <= 1:
            break
        zero_numbers = []
        one_numbers = []
        for number in least_common_variants:
            nth_bit = number[0] >> (n_bits-bit_position-1) & 1
            if nth_bit:
                one_numbers.append(number)
            else:
                zero_numbers.append(number)
        if len(one_numbers) < len(zero_numbers):
             least_common_variants = one_numbers
        else: 
            least_common_variants = zero_numbers
    return most_common_variants[0][0] * least_common_variants[0][0]

def task1(input):
    n_bits = len(input[0][1])
    bit_counts = [0] * n_bits
    for number in input:
        for bit in range(n_bits):
            nth_bit = number[0] >> bit & 1
            bit_counts[n_bits-bit-1] += nth_bit

    gamma = [str(int(x > len(input)/2)) for x in bit_counts]
    gamma = int("".join(gamma),2)

    epsilon = [str(int(x <= len(input)/2)) for x in bit_counts]
    epsilon = int("".join(epsilon),2)
    
    return gamma * epsilon

    
def read_data():
    with open('input.txt') as file:
        input = file.read().splitlines()

    input = [[int(line, 2), line] for line in input]
    
    return input
    
if __name__ == "__main__":
    main()