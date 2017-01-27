
import re
import json
import codecs
import sys
from collections import OrderedDict


def sortcards(cards):
    classes = OrderedDict([
        ('Special classes:', None),
        ('multicards', []),
        ('Inclusive classes:', None),
        ('X cards', []),
        ('kicker cards', []),
        ('counter cards', []),
        ('uncast cards', []),
        ('choice cards', []),
        ('equipment', []),
        ('levelers', []),
        ('legendary', []),
        ('Exclusive classes:', None),
        ('planeswalkers', []),
        ('lands', []),
        ('instants', []),
        ('sorceries', []),
        ('enchantments', []),
        ('noncreature artifacts', []),
        ('creatures', []),
        ('other', []),
        ('By color:', None),
        ('white', []),
        ('blue', []),
        ('black', []),
        ('red', []),
        ('green', []),
        ('colorless nonland', []),
        ('colorless land', []),
        ('unknown color', []),
        ('By number of colors:', None),
        ('zero colors', []),                
        ('one color', []),
        ('two colors', []),
        ('three colors', []),
        ('four colors', []),
        ('five colors', []),
        ('more colors?', []),
    ])

    for card in cards:
        # special classes
        if '|\n|' in card:
            # better formatting pls???
            classes['multicards'] += [card.replace('|\n|', '|\n~~~~~~~~~~~~~~~~\n|')]
            continue
        
        # inclusive classes
        if 'X' in card:
            classes['X cards'] += [card]
        if 'kick' in card:
            classes['kicker cards'] += [card]
        if '%' in card or '#' in card:
            classes['counter cards'] += [card]
        if 'uncast' in card:
            classes['uncast cards'] += [card]
        if '[' in card or ']' in card or '=' in card:
            classes['choice cards'] += [card]
        if '|equipment|' in card or 'equip {' in card:
            classes['equipment'] += [card]
        if 'level up' in card or 'level &' in card:
            classes['levelers'] += [card]
        if '|legendary|' in card:
            classes['legendary'] += [card]

        # exclusive classes
        if '|planeswalker|' in card:
            classes['planeswalkers'] += [card]
        elif '|land|' in card:
            classes['lands'] += [card]
        elif '|instant|' in card:
            classes['instants'] += [card]
        elif '|sorcery|' in card:
            classes['sorceries'] += [card]
        elif '|enchantment|' in card:
            classes['enchantments'] += [card]
        elif '|artifact|' in card:
            classes['noncreature artifacts'] += [card]
        elif '|creature|' in card or 'artifact creature' in card:
            classes['creatures'] += [card]
        else:
            classes['other'] += [card]

        # color classes need to find the mana cost
        fields = card.split('|')
        if len(fields) != 11:
            classes['unknown color'] += [card]
        else:
            cost = fields [3]
            color_count = 0
            if 'W' in cost or 'U' in cost or 'B' in cost or 'R' in cost or 'G' in cost:
                if 'W' in cost:
                    classes['white'] += [card]
                    color_count += 1
                if 'U' in cost:
                    classes['blue'] += [card]
                    color_count += 1
                if 'B' in cost:
                    classes['black'] += [card]
                    color_count += 1
                if 'R' in cost:
                    classes['red'] += [card]
                    color_count += 1
                if 'G' in cost:
                    classes['green'] += [card]
                    color_count += 1
                # should be unreachable
                if color_count == 0:
                    classes['unknown color'] += [card]
            else:
                if '|land|' in card:
                    classes['colorless land'] += [card]
                else:
                    classes['colorless nonland'] += [card]
            
            if color_count == 0:
                classes['zero colors'] += [card]
            elif color_count == 1:
                classes['one color'] += [card]
            elif color_count == 2:
                classes['two colors'] += [card]
            elif color_count == 3:
                classes['three colors'] += [card]
            elif color_count == 4:
                classes['four colors'] += [card]
            elif color_count == 5:
                classes['five colors'] += [card]
            else:
                classes['more colors?'] += [card]
        
    return classes
def main():
    f = open("C:\\Users\\Student 6\\Documents\\Visual Studio 2015\\Projects\\mtg neural network card maker\\input_(16).txt", 'r')
    text = f.read()
    f.close()

    cards = text.split('\n\n')[1:-1]
    classes = sortcards(cards)

    for cardclass in classes:
        if classes[cardclass] == None:
            print (cardclass)
        else:
            print('  ' + cardclass + ': ' + str(len(classes[cardclass])))
    
if __name__ == '__main__':
        main()

