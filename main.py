from bruteforce_algo.bruteforce import bruteforce_entry_point
from optimized_algo.optimized import optimized_entry_point


def main():
    test_file_path = "./input/bruteforce_data.csv"
    first_file_path = "./input/dataset1_Python+P7.csv"
    second_file_path = "./input/dataset2_Python+P7.csv"

    bruteforce_entry_point(test_file_path)
    optimized_entry_point(test_file_path, "Test File")

    optimized_entry_point(first_file_path, "File 1")
    optimized_entry_point(second_file_path, "File 2")


if __name__ == '__main__':
    main()
