Implement the following:
- training size optimization
- compare results to baseline performance (ARIMA, random walk simulation)
- 

ps: inital RMSE from LSTM
    train = 0.0066
    validation = 0.0436

Initial RMSE from LSTM w/ regularization
    train: 0.0368
    test: 0.0291

Training notes
    Regularization:
        - looped through lambda values from 0.10 to 1 and found that 0.10 led to the smallest validation RMSE