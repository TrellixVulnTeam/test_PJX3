import argparse

# with open('md5.txt', 'w') as fp:
# 	fp.write('-f\nbar')

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument('-f')
parser.parse_args(['@md5.txt'])

args = parser.parse_args()

print(args)


print("fuck")