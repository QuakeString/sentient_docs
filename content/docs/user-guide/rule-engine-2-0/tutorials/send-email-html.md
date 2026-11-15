+++
title = "Send HTML or image inside email"
description = "Tutorial to send HTML page or image inside email message"

[extra]
status = "imported"
checked = ""
source = "docs/user-guide/rule-engine-2-0/tutorials/send-email-html.md"
+++
This Tutorial is to show you how to send an email message with HTML page or image inside.

## Prerequisites

* [Getting Started](/docs/getting-started-guides/helloworld/) guide.
* [Rule Engine Overview](/docs/user-guide/rule-engine-2-0/overview/).
* [Send email](/docs/user-guide/rule-engine-2-0/nodes/external/send-email/) node.


## Message flow
- Like a start point we will use [Generator](/docs/user-guide/rule-engine-2-0/nodes/action/generator/) that will imitate regular rule chain messages flow: prepared message and metadata
  where we can contain some dynamic field for **to email** node.
- The [To email node](/docs/user-guide/rule-engine-2-0/nodes/transformation/to-email/) prepares data, destination email, and other for email message.
- The [Send email node](/docs/user-guide/rule-engine-2-0/nodes/external/send-email/) sends a message.

## Configuring Rule Nodes

#### Configuring "to email" node

At first, lets create and configure "to email" node.

1. Go to rule chain, find `to email` node and drag it to the canvas.
2. Specify: **Name**, **From Template**, **To Template** - we will use pattern to find an email in data of message, **Subject Template**. Select **Mail Body Type** HTML or Dynamic. We will use the Dynamic.
3. Specify HTML to **Body Template** (you can use our example).
4. Press **Add**.


<div class="st-gallery"><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/add_rule_node_to_email.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/mail_body_type.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/dynamic_body_template.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


<div class="st-content-toggle" id="bodyTemplateExamples">
    <div class="panel panel-default">
        <div class="panel-heading">
            
            
            
            
            <a class="content-toggle-button" data-target="#loriot-account">
                <div class="content-toggle-button-text">
                    Example of HTML page
                </div>
            </a>
            
            
            
            
            <a class="content-toggle-button" data-target="#basic-credential">
                <div class="content-toggle-button-text">
                    Example of HTML with image
                </div>
            </a>
            
        </div>
        
        
        
        
        
        <div id="loriot-account" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


Example of HTML
```html
<table class="main" style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; box-sizing: border-box; border-radius: 3px; width: 100%; background-color: #f6f6f6; margin: 0px auto;" cellspacing="0" cellpadding="0" bgcolor="#f6f6f6">
    <tbody>
    <tr style="box-sizing: border-box; margin: 0px;">
        <td class="content-wrap" style="box-sizing: border-box; vertical-align: top; margin: 0px; padding: 20px;" align="center" valign="top">
            <table style="box-sizing: border-box; border: solid 1px #e9e9e9; border-radius: 3px; margin: 0px; height: 127px; padding: 20px; background-color: #ffffff; width: 600px; max-width: 600px !important;" width="600" cellspacing="0" cellpadding="0">
                <tbody>
                <tr style="box-sizing: border-box; margin: 0px;">
                    <td class="content-block" style="color: #348eda; box-sizing: border-box; border-radius: 6px; vertical-align: top; margin: 0px; padding: 0px 0px 20px; width: 839px;" valign="top">
                        <h2>Test message using 'to email' rule node</h2>
                    </td>
                </tr>
                <tr style="box-sizing: border-box; margin: 0px;">
                    <td class="content-block" style="box-sizing: border-box; vertical-align: top; margin: 0px; padding: 0px 0px 20px; width: 600px;" valign="top"><span style="color: #000000;">This email is indicating that your outgoing mail settings were set up correctly.</span></td>
                </tr>
                <tr style="box-sizing: border-box; margin: 0px;">
                    <td class="content-block" style="box-sizing: border-box; vertical-align: top; margin: 0px; padding: 0px 0px 20px; width: 600px;" valign="top"><span style="color: #000000;">&mdash; The SENTIENT :)</span></td>
                </tr>
                </tbody>
            </table>
        </td>
    </tr>
    </tbody>
</table>

```

                </td></tr></table>
            </div>
        </div>
        
        
        
        
        
        <div id="basic-credential" class="panel-collapse collapse">
            <div class="panel-body">
                
                <table><tr><td>
                    


To send an image, you just need to specify the name of the image with the file extension.

Example of HTML with image
```html
<img src="cid:st.example.png" alt="Example image">
```


                </td></tr></table>
            </div>
        </div>
        
    </div>
</div>


#### Configuring generator
At the second stage, let's configure the "generator" node:
1. Find in the Rule Chain `Generator` and drag it to the canvas
2. Specify name field, choose "1" for **message count** and, for example "2" for **Period in seconds**
3. Now we need to prepare JS code, also you can use our example.

*Here we need to specify fields in metadata, that are dynamic in "to email" node. In our example it is "isHtml" and "userEmail" fields.*


<div class="st-tabs">

<div class="st-tab" data-label="JS code for HTML page">

Example of generator JS code
```js
var metadata = { userEmail: 'info@sentient.org', isHtml: true };
var msgType = "POST_TELEMETRY_REQUEST";
return { msg: {}, metadata: metadata, msgType: msgType }
```


<div class="st-gallery"><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/html_to_email_generator.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


</div>

<div class="st-tab" data-label="JS code for image">

_To send an image you need to encode the image to Base64. To do this you need to find some service that can do this and set the result string for `encodedImage` in the next example._

Example of generator JS code
```js
var encodedImage = 'HERE_YOU_BASE_64_ENCODED_IMAGE';
var images = {
    "st.example.png": encodedImage
};
var metadata = { 
    userEmail: 'info@sentient.org', 
    images: JSON.stringify(images), 
    isHtml: true 
};
var msgType = "POST_TELEMETRY_REQUEST";
return { msg: {}, metadata: metadata, msgType: msgType }
```


<div class="st-gallery"><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/function_generate_image_to_email.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


</div>

</div>


#### Send email and finishing
Find and configure new **send email** node and connect all nodes between themselves, like on the screen shoot.
Save rule chain.


<div class="st-gallery"><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/rule_chain.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## Result
Check destination email to see the result of the “to email” node work. 
We got the next message:


<div class="st-gallery"><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/message_from_st_html.webp" alt="" loading="lazy"><figcaption></figcaption></figure><figure><img src="/images/user-guide/rule-engine-2-0/tutorials/html-in-email/message_from_st_image.webp" alt="" loading="lazy"><figcaption></figcaption></figure></div>


## See Also

- [Send email](/docs/tutorials/send-email/).

## Next steps
