# BustaBit Data Analysis
This is a independent project dedicated to beating the BustaBit system. This project is centered around the Bitcoin gambling website: https://bustabit.com 

If you're not sure how it works, check it out for a while. You can watch the games, and not participate. Actually, I would recommend not participating, as gambling is a really irresponsible habit, and bitcoin gambling is illegal in some jurisdictions. With THAT being said, let's get on to the good stuff.

## Preface
So, in the chat of bustabit, there are chat commands where you can calculate the probability of your multiplier NOT busting. These are not padded probabilities, they're taken straight from datasets within the game. To calculate probability, you go in the SPAM chat channel and you issue a command like this: ```!prob 1.1``` and that would tell me the probability of rolling >= 1.1x is 89.9264%. Simply put, if I bet 10,000 bits (around $14.78 at the time of typing this), there is an 89.9264% chance of me getting $1.48 in profit. Obviously, this is very oversimplified, but you get the gist of it. For reference, a bit is a millionth of a bitcoin. It's a way of dividing a bitcoin into a smaller, simplified unit.

## What I'm trying to test
I want to test how much money you would gain **or lose** if you kept betting at a certain multiplier over a period of x amount of games. The creator of the website, Ryan, says the average time of a game (including wait time) is 30 seconds. So, we will be testing profit **or losses** over the course of 1,000 games, which is 30,000 seconds, or 8 hours and 20 minutes. So, this is if you left your computer running for this long, auto betting on a single multiplier. I want to find the most optimal multiplier.

## Probabilities of low multipliers
I will only be testing the following 10 multipliers, and their probabilities are below
+ **1.06x**: 93.352192%
+ **1.08x**: 91.607292%
+ **1.1x**: 89.926424%
+ **1.12x**: 88.306128%
+ **1.16x**: 85.234610%
+ **1.2x**: 82.369581%
+ **1.24x**: 79.690896%
+ **1.3x**: 75.984343%
+ **1.36x**: 72.607261%
+ **1.42x**: 69.517590%

## How can we replicate this model in Python for data analysis
Simple, well kind of. So, I'm positive there are better ways of doing this, but here is how I'm gonna tackle this. I'll be using a random number generator. Sounds stupid, and yeah, it probably is.. But I want to get it as accurate as possible, so I'll be using https://random.org random API, to generate a very "random" number for us. Their API selects integers at random, using a seed that comes from atmospheric white-noise. So, if this isn't random, I'm not sure what is.
So for example, our multiplier up way up there, 1.06x, has a probability of 93.352192% to roll over it. So, simply put, in our random number generator, we will generate a number between 1 and 100,000,000 , and if the random number is >= 93352192 , then that roll will be a "winning" roll. Yes, I know this is very hacky, but we can even rinse and repeat this 10-20 times for each multiplier to reduce our error (assuming BustaBit is fair, and it seems it's as fair as an online casino can get)

## How we can test this
So, simply put, I will generate a batch of 1000 random numbers for each multiplier (1 to 100,000,000), and if the number is greater than our probability number, we lose. The 1000 random numbers will simulate 1000 games (which will take 8 hours and 20 minutes running at auto). We will have a starting bank balance, and an ending bank balance (units will be bits).
For each random roll, a win would be:
```python
totalBalance += (bet * multiplier)
```
simple enough, and for a loss:
```python
totalBalance -= bet
```
