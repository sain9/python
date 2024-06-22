print("\033[31mThis text is red!\033[0m")
print("\033[32mThis text is green!\033[1m")
print("\033[42m\033[37mThis text is white on a green background!\033[0m")

print("\033[33mThis text is yellow!\033[0m")
print("\033[44mThis text has a blue background!\033[0m")
print("\033[1mThis text is bright!\033[0m")

print(f'\033[1m\033[31m\033[43mBold Red on Yellow\033[0m')
print(f'\033[36m\033[40mCyan on Black\033[0m')
print(f'\033[35m\033[42mMagenta on Green\033[0m')
print(f'\033[1m\033[34m\033[47mBold Blue on White\033[0m')
print(f'\033[7m\033[33mReversed Yellow\033[0m')

print(f'\033[1m\033[32mBold Green Text\033[0m')
print(f'\033[4m\033[31mUnderlined Red Text\033[0m')
print(f'\033[35m\033[47mMagenta Text on White Background\033[0m')
print(f'\033[36m\033[44mCyan Text on Blue Background\033[0m')
print(f'\033[1m\033[33m\033[41mBold Yellow Text on Red Background\033[0m')
print(f'\033[7mReversed Colors\033[0m')

# Example of bold cyan text on a black background
print(f'\033[1m\033[36m\033[40mBold Cyan on Black\033[0m')


# Example of bold bright white text on a red background
print(f'\033[1m\033[97m\033[41mBold Bright White on Red\033[0m')
# Example of bold yellow text with underlines
print(f'\033[1m\033[4m\033[33mBold Yellow Underlined\033[0m')
print(f'\033[1m\033[4m\033[31mCode Output\033[0m')

# Summary of ANSI Escape Codes
# Text colors:
# Black: \033[30m
# Red: \033[31m
# Green: \033[32m
# Yellow: \033[33m
# Blue: \033[34m
# Magenta: \033[35m
# Cyan: \033[36m
# White: \033[37m

# Background colors:
# Black: \033[40m
# Red: \033[41m
# Green: \033[42m
# Yellow: \033[43m
# Blue: \033[44m
# Magenta: \033[45m
# Cyan: \033[46m
# White: \033[47m
# Styles:

# Bold: \033[1m
# Underline: \033[4m
# Reset: \033[0m