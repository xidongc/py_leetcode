# Complete the should_allow_charge function below.
import re
def should_allow_charge(charge_and_rules):
    if charge_and_rules[0].startswith('CHARGE'):
        conditions = charge_and_rules[0].split(': ')[1]
        conditionsList = conditions.split('&')
        card_country = conditionsList[0].split('=')[1]
        currency = conditionsList[1].split('=')[1]
        amount = int(conditionsList[2].split('=')[1])
        ip_country = conditionsList[3].split('=')[1]
    else:
        return 0
    allowCons,blockCons = '',''
    for i in range(1,len(charge_and_rules)):
        # Get Allow rules
        if charge_and_rules[i].startswith('ALLOW'):
            allowCons = charge_and_rules[i].split(': ')[1]
        # Get Block rules
        if charge_and_rules[i].startswith('BLOCK'):
            blockCons = charge_and_rules[i].split(': ')[1]
    # Apply allow rules
    if allowCons != '':
        # if (card_country == '' and card_country in allowCons) or (currency == '' and currency in allowCons) or (amount = 0 and currency in allowCons)
        if eval(allowCons.lower()):
            return 1
    # Apply block rules
    if blockCons != '':
        if eval(blockCons.lower()):
            return 0
    return 1

# case1:
# print(should_allow_charge([
#   "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
#   "ALLOW: amount < 1000",
# ]))
# 1
# case2:
# print(should_allow_charge([
#   "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
#   "BLOCK: amount > 100",
# ]))
# 0
# case3:
print(should_allow_charge( [
  "CHARGE: card_country=US&currency=USD&amount=150&ip_country=CA",
  "ALLOW: amount < 100",
  "BLOCK: card_country != ip_country AND amount > 100",
 ]))
# 0