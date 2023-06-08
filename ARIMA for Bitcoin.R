library('xts')
library('readr')
library('urca')

data = read.csv("C:/Users/Owner/Documents/Predicting Crypto Prices via Senitment Analysis/BTC-USD.csv")

#log data
y = ts(log(data$Close[1:365]), start=c(2022,1), frequency=365)

plot(y)

#create test train set
train = y[1:244] #good to go
test = y[245:365]

#Create ARIMA
library(forecast)

final=Arima(train, order=c(1,1,1), include.mean = T)

plot(train, type="l", 
     xlab = "Time Step",
     ylab = "Log Returns of Bitcoin")
lines(final$fitted, col="red")
abline( h=0, lty=2)

accuracy(final)

#Predict
test_ARIMA = Arima(test, model=final)

y_hat_test = test_ARIMA$fitted


plot(diff(test), type="l", 
     xlab = "Time Step",
     ylab = "Log Returns of Bitcoin")
lines(diff(y_hat_test), col="red")
abline( h=0, lty=2)
legend("topright", legend = c("Actual Values", "Predicted Values"), col = c("black", "red"), lty = 1, bty = "n")

accuracy(test_ARIMA)
