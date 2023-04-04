# Mobile Computing Lab 1 Data Analysis
#
# Alexis Elliott

import glob

import pandas as pd

import matplotlib.pyplot as plt

def summarize_sensor_trace(csv_file: str):
    '''
    This function computes the mean and variance of each of the 36 sensor 
    attributes in a given by a provide CSV file. 

    Inputs:
        csv_file (str): a string specifying the trial specific CSV file to be 
                        summarized
    
    Returns:
        A dataframe containing the mean and variance of each attribute
    '''

    df = pd.read_csv(f'../Data/Lab1/{csv_file}', index_col=False)

    data = {
        "mean": df.mean(),
        "variance": df.var()
    }

    ret = pd.DataFrame(data)
    ret = ret.drop('time')
    print(ret)


def visualize_sensor_trace(csv_file: str, attribute: str):
    '''
    This function graphs a dimension of an attribute's value 
    (e.g. controller_left_vel.x) as a function of time for a given CSV file. 

    Inputs:
        csv_file (str): the trial specific CSV file to be summarized
        attribute (str): the attribite to be graphed (e.g. controller_left_vel.x)

    Returns:
        Graphs the given atrribute for the provided CSV files as a function of
        time
    '''

    df = pd.read_csv(f'../Data/Lab1/{csv_file}', index_col=False)

    df.plot(x="time", y=attribute)
    plt.show()


# Define additional functions as needed here!

def activity_attribute_trends(activity: str):
    '''
    This function makes a dataset that averages each of the attribute values
    across all trials for a given activity

    Input:
        activity (str): the activity to be summarized
    
    Returns:
        a dataframe with the average mean and variance for all attribute values
        for the given activity
    '''

    activities = {
        'standing': 'STD',
        'sitting': 'SIT',
        'jogging': 'JOG',
        'arms chopping': 'CHP',
        'arms stretching': 'STR',
        'twisting': 'TWS'
    }

    files = glob.glob(f'../Data/Lab1/{activities[activity.lower()]}*')

    mean = pd.read_csv(files[1], index_col=False).mean()
    var = pd.read_csv(files[1], index_col=False).var()

    for file in files:
        df = pd.read_csv(file, index_col=False)
        temp1 = df.mean()
        temp2 = df.var()
        mean = pd.concat([mean, temp1], axis=1)
        var = pd.concat([mean, temp2], axis=1)
    
    mean = mean.mean(axis=1).drop('time')
    var = var.mean(axis=1).drop('time')

    ret = pd.concat([mean, var], axis=1, keys=['mean', 'variance'])
    
    print(ret)
        

#summarize_sensor_trace('STD_01.csv')
#visualize_sensor_trace('STD_01.csv', 'headset_rot.x')