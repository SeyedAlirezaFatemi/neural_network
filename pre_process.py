import csv


def convert_to_csv(in_path: str, out_path: str):
    with open(in_path, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(out_path, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)


if __name__ == '__main__':
    convert_to_csv('data/X_train.txt', 'data/X_train.csv')
    convert_to_csv('data/y_train.txt', 'data/y_train.csv')
