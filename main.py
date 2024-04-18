from bruteforce import entry_point
from optimized import optimized_entry_point


def main():
    entry_point()
    first_file_path = "./input/dataset1_Python+P7.csv"
    second_file_path = "./input/dataset2_Python+P7.csv"
    optimized_entry_point(first_file_path)
    optimized_entry_point(second_file_path)


if __name__ == '__main__':
    main()
