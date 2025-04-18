def sanitize_list(num):
    if len(num) == 0:
        return []
    
    first_element = num[0]
    if first_element < 0:
        sanitized_value = 0
    else:
        sanitized_value = first_element
    
    return [sanitized_value] + sanitize_list(num[1:])

lst = [1, -2, 3, -4, 5, -6]
sanitized_lst = sanitize_list(lst)

print(f"Original list: {lst}")
print(f"Sanitized list: {sanitized_lst}")
