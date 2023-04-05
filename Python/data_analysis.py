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
        summary: A dataframe containing the mean and variance of each attribute
    '''

    df = pd.read_csv(f'../Data/Lab1/{csv_file}', index_col=False)

    data = {
        "mean": df.mean(),
        "variance": df.var()
    }

    summary = pd.DataFrame(data)
    summary = summary.drop('time')
    return summary


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

    # set y-axis unit
    if 'rot' in attribute:
        y_axis = 'degrees'
    elif 'pos' in attribute:
        y_axis = 'meters'
    elif 'angularVel' in attribute:
        y_axis = 'radians/second'
    else: 
        y_axis = 'meters/second'
    plt.ylabel(y_axis)

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
        var = pd.concat([var, temp2], axis=1)
    
    mean = mean.mean(axis=1).drop('time')
    var = var.mean(axis=1).drop('time')

    summary = pd.concat([mean, var], axis=1, keys=['mean', 'variance'])
    
    return summary


def graph_all_attributes(csv_file: str):

    '''
    This function takes a csv file for a specific activity and trial. It then
    graphs each attribute as a function of time and saves the graph as a png
    file within the Graphs folder in my lab directory

    Input:
        csv_file (str): the trial specific CSV file that graphs will be 
                        generated for
    '''

    df = pd.read_csv(f'../Data/Lab1/{csv_file}', index_col=False)

    df.plot(x="time", y='headset_vel.x')

    for column in df:
        if column == 'time':
            continue
        file_name = '../Graphs/' + csv_file[0:6] + '_' + column + '.png'
        f = open(file_name, 'w') # clear the file if there is existing data
        df.plot(x="time", y=column)
        plt.title(column)
        plt.savefig(file_name)
        plt.close()

def graph_attribute(attribute: str, trial: str):

    '''
    This function graphs a specifc attribute (eg. 'headset_rot.y') for a 
    specific trial number and plots all 6 activity types. The graph
    is then saved as a png file within the Graphs folder in my lab directory

    Input:
        attribute (str): the attribute being plotted (eg. 'headset_rot.y')
        trial (str): the trial number being plotted (eg. '1')
    '''

    files = glob.glob(f'../Data/Lab1/*{trial}*')
    file_name = '../Graphs/' + attribute + '_all_trial0' + trial + '.png'
    f = open(file_name, 'w') # clear the file if there is existing data

    df1 = pd.read_csv(files[0], index_col=False)
    df2 = pd.read_csv(files[1], index_col=False)
    df3 = pd.read_csv(files[2], index_col=False)
    df4 = pd.read_csv(files[3], index_col=False)
    df5 = pd.read_csv(files[4], index_col=False)
    df6 = pd.read_csv(files[5], index_col=False)

    plt.plot(df1['time'], df1[attribute], label = files[0])
    plt.plot(df2['time'], df2[attribute], label = files[1])
    plt.plot(df3['time'], df3[attribute], label = files[2])
    plt.plot(df4['time'], df4[attribute], label = files[3])
    plt.plot(df5['time'], df5[attribute], label = files[4])
    plt.plot(df6['time'], df6[attribute], label = files[5])

    plt.title(attribute)
    plt.xlabel('time')
    # set y-axis unit
    if 'rot' in attribute:
        y_axis = 'degrees'
    elif 'pos' in attribute:
        y_axis = 'meters'
    elif 'angularVel' in attribute:
        y_axis = 'radians/second'
    else: 
        y_axis = 'meters/second'
    plt.ylabel(y_axis)
    plt.legend()
    plt.savefig(file_name)
    plt.close()

def graph_all_attributes(trial: str):
    '''
    This graphs all attributes for a given trial number and saves them all
    as png files within the Graph folder in my lab directory

    Input:
        trial (str): the trial number being plotted (eg. '1')
    '''

    attributes = ['headset_vel.x', 'headset_vel.y', 'headset_vel.z', 
                'headset_angularVel.x', 'headset_angularVel.y', 
                'headset_angularVel.z', 'headset_pos.x', 'headset_pos.y',
                'headset_pos.z', 'headset_rot.x', 'headset_rot.y', 'headset_rot.z'
                , 'controller_left_vel.x', 'controller_left_vel.y', 
                'controller_left_vel.z', 'controller_left_angularVel.x', 
                'controller_left_angularVel.y', 'controller_left_angularVel.z',
                'controller_left_pos.x', 'controller_left_pos.y', 
                'controller_left_pos.z', 'controller_left_rot.x', 
                'controller_left_rot.y', 'controller_left_rot.z',
                'controller_right_vel.x', 'controller_right_vel.y',
                'controller_right_vel.z', 'controller_right_angularVel.x',
                'controller_right_angularVel.y', 'controller_right_angularVel.z',
                'controller_right_pos.x', 'controller_right_pos.y', 
                'controller_right_pos.z', 'controller_right_rot.x', 
                'controller_right_rot.y', 'controller_right_rot.z']
    for attribute in attributes:
        graph_attribute(attribute, trial)

graph_all_attributes('1')


# graph_all_attributes('STD_01.csv')
# graph_all_attributes('SIT_01.csv')
# graph_all_attributes('JOG_01.csv')
# graph_all_attributes('CHP_01.csv')
# graph_all_attributes('STR_01.csv')
# graph_all_attributes('TWS_01.csv')
        

#summarize_sensor_trace('STD_01.csv')

# visualize_sensor_trace('STD_01.csv', 'headset_rot.y')
# visualize_sensor_trace('STD_01.csv', 'headset_rot.x')

# tws1 = summarize_sensor_trace('TWS_01.csv')
# chp1 = summarize_sensor_trace('CHP_01.csv')
# print(tws1)
# print(chp1)

# print("standing")
# print(activity_attribute_trends("standing"))
# print("sitting")
# print(activity_attribute_trends("sitting"))
# print("jogging")
# print(activity_attribute_trends("jogging"))
# print("arms chopping")
# print(activity_attribute_trends("arms chopping"))
# print("arms stretching")
# print(activity_attribute_trends("arms stretching"))
# print("twisting")
# print(activity_attribute_trends("twisting"))
