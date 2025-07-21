"""
Course    : CMPSC 131, Summer 2025
File      : PS5.py

Name              : Fatimah Abdallah
GitHub User       : Fatimah11
Collaboration Statement: This submission is my own work completed using only the resources provided in class.
"""

# Problem 1.1 - invert_dict
def invert_dict(d):
    inverted = {}
    for k in d:
        v = d[k]
        if v in inverted:
            inverted[v].append(k)
        else:
            inverted[v] = [k]
    return inverted

# Problem 1.2 - char_frequency
def char_frequency(s):
    result = {}
    for char in s:
        char = char.lower()
        if 'a' <= char <= 'z':
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result

# Problem 1.3 - find_missing_pangram_chars
def find_missing_pangram_chars(s):
    alphabet = {}
    for ch in s:
        ch = ch.lower()
        if 'a' <= ch <= 'z':
            alphabet[ch] = 1
    missing = []
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in alphabet:
            missing.append(ch)
    return missing

# Problem 1.4 - are_anagrams
def are_anagrams(s1, s2):
    def filter_alpha(text):
        clean = ""
        for ch in text:
            ch = ch.lower()
            if 'a' <= ch <= 'z':
                clean += ch
        return clean

    s1 = filter_alpha(s1)
    s2 = filter_alpha(s2)

    if len(s1) != len(s2):
        return False

    count1 = {}
    count2 = {}

    for ch in s1:
        count1[ch] = count1.get(ch, 0) + 1
    for ch in s2:
        count2[ch] = count2.get(ch, 0) + 1

    return count1 == count2

# Problem 1.5 - find_anagram_pairs
def find_anagram_pairs(lst):
    pairs = []
    n = len(lst)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if are_anagrams(lst[i], lst[j]):
                pairs.append((i, j))
            j += 1
        i += 1
    return pairs

# Problem 1.6 - is_steady
def is_steady(s):
    freq = {}
    for c in s:
        c = c.lower()
        if 'a' <= c <= 'z':
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

    all_counts = list(freq.values())
    if len(all_counts) == 0:
        return False

    for count in all_counts:
        if count != all_counts[0]:
            return False
    return True

# Problem 1.7 - nearly_equal
def nearly_equal(s1, s2):
    def letter_count(s):
        table = {}
        for c in s:
            c = c.lower()
            if 'a' <= c <= 'z':
                table[c] = table.get(c, 0) + 1
        return table

    d1 = letter_count(s1)
    d2 = letter_count(s2)

    checked = []
    for ch in d1:
        if ch not in checked:
            checked.append(ch)
    for ch in d2:
        if ch not in checked:
            checked.append(ch)

    for ch in checked:
        val1 = d1.get(ch, 0)
        val2 = d2.get(ch, 0)
        if abs(val1 - val2) > 2:
            return False
    return True

# Problem 1.8 - get_term
def get_term(code):
    c = str(code)
    if len(c) != 4:
        return False
    if c[0] != '2':
        return False

    sem = c[3]
    if sem == '1':
        season = "Spring"
    elif sem == '5':
        season = "Summer"
    elif sem == '8':
        season = "Fall"
    else:
        return False

    yr = "20" + c[1:3]
    return season + " " + yr

# Main function with test outputs
def main():
    print("Problem 1.1 - invert_dict:")
    print(invert_dict({'a': 1, 'b': 2, 'c': 1, 'd': 2, 3.75: 7}))
    print()

    print("Problem 1.2 - char_frequency:")
    print(char_frequency("~ABC abc!!!!"))
    print()

    print("Problem 1.3 - find_missing_pangram_chars:")
    print(find_missing_pangram_chars("The quick brown fox"))
    print()

    print("Problem 1.4 - are_anagrams:")
    print("Lis ten vs Silent! ->", are_anagrams("Lis ten", "Silent!"))
    print("Listen vs Google ->", are_anagrams("Listen", "Google"))
    print()

    print("Problem 1.5 - find_anagram_pairs:")
    print(find_anagram_pairs(["Lis Ten", "silent", "enli st", "inlet s", "google"]))
    print()

    print("Problem 1.6 - is_steady:")
    print("ARE era ->", is_steady("ARE era"))
    print("ARE eras ->", is_steady("ARE eras"))
    print()

    print("Problem 1.7 - nearly_equal:")
    print("sesame vs SundrivE ->", nearly_equal("sesame", "SundrivE"))
    print("sesame vs SundrivEYYYYY ->", nearly_equal("sesame", "SundrivEYYYYY"))
    print("sesame vs SenateSeatsSoonPSU ->", nearly_equal("sesame", "SenateSeatsSoonPSU"))
    print()

    print("Problem 1.8 - get_term:")
    print("2255 ->", get_term(2255))
    print("2186 ->", get_term(2186))
    print()

# Run main if this is the entry point
if __name__ == "__main__":
    main()
