from django.shortcuts import render

from django.http import HttpResponse

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import numpy as np

import showinfo.models as showinfoModel


def index(request):
    # return "imagepage.html"
    return render(request, 'showinfo/imagepage.html')

# 绘制表格
def genmat1(request):
    nowdatelist = showinfoModel.Ordernums.objects.filter(orderdate='2017-10-17')

    x=[]
    y=[]
    for vars in nowdatelist:
        x.append(vars.warehouseno)
        y.append(vars.ordernum)

    fig=Figure(figsize=(6,6))
    ax=fig.add_subplot(111)
    ax.bar(x, y)
    canvas=FigureCanvasAgg(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(fig)
    return response

def genmat2(request):
    nowdatelist = showinfoModel.Ordernums.objects.filter(orderdate='2017-10-17')
    predatelist = showinfoModel.Ordernums.objects.filter(orderdate='2017-10-16')

    x = np.arange(4)
    y1 = []
    y2 = []
    xticks = []
    for vars in nowdatelist:
        y1.append(vars.ordernum)
        xticks.append(vars.warehouseno)
    for vars in predatelist:
        y2.append(vars.ordernum)

    fig=Figure(figsize=(6,6))
    ax=fig.add_subplot(111)
    bar_width = 0.35
    ax.bar(x, y1, bar_width, label='10-17')
    ax.bar(x+bar_width, y2, bar_width, label='10-16')
    ax.set_xticks(x+bar_width/2)
    ax.set_xticklabels(xticks)


    canvas=FigureCanvasAgg(fig)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(fig)
    return response
