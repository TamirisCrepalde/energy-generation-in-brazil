import pandas as pd
import numpy as np
from typing import Union, Callable
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid', {'grid.color': '.6', 'grid.linestyle': ':'})
sns.set_palette('pastel')

def lineplot(df:pd.DataFrame,
             x:str,
             y:str,
             df_twin:pd.DataFrame=None,
             hue:str=None,
             style:str=None,
             size:str=None,
             sizes:tuple=(2, 2.5),
             # palette:str='pastel',
             estimator:Callable=sum,
             err_style:str=None,
             rotate:bool=False,
             figsize:tuple=(15,10),
             twinx:bool=False,
             xlabel:str=None,
             ylabel:str=None,
             ylabeltwin:str=None,
             ylim:tuple=None,
             title:str=None
            ):
    
    fig, axes = plt.subplots(1, 1, figsize=figsize)
    
    axes.set_xlabel(xlabel);
    axes.set_ylabel(ylabel);
    axes.set_ylim(ylim);
    plt.suptitle(title);

    sns.lineplot(
        ax=axes,
        data=df.reset_index(),
        x=x,
        y=y,
        hue=hue,
        # palette=palette,
        size=size,
        sizes=sizes,
        estimator=estimator,
        err_style=err_style
    );
    
    if twinx is True:
        axes1 = axes.twinx()
        
        axes1.set_ylabel(ylabeltwin);
        axes1.set_ylim(ylim);        

        sns.lineplot(
            ax=axes1,
            data=df_twin.reset_index(),
            x=x,
            y=y,
            style=style,
            hue=hue,
            size=size,
            sizes=sizes,
            estimator=estimator,
            err_style=err_style
        );
    
    if rotate is True:
        plt.xticks(rotation=45);
    
    
def barplot(df:pd.DataFrame,
            x:str,
            y:str,
            hue:str=None,
            estimator:Callable=sum,
            ci:str=None,
            dodge:bool=True,
            rotate:bool=False,
            order:Union[list, str]=None,
            figsize:tuple=(15,10),
            xlabel:str=None,
            ylabel:str=None,
            ylim:tuple=None,
            title:str=None
           ):
    
    plt.figure(figsize=figsize)
    
    ax = sns.barplot(
        data=df.reset_index(), 
        x=x, 
        y=y,
        dodge=dodge,
        hue=hue,
        order=order,
        estimator=estimator,
        ci=ci
        );

    if rotate is True:
        plt.xticks(rotation=45);
        
    ax.set_ylabel(xlabel);
    ax.set_ylabel(ylabel);
    ax.set_ylim(ylim);
    plt.suptitle(title);
    