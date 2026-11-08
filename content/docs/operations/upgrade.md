+++
title = "Upgrade and roll back"
description = "Upgrade SENTIENT to a new release and go back if something goes wrong."
weight = 15

[extra]
status = "checked"
checked = "4.3.0.57"
+++
Every SENTIENT release lists its changes in its release notes on the release page. Read them before you upgrade, especially any section about breaking changes.

Database changes run automatically the first time the new version starts. They only go forward: an older SENTIENT cannot run on a database that a newer one has upgraded. That is why every way back below starts from a copy of the database made before the upgrade.

## With Platform Manager

1. Open the Platform Manager and go to **Update**. It shows the **Installed version** and looks for a newer SENTIENT on your update channel (**Stable**, **Release candidate** or **Nightly**).
2. Click **Update to …**. For a plant without internet access, click **Choose package…** and pick the folder of an offline SENTIENT package.
3. If the update reports breaking changes, read them. Then tick **Accept breaking changes**.
4. Click **Update SENTIENT**.

The Platform Manager copies the database first. If the update fails, it puts everything back automatically.

**Roll back later:** if the update worked but you want the previous version back, click **Roll back last update…** on the same screen. It returns to the version and the database copy from before the update. Any data written since the update is lost, so roll back soon or not at all.

The database copies that updates keep are listed under **Kept after earlier changes**. Remove them once you are sure you no longer need them, because they use disk space.

## With Docker

1. [Back up](/docs/operations/backup-restore/) the database and `st-data`.
2. Set the new release in your compose file, for example `image: "quakestring/sentient:4.3.0.58"`. If you use `latest`, the new release is whatever `pull` fetches.
3. Pull and recreate:

   ```bash
   docker compose -f $F pull sentient
   docker compose -f $F up -d
   docker compose -f $F logs -f sentient     # watch the database changes run
   ```

4. Open the web UI and check that the version shown at the bottom of the sign-in page is the new one.

**Roll back:** set the previous image tag again, restore the database backup you made in step 1, then run `up -d`. Starting the old image on the upgraded database does not work.

## Several releases at once

You can go straight from an older release to the newest. The database changes of every release in between run in order. Read the release notes of every release you skip.

## If the upgrade fails

- The Platform Manager has already put the old version back. Its **Logs** screen shows what failed.
- With Docker, `docker compose -f $F logs sentient` shows the step that failed. Roll back as above, and send the log to support. See [Collect logs for support](/docs/troubleshooting/logs/).
