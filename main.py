tile_values = {'a' : 1, 'b' : 4, 'c' : 5, 'd' : 3, 'e' : 1, 'f' : 5, 'g' : 3, 'h' : 4, 'i' : 1, 'j' : 7, 'k' : 6, 'l' : 3, 'm' : 4, 'n' : 2, 'o' : 1, 'p' : 4, 'q' : 8, 'r' : 2, 's' : 2, 't' : 2, 'u' : 4, 'v' : 5, 'w' : 5, 'x' : 7, 'y' : 4, 'z' : 8,}

f = open("enable2.txt", 'r', encoding='utf-8')
words = f.read().split("\n")
f.close()
string_words = str(words)

tiles = list(input("letters > "))
doubles = int(input("double letter tile: "))
triples = int(input("triple letter tile: "))
double_word = int(input("double word tile: "))
#swaps = int(input("swaps: "))
tile_vals = []
for x in range(len(tiles)):
    tile_vals.append(tile_values[tiles[x]])
if 0 <= doubles <= 24:
    tile_vals[doubles] *= 2
if 0 <= triples <= 24:
    tile_vals[triples] *= 2
chain = []
letter_chain = []
potential_words = []
potential_words_vals = []
update = 0
def check_iteration():
    global chain
    global letter_chain
    global potential_words
    global string_words
    global potential_words_vals
    global update
    for tile in get_neighbours(chain[-1], chain):
        chain.append(tile)
        letter_chain += tiles[tile]
        update += 1
        if "'" + letter_chain in string_words:
            if letter_chain in words:
                potential_words.append(letter_chain)
                potential_words_vals.append(chain.copy())
                #words.remove(letter_chain)
                #string_words = str(words)
                update += 2
            if len(letter_chain) < 25:
                check_iteration()
                chain.remove(tile)
                letter_chain = letter_chain[:-1]
            else:
                chain.remove(tile)
                letter_chain = letter_chain[:-1]
        else:
            chain = chain[:-1]
            letter_chain = letter_chain[:-1]

def get_neighbours(tile_index, already_used):
    return_list = []
    if not tile_index % 5 == 0 and not tile_index-1 in already_used:
        return_list.append(tile_index-1)
        if tile_index >= 5 and not tile_index-6 in already_used:
            return_list.append(tile_index - 6)
        if not tile_index >= 20 and not tile_index+4 in already_used:
            return_list.append(tile_index + 4)
    if not tile_index % 5 == 4 and not tile_index+1 in already_used:
        return_list.append(tile_index + 1)
        if not tile_index <= 4 and not tile_index-4 in already_used:
            return_list.append(tile_index - 4)
        if tile_index <= 19 and not tile_index+6 in already_used:
            return_list.append(tile_index + 6)
    if not tile_index >= 20 and not tile_index+5 in already_used:
        return_list.append(tile_index+5)
    if not tile_index <= 4 and not tile_index-5 in already_used:
        return_list.append(tile_index -5)
    return return_list

for x in range(25):
    print("analysing... " + str(x + 1) + "/25")
    chain = [x]
    letter_chain = tiles[x]
    check_iteration()

#print("calculating point values...")

point_comparison = []
for item in potential_words_vals:
    points = 0
    for subitem in item:
        points+=tile_vals[subitem]
    if double_word in item:
        points *= 2
    if len(item) >= 6:
        points += 10

    point_comparison.append(points)
print(update)
print(sorted(dict(zip(potential_words, point_comparison)).items(), key=lambda x:x[1], reverse=True))