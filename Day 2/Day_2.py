import re

def part_one():
    pattern1 = re.compile(r'(\d+)\s(g|r|b)')
    pattern2 = re.compile(r'Game\s(\d+)')

    sum = 0

    mp = {
        'r': 12,
        'g': 13,
        'b': 14,
    }

    with open('input.txt', 'r') as f:
        for line in f:
            balls = pattern1.finditer(line)

            for ball in balls:
                if (int(ball.group(1)) > mp[str(ball.group(2))]):
                    break

            else:
                game_number = pattern2.search(line)
                sum += int(game_number.group(1))
                
    print(sum)

def part_two():
    pattern = re.compile(r'(\d+)\s(g|r|b)')

    sum = 0

    mp = {
        'r': 0,
        'g': 0,
        'b': 0,
    }

    with open('input.txt', 'r') as f:
        for line in f:
            balls = pattern.finditer(line)

            for ball in balls:
                mp[str(ball.group(2))] = max(mp[str(ball.group(2))], int(ball.group(1)))

            sum += (mp['r'] * mp['g'] * mp['b'])

            mp['r'] = mp['g'] = mp['b'] = 0
        
    print(sum)

part_one()
part_two()
