from behavioral.template_method_pattern import (
    InventoryReport,
    ReportGenerator,
    SalesReport,
    run_report,
)


def test_sales_report_runs_full_pipeline() -> None:
    report = SalesReport()
    assert isinstance(report, ReportGenerator)
    assert report.run() == "Total sales: 2950"


def test_inventory_report_formats_items() -> None:
    report = InventoryReport()
    output = run_report(report)
    assert output == "Inventory summary: mice=25, keyboards=12"
