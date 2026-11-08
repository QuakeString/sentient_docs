+++
title = "Version control"
description = "Keep dashboards, rule chains, device profiles and other configuration in a Git repository: commit versions, compare, restore and move them between SENTIENT servers."

[extra]
status = "checked"
checked = "4.3.0.57"
+++
**Version control** stores your SENTIENT configuration in a **Git** repository: dashboards, rule chains, device profiles, devices, assets, customers, entity views and widget bundles. You can then:

- see who changed a dashboard and when, and go back to an earlier version;
- compare a version with what is in SENTIENT now;
- move a tested configuration from a test server to the plant server, by committing on one and restoring on the other.

Telemetry is not stored in Git; only configuration.

## Connect a repository

The tenant administrator sets the repository under **Settings > Repository**.

**Local only** needs no Git server at all: SENTIENT keeps the versions in a repository on its own disk, with no network access or sign-in. It is the simplest choice for an offline plant, and you can add a remote address later to copy the history there. The versions are kept in the folder set by `VC_REPOS_PATH` (`/var/lib/sentient/vc-repos` in Docker); back it up with the database.

For a shared or remote repository, create an empty one first on GitHub, GitLab, Gitea, Azure DevOps or your own Git server, then switch **Local only** off and fill in:

| Setting | What to enter |
|---|---|
| **Repository URL** | For example `https://git.example.com/plant/sentient-config.git`, or `git@git.example.com:plant/sentient-config.git` for SSH |
| **Default branch name** | The branch SENTIENT uses unless you choose another, usually `main` |
| **Read-only** | SENTIENT only reads: you can restore but not commit. Use it on a production server that should only receive tested versions |
| **Authentication method** | **Password / access token**: a user name and a password or access token (for GitHub and GitLab, a token with write access to the repository). **Private key**: an SSH key, with its passphrase if it has one |

Click **Check access**, then **Save**. Each tenant uses its own repository. **Show merge commits** also lists merges in the version history.

## Commit a version

- **One entity:** open it (for example a dashboard, or a rule chain's details) and its **Version control** tab, then **Create version**. Choose the branch and type a name for the version, such as `Boiler house: new trend chart`.
- **Many entities:** open **Advanced features > Version control** in the left menu and click **Create entities version**. Choose **All entities** or the entity types to include, and for each whether to include its **relations**, **attributes**, **credentials** and **calculated fields**.

Include credentials only if the repository is as private as the devices' tokens should be.

**Auto-commit** commits an entity by itself every time it is saved. Choose the entity types under **Settings > Auto-commit**. It does not work with a read-only repository.

## Restore a version

- **One entity:** in its **Version control** tab, click a version and **Restore version**. **Compare with current** first shows what would change.
- **Many entities:** under **Advanced features > Version control**, click a version, then **Restore entities from version**. Choose the entity types, and per type the **Sync strategy**:
  - **Merge** updates and adds entities, and leaves entities that are not in the version alone.
  - **Overwrite** also deletes entities of that type that are not in the version (**Remove other entities**).

## Move a configuration between servers

1. On the test server, commit **All entities** to a branch, for example `release-2025-06`.
2. On the plant server, connect the same repository, read-only if you like.
3. Restore that version there with **Merge**.

Devices keep their own credentials on each server unless you included credentials.

## Related

- [Dashboards](/docs/user-guide/dashboards/)
- [Rule engine](/docs/user-guide/rule-engine-2-0/overview/)
