import time

# Bubble Sort Algorithm
def bubble_Sort(my_data, drawData, sortSpeed):

    # for every element in your list
        for _ in range(len(my_data)-1):
            for i in range(len(my_data)-1):
                # if this element is greater than the next
                # element
                if my_data[i] > my_data[i+1]:
                    # swap the values
                    my_data[i], my_data[i+1] = my_data[i+1], my_data[i]
                    # TEST
                    # print("Swapped: {} with {}".format(my_data[i], my_data[i+1]))
                    drawData(my_data, ['green' if x == i or x == i+1 else 'red' for x in range(len(my_data))])
                    time.sleep(sortSpeed)

            drawData(my_data, ['green' for x in range(len(my_data))])

