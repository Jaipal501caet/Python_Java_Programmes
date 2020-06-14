normal_hour_rate = 100
extend_hour_rate = normal_hour_rate*1.5
normal_hour=40
work_hour = int(input("Enter the working hour : "))

if(work_hour > 40):
    payment= work_hour*extend_hour_rate
    print("As you worked for : ", work_hour,
          "which is more than : ", normal_hour, "So total payment will be at 1.5 rate of 100 : ", payment)
else:
    payment=work_hour*normal_hour_rate
    print("Total payment is : ", payment)