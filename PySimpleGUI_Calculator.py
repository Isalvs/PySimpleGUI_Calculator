import PySimpleGUI as sg

'''

    Make a: Simple Calculator
    Input: any sort of numbers
    Output: the result of input mathematical sentence

'''


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 20', button_element_size=(6, 2))
    buttonSize = (6, 2)
    layout = [
        [sg.Text('', key='-TEXT-', font='Franklin 26', expand_x=True, justification='right',
                 right_click_menu=theme_menu)],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7, size=buttonSize), sg.Button(8, size=buttonSize), sg.Button(9, size=buttonSize),
         sg.Button('*', size=buttonSize)],
        [sg.Button(4, size=buttonSize), sg.Button(5, size=buttonSize), sg.Button(6, size=buttonSize),
         sg.Button('/', size=buttonSize)],
        [sg.Button(1, size=buttonSize), sg.Button(2, size=buttonSize), sg.Button(3, size=buttonSize),
         sg.Button('-', size=buttonSize)],
        [sg.Button(0, expand_x=True), sg.Button('.', size=buttonSize), sg.Button('+', size=buttonSize)]
    ]

    return sg.Window('Calculator', layout)


sg.theme('lightGrey1')

sg.set_options(font='Franklin 20', button_element_size=(6, 2))

button_size = (6, 2)

theme_menu = ['menu', ['LightGrey1', 'dark', 'darkGray1', 'random']]
window = create_window('dark')

current_Values = []
full_operation = []

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
        current_Values.append(event)
        num_to_string = ''.join(current_Values)
        window['-TEXT-'].update(num_to_string)
        print(event)

    if event in ['+', '-', '*', '/']:
        print(event)
        full_operation.append(''.join(current_Values))
        current_Values = []
        full_operation.append(event)
        window['-TEXT-'].update('')

    if event in 'Enter':
        full_operation.append(''.join(current_Values))
        # if you pass some string with number and operator to function eval, it will calculate the expression
        result = eval(' '.join(full_operation))
        window['-TEXT-'].update(result)
        full_operation = []
        current_Values = []
        full_operation.append(str(result))
        print(full_operation)

    if event in 'Clear':
        print(event)
        full_operation = []
        current_Values = []
        window['-TEXT-'].update(' ')

window.close()
