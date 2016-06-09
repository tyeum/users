def test_users(Command, Ansible):
    Command('''ssh dummy@localhost sudo whoami''').stdout == 'root'
