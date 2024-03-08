import sys

def filter_duplicates(input_file, output_file):
    unique_entries = set()
    duplicate_entries = set()
    with open(input_file, 'r') as file:
        for line in file:
            entry = line.strip()
            if entry not in unique_entries:
                unique_entries.add(entry)
            else:
                duplicate_entries.add(entry)

    with open(output_file, 'w') as file:
        for entry in unique_entries:
            if entry not in duplicate_entries:
                file.write(entry + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py input_file output_file")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    filter_duplicates(input_filename, output_filename)
    print("The operation is complete.")
