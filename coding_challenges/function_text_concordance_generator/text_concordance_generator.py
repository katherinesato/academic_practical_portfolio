"""
Text Concordance Builder

Description:
    A robust Python utility designed to parse text files and generate 
    a word concordance. The function maps every unique word in a document 
    to a chronological list of the line numbers where it appears.

Skills Demonstrated:
    - File I/O & Memory Efficiency (line-by-line streaming)
    - String Manipulation & Normalization (punctuation stripping, lowercase)
    - Advanced Data Structures (dict[str, list[int]])
    - Algorithmic Logic & Duplicate Prevention

Author: Katherine Borges Sato

"""
import string


def build_concordance(filename: str) -> dict[str, list[int]]:
    """Return a concordance of words in the text file
    with the specified filename.

    The concordance is stored in a dictionary. The keys are the words in the
    text file. The value associated with each key is a list containing the line
    numbers of all the lines in the file in which the word occurs.)

    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    file = open(filename, "r", encoding="utf-8")
    conc = {}
    num_line = 0

    for line in file:
        num_line += 1
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            if word != '':
                if word not in conc:
                    conc[word] = []
                if num_line not in conc[word]:
                    conc[word].append(num_line)

    file.close
    return conc


if __name__ == '__main__':
    t_conc1 = build_concordance('input1_ballad.txt')
    if len(t_conc1) != 0:
        print('Concordance for "input1_ballad.txt":\n', t_conc1)
    else:
        print('There are no words in this text file')

    t_conc2 = build_concordance('input2_no_coward_soul_is_mine.txt')
    if len(t_conc2) != 0:
        print('Concordance for "input2_no_coward_soul_is_mine.txt":\n', t_conc2)
    else:
        print('There are no words in this text file')
