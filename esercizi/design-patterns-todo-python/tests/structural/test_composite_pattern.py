from structural.composite_pattern import DirectoryNode, FileNode, build_sample_tree


def test_file_node_reports_size_and_description() -> None:
    file_node = FileNode("report.pdf", 512)
    assert file_node.get_size() == 512
    assert file_node.describe() == "- report.pdf (size=512)"


def test_directory_sums_child_sizes_and_formats_tree() -> None:
    root = DirectoryNode("root")
    root.add_child(FileNode("readme.txt", 64))
    assets = DirectoryNode("assets")
    assets.add_child(FileNode("logo.png", 256))
    root.add_child(assets)

    assert root.get_size() == 320
    expected = "\n".join(
        [
            "root/",
            "  - readme.txt (size=64)",
            "  assets/",
            "    - logo.png (size=256)",
        ]
    )
    assert root.describe() == expected


def test_build_sample_tree_returns_populated_structure() -> None:
    root = build_sample_tree()
    assert isinstance(root, DirectoryNode)
    assert root.get_size() > 0
    description = root.describe()
    assert description.startswith("workspace/")
    assert "documents/" in description
