class DPLLSolver:
    """
    DPLL Boolean SAT Solver.
    Clauses represented as list of sets of signed literals: e.g. {1, -2} for (x1 or not x2).
    """
    def solve(self, clauses, assignment=None):
        if assignment is None:
            assignment = {}

        changed = True
        while changed:
            changed = False
            for c in clauses:
                unassigned = []
                satisfied = False
                for lit in c:
                    var = abs(lit)
                    val = assignment.get(var)
                    if val is not None:
                        if (lit > 0 and val) or (lit < 0 and not val):
                            satisfied = True
                            break
                    else:
                        unassigned.append(lit)
                if satisfied:
                    continue
                if not unassigned:
                    return None
                if len(unassigned) == 1:
                    unit = unassigned[0]
                    var = abs(unit)
                    assignment[var] = (unit > 0)
                    changed = True

        all_sat = True
        for c in clauses:
            sat = False
            for lit in c:
                var = abs(lit)
                val = assignment.get(var)
                if val is not None and ((lit > 0 and val) or (lit < 0 and not val)):
                    sat = True
                    break
            if not sat:
                all_sat = False
                break
        if all_sat:
            return assignment

        all_vars = {abs(lit) for c in clauses for lit in c}
        unassigned_vars = [v for v in all_vars if v not in assignment]
        if not unassigned_vars:
            return None

        branch_var = unassigned_vars[0]
        a1 = dict(assignment)
        a1[branch_var] = True
        res = self.solve(clauses, a1)
        if res is not None:
            return res
        a2 = dict(assignment)
        a2[branch_var] = False
        return self.solve(clauses, a2)
