

def identity(nums):
    """Identity:
    Given a list of numbers, write a list comprehension that produces a copy of the list.
        >>> identity([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
        >>> identity([])
        []
    """
    tab_copied = [x for x in nums]
    return tab_copied


def doubled(nums):
    """Doubled:
    Given a list of numbers, write a list comprehension that produces a list of each number doubled.
        >>> doubled([1, 2, 3, 4, 5])
        [2, 4, 6, 8, 10]
        >>> doubled([-2, 2, -10, 10])
        [-4, 4, -20, 20]
    """
    copied = [x * 2 for x in nums]
    return copied


def squared(nums):
    """Squared:
    Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
        >>> squared([1, 2, 3, 4, 5])
        [1, 4, 9, 16, 25]
        >>> squared([-2, 2, -10, 10])
        [4, 4, 100, 100]
    """
    sqrt_numbers = [x ** 2 for x in nums]
    return sqrt_numbers


def evens(nums):
    """Evens:
    Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
        >>> evens([1, 2, 3, 4, 5])
        [2, 4]
        >>> evens([1, 3, 5])
        []
        >>> evens([-2, -4, -7])
        [-2, -4]
    """
    even = [x for x in nums if x % 2 == 0 or float(x % 2) == 0]
    return even


def odds(nums):
    """Odds:
    Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
        >>> odds([1, 2, 3, 4, 5])
        [1, 3, 5]
        >>> odds([2, 4, 6])
        []
        >>> odds([-2, -4, -7])
        [-7]
    """
    odd = [x for x in nums if x % 2 != 0 or float(x % 2) != 0]
    return odd


def positives(nums):
    """Positives:
    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
        >>> positives([-2, -1, 0, 1, 2])
        [1, 2]
        >>> positives([-2, -8, 7, 3, -0.34, 0.55])
        [7, 3, 0.55]
        >>> positives([])
        []
    """
    positive_nums = [x for x in nums if x > 0]
    return positive_nums


def selective_stringify_nums(nums):
    """Selectively stringify nums:
    Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
        >>> selective_stringify_nums([25, 91, 22, -7, -20])
        ['25', '-20']
        >>> selective_stringify_nums(["string", 0.78, 55, 10, -20, 10.0])
        ['55', '10', '-20', '10.0']
    """
    separator = ', '
    numbers = [str(x) for x in list(filter(lambda x: x % 5 == 0, filter(lambda x: x != str(x), nums)))]
    return numbers

def words_not_the(sentence):
    """Words not 'the'
    Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
        >>> words_not_the('the quick brown fox jumps over the lazy dog')
        [5, 5, 3, 5, 4, 4, 3]
    """
    lengths = [len(x) for x in sentence.split() if x !='the']
    return lengths

def vowels(word):
    """Vowels:
    Given a string representing a word, write a list comprehension that produces a list of all the vowels in that word.
        >>> vowels('mathematics')
        ['a', 'e', 'a', 'i']
    """
    vowels = ["a","e","i","o","u","y"]
    checked = [x for x in word if x in vowels]
    return checked

# STOP HERE! You solved everything!
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n*** ALL TESTS PASSED!\n')
