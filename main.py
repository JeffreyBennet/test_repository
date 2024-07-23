def sort_list_ascending(input_list):
    """
    Sorts a list in ascending order.

    :param input_list: List of elements to be sorted.
    :return: Sorted list in ascending order.
    """
    return sorted(input_list)

def sort_list_descending(input_list):
    """
    Sorts a list in descending order.

    :param input_list: List of elements to be sorted.
    :return: Sorted list in descending order.
    """
    return sorted(input_list, reverse=True)

if __name__ == "__main__":
    # Example list
    example_list = [34, 2, 23, 67, 100, 88, 5]

    # Sorting the list in ascending order
    sorted_list_ascending = sort_list_ascending(example_list)
    print("Sorted list in ascending order:", sorted_list_ascending)

    # Sorting the list in descending order
    sorted_list_descending = sort_list_descending(example_list)
    print("Sorted list in descending order:", sorted_list_descending)
