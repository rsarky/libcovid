import matplotlib.pyplot as plt
import models


def main(args):
    S, I, R = models.SIR(t=0.9)
    s_line, = plt.plot(S)
    i_line, = plt.plot(I)
    r_line, = plt.plot(R)
    plt.legend([s_line, i_line, r_line],['Susceptible',  'Infectious', 'Removed'])
    plt.show()



if __name__ == '__main__':
    import sys
    main(sys.argv)
