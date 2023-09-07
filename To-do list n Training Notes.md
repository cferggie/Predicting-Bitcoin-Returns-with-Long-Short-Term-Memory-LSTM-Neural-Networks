Implement the following:
- training size optimization
- compare results to baseline performance (ARIMA, random walk simulation)

OG Scores from paper: 

Model  Train RMSE  Test RMSE

ARIMA    0.0355      0.0292

LSTM     0.0056      0.0365

Inital RMSE from LSTM:
    train = 0.0066
    validation = 0.0436

RMSE from LSTM w/ regularization
    train: 0.0368
    test: 0.0291

Training notes
    Regularization:
        - looped through lambda values from 0.10 to 1 and found that 0.10 led to the smallest validation RMSE
        - looped through 0.01 to 1 
        - chose 0.01 which gave the lowest RMSE
        *Process was successful, but there is probably a more efficient method to finding the optimal lambda
