function multiply(x, y):
    result = 0
    shift_count = 0
    
    while y > 0:
        if y & 1 == 1:  # If the least significant bit of y is 1
            result = result + (x << shift_count)  # Add x shifted by shift_count positions
        y = y >> 1  # Right shift y by 1 (to process the next bit)
        shift_count = shift_count + 1  # Increment the shift count
    
    return result
