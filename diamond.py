# coding: utf-8

def diamond(letter):
    
    if letter == 'A':
        return 'A'
    
    before = ord(letter) - ord('A')
    content = before * " " +'A'
    middle = ''
    factor = +1
    counter = 1
    iterations = 2 * before
    for iteration in xrange(0, (iterations - 1)):
        before = before - 1 * factor
        current_letter = chr(ord('A') + (counter + 1) / 2)
        middle += get_line(before, counter, current_letter)
        if current_letter == letter:
            factor = -1
        counter = counter + 2 * factor


    return content + '\n' + middle + content


def get_line(spaces_before, spaces_between, letter):
    return (spaces_before * " ") + letter + (spaces_between * " ") + letter + '\n'