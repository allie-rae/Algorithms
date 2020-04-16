#!/usr/bin/python

import argparse



def find_max_profit(prices):
    max_profit = None
    for i in range(0, len(prices)):
        print('i', i, prices[i])
        if i > 0:
            for j in range(0, i):
                print('j', j, prices[j])
                if max_profit == None:
                    max_profit = prices[i] - prices[j]
                elif max_profit != None:
                    potential_max_profit = prices[i] - prices[j]
                    if potential_max_profit > max_profit:
                        max_profit = potential_max_profit
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
