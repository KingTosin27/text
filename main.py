# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open('story.txt') as f:
        contents = f.read()
        print(contents)
    
    return "Hello World"


def count_words(text):
    text = read_file_content("./story.txt")
     return {"as": 10, "would": 20}
numberofwords = countwords(".story.txt")
print(numberofwords)


   