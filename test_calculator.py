import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5
    assert calculator.calculate(3, 2, "subtract") == 1
    assert calculator.calculate(10, 2, "multiply") == 20
    assert calculator.calculate(6, 1, "divide") == 6
# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0
    assert calculator.calculate(3, 4, "multiply") == 12.0
    assert calculator.calculate(3, 4, "subtract") == -1.0
    assert calculator.calculate(6, 3, "divide") == 2.0

# Add more tests to cover edge cases and negative scenarios

