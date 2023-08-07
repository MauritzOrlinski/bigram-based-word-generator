FILTER_LIST = [",", ".", "!", "?", ":", ";", "(", ")", "[", "]", "{", "}", "'", '"', "-", "_", "+", "=", "*", "/", "\\", "|", "<", ">", "@", "#", "$", "%", "^", "&", "~", "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def get_words_from_file(file_paths: list):
    """
    This function reads the data from the file and returns it as a string.
    :param file_path: the path of the file.
    :return: the data from the file as a string.
    """
    words = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            for line in file:
                for word in line.split():
                    for char in word:
                        if char in FILTER_LIST:
                            word = word.replace(char, "")
                    words.append(word)
    return words
