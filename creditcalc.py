import math
import argparse


parser = argparse.ArgumentParser(description="This program is Loan Calculator.")
#parser.add_argument("-t", "--type", required=True,
parser.add_argument("-t", "--type", choices=["diff", "annuity"], required=True,
                    help="Incorrect parameters.")
parser.add_argument("-i", "--interest", required=True,
                    help="Incorrect parameters.")
parser.add_argument("-pr", "--principal")
parser.add_argument("-pa", "--payment")
parser.add_argument("-pe", "--periods")
args = parser.parse_args()


msg_ = [""] * 15
msg_[0] = "Enter the loan principal:"
msg_[1] = '''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:'''
msg_[2] = 'Enter the annuity payment:'
msg_[3] = "Enter the number of periods:"
msg_[4] = 'It will take {} month{} to repay the loan'
msg_[5] = 'Your monthly payment = '
msg_[6] = ' and the last payment = '
msg_[7] = 'Invalid input. Please try again.'
msg_[8] = 'Enter the loan interest:'
msg_[9] = 'Your loan principal = {}!'
msg_[10] = 'It will take '
msg_[11] = '{} year{} '
msg_[12] = 'and '
msg_[13] = '{} month{} '
msg_[14] = 'to repay this loan!'

def is_num_str(v):
    isnum = False
    if len(v):
        if v[0] in "-+":
            v = v[1:]
        v = v.split(".", 1)
        if "".join(v).isdigit():
            isnum = True
    return isnum

def num_input():
    a = 0
    m = 7
    while m:
        i = input()
        if not is_num_str(i):
            print(msg_[m])
        else:
            a = float(i)
            if a >= 0:
                m = 0
            else:
                print(msg_[m])
    return a

def str_input(choices=""):
    a = ""
    m = 7
    while m:
        i = input()
        if not choices or i in choices:
            a = i
            m = 0
        else:
            print(msg_[m])
    return a


# print(msg_[0])
# amount = int_input()
print(msg_[1])
user_choices = str_input("nap")

principal = 0
payment = 0
months = 0
interest = 0

if user_choices != "p":
    print(msg_[0])
    principal = num_input()
if user_choices != "a":
    print(msg_[2])
    payment = num_input()
if user_choices != "n":
    print(msg_[3])
    months = int(num_input())
print(msg_[8])
interest = num_input()

if user_choices == "n":
    i = interest / 1200
    all_months = math.ceil(math.log(payment / (payment - i * principal), i + 1))
    #all_months = int(principal / payment)
    # if amount % payment:
        # all_months +=1
    years = int(all_months / 12)
    months = all_months % 12
    sm = "" if months == 1 else "s"
    sy = "" if years == 1 else "s"
    res = msg_[10]
    res += msg_[11].format(years, sy) if years > 0 else ""
    res += msg_[12] if years > 0 and months > 0 else ""
    res += msg_[13].format(months, sm) if months > 0 else ""
    res += msg_[14]
    print(res)
elif user_choices == "p":
    i = interest / 1200
    principal = int(payment / ((i * (1 + i) ** months) / (((1 + i) ** months - 1))))
    print(msg_[9].format(principal))
else:
    # user_choices == "a"
    i = interest / 1200
    payment = math.ceil(principal * ((i * (1 + i) ** months) / (((1 + i) ** months - 1))))
    lastpayment = 0
    # payment = int(amount / months)  # + 0.5
    # if amount % months:
        # payment += 1
    # lastpayment = principal % months  #
    # lastpayment = (principal - (months - 1) * payment)
    ret = msg_[5] + str(payment) + (msg_[6] + str(lastpayment) if lastpayment else "") + "!"
    print(ret)
