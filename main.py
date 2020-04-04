import matplotlib.pyplot as plt
import models


def main(args):
    S, E, I, R = models.SEIR(t=0.9)
    s_line, = plt.plot(S)
    e_line, = plt.plot(E)
    i_line, = plt.plot(I)
    r_line, = plt.plot(R)
    plt.legend([s_line, e_line, i_line, r_line],['Susceptible',  'Exposed', 'Infectious', 'Removed'])
    plt.show()



if __name__ == '__main__':
    import sys
    main(sys.argv)
