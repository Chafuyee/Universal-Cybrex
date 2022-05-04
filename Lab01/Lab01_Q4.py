
from statistics import median

"""
def get_income_statistics(stats_list):
    if len(stats_list) == 0:
        output_tuple = (0.0, 0.0)
        return output_tuple
    else:
        income_list = [value for value in stats_list if (value >= 0)]
        employed_list = [value for value in income_list if(value != 0)]
        employed_list = sorted(employed_list)
        print(employed_list)
        if len(employed_list) != 0:
            if (len(employed_list) % 2) == 0:
                median_income_index = int(len(employed_list) / 2)
                median_income = (employed_list[median_income_index] + employed_list[median_income_index+1]) / 2
                zero_count_list = [value for value in income_list if (value == 0)]
                zero_count = len(zero_count_list)
                income_count = len(employed_list)
                total = zero_count + income_count
                employment_percentage = (income_count / total) * 100
                output_tuple = (median_income, round(employment_percentage, 1))
                return output_tuple
            else:
                median_income_index = int(len(employed_list) // 2)
                median_income = (employed_list[median_income_index])
                zero_count_list = [value for value in income_list if (value == 0)]
                zero_count = len(zero_count_list)
                income_count = len(employed_list)
                total = zero_count + income_count
                employment_percentage = (income_count / total) * 100
                output_tuple = (median_income, round(employment_percentage, 1))
                return output_tuple
        else:
            output_tuple = (0.0, 0.0)
            return output_tuple
"""

"""
def get_income_statistics(stats_list):
    if len(stats_list) == 0:
        median_income = 0.0
        employment_rate = 0.0
        output_tuple = (median_income, employment_rate)
        return output_tuple
    else:
        income_list = [value for value in stats_list if (value >= 0)]
        employed_list = [value for value in income_list if (value != 0)]
        employed_list.sort()
        if len(employed_list) == 0:
            median_income = 0.0
            employment_rate = 0.0
            output_tuple = (median_income, employment_rate)
            return output_tuple
        else:
            if (len(employed_list) % 2) == 0:
                median_income_index = int((len(employed_list)-1) // 2)
                median_income = (employed_list[median_income_index] + employed_list[median_income_index+1]) / 2
                unemployed_list = [value for value in income_list if (value == 0)]
                zero_count = len(unemployed_list)
                income_count = len(employed_list)
                total_count = len(income_list)
                employment_rate = (income_count / total_count) * 100
                output_tuple = (median_income, round(employment_rate, 1))
                return output_tuple
            else:
                median_income_index = int((len(employed_list)-1) // 2) 
                median_income = (employed_list[median_income_index+1])
                unemployed_list = [value for value in income_list if (value == 0)]
                zero_count = len(unemployed_list)
                income_count = len(employed_list)
                total_count = len(income_list)
                employment_rate = (income_count / total_count) * 100
                output_tuple = (median_income, round(employment_rate))
                return output_tuple
"""

def get_income_statistics(stats_list):
    if len(stats_list) == 0:
        median_income = 0.0
        employment_rate = 0.0
        output_tuple = (median_income, employment_rate)
        return output_tuple
    else:
        income_list = [value for value in stats_list if (value >= 0)]
        employed_list = [value for value in income_list if (value != 0)]
        employed_list.sort()
        if len(employed_list) == 0:
            median_income = 0
            employment_rate = 0
            output_tuple = (round(float(median_income), 1), round(float(employment_rate), 1))
            return output_tuple
        else:
            if (len(employed_list) % 2) == 0:
                median_income_index = int((len(employed_list)-1) // 2)
                median_income = (employed_list[median_income_index] + employed_list[median_income_index+1]) / 2
                unemployed_list = [value for value in income_list if (value == 0)]
                zero_count = len(unemployed_list)
                income_count = len(employed_list)
                total_count = len(income_list)
                employment_rate = (income_count / total_count) * 100
                output_tuple = (round(float(median_income),1 ), round(float(employment_rate), 1))
                return output_tuple
            else:
                if len(employed_list) == 1:
                    median_income_index = 0
                    median_income = (employed_list[median_income_index])
                    unemployed_list = [value for value in income_list if (value == 0)]
                    zero_count = len(unemployed_list)
                    income_count = len(employed_list)
                    total_count = len(income_list)
                    employment_rate = (income_count / total_count) * 100
                    output_tuple = (round(float(median_income), 1), round(float(employment_rate), 1))
                    return output_tuple
                else:
                    median_income_index = int((len(employed_list)-1) // 2)
                    median_income = (employed_list[median_income_index])
                    unemployed_list = [value for value in income_list if (value == 0)]
                    zero_count = len(unemployed_list)
                    income_count = len(employed_list)
                    total_count = len(income_list)
                    employment_rate = (income_count / total_count) * 100
                    output_tuple = (round(float(median_income), 1), round(float(employment_rate), 1))
                    return output_tuple


