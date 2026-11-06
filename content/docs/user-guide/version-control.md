+++
title = "Version control"
description = "Version control"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/version-control.md"
+++
<table style="width:auto">
   <thead>
     <tr>
	 <td style="text-align: center"><strong><em>Available since TB Version 3.4</em></strong></td>
     </tr>
   </thead>
</table> 


SENTIENT Version control service provides the ability to export and restore SENTIENT Entities using Git.
As a Tenant administrator, you can configure access to the Git repository using UI or REST API.
As a platform user, you can export single or multiple SENTIENT Entities, browse version history and restore entities to the specific version.

This feature improves user experience when multiple engineers design the same Rule Chain or Dashboard and simplifies CI/CD. 
It also allows you to easily clone the solution between tenants or platform instances. 

## Architecture

### Entity External ID

Every SENTIENT entity has the "id" field, which is the unique identifier of the entity in scope of a particular SENTIENT environment.
Every exportable SENTIENT entity contains new filed "externalId". 
The field is used to identify the same Entity in case of import and export between multiple environments.
Both "id" and "externalId" fields is of type [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier).

The "externalId" is also used to automatically substitute entity ids in the rule chains (rule nodes) and dashboards (aliases and widget actions).
So, if you decide to import rule chain that is referencing some devices or assets, make sure you have exported/imported the corresponding devices or assets as well.

### Exportable Entities and settings


Initial release of this feature supports following entities: Device, Asset, Entity View, Customer, Dashboard, Widget Bundle, Rule Chain, Entity group, Role, Converter and Integration.


We intentionally omit support of the User entity, since user email is unique in scope of the platform instance. It seems wrong to export user emails and credentials to Git.

While exporting the entity, we store the JSON representation of the entity in Git. It is also possible to export entity attributes, relations and credentials (device only).

### Repository structure

When you first export the entity to Git, the entity "id" is used to name the file inside git repository. 
Then, when you import entities from Git to SENTIENT, the "id" from the file name becomes "externalId" of the entity.
The "externalId" is unique in scope of Tenant. So, you may import/export entities between tenants of the same platform instance, or between different instances.
Any time you perform export and import operations, the "externalId" is used to find the right entity to update.
See example below.

Let's assume you have a development SENTIENT instance and exported a single dashboard with the name "Dashboard 1" and id "4864b750-da7d-11ec-a496-97fa2815d2fe". 
Then the repository will have a single file with the following full name and path:

```bash
dashboard/4864b750-da7d-11ec-a496-97fa2815d2fe.json
```

Let's assume you have imported the dashboard "D1" to the production SENTIENT instance. The "externalId" filed is set when you first import the entity to the new SENTIENT instance. 
In such a case, the dashboard entity in production environment will have different id, but the "externalId" of the dashboard will be set to the same "4864b750-da7d-11ec-a496-97fa2815d2fe".


Customer hierarchy is stored in the 'hierarchy' folder which is recursive and similar to the 'Customer hierarchy' page in the UI.
Entity groups are stored in the 'groups' folder. Each group has 'id.json' file which stores group entity and 'id_entities.json' file which stores list of entity ids in the group. 
Reserved group 'All' does not contain the 'id_entities.json' file because group 'All' contains all entities.


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/version-control-4-ce.webp" alt="Git repository structure" loading="lazy"><figcaption>Git repository structure</figcaption></figure></div>


### Sync strategy

Platform supports two sync strategies for export to Git: Merge and Overwrite. 
"Merge" is the default sync strategy which simply appends the selected entities to the repository. This strategy is useful when you want to save one or multiple files without deleting all other files from the repository.
"Overwrite" strategy completely rewrite the corresponding repository files. This strategy is useful when you want to completely synchronize the list of entities (e.g. Dashboards) in your instance and your Git repository. 
All entities that were previously save to the Git but are not present in your platform instance will be deleted from the Git repository in the corresponding commit.

### Scalability

SENTIENT Version Control service is available as part of a monolithic SENTIENT instance or as a separate microservice for horizontal scalability.
Every instance of the Version Control service is responsible for handling synchronization tasks for the specific partition(s) of the Tenants in the cluster.
Each "commit" API call may take some time. Concurrent "commit" API calls in scope of the same Tenant are not supported. 
The system will cancel the "commit" API call if it is in progress and the new "commit" API call arrives.

## Usage

### Git Settings configuration

As a Tenant administrator, you can navigate to the "Version control" page of the "Advanced features" section. The page allows you to provision Git repository URL, default branch name and authentication settings.
We expect you to provide URL to the empty Git repository.


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/version-control-1-ce.webp" alt="Configure Git settings" loading="lazy"><figcaption>Configure Git settings</figcaption></figure></div>


### Export to Git

#### Single Entity Export

Navigate to entity details and open the "Version control" tab. 
Rule Chains and Dashboards have built-in version control button and popup widget to the corresponding editors.
See screenshots below.

**Device:**


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/version-control-devices-1-ce.webp" alt="Entity export" loading="lazy"><figcaption>Entity export</figcaption></figure><figure><img src="/images/user-guide/version-control/version-control-devices-2-ce.webp" alt="Entity version history" loading="lazy"><figcaption>Entity version history</figcaption></figure></div>


**Rule Chain:**


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/version-control-rule-chain-1-ce.webp" alt="Rule Chain export" loading="lazy"><figcaption>Rule Chain export</figcaption></figure><figure><img src="/images/user-guide/version-control/version-control-rule-chain-2-ce.webp" alt="Rule Chain version history" loading="lazy"><figcaption>Rule Chain version history</figcaption></figure></div>


**Dashboard:**


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/version-control-dashboard-1-ce.webp" alt="Dashboard export" loading="lazy"><figcaption>Dashboard export</figcaption></figure><figure><img src="/images/user-guide/version-control/version-control-dashboard-2-ce.webp" alt="Dashboard version history" loading="lazy"><figcaption>Dashboard version history</figcaption></figure></div>


#### Multiple Entity Export

Navigate to version control page. You may select one or more entity types to restore. By default, all entity types are selected.


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/version-control-2-ce.webp" alt="Entity export" loading="lazy"><figcaption>Entity export</figcaption></figure><figure><img src="/images/user-guide/version-control/version-control-3-ce.webp" alt="Entity version history" loading="lazy"><figcaption>Entity version history</figcaption></figure></div>


#### Auto-commit

Auto-commit is a useful feature to automatically commit the Dashboard and Rule Chains when we save the entity via UI or REST API call. 
The auto-commit happens asynchronously to improve UI experience. 
The auto-commit does not happen when you assign entity to the customer (change entity owner). 
In such case you should commit all entities of the specific entity type with the overwrite strategy.


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/auto-commit-settings-1-ce.webp" alt="Git auto commit settings" loading="lazy"><figcaption>Git auto commit settings</figcaption></figure></div>


### Restore from Git

Navigate to version control page. Select the commit and specify restore settings.


<div class="st-gallery"><figure><img src="/images/user-guide/version-control/version-control-5-ce.webp" alt="Restore specific version" loading="lazy"><figcaption>Restore specific version</figcaption></figure></div>


## Next steps
