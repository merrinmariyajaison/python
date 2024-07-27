def copy_file(source_file, destination_file):
    src = open(source_file, 'r')
    dest = open(destination_file, 'w')

    for line in src:
        dest.write(line)
    
    src.close()
    dest.close()
    print(f"Contents copied from {source_file} to {destination_file} successfully.")


source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")
copy_file(source_file, destination_file)
