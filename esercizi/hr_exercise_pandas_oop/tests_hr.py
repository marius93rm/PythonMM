import os
import unittest
import tempfile

from hr_domain import Role, Department, Employee, Manager, Contractor, InvalidSalaryError
from hr_analysis import load_employees_csv, compute_total_compensation, department_stats, generate_reports

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
EMP_PATH = os.path.join(DATA_DIR, "employees.csv")

class TestDomain(unittest.TestCase):
    def test_employee_compensation_with_bonus(self):
        r = Role("Developer", 2)
        d = Department("Engineering", "CC100")
        e = Employee(1, "Alice", "Rossi", r, d, base_salary=60000, bonus_percent=10, workload_percent=1.0)
        self.assertAlmostEqual(e.total_compensation(), 66000.0, places=2)

    def test_manager_extra_bonus(self):
        r = Role("Manager", 3)
        d = Department("Sales", "CC200")
        m = Manager(2, "Franco", "Marroni", r, d, base_salary=70000, bonus_percent=12, workload_percent=1.0)
        self.assertAlmostEqual(m.total_compensation(), 82320.0, places=2)

    def test_contractor_ignores_bonus(self):
        r = Role("Contractor", 2)
        d = Department("Engineering", "CC100")
        c = Contractor(3, "Diego", "Neri", r, d, base_salary=40000, bonus_percent=99, workload_percent=0.8)
        self.assertAlmostEqual(c.total_compensation(), 32000.0, places=2)

    def test_invalid_salary_raises(self):
        r = Role("Developer", 2)
        d = Department("Engineering", "CC100")
        with self.assertRaises(InvalidSalaryError):
            Employee(9, "X", "Y", r, d, base_salary=-1, bonus_percent=0, workload_percent=1.0)


class TestPandasPipeline(unittest.TestCase):
    def test_load_and_compute(self):
        df = load_employees_csv(EMP_PATH)
        self.assertGreaterEqual(len(df), 5)
        df2 = compute_total_compensation(df)
        self.assertIn("total_compensation", df2.columns)

    def test_department_stats_values(self):
        df = compute_total_compensation(load_employees_csv(EMP_PATH))
        stats = department_stats(df)
        depts = set(stats["department"].tolist())
        self.assertTrue({"Engineering","Sales","HR"}.issubset(depts))
        eng_mean = float(stats.loc[stats["department"]=="Engineering","mean"].iloc[0])
        self.assertAlmostEqual(eng_mean, 64666.67, places=2)

    def test_generate_reports_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs = generate_reports(EMP_PATH, tmp)
            self.assertTrue(os.path.exists(outputs["csv"]))
            self.assertTrue(os.path.exists(outputs["md"]))
            import pandas as pd
            s = pd.read_csv(outputs["csv"])
            for col in ["department","count","mean","median","min","max"]:
                self.assertIn(col, s.columns)

if __name__ == "__main__":
    unittest.main()
