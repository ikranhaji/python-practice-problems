# Write a function that meets these requirements.
#
# Name:       basic_calculator
# Parameters: left, the left number
#             op, the math operation to perform
#             right, the right number
# Returns:    the result of the math operation
#             between left and right
#
# The op parameter can be one of four values:
#   * "+" for addition
#   * "-" for subtraction
#   * "*" for multiplication
#   * "/" for division
#
# Examples:
#     * inputs:  10, "+", 12
#       result:  22
#     * inputs:  10, "-", 12
#       result:  -2
#     * inputs:  10, "*", 12
#       result:  120
#     * inputs:  10, "/", 12
#       result:  0.8333333333333334

def basic_calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2
