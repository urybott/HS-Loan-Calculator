import math
import argparse


msg_ = [""] * 20
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
msg_[15] = 'Incorrect parameters'
msg_[16] = "Month {}: payment is {}"
msg_[17] = "Overpayment ="

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

parser = argparse.ArgumentParser(description="This program is Loan Calculator.")
# parser.add_argument("-t", "--type", choices=["diff", "annuity"], required=True,
#                     help="Incorrect parameters.")
parser.add_argument("-t", "--type")
parser.add_argument("-i", "--interest", type=float)
parser.add_argument("--principal", type=int)  # "-pr", 
parser.add_argument("--payment", type=int)  # "-pa", 
parser.add_argument("--periods", type=int)  # "-pe", 
args = parser.parse_args()

typ = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest

err = False
if typ is None or not typ in ["diff", "annuity"] or args.interest is None:
    err = 1  # True
elif typ == "diff" and (not payment is None or [periods, principal].count(None) != 0):
    err = 2  # True
elif typ == "annuity" and [payment, periods, principal].count(None) != 1:
    err = 3  # True
elif len([v for v in [payment, periods, principal, interest] if not v is None and v < 0]) > 0:
    err = 4  # True

if err:
    print(msg_[15])  # , err
    # raise Exception("stop")
else:
    interes = interest / 1200

    if periods is None:
        periods = math.ceil(math.log(payment / (payment - interes * principal), interes + 1))
        years = int(periods / 12)
        months = periods % 12
        sm = "" if months == 1 else "s"
        sy = "" if years == 1 else "s"
        res = msg_[10]
        res += msg_[11].format(years, sy) if years > 0 else ""
        res += msg_[12] if years > 0 and months > 0 else ""
        res += msg_[13].format(months, sm) if months > 0 else ""
        res += msg_[14]
        print(res)
        print(msg_[17], payment * periods - principal)

    elif principal is None:
        principal = int(payment / ((interes * (1 + interes) ** periods) / (((1 + interes) ** periods - 1))))
        print(msg_[9].format(principal))
        print(msg_[17], payment * periods - principal)

        # payment is None
    elif typ == "diff":
        payment = 0
        summ = 0
        p = principal / periods
        for m in range(periods):
            payment = int(p + interes * (principal - (principal * m) / periods) + 0.9)
            summ += payment
            print(msg_[16].format(m + 1, payment))
        print(msg_[17], summ - principal)

    else:  # typ == "annuity"
        payment = math.ceil(principal * ((interes * (1 + interes) ** periods) / (((1 + interes) ** periods - 1))))
        lastpayment = 0
        ret = msg_[5] + str(payment) + (msg_[6] + str(lastpayment) if lastpayment else "") + "!"
        print(ret)
        print(msg_[17], payment * periods - principal)

