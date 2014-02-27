import numpy

column_histogram_size = 3

kernel_histogram = numpy.asarray([None] * column_histogram_size * column_histogram_size)
kernel_histogram_marker = 0
q = raw_input('Numbers to Add?')
while q != '-1':
    numb = [int(x) for x in q.split(',')]
    kernel_histogram[kernel_histogram_marker:kernel_histogram_marker + column_histogram_size] = numb
    kernel_histogram_marker += column_histogram_size
    kernel_histogram_marker %= column_histogram_size * column_histogram_size
    print kernel_histogram
    q = raw_input('Numbers to Add?')
#single_column_histogram = numpy.asarray([None] * column_histogram_size)
#single_column_histogram_marker = 0
#
#q = raw_input('Number to Add?')
#while q != -1:
#    single_column_histogram[single_column_histogram_marker] = int(q)
#    single_column_histogram_marker += 1
#    single_column_histogram_marker %= column_histogram_size
#    print single_column_histogram
#    q = raw_input('Next Number?')