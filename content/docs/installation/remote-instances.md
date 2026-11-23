+++
title = "Manage SENTIENT on other computers"
description = "Connect the Platform Manager to SENTIENT on other Linux and Windows servers over SSH, and prepare a server for it."
weight = 14
+++
The Platform Manager looks after SENTIENT on the computer it runs on, and on other computers you add as **remote instances**. A remote instance gets its own card on the **Instances** page. Open it, and every page of the Platform Manager (Status, Control, Logs, Update, Backup and restore, Platform settings, Migration, Repair, Gateway) works on that server.

The Platform Manager reaches the server over **SSH**, with the SSH client that comes with Windows 10 and later and with every Linux. Nothing else needs to be open on the server.

## What the server needs

| | Linux | Windows |
|---|---|---|
| System | Ubuntu, Debian, Red Hat, Rocky, Alma, Fedora, openSUSE and others, on x86_64 | Windows 10 or 11, Windows Server 2019 or later, on x86_64 |
| SSH server | `openssh-server` | OpenSSH Server (a Windows feature) |
| Account | `root`, or a user that may use `sudo` | A user in the **Administrators** group |
| Port | TCP 22 (or the port you choose) open from your computer | TCP 22 open in Windows Defender Firewall |

## Linux servers

1. Install the SSH server if it is missing.
   - Debian and Ubuntu: `sudo apt install openssh-server`
   - Red Hat, Rocky, Alma and Fedora: `sudo dnf install openssh-server`
2. Start it now and with the system: `sudo systemctl enable --now ssh` (the service is called `sshd` on the Red Hat family).
3. If a firewall is on, allow TCP port 22. For example: `sudo ufw allow 22/tcp`.
4. Choose how the Platform Manager signs in:
   - **Key file** (recommended): add the public key to `~/.ssh/authorized_keys` of the user on the server, for example with `ssh-copy-id user@server` from your computer.
   - **Password**: the user's password.
5. The Platform Manager runs its work on the server as administrator. Sign in as `root`, or as a user that may use `sudo`. When `sudo` asks for a password and you sign in with a key, enter that password as the **sudo password** when you add the instance.

## Windows servers

1. Turn on OpenSSH Server: **Settings > System > Optional features > Add a feature > OpenSSH Server**. Or, in PowerShell as administrator:

   ```powershell
   Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
   ```

2. Start it now and with Windows:

   ```powershell
   Start-Service sshd
   Set-Service sshd -StartupType Automatic
   ```

3. Check that Windows Defender Firewall allows TCP port 22. Installing the feature adds the rule **OpenSSH SSH Server (sshd)**.
4. Sign in with an account in the **Administrators** group.
   - **Key file**: for an administrator, Windows reads keys from `C:\ProgramData\ssh\administrators_authorized_keys`, not from the user's own folder. Put the public key there. The file must be readable only by Administrators and SYSTEM:

     ```powershell
     icacls C:\ProgramData\ssh\administrators_authorized_keys /inheritance:r /grant "Administrators:F" /grant "SYSTEM:F"
     ```

   - **Password**: the account's Windows password.

## Add the instance

1. Open **Instances** and select **Add a remote instance**.
2. Enter a name, the server's address and port, and choose **Linux** or **Windows**. The **(i)** next to the choice repeats the setup steps above.
3. Enter the user and how it signs in: a key file (and its passphrase, if it has one) or a password.
4. Choose a colour. While the instance is open, the top bar takes this colour, so it is always clear which computer you are working on.
5. Select **Connect**. The Platform Manager shows the server's **key fingerprint**. Compare it with the one on the server before you accept it:
   - Linux: `ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub`
   - Windows: `ssh-keygen -lf C:\ProgramData\ssh\ssh_host_ed25519_key.pub`

   After you accept it, the Platform Manager refuses a server that shows a different key.
6. The Platform Manager finds out the system and how SENTIENT runs there, and saves the instance. The key passphrase or password is kept in this computer's secret store, never in the instance list.

The first time you work on the server, the Platform Manager copies its own matching build there and checks it by its SHA-256. It does this again only after it is updated.

## When the connection drops

Work on a server (an update, a backup, a migration) runs on the server by itself: as a systemd unit on Linux, as a scheduled task on Windows. A dropped connection does not stop it. The Platform Manager reconnects and follows the progress again. If you close the Platform Manager during a job, the server's card shows **A job is running on this server** with **Follow** the next time you open it. Only one job runs on a server at a time.

## What stays on the server

Two things are done on the server itself, not from another computer: **installing a gateway** (its access token stays on that server) and **uninstalling SENTIENT**.
