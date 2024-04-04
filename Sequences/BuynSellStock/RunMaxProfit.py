from MaxProfit import Solution

def main():
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]

    solution = Solution()
    print("Maximum profit for prices1:", solution.maxProfit(prices1))  # Output: 5
    print("Maximum profit for prices2:", solution.maxProfit(prices2))  # Output: 0

if __name__ == "__main__":
    main()