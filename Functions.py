

def write_to_file(file_name, string_to_write):
    """
    :param file_name: Name of the text file to write to.
    :param string_to_write: The string to write to the txt file.
    :return: None
    """
    f = open(file_name, "a")
    f.write(string_to_write + "\n")
    f.close()


def read_from_file(file_name):
    """
    :param file_name: Name of the text file in directory to read information from.
    :return: Lines from the document.
    """
    f = open(file_name)
    lines = f.readlines()
    return lines


def listen_on_move(x, y):
    """
    Given the position of the mouse this function will record the information in the correct format in a text file.
    :param x: X coordinate of the mouse position.
    :param y: Y coordinate of the mouse position.
    :return: None
    """
    write_to_file("loggedInfo", "MM(" + str(x) + ", " + str(y) + ")")





def listen_on_release(key):
    print("released")


def listen_on_click(x, y, button, pressed):
    """
    Given the position of the mouse click this function will record the information in the correct format in a txt file.
    :param x: X coordinate of the mouse click position.
    :param y: Y coordinate of the mouse click position.
    :param button: The button on the mouse that was touched.
    :param pressed: A bool that records whether the mouse was pressed or released.
    :return: None
    """
    if button == button.left:
        write_to_file("loggedInfo", "MCL(" + str(x) + ", " + str(y) + ")")

    if button == button.right:
        write_to_file("loggedInfo", "MCR(" + str(x) + ", " + str(y) + ")")


def listen_on_scroll(x, y, dx, dy):
    pass


def get_move_mouse_coordinates(stored_line):
    """
    When the input line starts with MM it indicates a recorded mouse move. This function decodes that line and returns
    the mouse position.
    :param stored_line: A line from the stored data in the loggedInfo txt file.
    :return: A list [x position, y position]
    """
    move_x_pos = ""
    move_y_pos = ""
    move_comma_pos = 0
    for i in range(len(stored_line) - 3):
        if stored_line[i + 3] == ",":
            move_comma_pos = i + 3
            break
        move_x_pos += (stored_line[i + 3])
    for j in range(len(stored_line) - move_comma_pos - 4):
        move_y_pos += stored_line[j + move_comma_pos + 2]

    return [move_x_pos, move_y_pos]


def get_click_mouse_coordinates_and_button(stored_line):
    """
    When the input line starts with MC it indicates a recorded mouse click. This function decodes that line and returns
    the mouse click position, button, and pressed or released.
    :param stored_line:
    :return: A list [x position, y position, mouse button, pressed true or false]
    """
    click_x_pos = ""
    click_y_pos = ""
    click_button = ""
    click_comma_pos = 0

    # Get information on which button was used.
    if stored_line[2] == "L":
        click_button = "left"
    elif stored_line[2] == "R":
        click_button = "right"

    # Get location to preform mouse click.
    for l in range(len(stored_line) - 4):
        if stored_line[l + 4] == ",":
            click_comma_pos = l + 4
            break
        click_x_pos += (stored_line[l + 4])
    for j in range(len(stored_line) - click_comma_pos - 4):
        click_y_pos += stored_line[j + click_comma_pos + 2]
    return [click_x_pos, click_y_pos, click_button]


def main_display(chn, mode="Record"):
    """
    This function is called to update the main screen display.
    :param chn: Int, describes the selected channel.
    :param mode: String, "Record" or "Play" depending on the mode.
    :return: None
    """
    print("-----------------------------------------------------------------------")
    channel_display(chn)
    print("-----------------------------------------------------------------------")


def channel_display(chn):
    """
    This function is called from the main_display function to print the appropriate image depending on the channel.
    :param chn: Int, describes the selected channel.
    :return: None
    """
    if chn == 1:
        print("-----------")
        print("-CHANNEL 1-                    CHANNEL 2                    CHANNEL 3 ")
        print("-----------")
    elif chn == 2:
        print("                              -----------                             ")
        print("CHANNEL 1                     -CHANNEL 2-                   CHANNEL 3 ")
        print("                              ------------                            ")
    elif chn == 3:
        print("                                                           -----------")
        print("CHANNEL 1                      CHANNEL 2                   -CHANNEL 3-")
        print("                                                           -----------")
    else:
        print(" ")
        print("CHANNEL 1                      CHANNEL 2                    CHANNEL 3 ")
        print(" ")


def ask_question_int(question, responses):
    """
    This function is used when asking the user for input that is an integer. It deals with user incorrect input.
    :param question: String, question to ask the user.
    :param responses: List where elements are integers of acceptable responses.
    :return: String of user response.
    """
    response = 0

    while response not in responses:
        response = int(input(question))

    return response


def ask_question_string(question, responses):
    """
    This function is used when asking the user for input that is an integer. It deals with user incorrect input.
    :param question: String, question to ask the user.
    :param responses: List where elements are strings of acceptable responses.
    :return: String of user response.
    """
    response = "not correct"

    while response not in responses:
        response = input(question)

    return response

