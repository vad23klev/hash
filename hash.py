from csv import reader
import hashlib
import csv
import sys

# initializing string
str2hash = "GeeksforGeeks"

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())

print(sys.argv)
# open file in read mode
if (len(sys.argv) >= 3) :
    number = int(sys.argv[2])
    file_name = sys.argv[1]
    with open(file_name, 'r') as read_obj:
        with open('hashed.csv', mode='w') as hashed_file:
            hashed_writer = csv.writer(hashed_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # pass the file object to reader() to get the reader object
            csv_reader = reader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                print(row)
                result = hashlib.md5(row[number].encode())
                print(result.hexdigest())
                row[number] = result.hexdigest()
                hashed_writer.writerow(row)
else:
    print("Первый аргумент путь до файда")
    print("Второй аргумент номер колонки для хеша(начиная с 0)")