
def count_words_in_file(input_file, output_file):
    try:
    
        with open(input_file, 'r') as file:
            content = file.read()
        
    
        words = content.split()
        word_count = len(words)

        # Open the output file in write mode and write the word count result
        with open(output_file, 'w') as result_file:
            result_file.write(f"Word count: {word_count}\n")

        print(f"Word count written to '{output_file}' successfully.")
    
    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = r'C:\Users\SHREYA\Desktop\python tasks\basic arithmetic operator\file handling\input_file.txt'
output_file = r'C:\Users\SHREYA\Desktop\python tasks\basic arithmetic operator\file handling\output_file.txt'

count_words_in_file(input_file, output_file)
