from collections import defaultdict


def time_to_minute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m



def solution(fees, records):
    answer = dict()
    
    car = defaultdict(list)    
    s_time, s_fee, p_time, p_fee = fees
    for r in records:
        now, c_num, state = r.split(' ')
        if len(car[c_num]) == 0:
            car[c_num] = [now, 0, state]
        else:
            if state == 'OUT':
                prev, total, p_state = car[c_num]
                total += (time_to_minute(now) - time_to_minute(prev))
                car[c_num] = [now, total, state]
            else:
                car[c_num] = [now, car[c_num][1], state]
    
    for c in car:
        now, total, state = car[c]
        if state == 'IN':
            car[c][1] += (time_to_minute('23:59') - time_to_minute(now))
    
    for c in car:
        now, total, state = car[c]
        if total <= s_time:
            answer[c] = s_fee
        else:
            temp_answer = s_fee
            total -= s_time
            
            rest, mod = divmod(total, p_time)
            if mod > 0:
                temp_answer += ((rest + 1) * p_fee)
            else:
                temp_answer += (rest * p_fee)
            answer[c] = temp_answer
    
    answer = sorted(answer.items())
    
    result = []
    for a in answer:
        result.append(a[1])
    return result


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))