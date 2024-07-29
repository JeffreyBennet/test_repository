def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.

    Args:
        nums (List[int]): List of integers.
        target (int): The target sum for which we need to find two numbers in the list.

    Returns:
        List[int]: Indices of the two numbers such that they add up to target.
    """
    num_to_index = {}

    for i, num in enumerate(nums):
        difference = target - num
        if difference in num_to_index:
            return [num_to_index[difference], i]
        num_to_index[num] = i

    return []