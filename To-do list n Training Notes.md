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
    - 1, severe high bias
    - 2, high bias persists
    - 5, high bias
    - 8, 
        train RMSE 0.0314, validation RMSE 0.0190, test RMSE 0.0204
    - 9, 
        train RMSE 0.0320, validation RMSE 0.0190, test RMSE 0.0189
    - 11, 
        train RMSE 0.0320, validation RMSE 0.0190, test RMSE 0.0189
    - 12, ****
      train RMSE 0.0328, validation RMSE 0.0175, test RMSE 0.0178
    - 13, 
        train RMSE 0.0328, validation RMSE 0.0175, test RMSE 0.0178
    - 14, 
        train RMSE 0.0321, validation RMSE 0.0182, test RMSE 0.0198

    Hidden Size:
        - 1: underfit/high bias
        - 10: underfit/high bias
        - 20: underfit/high bias
            train RMSE 0.0358, validation RMSE 0.0177, test RMSE 0.0173
        - 30: ****LOWEST VALIDATION SCORE
            train RMSE 0.0328, validation RMSE 0.0175, test RMSE 0.0178
        - 40: 
            train RMSE 0.0231, validation RMSE 0.0287, test RMSE 0.0320
        - 50: 
            train RMSE 0.0288, validation RMSE 0.0178, test RMSE 0.0231
        - 60: 
            train RMSE 0.0237, validation RMSE 0.0210, test RMSE 0.0276
        - 70:
           train RMSE 0.0219, validation RMSE 0.0228, test RMSE 0.0324 
        - 80:
            train RMSE 0.0167, validation RMSE 0.0264, test RMSE 0.0312
        - 90:
            train RMSE 0.0211, validation RMSE 0.0247, test RMSE 0.0305
        - 100:
            train RMSE 0.0119, validation RMSE 0.0395, test RMSE 0.0329
        - 110:
            train RMSE 0.0193, validation RMSE 0.0195, test RMSE 0.0318
        - 120:
            train RMSE 0.0036, validation RMSE 0.0280, test RMSE 0.0409



    Number of layers:

        
