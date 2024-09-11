# Problem:
# - Input: An integer that represents the given number of available blocks
# - Output: An integer that represents the leftover blocks from structure
# - Requirements:
#   - Top layer is a single block
#   - A block in an upper layer must be supported by four blocks in lower layer
#   - A block in lower layer can support more than one block in an upper layer
#   - There may be no gaps between blocks
#   - The leftover blocks must be based upon the tallest possible valid structure
#   - The number of blocks in a layer is row^2

# Test Cases:
# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True

# Data Structures
# - Integers will be a needed data structure. 
# - COULD use nested list to represent each layer?? prob not tho

# Algorithm
# - 1. Find out the largest valid structure that can be made with blocks
#   - initialize valid_structure_blocks to 0
#   - initialize block_layer to 1
#   - while valid_structure_blocks <= given integer
#     - check if adding block_layer^2 will make valid blocks > given integer
#     - if not, add block_layer^2 to sum
#     - increment block_layer
# - 2. Subtract the block number of the structure from given int
# - 3. Return difference

def calculate_leftover_blocks(my_blocks):
    valid_structure_blocks = 0
    block_layer = 1
    while valid_structure_blocks <= my_blocks:
        if valid_structure_blocks + block_layer**2 <= my_blocks:
            valid_structure_blocks += block_layer**2
            block_layer += 1
        else:
            break
    difference = my_blocks - valid_structure_blocks
    return difference

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True