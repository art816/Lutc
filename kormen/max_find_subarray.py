__author__ = 'art'


def find_max_subarray(a_list):
    """"""

    i_pol = 0
    while i_pol < len(a_list) - 1 and a_list[i_pol] < 0:
        i_pol += 1
    sum_subarray = a_list[i_pol]
    start_ind = end_ind = i_pol
    sum_wind = 0
    sum_rigth = 0
    rigth_ind = None

    # print(a_list[:], sum_subarray, sum_wind, start_ind, end_ind)

    for i in range(i_pol+1, len(a_list)):
        # sum_wind += a_list[i]
        if rigth_ind:
            sum_rigth += a_list[i]
        elif a_list[i] > 0:
            sum_rigth += a_list[i]
            rigth_ind = i
        # print(a_list[:i+1], sum_subarray, sum_wind, sum_rigth, start_ind, end_ind, rigth_ind)

        if a_list[i] >= 0:

            if sum_wind + a_list[i] >= 0:

                if sum_subarray + sum_wind + a_list[i] >= sum_rigth:
                    end_ind = i
                    sum_subarray += sum_wind + a_list[i]
                    sum_wind = 0
                    sum_rigth = 0
                    rigth_ind = None
                    # print('a')
                else:
                    start_ind = rigth_ind
                    end_ind = i
                    sum_subarray = sum_rigth
                    sum_wind = 0
                    sum_rigth = 0
                    rigth_ind = None
                    # print('b')

            elif sum_rigth > sum_subarray:
                start_ind = rigth_ind
                end_ind = i
                sum_subarray = sum_rigth
                sum_wind = 0
                sum_rigth = 0
                rigth_ind = None
                # print('c')
            else:
                sum_wind += a_list[i]
                # print('d')

        else:
            sum_wind += a_list[i]
            if sum_rigth < 0:
                rigth_ind = None
                sum_rigth = 0

    print(sum_subarray, start_ind, end_ind)
    return sum_subarray, start_ind, end_ind
