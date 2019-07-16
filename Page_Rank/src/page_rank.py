from fractions import Fraction

#page_rank
#this is the main class to run
# 
# Author: Kyle Knight

# Runs the whole algorithem on the file provided
def compute(file):
    graph = read_in_array(file)
    matrix = adjacency_matrix(graph)
    calc_outs(matrix)
    ranks = calc_ranks(matrix)
    write_to_file(file, ranks, matrix)
    print("calculated results for "+file)

# Reads in a file and prints the contents
def read_in_file(name):
    #name = "graph3VDead.txt"
    with open("data/"+name) as file:
        for line in file:
            print(line,end="")

# this reads in the connections from the file being tested
# they are saved in an array
def read_in_array(name):
    with open("data/"+name) as file:
        table = []
        for line in file:
            table.append(line.split())
        return table

# calculates the adjacency_matrix from the connections that 
# are provided X axis if from and Y axis is to
def adjacency_matrix(graph):
    num_pages = 0
    # calculates the number of pages
    for i in graph:
        for j in i:
            if int(j) > num_pages:
                num_pages = int(j)

    num_pages = num_pages+1 # adds one becaues range is not inclusive
    matrix = [[0 for x in range(num_pages)] for y in range(num_pages)]  # creates a matrix of 0s
    
    # inputs ones int the matrix for conections
    for i in graph:
        matrix [int(i[1])][int(i[0])] = 1
    return matrix

# calculates how many outs each pages has
def calc_outs(matrix):
    num_pages = len(matrix)
    for column in range(num_pages):
        outs = 0
        for row in range(num_pages):
            outs += matrix[row][column]
        if outs != 0:
            for i in range(num_pages):
                matrix[i][column] = Fraction(matrix[i][column], outs)   
    return matrix    

# calculats what the page rankes are
# loops till convergence is reached
def calc_ranks(matrix):
    num_pages = len(matrix)
    ranks = [[Fraction(1, num_pages) for x in range(num_pages)]]
    for j in range(100):
        iteration = []
        for num in range(num_pages):
            start=ranks[j]
            end = 0
            for i in range(num_pages):
                end += start[i]*matrix[num][i]
            iteration.append(end.limit_denominator(100000))
        ranks.append(iteration)
        if check_for_convergence(ranks[j], ranks[j+1]):
            return ranks
    return ranks

# checks to see if convergence has been reached
def check_for_convergence(old, new):
    converge = []
    for rank, elem in enumerate(old):
        change = 0
        if old[rank] != 0:
            change = (old[rank]-new[rank])*(Fraction(old[rank].denominator, old[rank].numerator)) 
        if change < -.05 or change > .05:
            converge.append(False)
        else:
            converge.append(True)
    return all(items == True for items in converge)

# writes and formats the results to a file
def write_to_file(name, ranks, matrix):
    with open("results/results_"+name, "w") as file:
        file.write('Results for {}\n\n'.format(name))
        file.write('With denomanator limited to less than 100,000\nit took {} iterations\n\n'.format(len(ranks)-1))       
        # print matrix
        file.write("Graph of Connections\n")
        file.write('{:4}'.format(' X axis: Page From\n Y axis: Page To\n Divided By number of connections\n\n'))
        file.write('{:4}'.format(''))
        for num in range(len(matrix)):
            file.write('{:^5}'.format(':'+str(num)+':'))
        file.write('\n')
        for num in range(len(matrix)):
            file.write('{:>4}: '.format(':'+str(num)))
            for rank in matrix[num]:
                file.write('{:5}'.format(str(rank)))
            file.write('\n')

        # print results
        file.write('\n\nVertix ID, PageRank Value\n')
        num_pages=0
        for page in ranks[len(ranks)-1]:
            # file.write('{:9},{:10}\n'.format(num_pages,str(page.limit_denominator(100))))
            # file.write('{:9},{:<10}\n'.format(num_pages,float(page.limit_denominator(100))))
            file.write('{:9},{:<10}\n'.format(num_pages,round(float(page), 3)))
            num_pages += 1
        
        #print iterations
        file.write('\n{:5}'.format('iter'))
        for num in range(len(ranks[0])):
            file.write('{:15}'.format('page '+str(num)))
        file.write('\n')
        print(ranks[0][0])
        for iteration, elem in enumerate(ranks):
            file.write('{:3}: '.format(iteration))
            for node, elem in enumerate(ranks[iteration]):
                file.write(('{:15}'.format(str((ranks[iteration][node]).limit_denominator()))))
            file.write("\n")



#this is the main
if __name__ == '__main__':    
    compute("graph3V.txt")
    compute("graph3VDead.txt")
    compute("graph3VSpider.txt")
    compute("graph7V.txt")
     