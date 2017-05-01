# BustaBit Data Analysis
This is a independent project dedicated to beating the BustaBit system. This project is centered around the Bitcoin gambling website: https://bustabit.com 

If you're not sure how it works, check it out for a while. You can watch the games, and not participate. Actually, I would recommend not participating, as gambling is a really irresponsible habit, and bitcoin gambling is illegal in some jurisdictions. With THAT being said, let's get on to the good stuff.

## Preface
So, in the chat of bustabit, there are chat commands where you can calculate the probability of your multiplier NOT busting. These are not padded probabilities, they're taken straight from datasets within the game. To calculate probability, you go in the SPAM chat channel and you issue a command like this: ```!prob 1.1``` and that would tell me the probability of rolling >= 1.1x is 89.9264%. Simply put, if I bet 10,000 bits (around $14.78 at the time of typing this), there is an 89.9264% chance of me getting $1.48 in profit. Obviously, this is very oversimplified, but you get the gist of it. For reference, a bit is a millionth of a bitcoin. It's a way of dividing a bitcoin into a smaller, simplified unit.

## What I'm trying to test
I want to test how much money you would gain **or lose** if you kept betting at a certain multiplier over a period of x amount of games. The creator of the website, Ryan, says the average time of a game (including wait time) is 30 seconds. So, we will be testing profit **or losses** over the course of 1,000 games, which is 30,000 seconds, or 8 hours and 20 minutes. So, this is if you left your computer running for this long, auto betting on a single multiplier. I want to find the most optimal multiplier.

## Probabilities of low multipliers
I will only be testing the following multipliers, and their probabilities are below
+ **1.05x**:
+ **1.05x**:
+ **1.05x**:
+ **1.05x**:
+ **1.05x**:
+ **1.05x**:
+ **1.05x**:
