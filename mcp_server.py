import sys
import json
from client import DPLLSolver

dpll = DPLLSolver()

def handle_call(name, arguments):
    if name == "solve":
        clauses = [set(c) for c in arguments["clauses"]]
        return {"satisfiable": True, "assignment": dpll.solve(clauses)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
