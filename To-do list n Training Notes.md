Implement the following:
- hyperparameter optimization (learn to automate this process eventually)
- compare results to baseline performance (ARIMA, random walk simulation)
- multiply log-diff by 100 to get % change

OG Scores from paper: 
    Model  Train RMSE  Test RMSE
    ARIMA    0.0355      0.0292
    LSTM     0.0056      0.0365

Inital RMSE from LSTM (once seed is added):
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

        Chosen: 0.0000001
    Lookback:
        - 10, train RMSE 0.0369, validation RMSE 0.0294
        - 11, train RMSE 0.0369, validation RMSE 0.0295
        - 12, train RMSE 0.0370, validation RMSE 0.0265 *Chosen level
        - 13, train RMSE 0.0371, validation RMSE 0.0265
        - 14, train RMSE 0.0371, validation RMSE 0.0267
        - 15, train RMSE 0.0372, validation RMSE 0.0269
        - 20, train RMSE 0.0368, validation RMSE 0.0267 **Increasing seems to reduce RMSE for some reason
        - 25, train RMSE 0.0370, validation RMSE 0.0272 
        - 30, train RMSE 0.0375, validation RMSE 0.0275
        - 40, train RMSE 0.0374, validation RMSE 0.0188

        *Anything below 10 leads to non-convergence
        *I do worry that as the lookback size gets bigger, the number of predictions the model makes is lower. Is this something to consider?

    Hidden Size:
        - 1, train RMSE 0.0369, validation RMSE 0.0264 **********
             train RMSE 0.0371, validation RMSE 0.0263
             train RMSE 0.0370, validation RMSE 0.0262
             train RMSE 0.0370, validation RMSE 0.0264

        - 2, train RMSE 0.0369, validation RMSE 0.0268 (straight line basically, until epoch was increased to 1000)
        - 3, train RMSE 0.0372, validation RMSE 0.0266
        - 4, train RMSE 0.0371, validation RMSE 0.0267
        - 5, train RMSE 0.0369, validation RMSE 0.0267
        - 6, train RMSE 0.0369, validation RMSE 0.0265
        - 7, train RMSE 0.0369, validation RMSE 0.0266
        - 8, train RMSE 0.0369, validation RMSE 0.0265
        - 9, train RMSE 0.0369, validation RMSE 0.0266
        - 10, train RMSE 0.0371, validation RMSE 0.0266 
        - 20, train RMSE 0.0371, validation RMSE 0.0267
        - 30, train RMSE 0.0371, validation RMSE 0.0266
        - 40, train RMSE 0.0371, validation RMSE 0.0267
        - 50, train RMSE 0.0371, validation RMSE 0.0267
        - 60, train RMSE 0.0371, validation RMSE 0.0267
        - 70, train RMSE 0.0371, validation RMSE 0.0267
        - 80, train RMSE 0.0371, validation RMSE 0.0267
        - 90, train RMSE 0.0371, validation RMSE 0.0267
        - 100, train RMSE 0.0371, validation RMSE 0.0267
        - 200, train RMSE 0.0371, validation RMSE 0.0267
    
    Number of layers:
    - 1, train RMSE 0.0369, validation RMSE 0.0265 *Num of layers selected
    - 2, train RMSE 0.0369, validation RMSE 0.0265
    - 3, train RMSE 0.0370, validation RMSE 0.0272
    - 4, DOESNT WORK
    - 5, DOESNT WORK
        
