var baseBet = 100;
var cashout;
var mult;
cashout = 1.7;
greed_percent = 18;

if (!mult)
    mult = cashout / (cashout - 1) * (1 + greed_percent/100);
else if (!cashout)
    cashout = mult / (mult - 1) * (1 + greed_percent/100);

var satoshis = baseBet * 100;
var crash = Math.floor(cashout*100 + 1e-6);

var currentBet = false;

engine.on('game_starting', function () {
    if (currentBet && engine.lastGamePlay() === 'LOST')
        currentBet *= mult;
    else
        currentBet = satoshis;

    if (currentBet < engine.getBalance()) {
        console.log('place bet of', Math.round(currentBet/100), 'at', crash/100);
        engine.placeBet(Math.round(currentBet/100)*100, crash, false);
    }
    else {
        engine.stop();
        console.log('You ran out of bits :(');
    }
});
