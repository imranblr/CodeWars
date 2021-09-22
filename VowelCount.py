def get_count(input_str):
    num_vowels = 0
    vowels=['a', 'e', 'i', 'o', 'u']
    mylist=list(input_str)
    for x in mylist:
        if x.lower() in vowels: num_vowels+=1
    return num_vowels