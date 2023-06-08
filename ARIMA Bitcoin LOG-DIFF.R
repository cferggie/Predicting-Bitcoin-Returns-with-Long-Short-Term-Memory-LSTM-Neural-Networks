library('xts')
library('readr')
library('urca')

data = read.csv("C:/Users/Owner/Documents/Predicting Crypto Prices via Senitment Analysis/BTC-USD.csv")

#log data
y = ts(log(data$Close[1:365]), start=c(2022,1), frequency=365)

plot.ts(y)

#diff
y = diff(y)

plot.ts(y)

#create test train set
train = y[1:243] #good to go
test = y[244:364]

#create the model
final=Arima(train, order=c(1,0,1), include.mean = T)

plot(train, type="l", 
     xlab = "Time Step",
     ylab = "Log Returns of Bitcoin")
lines(final$fitted, col="red")
abline( h=0, lty=2)

accuracy(final)
#predict
test_ARIMA = Arima(test, model=final)

accuracy(test_ARIMA)

plot(test, type="l", 
     xlab = "Time Step",
     ylab = "Log Returns of Bitcoin")
lines(test_ARIMA$fitted, col="red")
abline( h=0, lty=2)
legend("topright", legend = c("Actual Values", "Predicted Values"), col = c("black", "red"), lty = 1, bty = "n")






