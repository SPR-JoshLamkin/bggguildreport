import json

def main(old_file, new_file):

    of = open(old_file, 'r')
    old_lists = json.load(of)

    nf = open(new_file, 'r')
    new_lists = json.load(nf)

    new_top50 = new_lists['top50']
    old_top50 = old_lists['top50']

    old_top50_gameids = [x[1] for x in old_top50]

    for index, game_info in enumerate(new_top50):
        try:
            old_index = old_top50_gameids.index(game_info[1])
        except ValueError:
            old_index = -1

        detail_string = str(index + 1) + ' ('
        if old_index > -1:
            diff = old_index - index
            if diff > -1:
                detail_string += '+' + str(diff) + '). '
            else:
                detail_string += str(diff) + '). '
        else:
            detail_string += 'new). '

        detail_string += '%s %d %.3f %.3f' % (game_info[0], game_info[2], game_info[3], game_info[4])
        print detail_string

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--old', type=str, help='Old lists')
    parser.add_argument('--new', type=str, help='New lists')
    args = parser.parse_args()
    main(args.old, args.new)
