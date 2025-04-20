def get_words(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    # Remove punctuation from each word
    clean_words = [word.strip(".,!?;:") for word in words]
    return clean_words

def count_unique_words(words):
    return len(set(words))

def find_longest_word(words):
    return max(words, key=len)

def count_specific_word(words, target):
    return words.count(target.lower())

def percentage_longer_than_average(words):
    average = sum(len(word) for word in words) / len(words)
    longer_words = [word for word in words if len(word) > average]
    return (len(longer_words) / len(words)) * 100

# Main part
text = "This is a simple example. This example is just a test!"

words = get_words(text)

print("Unique words:", count_unique_words(words))
print("Longest word:", find_longest_word(words))
print("Occurrences of 'example':", count_specific_word(words, "example"))
print("Percentage of words longer than average:", round(percentage_longer_than_average(words), 2), "%")
