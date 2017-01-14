#2017-budget-planning

prev_monthly_act_pay = 2132770
prev_annual_act_pay = prev_monthly_act_pay * 12
prev_annual_surf_pay = 28000000
prev_monthly_surf_pay = prev_annual_surf_pay / 12
tax = 100 - prev_monthly_act_pay / prev_monthly_surf_pay * 100


print ("--------------------------------")
print ("tax = " + str(tax) + "%")
print ("prev_annual_surf_pay = " + str(prev_annual_surf_pay))



increase_rate = 0.08

cur_annual_surf_pay = prev_annual_surf_pay * (1+increase_rate)
cur_monthly_surf_pay = cur_annual_surf_pay / 12
cur_annual_act_pay = cur_annual_surf_pay * (100-tax)
cur_monthly_act_pay = cur_monthly_surf_pay * ((100-tax)/100)

print ("cur_annual_surf_pay = " + str(int(cur_annual_surf_pay)))
print ("cur_monthly_surf_pay = " + str(int(cur_monthly_surf_pay)))
print ("cur_monthly_act_pay = " + str(int(cur_monthly_act_pay)))
print ("--------------------------------")


rent = 200000
dating = 700000
phone = 110000
transportation = 110000

routine_spent = rent + dating + phone + transportation
potential_pay = 500000
deposit = 10000000

spare = {}

spare[1] = prev_monthly_act_pay - 850000
spare[2] = cur_monthly_act_pay - 1000000
spare[3] = cur_monthly_act_pay
spare[4] = 0
spare[5] = -1500000
spare[6] = 0
spare[7] = 0
spare[8] = 0
spare[9] = 0
spare[10] = 0
spare[11] = 0
spare[12] = 0


for n in range(1, 13):
#    spare[n] = cur_monthly_act_pay - routine_spent
    spare[n] = spare[n] - routine_spent + potential_pay

    if n>1:
        deposit = deposit + spare[n-1]
    print (str(n) + "\t" + str(int(spare[n])) + "(" + str(deposit) + ")" )
#
#
#
#
#
#
#
