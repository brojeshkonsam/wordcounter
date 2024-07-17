def count_words(text):
    """
    Counts the number of words in the given text.
    
    Parameters:
    text (str): The input text to count words from.
    
    Returns:
    int: The number of words in the text.
    """
   
    words = text.split()
   
    return len(words)

def main():
    """
    Main function to run the word count program.
    """
    while True:
     
        user_input = input("Please enter a sentence or paragraph: ").strip()
        
       
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        
        
        word_count = count_words(user_input)
        
       
        print(f"The number of words in the input is: {word_count}")
        
     
        again = input("Do you want to enter another text? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the word count program. Goodbye!")
            break


if __name__ == "__main__":
    main()
