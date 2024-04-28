from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """Determines if a number is even and returns a list of even integers.
    
    Args:
        int_list: A list of integers.
        
    Returns:
        A list of even integers.
    """
    # TODO : Implement even_list
    pass

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    return sum(num ** 2 for num in even_int_list)

#Main Function
def main():
    # Example list
    int list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

# Boilerplate code
if _name_ == "_main_":
    main()
