import argparse


def main(input_path, output_path):

    output = open(output_path, 'w')

    output.close()

if __name__ == '__main__':
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input')
    parser.add_argument('--output', default='./output')
    args = parser.parse_args()

    main(args.input, args.output)


