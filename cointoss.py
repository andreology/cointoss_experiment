import numpy as np
import random

#Simulating a Coin Toss Experiment
def coin(N):
    heads, tails = 0, 0
    #begin experiement for n times
    for k in range(0, N):
        coin = random.randint(0, 2)
        if coin == 1:
            heads = heads+1
        else:
            tails = tails+1
    #save results and use law of probability to compute
    p_heads = heads/N
    p_tails = tails/N
    print('probability of heads = ', p_heads)
    print('probability of tails= ', p_tails)

#A computationally efficient  approach by using arrays
def coin2(N):
    coin = np.random.randint(2, size=N)
    heads = np.sum(coin)
    tails = N - heads
    #gathering results from experiement
    p_heads = heads / N
    p_tails = tails / N
    print('Probability of Heads landing = ', p_heads)
    print('Probability of Tails landing = ', p_tails)

#tester method
def main():
    print('Model One')
    coin(4)
    print('Model Two')
    coin2(4)

if __name__ == "__main__":
    main()
