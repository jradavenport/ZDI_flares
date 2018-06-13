
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cm as CM
import matplotlib.colors as COL
from matplotlib import ticker

import pdb

# 5 continuous variables - x,y, color, area, symbol
# scatter plot

# Need to fix tick labels on both plots Notch, Magna
# Need to fix marker locations for verts in Notchplot -- see colorbar


areaRange = [100,240]
symRange = [3,8]
rotRange = [0.,0.5]
labelSize1 = 7
fontSize1 = 9
legendSize1 = 5


widthST = 3.45 #inches
heightST = 2.5875  # fig.set_figwidth assumes inches
Rect = (-0.04,-0.05,1,1) # makes the plot take up more of the plotting space



def MagnaPlot(xin,yin,colin,areain,symbin,
              cmap='Spectral_r',
              ax=None,
              xlims=None,
              ylims=None,
              xlabel="Period (days)",
              ylabel="Mass ($M_{\odot}$)",
              collabel="Shape: axisymmetry       Color: poloidal",
              arealabel="Size: $<B^{2}>$ (kG$^{2}$)",
              file=None,
              AbsCol=True,   # set color and symbol on 0-1 range, assumes inputs are in (0,1)
              AbsSym=True):


    if ax is None:
        fig, axis = plt.subplots()
    else:
        axis = ax
        fig = axis.get_figure()


    if AbsCol:
        colout = CM.ScalarMappable(norm=COL.Normalize(vmin=np.minimum(0,min(colin)),
                                                  vmax=np.maximum(max(colin),1)),
                               cmap=plt.get_cmap(cmap)).to_rgba
    else:
        colout = CM.ScalarMappable(norm=COL.Normalize(vmin=min(colin),
                                              vmax=max(colin)),
                           cmap=plt.get_cmap(cmap)).to_rgba

    areaout = COL.Normalize(vmin=min(areain),vmax=max(areain))(areain).data*(areaRange[1]-areaRange[0]) + areaRange[0]

    if AbsSym:
        symout = COL.Normalize(vmin=np.minimum(0,min(symbin)),vmax=np.maximum(max(symbin),1))(symbin).data*(symRange[1]-symRange[0]) + symRange[0]
    else:
        symout = COL.Normalize(vmin=min(symbin),vmax=max(symbin))(symbin).data*(symRange[1]-symRange[0]) + symRange[0]


    num = len(xin)

    fig.set_figwidth(widthST)
    fig.set_figheight(heightST)
    axis.tick_params(which='both',labelsize=labelSize1)
    
    axis.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))
    axis.xaxis.set_minor_locator(ticker.AutoMinorLocator(5))

    #pdb.set_trace()

    for i in range(num):
        poly = np.int(symout[i])
        marks = (poly,0,(symout[i] - poly)*360.)
        axis.scatter(xin[i],yin[i],c=colout(colin[i]),edgecolors='',s=areaout[i],alpha=0.8,marker=marks)


    axis.set_ylabel(ylabel,size=fontSize1)
    axis.set_xlabel(xlabel,size=fontSize1)

    axis.set_position([0.15,0.15,0.6,0.8])

    colAx = fig.add_axes([0.85,0.15,0.06,0.8])
    legAx = colAx.twinx()

    legAx.set_ylim([min(areain),max(areain)])

    if AbsCol:
        colAx.set_ylim([-0.1,1.1])
    else:
        colAx.set_ylim([min(colin),max(colin)])

    legAx.set_ylim([-0.1,1.1])


    colAx.set_xticklabels([])
    colAx.set_xticks([])

    colAx.tick_params(labelsize=legendSize1)
    legAx.tick_params(labelsize=legendSize1)


    legAx.tick_params(which='minor',labelsize=legendSize1)
    colAx.tick_params(which='minor',labelsize=legendSize1)

    legAx.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    colAx.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

    legAx.set_ylabel(arealabel,size=legendSize1,rotation=-90.,labelpad=10)
    colAx.set_ylabel(collabel,size=legendSize1,labelpad=3)

    legendx = np.ones(6)
    legendy = np.linspace(0,1,6)
    areasleg = legendy*(areaRange[1]-areaRange[0]) + areaRange[0]
    symsleg = legendy*(symRange[1]-symRange[0]) + symRange[0]

    legy = legAx.get_yticks()
    #pdb.set_trace()

    legAx.set_yticklabels(legy*(max(areain) - min(areain)) + areain[0])

    numleg = len(legendx)

    for j in range(numleg):
        poly = np.int(symsleg[j])
        legmark = (poly,0,(symsleg[j] - poly)*360.)
        colAx.scatter(legendx[j],legendy[j],c=colout(legendy[j]),marker=legmark,edgecolors='',s=areasleg[j])

    if xlims is not None:
        axis.set_xlim(xlims)

    if ylims is not None:
        axis.set_ylim(ylims)

    #fig.set_tight_layout({'rect':Rect})

    if file is not None:
        fig.savefig(file)

    return fig, axis




def NotchPlot(xin,yin,colin,areain,rotin,
              cmap='Spectral_r',
              ax=None,
              xlims=None,
              ylims=None,
              xlabel="Period (days)",
              ylabel="Mass ($M_{\odot}$)",
              collabel="Rotation: axisymmetry       Color: poloidal",
              arealabel="Size: $<B^{2}>$ (kG$^{2}$)",
              file=None,
              AbsCol=True,   # set color and symbol on 0-1 range, assumes inputs are in (0,1)
              AbsRot=True):

    if ax is None:
        fig, axis = plt.subplots()
    else:
        axis = ax
        fig = axis.get_figure()


    if AbsCol:
        colout = CM.ScalarMappable(norm=COL.Normalize(vmin=np.minimum(0,min(colin)),
                                                  vmax=np.maximum(max(colin),1)),
                               cmap=plt.get_cmap(cmap)).to_rgba
    else:
        colout = CM.ScalarMappable(norm=COL.Normalize(vmin=min(colin),
                                              vmax=max(colin)),
                           cmap=plt.get_cmap(cmap)).to_rgba

    areaout = COL.Normalize(vmin=min(areain),vmax=max(areain))(areain).data*(areaRange[1]-areaRange[0]) + areaRange[0]

    if AbsRot:
        rotout = COL.Normalize(vmin=np.minimum(0,min(rotin)),vmax=np.maximum(max(rotin),1))(rotin).data * (0.5)
    else:
        rotout = COL.Normalize(vmin=min(rotin),vmax=max(rotin))(rotin).data * (0.5) 

    num = len(xin)

    fig.set_figwidth(widthST)
    fig.set_figheight(heightST)
    axis.tick_params(which='both',labelsize=labelSize1)
    
    axis.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))
    axis.xaxis.set_minor_locator(ticker.AutoMinorLocator(5))

    #pdb.set_trace()

    for i in range(num):
        theta = np.linspace(0,2*np.pi,1000)
        radius = 50   # seems arbitrary?
        verts = np.zeros((len(theta),2))
        verts = np.column_stack([radius * np.cos(theta), radius * np.sin(theta)])

        phase = rotout[i]
        shift = np.int(phase*len(theta))
        verts[shift,:] = [radius*2.5 * np.cos(2*np.pi*phase),radius*2.5*np.sin(2*np.pi*phase)]

        axis.scatter(xin[i],yin[i],c=colout(colin[i]),edgecolors=colout(colin[i]),s=areaout[i],alpha=0.6,verts=verts)

    axis.set_ylabel(ylabel,size=fontSize1)
    axis.set_xlabel(xlabel,size=fontSize1)

    axis.set_position([0.15,0.15,0.6,0.8])

    colAx = fig.add_axes([0.85,0.15,0.06,0.8])
    legAx = colAx.twinx()

    legAx.set_ylim([min(areain),max(areain)])

    if AbsCol:
        colAx.set_ylim([-0.1,1.1])
    else:
        colAx.set_ylim([min(colin),max(colin)])

    legAx.set_ylim([-0.1,1.1])

    colAx.set_xticklabels([])
    colAx.set_xticks([])

    colAx.tick_params(labelsize=legendSize1)
    legAx.tick_params(labelsize=legendSize1)

    legAx.tick_params(which='minor',labelsize=legendSize1)
    colAx.tick_params(which='minor',labelsize=legendSize1)

    legAx.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    colAx.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

    legAx.set_ylabel(arealabel,size=legendSize1,rotation=-90.,labelpad=10)
    colAx.set_ylabel(collabel,size=legendSize1,labelpad=3)

    legendx = np.ones(6)
    legendy = np.linspace(0,1,6)
    areasleg = legendy*(areaRange[1]-areaRange[0]) + areaRange[0]
    rotleg = legendy*(rotRange[1]-rotRange[0]) + rotRange[0]

    legy = legAx.get_yticks()
    #pdb.set_trace()

    legAx.set_yticklabels(legy*(max(areain) - min(areain)) + areain[0])

    numleg = len(legendx)

    for i in range(numleg):
        theta = np.linspace(0,2*np.pi,1000)
        radius = 50   # seems arbitrary?
        verts = np.zeros((len(theta),2))
        verts = np.column_stack([radius * np.cos(theta), radius * np.sin(theta)])

        phase = rotleg[i]
        shift = np.int(phase*len(theta))
        verts[shift,:] = [radius*2.5 * np.cos(2*np.pi*phase),radius*2.5*np.sin(2*np.pi*phase)]
        colAx.scatter(legendx[i],legendy[i],c=colout(legendy[i]),edgecolors=colout(legendy[i]),s=areaout[i],
                                            alpha=0.6,verts=verts)
#    for j in range(numleg):
#        poly = np.int(symsleg[j])
#        legmark = (poly,0,(symsleg[j] - poly)*360.)
#        colAx.scatter(legendx[j],legendy[j],c=colout(legendy[j]),marker=legmark,edgecolors='',s=areasleg[j])

    if xlims is not None:
        axis.set_xlim(xlims)

    if ylims is not None:
        axis.set_ylim(ylims)

    #fig.set_tight_layout({'rect':Rect})

    if file is not None:
        fig.savefig(file)

    return fig,axis





