def count_lower_upper(Str):
    lower_cnt = 0
    upper_cnt = 0
    cnts={}

    for char in Str:
        if char.islower():
            lower_cnt += 1
        elif char.isupper():
            upper_cnt += 1
            
    cnts = {
        'lowercase': lower_cnt,
        'uppercase': upper_cnt
    }
    
    return cnts

Str = "I am Somya Srivastava. I'm Student at PDEU."

print(count_lower_upper(Str))
