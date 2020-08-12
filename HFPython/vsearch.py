def search4vowels(word:str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for letter in found:
        print(letter)
    
