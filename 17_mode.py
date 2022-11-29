def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # count = 0
    # freq = None

    # for num in nums:
    #     if nums.count(num) > count:
    #         count = nums.count(num)
    #         freq = num

    # return freq

    counter = {}
    highest_frequency = 0
    most_frequent = nums[0]

    for num in nums:
        counter[num] = counter[num] + 1 if num in counter else 1

    for (num, frequency) in counter.items():
        if frequency > highest_frequency:
            most_frequent = num
            highest_frequency = frequency
    
    return most_frequent

    # refactor to O(n) - freq counter