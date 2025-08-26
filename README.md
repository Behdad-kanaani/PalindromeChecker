# PalindromeChecker

A simple Python script to check if a string can be rearranged into a palindrome.  
A string can form a palindrome if it has at most one character with an odd count.

---

## Features

- No external libraries required
- Simple and efficient algorithm
- Includes demo test cases
- Perfect for learning basic algorithms and string manipulation

---

## How It Works

1. Count the frequency of each character in the string.
2. Count how many characters have an odd frequency.
3. A string can be rearranged into a palindrome if **at most one character** has an odd count.

**Example:**

- `"aabbc"` → True  (only `'c'` has odd count)  
- `"aabbcd"` → False (`'c'` and `'d'` have odd counts)

---

## Usage

Clone the repository and run the script:

```bash
python palindrome_checker.py
````

You will see output for some demo test cases:

```
Can 'aabbc' be rearranged into a palindrome? True
Can 'aabbcd' be rearranged into a palindrome? False
Can 'racecar' be rearranged into a palindrome? True
Can 'hello' be rearranged into a palindrome? False
Can '' be rearranged into a palindrome? True
```

---

## Contributing

Feel free to fork this repository and submit pull requests.
You can add more test cases or extend the script to handle phrases, ignore spaces, or work with Unicode characters.

---

## Author

Behdad Kanani
[GitHub: Behdad-kanaani](https://github.com/Behdad-kanaani)
