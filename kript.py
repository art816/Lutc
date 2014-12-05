__author__ = 'art'

import re
import itertools


def solve(puzzle):
	words = re.findall('[A-Z]+', puzzle.upper())
	unique_characters = set(''.join(words))
	assert len(unique_characters) <= 10, 'Too many letters'
	first_letters = {word[0] for word in words}
	n = len(first_letters)
	sorted_characters = ''.join(first_letters) + \
	                    ''.join(unique_characters - first_letters)
	# print(sorted_characters)
	# print(first_letters)
	# print(unique_characters - first_letters)
	characters = tuple(ord(c) for c in sorted_characters)
	# print(characters)
	digits = tuple(ord(c) for c in '0123456789')
	# print(digits)
	zero = digits[0]
	for guess in itertools.permutations(digits, len(characters)):
		# print(zero, '\t', guess)
		if zero not in guess[:n]:
			# print(zero, '\t', guess[:n], '\t', guess[0], '\t', n)
			equation = puzzle.upper().translate(dict(zip(characters, guess)))
			if eval(equation):
				return equation


def kript(puzzle):
	# ans = eval(puzzle)
	new_str = puzzle + ' == ' + str(eval(puzzle))
	print(new_str)
	unique_digits = set(''.join(re.findall('\d', new_str)))
	# print('unique_digits==',unique_digits,'\tlen==', len(unique_digits))
	digits = tuple(ord(c) for c in unique_digits)
	# print(digits)
	abc = tuple(range(ord('A'), ord('Z') + 1))
	# print(abc)
	for guess in itertools.permutations(abc, len(unique_digits)):
		# print(guess)
		ans = new_str.translate(dict(zip(digits, guess)))
		return ans

if __name__ == '__main__':
	import sys
	for puzzle in sys.argv[1:]:
		print(puzzle)
		# solution = solve(puzzle)
		solution = kript(puzzle)
		print(solution)
		solution = solve(solution)
		if solution:
			print(solution)
