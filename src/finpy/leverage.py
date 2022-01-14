""" Leverage Quotient and Debt Ratio
todo: define class
"""


def leverage_quotient(debt, equity):
    return debt / equity


def debt_ratio(debt, equity):
    return equity / (equity + debt)


def expected_loss(pd: float, ead: float, lgd: float):
    """
    :param pd: Probability of default (PD) for one year (eg. 4% means every 25 years)
    :param ead: Exposure at default (EAD) is the value of a default in given year
    :param lgd: Loss given defaut (LGD). How much is lost if credit defaults (eg. loss_default = 25% means 75% is lost)
    :return: expected loss (EL) for a given year
    """
    return pd * ead * (1 - lgd)


if __name__ == '__main__':
    print(leverage_quotient(200, 100))
    print(debt_ratio(200, 100))
