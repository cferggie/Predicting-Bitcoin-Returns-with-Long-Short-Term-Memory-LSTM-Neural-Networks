Implement the following:
- hyperparameter optimization (learn to automate this process eventually)
- compare results to baseline performance (ARIMA, random walk simulation)

*There was a lot of work done, but i noticed the code was a bit messy and so I am redoing my approach to optimization that I previously had implemented

OG Scores from paper: 
    Model  Train RMSE  Test RMSE
    ARIMA    0.0355      0.0292
    LSTM     0.0056      0.0365

Inital RMSE from LSTM (once seed is added):
    train = 0.0066
    validation = 0.0436

Starting Hyper Parameters:
- Lookback = 12
- Hidden size = 1
- Num layers = 1
- Epochs = 1000
- Batch Size = 30
- Training Size = 70%


Training notes
    Issues: the rmse is misleading at times. The rmse will display a score of 0.363 for example, but the prediction will be a straight line         indicating high bias


    Epochs:
    Batch size:
    Regularization:
        - not needed
    
    Lookback:


    Hidden Size:
        - 1: underfit/high bias
        - 10: underfit/high bias
        - 20: underfit/high bias
            train RMSE 0.0358, validation RMSE 0.0177, test RMSE 0.0173
        - 30: 
            train RMSE 0.0328, validation RMSE 0.0175, test RMSE 0.0178
        - 40: 
            train RMSE 0.0231, validation RMSE 0.0287, test RMSE 0.0320
        - 50: 
            train RMSE 0.0288, validation RMSE 0.0178, test RMSE 0.0231
        - 60: 
            train RMSE 0.0237, validation RMSE 0.0210, test RMSE 0.0276

    Number of layers:

        
