import matplotlib.pyplot as plt
import random as rand


def get_middle(a, b):
    # a and b two lists with the coordonates of the two points a first point and b second
    x_a, y_a = a[:]
    x_b, y_b = b[:]
    # (x_m, y_m) the coordonates of the middle point
    x_m = (x_a + x_b) / 2
    y_m = (y_a + y_b) / 2
    return [x_m, y_m]


def triangle(t):
    # 1, 2, 3 the three triangle points
    x_1, y_1 = [0 , 0] # y = x with second point
    x_2, y_2 = [5 , 5]
    x_3, y_3 = [10, 0] # y = -x + 10 with second point 

    # 0 the coordinates of the first random point
    x_0 = rand.uniform(1, 10)
    if x_0 < x_2:
        y_0 = rand.uniform(0, x_0)
    else:
        y_max = - x_0 + 10
        y_0 = rand.uniform(1, y_max)

    m = [x_0, y_0] # list of the first point to start with
        
    # the coordinates list to plot
    x_list = [x_1, x_2, x_3, x_0]
    y_list = [y_1, y_2, y_3, y_0]
    

    # start looping
    for _ in range(0, t):

        # choose which point to go to
        p = rand.randint(1,3)
        if p == 1:
            p = x_1, y_1
        elif p == 2:
            p = x_2, y_2
        elif p == 3:
            p = x_3, y_3

        # get the middle point coordinates
        m = get_middle(m, p)

        # append each coordinate to its plot list
        x_list.append(m[0])
        y_list.append(m[1])

    plt.plot(x_list, y_list, 'o', markersize=1)
    plt.show()


if __name__ == "__main__":
    while 1:
        t = int(input('How many dots do you want to plot in the triangle: '))
        if t == 0:
            break
        triangle(t)


