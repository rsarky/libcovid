
def SIR(N=10000, i0=1, e=4, t=0.35, gamma=0.8, days=100):
    """
    N     population
    i0    initial infected population
    e     avg no. of contacts per person per unit time (1 day)
    t     probability of transmission in a contact with an infected item
    gamma rate of recovery and death per person per unit time
    days  Number of days (time steps) to run the simulation for
    returns tuple: (S, I, R)
    S,I,R are lists of length 'days'. Each element of the list contains the
    number of people in the compartment on that day.
    """
    beta = e*t
    S = [N-i0] # #Susceptibile
    I = [i0] # #Infected
    R = [0] # #Removed
    in_steady_state = False

    for i in range(days):
        delta_S = -1*beta*(I[-1]/N)*S[-1]
        delta_I = -delta_S - gamma*I[-1]
        new_S, new_I = max(S[-1] + delta_S, 0), min(I[-1] + delta_I, N)
        new_R = N - new_S - new_I
        S.append(new_S)
        I.append(new_I)
        R.append(new_R)

    return (S, I, R)

def SEIR(N=10000, i0=1, a=4, e=4, t=0.35, gamma=0.8, days=100):
    """
    N     population
    i0    initial infected population
    a     incubation period
    e     avg no. of contacts per person per unit time (1 day)
    t     probability of transmission in a contact with an infected item
    days  Number of days (time steps) to run the simulation for
    gamma rate of recovery and death per person per unit time
    returns tuple: (S, E, I, R)
    S,E,I,R are lists of length 'days'. Each element of the list contains the
    number of people in the compartment on that day.
    """
    beta = e*t
    S = [N-i0] # #Susceptibile
    E = [0]
    I = [i0] # #Infected
    R = [0] # #Removed
    in_steady_state = False

    for i in range(days):
        delta_S = -1*beta*(I[-1]/N)*S[-1]
        delta_E = -delta_S - (1/a)*E[-1]
        delta_I = (1/a)*E[-1] - gamma*I[-1]
        new_S, new_E, new_I = max(S[-1] + delta_S, 0), min(E[-1] + delta_E, N), min(I[-1] + delta_I, N)
        new_R = N - new_S - new_I - new_E
        S.append(new_S)
        E.append(new_E)
        I.append(new_I)
        R.append(new_R)

    return (S, E, I, R)
