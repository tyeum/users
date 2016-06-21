Users
#####

An Ansible role to create users, groups, email aliases, configure sudo and lock
down root account. The intended use case is to replace setting up an LDAP or
NIS server. The role also installs sudo and creates a sudoers group that can use
sudo with a password. A password is also set if provided. For generating the
password hash needed, under Debian run: :code:`echo MyPassword | mkpasswd -m
sha-512 -s` and under OpenBSD run: :code:`echo MyPassword | encrypt`. If
provided, email alias and SSH authorized keys are set. If
:code:`users_lock_root` is set to :code:`True` (by default it is) then local and
SSH root login is disabled. Another use case is to manage system users, for
example to disable the local root login add root to the :code:`users` variable
with the password :code:`!`, setting an email address will also set mail
forwarding.

Requirements
------------

- `Ansible 2.0 or later <https://www.ansible.com/>`_.
- `OpenBSD <http://www.openbsd.org/>`_ or `Debian <http://www.debian.org/>`_
  (OpenBSD 5.9 and Debian Jessie are tested, other versions and derivatives
  should also work).

Role Variables
--------------

.. code:: yaml

    users:
    - name: mandatory
      groups: optional, list of other groups
      shell: optional
      uid: optional
      password: optional
      pubkeys: optional list of public SSH keys
      email: optional, used for mail forwarding

    users_lock_root: boolean, default to True

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

To install the dependencies:

.. code:: shell

    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD)

To run the full test suite:

.. code:: shell

    molecule test

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
