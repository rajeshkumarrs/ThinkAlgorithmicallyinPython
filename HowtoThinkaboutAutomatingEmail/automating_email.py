import smtplib
import getpass

# function to get keyboard input
def prompt(prompt):
    return input(prompt).strip()


# get user name
user_name = prompt("user name: ")
# get password
password = getpass.getpass(prompt="password: ")
fromaddr = user_name + "@gmail.com"

# send email based on the list of dictionary of the input file
def send_email(file_rows):
    for row in file_rows:
        toaddrs = row['email']
        msg = "Dear {0}, Your score or the book assignment is broken down below by question number. \n\n\t1. {1}: {2} \n\t2. {3}: {4} \n\t3. {5}: {6}".format(
            row['firstname'], row['problem1score'], row['problem1comments'], row['problem2score'], row['problem2comments'], row['problem3score'], row['problem3comments'])
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(user_name, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

# read csv file into list of dictionaries
def read_file(filename):
    file_rows = []
    with open(filename, "r") as f:
        contents = f.read().splitlines()
        header = contents[0].split(",")
        for row in range(1, len(contents)):
            file_rows_dict = {}
            row_lst = contents[row].split(",")
            for j in range(len(row_lst)):
                file_rows_dict[header[j]] = row_lst[j]
            file_rows.append(file_rows_dict)
        return file_rows


if __name__ == '__main__':
    file_rows = read_file("./exam.csv")
    send_email(file_rows)
