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

    plt.title(attribute + ' trail0' + trial)
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


def summarize_significant_attributes(signif_attributes):
    '''
    This function prints tables that have computed the mean and variance for the 
    inputed significant attributes for all activties types
    Input:
        signif_attributes : a list of strings representing the selected 
                            significant attributes
    '''

    print('\n')
    activities = ['standing', 'sitting', 'jogging', 'arms chopping', 
                  'arms stretching', 'twisting']
    for activity in activities:
        print(activity)
        summary = activity_attribute_trends(activity)
        summary = summary.loc[signif_attributes]
        print(summary)
        print('\n')


def graph_signif_attributes(attributes, trial_num: int):
    '''
    This function graphs the significant attributes provided across all
    activities and saves the graphs into the Graphs folder within my lab
    directory, creating a new graph for each trial.

    Input:
        attributes: a list of strings representing the selected 
                    significant attributes
        trial_num (str): the number of trials being graphed
    '''
    for index in range(trial_num):
        trial = str(index + 1)
        for attribute in attributes:
            graph_attribute(attribute, trial)


def dif_controller_yposition(csv_file_1: str, csv_file_2: str, trial: str):
    '''
    This function graphs difference in the y psoition between the right and left
    controller as a function of time between two difference activities for one 
    trial and saves the graph into the Graphs folder within my lab directory.

    Input:
        csv_file_1 (str): the csv file of sensor data for the first activity being 
                    plotted
        csv_file_2 (str): the csv file of sensor data for the second activity being 
        plotted
        trial (str): the trial number being graphed
    '''

    file_name = '../Graphs/difference_in_controller_pos.y_trial0' + trial + '.png'
    f = open(file_name, 'w') # clear the file if there is existing data

    df1 = pd.read_csv(f'../Data/Lab1/{csv_file_1}', index_col=False)
    df2 = pd.read_csv(f'../Data/Lab1/{csv_file_2}', index_col=False)
    left1 = df1.loc[:,'controller_left_pos.y']
    right1 = df1.loc[:,'controller_right_pos.y']
    left2 = df2.loc[:,'controller_left_pos.y']
    right2 = df2.loc[:,'controller_right_pos.y']

    dif1 = []
    dif2 = []

    for index,value in enumerate(left1):
        dif1.append(left1[index] - right1[index])

    for index,value in enumerate(left2):
        dif2.append(left2[index] - right2[index])

    dif1 = pd.Series(dif1)
    dif2 = pd.Series(dif2)

    data = {
        'time' : df1.loc[:,'time'],
        csv_file_1 : dif1,
        csv_file_2 : dif2
    }

    accel_df = pd.DataFrame(data)
    accel_df.plot(x='time', y=[csv_file_1, csv_file_2])
    plt.ylabel('meters')
    plt.title('difference in controller position trial 0' + trial)
    plt.legend()
    plt.savefig(file_name)


signif_attr = ['controller_right_pos.y', 'controller_left_pos.y',
                'controller_right_pos.z', 'controller_left_pos.z', 
                'headset_pos.y', 'headset_pos.z']