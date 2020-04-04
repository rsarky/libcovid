import matplotlib.pyplot as plt


def main(args):
    N = 100000
    i0 = 1
    e = 4 # avg no. of contacts per person per unit time (1 day)
    t = 0.5 # probability of transmission in a contact
    beta = e*t
    gamma = 0.8 # rate of recovery
    S = [N-i0] # #Susceptibile
    I = [i0] # #Infected
    R = [0] # #Removed
    in_steady_state = False

    while not in_steady_state:
        delta_S = -1*beta*(I[-1]/N)*S[-1]
        delta_I = -delta_S - gamma*I[-1]
        new_S, new_I = max(S[-1] + delta_S, 0), min(I[-1] + delta_I, N)
        new_R = N - new_S - new_I
        S.append(new_S)
        I.append(new_I)
        R.append(new_R)
        if abs(I[-1] - I[-2]) < 1:
            in_steady_state = True

    s_line, = plt.plot(S)
    i_line, = plt.plot(I)
    r_line, = plt.plot(R)
    plt.legend([s_line, i_line, r_line],['Susceptible',  'Infectious', 'Removed'])
    plt.show()


if __name__ == '__main__':
    import sys
    main(sys.argv)
