
user1 = input("시급은 얼마입니까?")

hourly_wage = int(user1)

user2 = input("몇 시간 일했습니까?")

time = int(user2)

total_wage = hourly_wage * time

fmt = """시급 {0}원으로 {1}시간 일했으므로 수당은 {2}원입니다."""
desc = fmt.format(hourly_wage, time, total_wage)

print(desc)