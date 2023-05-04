final_repeat = True           # repeats the whole program if chosen
while final_repeat == True:
    
    repeat = True            # repeats the calculator section if chosen
    while repeat == True:

        while True:   # takes the users 1st number. Loops until input is valid
            try:
                num1 = int(input('Enter your first number: '))
                break
            except:
                print('That is not a valid number!')
            

        choice = False  # takes users calculation choice. Loops until input is valid
        while choice == False:
            calculation = input('Enter either +, -, /, *: ')
            if calculation == '+' or calculation == '-' or calculation == '/' or calculation == '*':
                choice = True
            else:
                print('That is not a valid entry!')
            

        while True:  # takes users second number. Loops until input is valid
            try:
                num2 = int(input('Enter your second number: '))
                break
            except:
                print('That is not a valid number!')
            

        if calculation == '+':  # calculation for plus 
            result = num1+num2
            print(f'{num1} + {num2} = {result}')
            with open('storage.txt', 'a') as f:  # opens and copies the calculation to .txt file
                print(f'{num1} + {num2} = {result}', file=f)
        
        elif calculation == '-':  # calculation for minus
            result = num1-num2
            print(f'{num1} - {num2} = {result}')
            with open('storage.txt', 'a') as f:
                print(f'{num1} - {num2} = {result}', file=f)
        
        elif calculation == '/':  # calculation for division
            try:
                result = num1/num2
                print(f'{num1} / {num2} = {result}')
                with open('storage.txt', 'a') as f:
                    print(f'{num1} / {num2} = {result}', file=f)
            except ZeroDivisionError:
                print('Sorry, but you cant divide by 0')  # cant divide by 0. Prompts to start again
        
        elif calculation == '*':  # calculation for mulitply
            result = num1*num2
            print(f'{num1} * {num2} = {result}')
            with open('storage.txt', 'a') as f:
                print(f'{num1} * {num2} = {result}', file=f)


        valid_answer = False  # asks if user wants to do another sum
        while valid_answer == False:
            repeat_question = input('Would you like to do another sum? y/n: ').lower()
            if repeat_question == 'y':  # this choice loops back to line 4
                repeat = True
                valid_answer = True
            elif repeat_question == 'n':  # this choice continues to next section
                repeat = False
                valid_answer = True
            else:
                print('That is not a valid input!')
                
                
    valid_answer2 = False  # asks if user wants to import their previous sums
    while valid_answer2 == False:
        import_question = input('Would you like to import your previous calculations from a stored file? y/n: ').lower()
        if import_question == 'y':  # this choice asks user for the file they want
            valid_answer2 = True
            file = None
            while file == None:
                try:
                    file_input = input('Please type the name of the file you want to open: ')
                    file = open(file_input, 'r')  # opens the file the user inputs
                    read = file.readlines()  # returns the file contents as a list
                    for i in read:  # iterates through the list, printing 1 line at a time
                        print(i)
                except FileNotFoundError as error:  # loops if file not found
                    print('Sorry but I cant find that file. Please try again.')
                    print(error)
                finally:  # closes the file. This always runs if file open or not
                    if file is not None:
                        file.close()
        elif import_question == 'n':  # this choice continues to next section
            valid_answer2 = True
            print('Ok!')
        else:
            print('That is not a valid input!')
            

    valid_answer3 = False  # asks the user if they wish to start again
    while valid_answer3 == False:
        start_again = input('Would you like to use the program again? y/n: ').lower()
        if start_again == 'y':
            valid_answer3 = True
            repeat = True
            final_repeat = True  # loops back to line 1. Whole program runs again
        elif start_again == 'n':  # ends the whole program
            valid_answer3 = True
            final_repeat = False
            print('Ok. Have a nice day!')
        else:
            print('That is not a valid input!')
            
            

# The txt file that the sums are stored to is called storage.txt