import numpy as np
import Image
import datetime


def calculate_median(data_array):
    return int(np.median(data_array[~np.isnan(data_array)]))

window_half_height = 2
window_height = 2 * window_half_height + 1
window_area = window_height * window_height

empty_np = np.asarray([None] * window_height)

image = Image.open('map.png').convert('RGB')
#base_data = np.zeros((row_count, column_count, 3))
base_data = np.asarray(image, np.uint8)
row_count = base_data.shape[0]
column_count = base_data.shape[1]
print base_data.shape

#Doing it separately for R, G, B
answer_data = np.zeros((row_count, column_count, 3))
start_time = datetime.datetime.now()
for color in range(3):
    column_histogram_array = np.asarray([[None] * window_height] * column_count, dtype=float)
    column_histogram_marker = np.asarray([0] * column_count)
    for data_row_number in range(row_count + window_height):
        kernel_histogram_array = np.asarray([None] * window_area, dtype=float)
        kernel_histogram_marker = 0
        output_row_number = data_row_number - window_half_height
        #this_row_data_count_per_column = window_height
        #if output_row_number < window_half_height:
        #    this_row_data_count_per_column = window_half_height + 1 + output_row_number
        #if output_row_number >= row_count - window_half_height:
        #    this_row_data_count_per_column = window_half_height + (row_count - output_row_number)
        if data_row_number < row_count:
            this_row_data = base_data[data_row_number, :, color]
        for data_column_number in range(column_count + window_height):
            output_column_number = data_column_number - window_half_height
            if data_column_number < column_count:
                if data_row_number < row_count:
                    column_histogram_array[data_column_number][column_histogram_marker[data_column_number]]\
                        = this_row_data[data_column_number]
                    column_histogram_marker[data_column_number] += 1
                    column_histogram_marker[data_column_number] %= window_height
                else:
                    column_histogram_array[data_column_number][column_histogram_marker[data_column_number]] = np.nan
                    column_histogram_marker[data_column_number] += 1
                    column_histogram_marker[data_column_number] %= window_height
                kernel_histogram_array[kernel_histogram_marker:kernel_histogram_marker + window_height]\
                    = column_histogram_array[data_column_number]
                kernel_histogram_marker += window_height
                kernel_histogram_marker %= window_area
            else:
                kernel_histogram_array[kernel_histogram_marker:kernel_histogram_marker + window_height] = empty_np
                kernel_histogram_marker += window_height
                kernel_histogram_marker %= window_area
            if 0 <= output_row_number < row_count and 0 <= output_column_number < column_count:
                answer_data[output_row_number, output_column_number, color] = calculate_median(kernel_histogram_array)

print 'Elapsed Time =', (datetime.datetime.now() - start_time).total_seconds()
answer_data = np.uint8(answer_data)
result_image = Image.fromarray(answer_data)
result_image.save('map2.png')
