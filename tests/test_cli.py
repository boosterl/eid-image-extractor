from click.testing import CliRunner
from eid_image_extractor.__main__ import main

def test_cli_help_flag():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0

def test_cli_without_inserted_id():
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert "Reading E-ID data ⌛" in result.stdout
    assert "E-ID card not inserted, or could not be read ❌" in result.stderr
    assert result.exit_code == 1

def test_cli_non_existing_argument():
    runner = CliRunner()
    result = runner.invoke(main, ["--no"])
    assert result.exit_code == 2
    
