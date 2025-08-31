import builtins
import importlib
from jira import build_story

def test_build_story_content():
    data = {
        'adjective1':'sleepy','animal':'kangaroo','verb1':'dance','place':'school',
        'adjective2':'sparkly','food':'pizza','verb2':'sing','friend':'Rahul','object':'table'
    }
    s = build_story(data)
    assert "One sleepy morning" in s
    assert "kangaroo" in s
    assert "Rahul" in s

def test_main_flow(monkeypatch, capsys):
    inputs = iter(['sleepy','kangaroo','dance','school','sparkly','pizza','sing','Rahul','table'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(inputs))
    # Reload module to ensure main available and deterministic during test runs
    import jira
    jira.main()
    captured = capsys.readouterr()
    assert "Here’s your Mad Libs story" in captured.out
    assert "One sleepy morning" in captured.out