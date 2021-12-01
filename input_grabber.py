from requests import request
import sys

year = sys.argv[1]
day = sys.argv[2]
session_cookie = sys.argv[3]
target_file = sys.argv[4]

response = request('get', 'https://adventofcode.com/{}/day/{}/input'.format(year, day), cookies={'session': session_cookie})

with open(target_file, mode='w') as input_file:
    input = response.content.decode('utf-8')
    input_file.write(input)
    print('Input for year {} day {} written to {}'.format(year, day, target_file))
