import csv
import random


class GraphGenerator:
    def generate_random(self, file_name, e, v, min_r, max_r):
        with open(file_name, 'w', newline='') as csv_file:
            graph_writer = csv.writer(csv_file, delimiter=',',
                                      quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for i in range(0, v):
                x = random.randrange(0, e - 1) + 14
                y = random.randrange(0, e - 1) + 14
                while x == y:
                    y = random.randrange(0, e - 1)
                r = random.randrange(min_r, max_r)
                graph_writer.writerow([x, y, r])


GraphGenerator().generate_random('file4.csv', 15, 200, 1, 3)