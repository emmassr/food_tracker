from lib.start import Start

def test_display_welcome_message(capsys):
    main = Start()
    main.run()
    captured = capsys.readouterr()
    assert 'Welcome\n' in captured.out


def test_displays_menu(capsys):
    main = Start()
    main.run()
    captured = capsys.readouterr()
    assert 'Please pick an option\n' in captured.out

def test_number():
    main = Start()
    assert main.number() == 5