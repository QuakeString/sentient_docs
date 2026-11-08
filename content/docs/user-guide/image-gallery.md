+++
title = "Image gallery"
description = "Image gallery"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/image-gallery.md"
+++


The Image gallery serves as a centralized repository for storing and managing images. 
This is an important resource for improving the visual appeal and functionality of widgets, dashboards, devices, and asset profiles in a mobile application. 
Users can easily upload, organize, and select images to customize their interface and user experience, ensuring an integrity and branded look across the platform.


![image](/images/user-guide/image-gallery/image-gallery-ce.webp)


## Cache configuration

Our image API uses *ETags* to optimize caching, ensuring images are only downloaded when they have changed, thus saving bandwidth.
By default, we do not apply Cache-Control headers, relying on the efficiency of ETags.
However, you can customize caching behavior through environment variables: 

- *CACHE_SPECS_IMAGE_ETAGS_TTL* - image ETags cache TTL. The default value is 44640 minutes, after which the cache will be deleted;
- *CACHE_SPECS_IMAGE_ETAGS_MAX_SIZE* - maximum cache size, in bytes. 0 means the cache is disabled;
- *CACHE_SPECS_IMAGE_SYSTEM_BROWSER_TTL* - browser cache TTL for system images, in minutes. Default value is 0 minutes - the cache is disabled;
- *CACHE_SPECS_IMAGE_TENANT_BROWSER_TTL* - browser cache TTL for tenant images, in minutes. Default value is 0 minutes - the cache is disabled.

These configurations control the Time To Live (TTL) for your system and tenant images in a user's browser cache.
Setting a longer TTL improves load time for repeated visits and reduces server load, while a shorter TTL ensures users receive more frequent content updates.
Adjust these settings based on the update frequency of your images. How to do it, read [here](/docs/user-guide/install/how-to-change-config/).

Additionally, the system administrator can set restrictions on the maximum size of a single image and the total size of images by configuring [tenant profiles](/docs/user-guide/tenant-profiles/#files-limits).
Values are specified in bytes.


## Add image

Add your images to the Image gallery serves in [image file format](#upload-image) (PNG, JPEG, GIF, etc.) or [JSON file format](#import-image-from-json).

### Upload image

To upload new image in **image file format**, follow these steps:


1. Go to the "Image gallery" page in the "Resources" section. Then, click the “Upload image” button in the top right corner of the screen;

1. Select or drop image in the "Upload image" window and then click "Upload";

1. The image has been uploaded.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/upload-image-1-ce.webp" alt="Go to the &quot;Image gallery&quot; page in the &quot;Resources&quot; section. Then, click the “Upload image” button in the top right corner of the screen;" loading="lazy"><figcaption>Go to the "Image gallery" page in the "Resources" section. Then, click the “Upload image” button in the top right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/upload-image-2-ce.webp" alt="Select or drop image in the &quot;Upload image&quot; window and then click &quot;Upload&quot;;" loading="lazy"><figcaption>Select or drop image in the "Upload image" window and then click "Upload";</figcaption></figure><figure><img src="/images/user-guide/image-gallery/upload-image-3-ce.webp" alt="The image has been uploaded." loading="lazy"><figcaption>The image has been uploaded.</figcaption></figure></div>


### Import image from JSON

To import your images in **JSON file format**, follow these steps:


1. Go to the "Image gallery" page in the "Resources" section. Then, click the "Import image" icon in the top right corner of the screen;

1. In the "Import image" window, upload a JSON image file and click "Import";

1. The image has been imported.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/upload-image-4-ce.webp" alt="Go to the &quot;Image gallery&quot; page in the &quot;Resources&quot; section. Then, click the &quot;Import image&quot; icon in the top right corner of the screen;" loading="lazy"><figcaption>Go to the "Image gallery" page in the "Resources" section. Then, click the "Import image" icon in the top right corner of the screen;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/upload-image-5-ce.webp" alt="In the &quot;Import image&quot; window, upload a JSON image file and click &quot;Import&quot;;" loading="lazy"><figcaption>In the "Import image" window, upload a JSON image file and click "Import";</figcaption></figure><figure><img src="/images/user-guide/image-gallery/upload-image-6-ce.webp" alt="The image has been imported." loading="lazy"><figcaption>The image has been imported.</figcaption></figure></div>


## System images

The image gallery contains system images that you can also use to design your dashboards, widgets, etc. By default, only your images are displayed in the image list.
To display your and system images, enable the Enable System Images option.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/include-system-images-1-ce.webp" alt="By default, in the Image gallery displays only your images. Enable the &quot;Include system images&quot; option to view your and the system&#39;s images" loading="lazy"><figcaption>By default, in the Image gallery displays only your images. Enable the "Include system images" option to view your and the system&#39;s images</figcaption></figure><figure><img src="/images/user-guide/image-gallery/include-system-images-2-ce.webp" alt="Now, in the Image gallery displays your and system images." loading="lazy"><figcaption>Now, in the Image gallery displays your and system images.</figcaption></figure></div>


<div class="st-callout info">


**Please note:**
Only the system administrator can delete, rename or update system images.


</div>


## Change the image view mode

You can view images in one of two modes: list or grid.
To change the image viewing mode, simply select the mode that suits you in the top left corner of the Image gallery window.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/image-viewing-mode-1-ce.webp" alt="The image list view." loading="lazy"><figcaption>The image list view.</figcaption></figure><figure><img src="/images/user-guide/image-gallery/image-viewing-mode-2-ce.webp" alt="The image grid view." loading="lazy"><figcaption>The image grid view.</figcaption></figure></div>


## Image operations

You can [download](#download-image), [export to JSON](#export-image-to-json), [edit](#edit-image), [embed](#embed-image), and [delete](#delete-image) image using the corresponding icon opposite the image's name.
Let's take a closer look at each operation.

### Download image

Downloading an image in image file format can be done in two ways, depending on the selected image viewing format:

- If you're using the list view of images, click the "Download image" icon next to the image name that you want to export.
- If you're using the grid view, hover your mouse pointer over the image you want to export and click the "Download image" icon.

The image in image file format will be saved to your PC.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/download-image-1-ce.webp" alt="If you&#39;re using the list view of images, click the &quot;Download image&quot; icon next to the image name that you want to export. The image in image file format will be saved to your PC." loading="lazy"><figcaption>If you&#39;re using the list view of images, click the "Download image" icon next to the image name that you want to export. The image in image file format will be saved to your PC.</figcaption></figure><figure><img src="/images/user-guide/image-gallery/download-image-2-ce.webp" alt="If you&#39;re using the grid view, hover your mouse pointer over the image you want to export and click the &quot;Download image&quot; icon. The image in image file format will be saved to your PC." loading="lazy"><figcaption>If you&#39;re using the grid view, hover your mouse pointer over the image you want to export and click the "Download image" icon. The image in image file format will be saved to your PC.</figcaption></figure></div>


### Export image to JSON

Exporting an image to JSON can be done in two ways, depending on the selected image viewing format:

- If you're using the list view of images, click the "Export image to JSON" icon next to the image name that you want to download.
- If you're using the grid view, hover your mouse pointer over the image you want to download and click the "Export image to JSON" icon.

The image in JSON format will be saved to your PC.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/export-image-1-ce.webp" alt="If you&#39;re using the list view of images, click the &quot;Export image to JSON&quot; icon next to the image name that you want to download. The image in JSON format will be saved to your PC." loading="lazy"><figcaption>If you&#39;re using the list view of images, click the "Export image to JSON" icon next to the image name that you want to download. The image in JSON format will be saved to your PC.</figcaption></figure><figure><img src="/images/user-guide/image-gallery/export-image-2-ce.webp" alt="If you&#39;re using the grid view, hover your mouse pointer over the image you want to download and click the &quot;Export image to JSON&quot; icon. The image in JSON format will be saved to your PC." loading="lazy"><figcaption>If you&#39;re using the grid view, hover your mouse pointer over the image you want to download and click the "Export image to JSON" icon. The image in JSON format will be saved to your PC.</figcaption></figure></div>


### Embed image

After you've added an image to the Image gallery, you can embed this image into HTML card widgets, in HTML section in the widget editor, in cell content functions, in custom actions, etc.

Images provided at the system level are available to all users using the platform, while tenant images may only be available to specific tenants.
Each image on the SENTIENT platform has a unique URL that allows you to download the image both with and without authentication.

Using the code snippet provided below, you can embed the image into components that operate based on plain HTML, without authentication. For example, in *HTML Card* widget, cell content functions, etc.

```java
<img src="relative link to the image" alt="text description of the image" />
```

To embed your image into an Angular HTML template, for example in the *Markdown/HTML Card* widget or HTML section in the widget editor, use the following code snippet:

```java
<img [src]="'image URL' | image | async" />
```

This specific method ensures that the authentication headers is automatically adds in the image request, allowing the same image URL to return different images for different users.

<br>
To obtain a link to the image for further embedding, follow these steps.

- Go to the "Image gallery" page in the "Resources" section;
- Click the "Embed image" of the corresponding image that you want to embed (if you’re using the grid view, hover your mouse pointer over the image you want to embed and click the "Embed image" icon);
- Select the code snippet for the Angular HTML template or for the components based on plain HTML, and copy the corresponding unique link for this image.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/embed-image-1-ce.webp" alt="Go to the &quot;Image gallery&quot; page in the &quot;Resources&quot; section. Click the &quot;Embed image&quot; icon of the corresponding image that you want to embed;" loading="lazy"><figcaption>Go to the "Image gallery" page in the "Resources" section. Click the "Embed image" icon of the corresponding image that you want to embed;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/embed-image-2-ce.webp" alt="Select the code snippet for the Angular HTML template or for the components based on plain HTML, and copy the corresponding unique link for this image." loading="lazy"><figcaption>Select the code snippet for the Angular HTML template or for the components based on plain HTML, and copy the corresponding unique link for this image.</figcaption></figure></div>


### Edit image

To open editing an image window, click the "Edit image" icon next to the image name that you want to edit (if you're using the grid view, hover your mouse pointer over the image you want to edit and click the "Edit image" icon).
An editing window will open. In this window you can change the name, download, export it to JSON, embed, and also [update the image](#update-image).


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/edit-image-1-ce.webp" alt="To open editing an image window, click the &quot;Edit image&quot; icon next to the image name that you want to edit;" loading="lazy"><figcaption>To open editing an image window, click the "Edit image" icon next to the image name that you want to edit;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/edit-image-2-ce.webp" alt="In this window, you can rename, download, export to JSON, embed, and update image." loading="lazy"><figcaption>In this window, you can rename, download, export to JSON, embed, and update image.</figcaption></figure></div>


To change the name of the image, enter a new name and click the "Save" icon in the "Edit image" window.


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/edit-image-3-ce.webp" alt="Enter a new name and click the &quot;Save&quot; icon to change the image name;" loading="lazy"><figcaption>Enter a new name and click the "Save" icon to change the image name;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/edit-image-4-ce.webp" alt="The image name has been changed." loading="lazy"><figcaption>The image name has been changed.</figcaption></figure></div>


#### Update image

Updating the image can be useful, for example, when one picture serves as the background for multiple dashboards. 
This allows you to make changes just once, and all dashboards using that image will automatically receive the updated version, saving you the effort of editing each dashboard individually.

To update the image, click the "Update image" button in the editing window. Select a new image or simply drag it to the "Update image" window and click "Update". 


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/update-image-1-ce.webp" alt="To update the image, click the “Update image” button in the image editing window;" loading="lazy"><figcaption>To update the image, click the “Update image” button in the image editing window;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/update-image-2-ce.webp" alt="Select a new image or simply drag it here and click the &quot;Update&quot; button;" loading="lazy"><figcaption>Select a new image or simply drag it here and click the "Update" button;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/update-image-3-ce.webp" alt="The image has been updated." loading="lazy"><figcaption>The image has been updated.</figcaption></figure></div>


### Delete image

To delete an image from the image list, follow these steps:


1. Click the "Delete image" icon opposite the image&#39;s name you want to delete;

1. Confirm deleting the image in the dialog box


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/delete-image-1-ce.webp" alt="Click the &quot;Delete image&quot; icon opposite the image&#39;s name you want to delete;" loading="lazy"><figcaption>Click the "Delete image" icon opposite the image&#39;s name you want to delete;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/delete-image-2-ce.webp" alt="Confirm deleting the image in the dialog box" loading="lazy"><figcaption>Confirm deleting the image in the dialog box</figcaption></figure></div>


To delete an image that is displayed as an image grid, follow these steps:


1. Hover your mouse over the image you want to delete and click the "Delete image" icon;

1. Confirm deleting the image in the dialog box


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/delete-image-3-ce.webp" alt="Hover your mouse over the image you want to delete and click the &quot;Delete image&quot; icon;" loading="lazy"><figcaption>Hover your mouse over the image you want to delete and click the "Delete image" icon;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/delete-image-4-ce.webp" alt="Confirm deleting the image in the dialog box" loading="lazy"><figcaption>Confirm deleting the image in the dialog box</figcaption></figure></div>


You can also delete multiple images (only via the image list view) at once:


1. Mark one or multiple images you want to delete. Click on the "Delete" bin icon in the top right corner;

1. Confirm deleting images in the dialog box


<div class="st-gallery"><figure><img src="/images/user-guide/image-gallery/delete-image-5-ce.webp" alt="Mark one or multiple images you want to delete. Click on the &quot;Delete&quot; bin icon in the top right corner;" loading="lazy"><figcaption>Mark one or multiple images you want to delete. Click on the "Delete" bin icon in the top right corner;</figcaption></figure><figure><img src="/images/user-guide/image-gallery/delete-image-6-ce.webp" alt="Confirm deleting images in the dialog box" loading="lazy"><figcaption>Confirm deleting images in the dialog box</figcaption></figure></div>


## Next steps
