#! /usr/bin/env python3
import sys
import time

from Graph import Graph

from State import State, Direction, TERMINAL_STATE

from Constants import CONST

CON_IN = sys.stdin
CON_OUT = sys.stdout

# Generate All possible next moves for each state to reduce number of iterations on each node
def genPossibleMoves(CAP_BOAT):
	moves = []
	for m in range(CAP_BOAT + 1):
		for c in range(CAP_BOAT + 1):
			if 0 < m < c:
				continue
			if 1 <= m + c <= CAP_BOAT:
				moves.append((m, c))
	return moves


# def runBFS(g, INITIAL_STATE):
# 	sys.stdout = open("outBFS.txt", "w")
# 	print("\n\nBFS :: \n")
# 	start_time = time.time()
# 	p = g.BFS(INITIAL_STATE)
# 	end_time = time.time()
# 	# print("Printing Solution...")
# 	if len(p):
# 		g.printPath(p, TERMINAL_STATE)
# 	else:
# 		print("No Solution")
# 	print("\n Elapsed time in BFS: %.2fms" % ((end_time - start_time)*1000))


def runDFS(g, INITIAL_STATE):
	sys.stdout = open("States_in_DFS.txt", "w")
	print("\n\nDFS :: \n")
	start_time = time.time()
	p = g.DFS(INITIAL_STATE)
	end_time = time.time()
	if len(p):
		g.printPath(p, TERMINAL_STATE)
	else:
		print("No Solution")
	print("\n Time Taken in DFS: %.2fms" % ((end_time - start_time)*1000))


def main():
	sys.stdin = open("in.txt", "r")

	m = int(input("m="))
	print(m)
	c = int(input("c="))
	print(c)
	k = int(input("k="))
	print(k)
	t = int(input("Time taken="))
	print(t)
	n = int(input("Nodes Explored="))
	print(n)

	CNST = CONST(m, c, k, t, n)

	moves = genPossibleMoves(CNST.CAP_BOAT)
	print(str(moves.__len__())+"= Total Number of Iterations ")

	INITIAL_STATE = State(CNST.MAX_M, CNST.MAX_C, Direction.OLD_TO_NEW, 0, 0, 0, CNST, moves)
	# TERMINAL_STATE = State(-1, -1, Direction.NEW_TO_OLD, -1, -1, 0)

	g = Graph()
	# sys.stdout = CON_OUT
	# print("\nRunning BFS>")
	# runBFS(g, INITIAL_STATE)
	# sys.stdout = CON_OUT
	# print("Executed BFS>")

	print("\nExectuing DFS")
	runDFS(g, INITIAL_STATE)
	sys.stdout = CON_OUT
	print("DFS States Explored.")


if __name__ == '__main__':
	main()
