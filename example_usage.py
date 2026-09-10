from client import DPLLSolver

def main():
    print("=== Testing DPLL Boolean SAT Solver ===")
    dpll = DPLLSolver()

    # (x1 or x2) and (not x1 or x2) and (x1 or not x2)
    clauses = [{1, 2}, {-1, 2}, {1, -2}]
    assignment = dpll.solve(clauses)

    print("Found satisfying assignment:", assignment)
    assert assignment is not None
    assert assignment[2] is True
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
