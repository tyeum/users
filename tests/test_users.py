from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_users(Command, Ansible, Sudo):
    with Sudo():
        assert Command('''ssh dummy@localhost sudo whoami''').stdout == 'root'


def test_users_prune(Command):
    assert Command('id prune').rc > 0
