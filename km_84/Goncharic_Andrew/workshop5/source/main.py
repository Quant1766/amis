import re
import matplotlib
import plotly
matplotlib.use('QT5Agg')
import numpy as np

import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly import tools


try:
    f = open('/Users/jbd/PycharmProjects/amis/km_84/Goncharic_Andrew/workshop5/source/bank-additional-full1.csv','r+',encoding='utf-8')
    keys = tuple(f.readline().strip().replace('"','').replace("'",'').split(','))
    print(keys)

    keys = [key.title() for key in keys]

    d = f.read().splitlines()#.strip().replace('"','').replace("'",'').splitlines()
except EOFError as fille_open_error:
    print("Check filepath or file: ", fille_open_error)

finally:
    f.close()

def getjob(row,index_key):
    try:
        res = re.findall(r'\w+.\w+',re.split(r',',row,maxsplit=index_key+1)[index_key])[0]
    except:
        res = None
    return res
def getphone(row):
    try:
        phone = re.findall(r'\+\d{9,11}',row)[0]
    except:
        phone = None
    return phone


def getAge(row,index_key):
    try:
        res = re.findall(r'\d+', re.split(r',', row, maxsplit=index_key + 1)[index_key])[0]
    except:
        res = None
        return res

def getMarital_status(row,index_key):
    try:
        res = re.findall(r'\w+.\w+',re.split(r',', row, maxsplit=index_key + 1)[index_key])[0]
    except:
        res = None
    finally:
        return res


def getAge(row,index_key):
    try:
        res = re.split(r',', row, maxsplit=index_key + 1)
        res = res[index_key]

        res = re.findall(r'\d+', res)[0]
        res = res if res else None
    except:
        res = None
    finally:
        return res


data  = {}


for i in range(len(d)):
    row = d[i].rstrip()
    if not row:
        print("Hollow row: ",i)
        continue
    job = getjob(row, list(keys).index('Job'))
    contact_phone = getphone(row)
    age = getAge(row,list(keys).index('Age'))
    marital_status = getMarital_status(row,list(keys).index('Marital'))
    try:
        data[job].append({contact_phone:{"age":age,
                            "marital status":marital_status
                            }}
                         )
    except:
        data[job] = [
            {contact_phone:{"age":age,
                            "marital status":marital_status
                            }}

        ]
def mat_plot():

    fig1,(ax1,ax2,ax3) = plt.subplots(1,3,sharey=True)
    ax1.plot(data.keys(),[len(d) for d in data.values()])


    ax2.bar(data.keys(),[len(d) for d in data.values()])

    ax3.pie(labels=data.keys(),x=[len(d) for d in data.values()])
    plt.show()


np_average_age = {i:[] for i in data.keys()}


for key in np_average_age:

    for val in  data[key]:
        age_ = list(val.values())[0]['age']
        if age_ is not None:
            age = int(age_)
        else:
            continue
        np_average_age[key].append(age)

np_average_age_ = {key:round(np.array(val).mean(),1) for key,val in np_average_age.items()}

# marital_job = {i:[] for i in data.keys()}

# for key in marital_job:
#
#     for val in  data[key]:
#
#         marital = list(val.values())[0]['marital']
#
#         np_average_age[key].append(age)
#

def plotly_graph():

    np_average_age = np.array(list(np_average_age_.values()))

    np_keys = np.array(list(data.keys()).copy())
    np_quntity_people_job = np.array([len(d) for d in data.values()])

    bar = go.Bar(
        x=np_keys,
        y=np_quntity_people_job,
        name="quntity people of job ",
    )
    pie = go.Pie(labels=np_keys,values=np_quntity_people_job)#,name="Pie")

    gra = go.Scatter(x=np_keys,y=np_average_age,name="AVERAGE age of proff")


    fig = tools.make_subplots(rows=2,cols=1)

    fig.append_trace(bar, 1,1)
    fig.append_trace(gra, 2,1)

    plotly.offline.plot(fig, filename='plotly.html')


    plotly.offline.plot([pie], filename='plotly_asd.html')



def plotly_try():
    np_average_age = np.array(list(np_average_age_.values()))

    np_keys = np.array(list(data.keys()).copy())
    np_quntity_people_job = np.array([len(d) for d in data.values()])

    bar = go.Bar(
        x=np_keys,
        y=np_quntity_people_job,
        name="quntity people of job ",
        # domain=dict(x=[0, 0.5])
    )


    gra = go.Scatter(x=np_keys, y=np_average_age, name="AVERAGE age of proff")


    data_ = [bar, gra]
    ann1 = dict(font=dict(size=20),
                showarrow=False,
                text='bar',
                x=0.500,
                y=0.50
                )
    ann2 = dict(font=dict(size=20),
                showarrow=False,
                text='gra',
                x=-20,
                y=-20
                )

    layout = go.Layout(title='Pie chart subplots',
                       annotations=[ann1, ann2],
                       )
    fig = go.Figure(data=data_, layout=layout)

    plotly.offline.plot(fig, filename='plotly_try.html')

plotly_graph()