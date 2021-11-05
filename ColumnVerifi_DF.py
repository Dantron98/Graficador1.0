def column_verification(file, eje, hat):
    while True:
        if eje in file.columns:
            break
        else:
            print('Column not found, please select another. Do you wanna see the file again? ')
            answer = input('y/n ')
            while True:
                if answer == 'y' or answer == 'n':
                    break
                else:
                    answer = input('y/n ')
            if answer == 'y':
                print(file)
            eje = input('What is the ' + hat + 'axe? ')

