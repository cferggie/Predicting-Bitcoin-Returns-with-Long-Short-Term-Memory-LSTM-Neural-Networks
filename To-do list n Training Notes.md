Implement the following:
- optimize lambda
- training size optimization
- compare results to baseline performance (ARIMA, random walk simulation)

OG Scores from paper: 
    Model  Train RMSE  Test RMSE
    ARIMA    0.0355      0.0292
    LSTM     0.0056      0.0365

Inital RMSE from LSTM:
    train = 0.0066
    validation = 0.0436

Training notes
    Regularization:
        - looped through lambda values from 0.10 to 1 and found that 0.10 led to the smallest validation RMSE
        - noticed that the predictions were a straight line. Lambda too high?
        - lambda was too high (suggests underfitting)
        - 0.0000001 seems to be small enough to get the model out of the underfitting rut
        - anything larger than 0.0000005 will lead to straight line predictions
        - current loss found in regularization notes seems to be the minimum loss given by regularization
    Lookback:
        - 1, train RMSE 0.0363, validation RMSE 0.0280
        - 2, train RMSE 0.0364, validation RMSE 0.0280
        - 3, train RMSE 0.0365, validation RMSE 0.0279 *******
        - 4, train RMSE 0.0364, validation RMSE 0.0281 
        - 5, train RMSE 0.0366, validation RMSE 0.0281
        - 6, train RMSE 0.0367, validation RMSE 0.0281
        - 7, train RMSE 0.0366, validation RMSE 0.0284
        - 8, train RMSE 0.0365, validation RMSE 0.0289
        - 9, train RMSE 0.0364, validation RMSE 0.0294
        - 10, train RMSE 0.0369, validation RMSE 0.0294
        
