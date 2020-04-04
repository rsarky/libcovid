
def SIR(N=10000, i0=1, e=4, t=0.35, gamma=0.8, days=100):
    """
    N     population
    i0    initial infected population
    e     avg no. of contacts per person per unit time (1 day)
    t     probability of transmission in a contact with an infected item
    gamma rate of recovery and death per person per unit time
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

