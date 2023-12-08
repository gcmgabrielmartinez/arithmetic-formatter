# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'])) #ok!

print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])) #ok!

print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'])) #ok!

print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])) #ok!

print(arithmetic_arranger(['3801 - 2', '123 + 49'])) #ok

print(arithmetic_arranger(['1 + 2', '1 - 9380'])) #ok

print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))

print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))


print(arithmetic_arranger(['3 + 855', '988 + 40'], True))

print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(['-vv'])
