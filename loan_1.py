# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

# write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

msg_ = [""] * 10
msg_[0] = "Enter the loan principal:"
msg_[1] = 'What do you want to calculate?\ntype "m" for number of monthly payments,\ntype "p" for the monthly payment:'
msg_[2] = 'Enter the monthly payment:'
msg_[3] = "Enter the number of months:"
msg_[4] = 'It will take {} month{} to repay the loan'
msg_[5] = 'Your monthly payment = '
msg_[6] = ' and the last payment = '
msg_[7] = 'Invalid input. Please try again.'

def is_str_int(v):
    res = False
    if len(v) > 0:
        if v[0] in "-+" :
            v = v[1:]
        if v.isdigit():
            res = True
    return res

def int_imput():
    a = 0
    m = 7
    while m:
        i = input()
        if not is_str_int(i):
            print(msg_[m])
        else:
            a = int(i)
            if a > 0:
                m = 0
            else:
                print(msg_[m])
    return a

def str_imput(choices=""):
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


print(msg_[0])
amount = int_imput()
print(msg_[1])
user_choices = str_imput("mp")
if user_choices == "m":
    print(msg_[2])
    payment = int_imput()
    months = round(amount / payment)
    s = "s" if months != 1 else ""
    print(msg_[4].format(months,s))
else:
    print(msg_[3])
    months = int_imput()
    payment = int(amount / months)  # + 0.5
    lastpayment = 0
    if amount % months:
        payment += 1
        lastpayment = (amount - (months - 1) * payment)

    ret = msg_[5] + str(payment) + (msg_[6] + str(lastpayment) if lastpayment else "")
    print(ret)
