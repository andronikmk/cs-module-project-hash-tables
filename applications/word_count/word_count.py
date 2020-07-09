def word_count(s):
    # Your code here
    freq = {}
    for piece in s.lower().split():
        word = ''.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = 1 + freq.get(word, 0)
    max_word = ''
    max_count = 0
    for (w,c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c
        return w, c



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))