# Task 1: Function to get and validate number between 3 and 9
def get_valid_number():
    print("Enter a number between 3 and 9: ")
    num = int(input())
    
    # Using comparison operators and while loop
    while num < 3 or num > 9:
        print("Invalid input. Please enter a number between 3 and 9:")
        num = int(input())
    
    return num


# Task 2: Generating personal code using student ID and keyword
def generate_personal_code(student_id, keyword):
    # Using string indexing to get first and last letter
    first_letter = keyword[0]
    last_letter = keyword[-1]
    
    # Using string concatenation with + operator
    personal_code = first_letter.upper() + "-" + student_id + "-" + last_letter.upper()
    
    return personal_code


# Task 3: Count character frequency using dictionary
def count_character_frequency(full_name):
    # Convert to lowercase and remove spaces
    name_without_spaces = ""
    
    # Using for loop to remove spaces
    for char in full_name:
        if char != " ":  # Using != comparison operator
            name_without_spaces = name_without_spaces + char.lower()  # Using + operator
    
    # Create empty dictionary
    freq_dict = {}
    
    # Count frequency using dictionary
    for char in name_without_spaces:
        if char in freq_dict:  # Using 'in' operator
            freq_dict[char] = freq_dict[char] + 1  # Using + operator
        else:
            freq_dict[char] = 1
    
    return freq_dict


# Task 4: Find unique vowels and consonants using lists/sets
def find_unique_vowels_consonants(full_name):
    # Define vowels set
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert to lowercase and remove spaces
    clean_name = ""
    for char in full_name:
        if char != " ":
            clean_name = clean_name + char.lower()
    
    # Using sets for unique values
    unique_vowels = set()
    unique_consonants = set()
    
    # Check each character
    for char in clean_name:
        if char in vowels_set:  # Using 'in' membership operator
            unique_vowels.add(char)
        else:
            unique_consonants.add(char)
    
    # Convert sets to sorted lists
    vowels_list = sorted(unique_vowels)
    consonants_list = sorted(unique_consonants)
    
    return vowels_list, consonants_list


# Task 5: Check balanced brackets using stack (list as stack)
def check_balanced_brackets(bracket_expr):
    # Create a stack using list
    stack = []
    
    # Using for loop to check each character
    for char in bracket_expr:
        # If opening bracket, push to stack
        if char == '(' or char == '[' or char == '{':
            stack.append(char)  # Push operation
        
        # If closing bracket, check with stack
        elif char == ')' or char == ']' or char == '}':
            # If stack is empty, not balanced
            if len(stack) == 0:  # Using comparison operator
                return False
            
            # Pop from stack and check if matches
            top = stack.pop()  # Pop operation
            
            # Check if brackets match using logical operators
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False
    
    # After loop, stack should be empty for balanced brackets
    if len(stack) == 0:
        return True
    else:
        return False


# Task 6: Process keyword tasks using queue (list as FIFO)
def process_keyword_queue(keyword):
    # Create a queue using list
    queue = []
    
    # Add tasks to queue (enqueue)
    for char in keyword:
        task = "Analyze " + char  # Using string concatenation
        queue.append(task)  # Enqueue at the end
    
    print("Queue Processing:")
    
    # Process tasks in FIFO order (dequeue from front)
    while len(queue) > 0:  # Using > comparison operator
        current_task = queue.pop(0)  # Dequeue from front
        print("Processing:", current_task)


# Task 7: Number pattern using loops
def print_number_pattern(number):
    print("Number Pattern:")
    
    # Using nested loops
    for i in range(1, number + 1):  # Outer loop for rows
        for j in range(1, i + 1):    # Inner loop for columns
            print(j, end=" ")
        print()  # New line after each row


# Task 8: Recursive digit sum
def recursive_digit_sum(student_id):
    # Convert student ID to string to access digits
    id_string = str(student_id)
    
    # Base case: if only one digit, return that digit
    if len(id_string) == 1:  # Using comparison operator
        return int(id_string)
    
    # Recursive case: first digit + sum of remaining digits
    first_digit = int(id_string[0])
    remaining_digits = id_string[1:]
    
    # Using recursion here
    return first_digit + recursive_digit_sum(remaining_digits)


# Function to display all results
def display_summary(student_id, full_name, keyword, personal_code, freq_dict, vowels, consonants, is_balanced, digit_sum):
    print("\n" + "="*50)
    print("PERSONAL PATTERN TOOLKIT - SUMMARY")
    print("="*50)
    
    print("\nPersonal Code:", personal_code)
    
    print("\nCharacter Frequency:")
    # Using for loop to display dictionary
    for char in freq_dict:
        print("  " + char + ":", freq_dict[char])
    
    print("\nUnique Vowels:", end=" ")
    # Using for loop to display vowels
    for i in range(len(vowels)):
        if i == len(vowels) - 1:
            print(vowels[i])
        else:
            print(vowels[i], end=", ")
    
    print("Unique Consonants:", end=" ")
    for i in range(len(consonants)):
        if i == len(consonants) - 1:
            print(consonants[i])
        else:
            print(consonants[i], end=", ")
    
    print("\nBalanced Brackets:", end=" ")
    if is_balanced == True:
        print("Yes")
    else:
        print("No")
    
    print("\nRecursive Digit Sum of Student ID:", digit_sum)
    print("="*50)


# Main function
def main():
    print("="*50)
    print("Personal Pattern Toolkit")
    print("="*50)
    
    # Taking inputs from user
    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    keyword = input("Enter Keyword: ")
    
    # Get valid number using Task 1 function
    number = get_valid_number()
    
    bracket_expression = input("Enter bracket expression: ")
    
    # Task 2 - Generate personal code
    personal_code = generate_personal_code(student_id, keyword)
    
    # Task 3 - Count character frequency
    freq_dict = count_character_frequency(full_name)
    
    # Task 4 - Find unique vowels and consonants
    vowels, consonants = find_unique_vowels_consonants(full_name)
    
    # Task 5 - Check balanced brackets
    is_balanced = check_balanced_brackets(bracket_expression)
    
    # Task 6 - Process queue
    print()
    process_keyword_queue(keyword)
    
    # Task 7 - Print number pattern
    print()
    print_number_pattern(number)
    
    # Task 8 - Calculate recursive digit sum
    digit_sum = recursive_digit_sum(student_id)
    
    # Display all results
    display_summary(student_id, full_name, keyword, personal_code, freq_dict, vowels, consonants, is_balanced, digit_sum)


# Run the program
if __name__ == "__main__":
    main()