from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_users(Command, Ansible):
    Command('''ssh dummy@localhost sudo whoami''').stdout == 'root'
