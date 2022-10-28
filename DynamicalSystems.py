import matplotlib.pyplot as plt
import numpy as np

# Continuous Dynamical Systems

def biff(q, rmin, rmax, stability, dr = 1e-4):
    """
        This function plots a biffrucation diagram of any single parameter
        family given a parameter interval [rmin, rmax] overwich the system 
        is either stable "s" or unstable "u". 
        
        If inputed wrong: nothing happens. 
        
        q must be a function of r
    """

    if(stability == "s" or stability =="u"):
        r = np.arange(rmin, rmax + dr, dr)
        if(stability == "s"):
            plt.plot(r, q(r), "r")
        elif(stability == "u"):
            plt.plot(r, q(r), "r--")
        return
    else:
        return
        

# Discrete Dynamical Systems
        
def iterate(f, x0, r, iterations, skip, xmin = 0, xmax = 1):
    """
        Iterates a map f(r,x) until it settles and plots the result
    """
    X_n=[]
    N=[]
    n=0
    x = x0;
    # Iterate the function until it settles.
    
    for i in range(iterations + skip):
        if i >= skip:
            X_n.append(x)
            N.append(n)
            n+=1
            x = f(r, x);
            # Configure and decorate the plot
    plt.figure()
    plt.grid()
    plt.plot(N, X_n)
    plt.ylim(xmin, xmax)
    plt.xlim(0, N[-1])
    plt.title("Iteration Diagram")
    plt.xlabel("$n$")
    plt.ylabel("$x_{n}$")
    plt.show()
    return


def cweb(f, xmin = 0, xmax = 1, x0=0.1, iterations=50):
    """ Plot a cobweb graph using the equation:
        x(n+1) = f(x(n))
    
        It iterates the plot to the number specified (initalized to 50). 

        The default value of x0 is 0.1 and it must 
        be in the interval ]xmin, xmax[ which are initialized to 0 and 1
    """

    # If x0 isn't in the specified interval, stop 
    if x0 <= xmin or x0 >= xmax: return
    
    plt.figure()
    plt.title("Cobweb Plot for x0 = " + str(x0))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.grid()

    # Plot y = f(x)
    dx = 1e-6
    X = np.arange(xmin, xmax + dx, dx)
    plt.plot(X, f(X), color="black", label="$f(x)$")

    # Plot y = x
    plt.plot([xmin, xmax], [xmin, xmax], color="red", label = "$x$")
    #"""
    # Plot Cobweb
    last_x, last_y = x0, 0
    for _ in range(iterations):
        next_x = f(last_x)
        # Plot vertical line 
        plt.plot([last_x, last_x], [last_y, next_x], color="blue")
        # Plot horizontal line
        plt.plot([last_x, next_x], [next_x, next_x], color="green")

        last_x, last_y = next_x, next_x
    #"""
    plt.show()
    return


def orbit(g, x0, skip, iterations, dr = 1e-4, r_min=0, r_max = 4, x_min = 0, x_max = 1):
    """
        Plots the orbit diagram of a 1 parameter dynamical system for some initial
        condition x0. g must be of the form g(r,x)
    """

    # Array of r values, the x axis of the bifurcation plot
    R = []
    # Array of x_t values, the y axis of the bifurcation plot
    X = []
    
    # Create the r values to loop. For each r value we will plot n_iter points
    r_for_iteration = np.arange(r_min, r_max + dr, dr)

    for r in r_for_iteration:
        x = x0;
        # For each r, iterate the logistic function and collect datapoint if n_skip iterations have occurred
        for i in range(iterations + skip +1):
            if i >= skip:
                R.append(r)
                X.append(x)
                
            x = g(r,x);
    # Plot the data    
    
    plt.figure()
    plt.plot(R, X, ls='', marker=',')
    plt.xlim(r_min, r_max)
    plt.ylim(x_min, x_max)
    plt.title("Orbit Diagram for $x_{0} = $" + str(x0))
    plt.xlabel("$r$")
    plt.ylabel("$x$")
    plt.grid()
    plt.show()
    return
