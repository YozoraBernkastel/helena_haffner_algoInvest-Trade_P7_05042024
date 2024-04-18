from bruteforce import bruteforce_entry_point
from optimized import optimized_entry_point


def main():
    first_file_path = "./input/dataset1_Python+P7.csv"
    second_file_path = "./input/dataset2_Python+P7.csv"

    bruteforce_entry_point()

    optimized_entry_point(first_file_path, "File 1")
    optimized_entry_point(second_file_path, "File 2")


if __name__ == '__main__':
    main()
