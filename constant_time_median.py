import numpy
import Image
import datetime


def calculate_median(data_list):
    return numpy.median(data_list)

window_half_height = 7
window_height = 2 * window_half_height + 1

image = Image.open('map.png').convert('RGB')
#base_data = numpy.zeros((row_count, column_count, 3))
base_data = numpy.asarray(image, numpy.uint8)
row_count = base_data.shape[0]
column_count = base_data.shape[1]
print base_data.shape

#Doing it separately for R, G, B
answer_data = numpy.zeros((row_count, column_count, 3))
start_time = datetime.datetime.now()
for color in range(3):
    column_histogram_list = [[] for x in range(column_count)]
    for data_row_number in range(row_count + window_height):
        kernel_histogram_list = []
        output_row_number = data_row_number - window_half_height
        this_row_data_count_per_column = window_height
        if output_row_number < window_half_height:
            this_row_data_count_per_column = window_half_height + 1 + output_row_number
        if output_row_number >= row_count - window_half_height:
            this_row_data_count_per_column = window_half_height + (row_count - output_row_number)
        if data_row_number < row_count:
            this_row_data = base_data[data_row_number, :, color]
        for data_column_number in range(column_count + window_height):
            output_column_number = data_column_number - window_half_height
            if data_column_number < column_count:
                if data_row_number < row_count:
                    column_histogram_list[data_column_number].append(this_row_data[data_column_number])
                if data_row_number >= window_height:
                    del column_histogram_list[data_column_number][0]
                kernel_histogram_list.extend(column_histogram_list[data_column_number])
            if data_column_number >= window_height:
                del kernel_histogram_list[:this_row_data_count_per_column]
            if 0 < output_row_number < row_count and 0 < output_column_number < column_count:
                answer_data[output_row_number, output_column_number, color] = calculate_median(kernel_histogram_list)

print 'Elapsed Time =', (datetime.datetime.now() - start_time).total_seconds()
answer_data = numpy.uint8(answer_data)
result_image = Image.fromarray(answer_data)
result_image.save('map2.png')
