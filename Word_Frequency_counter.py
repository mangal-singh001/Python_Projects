import string 
def words_frequency_counter(input_string):
    translator = str.maketrans('','' , string.punctuation)
    cleaned_string = input_string.translate(translator).lower()
    words = cleaned_string.split()
    
    dict = {}
    
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict
def main():
    
    input_string = input("Enter the text : ")
    dict = words_frequency_counter(input_string)
    print("Word frequencies")
    for word,frequency in dict.items():
        print(f"{word} : {frequency}")
        
if __name__ == "__main__":
    main()