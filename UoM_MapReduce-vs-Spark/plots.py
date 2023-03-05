import matplotlib.pyplot as plt
import numpy as np

q1_mapreduce_time = [
    22.522,
    16.835,
    11.898,
    11.678,
    16.203
]
q1_spark_time = [
    13755,
    12904,
    991,
    766,
    776
]

q2_mapreduce_time = [
    15.307,
    12.25,
    12.2,
    12.999,
    10.848
]
q2_spark_time = [
    12604,
    1033,
    679,
    724,
    654
]

q3_mapreduce_time = [
    15.62,
    11.899,
    15.05,
    13.9,
    16.217
]
q3_spark_time = [
    12609,
    886,
    688,
    710,
    751
]

q4_mapreduce_time = [
    11.978,
    16.291,
    11.385,
    11.049,
    16.301
]
q4_spark_time = [
    12984,
    975,
    745,
    602,
    675
]

q5_mapreduce_time = [
    15.356,
    13.455,
    11.459,
    11.461,
    15.126
]
q5_spark_time = [
    12468,
    1062,
    648,
    682,
    585
]

def plotify(list1, list2, title):
    list2 = [x / 1000 for x in list2]

    fig, ax = plt.subplots()

    x_values = np.arange(len(list1))

    ax.bar(x_values - 0.2, list1, color='b', width=0.4)
    ax.bar(x_values + 0.2, list2, color='g', width=0.4)

    ax.set_xlabel('Number of iterations')
    ax.set_ylabel('Running time (s)')
    ax.set_title(title)
    ax.legend(['Hadoop', 'Spark'])

    plt.savefig(f'{title}.png', format='png')


if __name__ == '__main__':
    plotify(q1_mapreduce_time, q1_spark_time, 'CarrierDelay')
    plotify(q2_mapreduce_time, q2_spark_time, 'NASDelay')
    plotify(q3_mapreduce_time, q3_spark_time, 'WeatherDelay')
    plotify(q4_mapreduce_time, q4_spark_time, 'LateAircraftDelay')
    plotify(q5_mapreduce_time, q5_spark_time, 'SecurityDelay')

    def avg(lst):
        return sum(lst) / len(lst)

    average_mapreduce = [
        avg(q1_mapreduce_time),
        avg(q2_mapreduce_time),
        avg(q3_mapreduce_time),
        avg(q4_mapreduce_time),
        avg(q5_mapreduce_time),
    ]

    average_spark = [
        avg(q1_spark_time),
        avg(q2_spark_time),
        avg(q3_spark_time),
        avg(q4_spark_time),
        avg(q5_spark_time),
    ]

    average_spark = [i / 1000 for i in average_spark]

    avg_list = [
        'CarrierDelay',
        'NASDelay',
        'WeatherDelay',
        'LateAircraftDelay',
        'SecurityDelay'
    ]

    fig, ax = plt.subplots()

    x_values = np.arange(len(avg_list))

    ax.bar(x_values - 0.2, average_mapreduce, color='b', width=0.4)
    ax.bar(x_values + 0.2, average_spark, color='g', width=0.4)

    # ax.set_xlabel('Number of iterations')
    # ax.set_ylabel('Running time (s)')
    ax.set_title('Time taken by')
    ax.legend(['Hadoop', 'Spark'])

    ax.set_xticks(x_values, avg_list, rotation=15)

    plt.savefig(f'average.png', format='png')
