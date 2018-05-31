import sys
# This is a automated email collecter designed for summer intern

# read email account and password from a txt file
def get_email_account():
	acc_path = sys.path[0] + r"\account.txt";
	f = open(acc_path);

	# get email account
	account = f.readline();
	account = account[9:];

	# get email password
	password = f.readline();
	password = password[10:];
	f.close()

	return (account, password);

# read the unread emails fulfill certain condition
def get_email_content():
	account, password = get_email_account();
	print(account + '\r');
	print(password);
	return;

get_email_content();
# write to excel file
# def wrt_excel:
# 	return 0;

