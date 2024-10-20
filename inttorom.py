def int_to_roman(num):
   # Define a mapping of integers to their corresponding Roman numerals
    val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]    
    roman_numeral = " "
    # Loop through the values and symbols
    for i in range(len(val)):
        # While num is greater than or equal to the value
        while num >= val[i]:
            roman_numeral += syms[i]  # Append the symbol
            num -= val[i]              # Decrease num by the value            
    return roman_numeral
# Example usage
number = 1994
print(f"The Roman numeral for {number} is {int_to_roman(number)}")