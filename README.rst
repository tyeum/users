Users
#####

.. image:: https://travis-ci.org/adarnimrod/users.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/users

An Ansible role to create users, groups, email aliases, configure sudo and lock
down root account SSH access. The intended use case is to replace setting up
an LDAP or NIS server. The role also installs sudo and creates a sudoers group
that can use sudo with a password. A password is also set if provided. For
generating the password hash needed, under Debian run: :code:`echo MyPassword
| mkpasswd -m sha-512 -s` and under OpenBSD run: :code:`echo MyPassword |
encrypt`. If provided, email alias and SSH authorized keys are set. If
:code:`users_lock_root_ssh` is set to :code:`True` (by default it is) then SSH
root login is disabled. Another use case is to manage system users, for example
to disable the local root login add root to the :code:`users` variable with the
password :code:`*************`, setting an email address will also set mail
forwarding.

Requirements
------------

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Python 2.7 and either Docker or Vagrant and Virtualbox.
Install the Python dependencies, dependent roles and roles required for
testing:

.. code:: shell

    pip install -r tests/requirements.txt
    ansible-galaxy install git+file://$(pwd),$(git rev-parse --abbrev-ref HEAD) -p .molecule/roles
    molecule dependency

To run the full test suite:

.. code:: shell

    pre-commit run --all-files
    molecule test --platform all

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
