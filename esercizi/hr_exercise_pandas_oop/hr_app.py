import os
import unittest

if __name__ == "__main__":
    input("Ambiente pronto. Premi Invio per eseguire i test...")
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=os.path.dirname(__file__), pattern="tests_hr.py")
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\nTutti i test sono passati. Genero i report in './reports'...")
        from hr_analysis import generate_reports
        employees_csv = os.path.join(os.path.dirname(__file__), "data", "employees.csv")
        out_dir = os.path.join(os.path.dirname(__file__), "reports")
        os.makedirs(out_dir, exist_ok=True)
        outputs = generate_reports(employees_csv, out_dir)
        print(f"Report CSV: {outputs['csv']}")
        print(f"Report MD : {outputs['md']}")
    else:
        print("\nAlcuni test sono falliti. Correggi gli errori prima di generare i report.")
