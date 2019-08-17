def multiEventPlotter(dfxlst, title, col = "total", labels = None): 
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12,4))
    handles = []
    
    for idx, dfx in enumerate(dfxlst): 
        if labels != None:
            h, = plt.plot(dfx["time"],dfx[col], label = labels[idx])  
        else:
            h, = plt.plot(dfx["time"],dfx[col])
            
        handles.append(h)
        
    plt.grid()
    if labels != None: plt.legend(loc = 'best', handles = handles)
    plt.xticks(rotation='vertical')
    plt.title(title)
    plt.xlabel("time stamp")
    plt.ylabel("Energy Consumption (kW-h)")
    plt.show()