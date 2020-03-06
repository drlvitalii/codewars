# You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button
# it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block in a direction and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes
# (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
#
# Note: you will always receive a valid array containing a random assortment of direction letters
# ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    count_n = 0
    count_s = 0
    count_w = 0
    count_e = 0

    for i in walk:
        if i == 's':
            count_s += 1
        if i == 'w':
            count_w += 1
        if i == 'e':
            count_e += 1
        if i == 'n':
            count_n += 1

    if count_e + count_s + count_n + count_w > 10:
        return False
    if count_e + count_s + count_n + count_w < 5:
        return False
    if count_w != count_e:
        return False
    if count_s != count_n:
        return False
    return True

