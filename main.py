################################################################################
#                                                                              #
#                            WRITTEN BY BEHDAD KANANI                          #
#                                                                              #
# Description:                                                                 #
#   Checks if a string can be rearranged into a palindrome without using       #
#   any external libraries.                                                    #
#                                                                              #
#                          Github: Behdad-kanaani/PalindromeChecker            #
#                                                                              #
################################################################################

def can_form_palindrome(s: str) -> bool:
    """
    Determines if a palindrome can be formed from the characters of the input string.

    Args:
        s (str): The input string.

    Returns:
        bool: True if a palindrome can be formed, False otherwise.

    Example:
        'aabbc' -> True  (only 'c' has odd count)
        'aabbcd' -> False ('c' and 'd' have odd counts)
    """
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1

    return odd_count <= 1


if __name__ == "__main__":
    # Demo test cases
    test_cases = [
        "aabbc",
        "aabbcd",
        "racecar",
        "hello",
        ""
    ]

    for case in test_cases:
        result = can_form_palindrome(case)
        print(f"Can '{case}' be rearranged into a palindrome? {result}")
