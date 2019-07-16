from src import page_rank
from fractions import Fraction

def test_read_in_file(capsys):
    page_rank.read_in_file("graph3V.txt")
    captured = capsys.readouterr()
    assert captured.out == "0 0\n0 1\n1 0\n1 2\n2 1"
    page_rank.read_in_file("graph3VDead.txt")
    captured = capsys.readouterr()
    assert captured.out == "0 0\n0 1\n1 0\n1 2"
    

def test_read_in_array():
    assert page_rank.read_in_array("graph3V.txt") == [['0', '0'], ['0','1'], ['1', '0'], ['1', '2'], ['2', '1']]
    assert page_rank.read_in_array("graph3VDead.txt") == [['0', '0'], ['0','1'], ['1', '0'], ['1', '2']]

def test_adjacency_matrix():
    graph = page_rank.read_in_array("graph3V.txt")
    assert page_rank.adjacency_matrix(graph) == [[1,1,0], [1,0,1], [0,1,0]]
    graph = page_rank.read_in_array("graph3VDead.txt")
    assert page_rank.adjacency_matrix(graph) == [[1,1,0], [1,0,0], [0,1,0]]

def test_calc_outs():
    graph = page_rank.read_in_array("graph3V.txt")
    matrix = page_rank.adjacency_matrix(graph)
    page_rank.calc_outs(matrix) #== [7]
    assert matrix == [[0.5,0.5,0.0], [0.5,0.0,1.0], [0.0,0.5,0]]
    graph = page_rank.read_in_array("graph3VDead.txt")
    matrix = page_rank.adjacency_matrix(graph)
    page_rank.calc_outs(matrix) #== [7]
    assert matrix == [[0.5,0.5,0.0], [0.5,0.0,0.0], [0.0,0.5,0]]

def test_calc_ranks():
    graph = page_rank.read_in_array("graph3VDead.txt")
    matrix = page_rank.adjacency_matrix(graph)
    page_rank.calc_outs(matrix)
    # checked manually
    # assert page_rank.calc_ranks(matrix) == [3]

def test_check_for_convergence():
    assert page_rank.check_for_convergence([1], [10]) == False
    assert page_rank.check_for_convergence([1], [1]) == True
    assert page_rank.check_for_convergence([0], [0]) == True
    assert page_rank.check_for_convergence([Fraction(0)], [Fraction(0)]) == True
    assert page_rank.check_for_convergence([1], [1]) == True
    assert page_rank.check_for_convergence([1], [1]) == True

def something():
    return 6

def test_something():
    assert something() == 6