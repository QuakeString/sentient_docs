+++
title = "Guides"
aliases = ["/docs/iot-video-tutorials/"]

[extra]
status = "imported"
checked = ""
source = "docs/guides.md"
+++
<script type="text/javascript">

    var reportedSearchInputs = [];
    var searchPageCount = 0;

    document.onmousemove = function(e) {
        var event = e || window.event;
        window.mouseX = event.clientX;
        window.mouseY = event.clientY;
        if (checkMouseMoved()) {
            checkSearchInput();
        }
    };

    jqueryDefer(function () {
        $( document ).ready(function() {
            var searchInput = $('#searchGuideInput');
            searchInput.keyup(function () {
                window.typeMouseX = window.mouseX;
                window.typeMouseY = window.mouseY;
                filterGuides();
            });
            searchInput.blur(function () {
                checkSearchInput();
            });
            searchInput.focus(
                function () {
                    $(this).parent('#searchGuideBox').addClass('focused');
                }).blur(
                function () {
                    $(this).parent('#searchGuideBox').removeClass('focused');
                });
            filterGuides();
        });
    });

    function checkMouseMoved () {
        if (typeof window.typeMouseX === "undefined" || typeof window.typeMouseY === "undefined") {
            return false;
        }
        return window.typeMouseX !== window.mouseX && window.typeMouseY !== window.mouseY;
    }

    function filterGuides() {
        $('.guides-list').find('.guide-container').removeClass('hidden');
        var guidesBlock = $('.guides-block');
        guidesBlock.removeClass('hidden');
        searchPageCount = 0;
        var searchText = $('#searchGuideInput').val();

        var keywords = searchText.split(' ');
        if (keywords && keywords.length) {
            var keyRegexps = [];
            for (var i=0;i<keywords.length;i++) {
                if (keywords[i].length) {
                    keyRegexps.push(new RegExp(keywords[i].toLowerCase()));
                }
            }
            guidesBlock.each( function() {
                var containers = $( this ).find('.guide-container');
                var total = containers.length;
                containers.each( function() {
                    var paragraphs = $(this).find('p');
                    var text = '';
                    paragraphs.each( function() {
                        text += $(this).html();
                        text += ' ';
                    });
                    var matches = testKeywords(keyRegexps, text.toLowerCase());
                    if (!matches) {
                        $( this ).addClass('hidden');
                        total--;
                    }
                });
                searchPageCount += total;
                if (!total) {
                    $( this ).addClass('hidden');
                }
            });
        }
    }
    
    function testKeywords(keyRegexps, input) {
        var result = true;
        for (var i=0;i<keyRegexps.length;i++) {
            result = result && keyRegexps[i].test(input);
        }
        return result;
    }

    function checkSearchInput() {
        var searchText = $('#searchGuideInput').val().trim();
        if (searchText.length >=3 && reportedSearchInputs.indexOf(searchText) === -1) {
            reportSearchInput(searchText);
            reportedSearchInputs.push(searchText);
        }
    }

    function reportSearchInput(searchText) {
        if (checkGTagDataLayer()) {
                return;
        }

        gtag("event", "search", {
                "search_term": searchText,
                "event_label": "Guides", 
                "searchPageCount": searchPageCount  
        });
    }
    
</script>

<ul id="markdown-toc">
    
    
        
    
    
    
        
        <li>
            <a href="#AnchorIDGettingStartedGuides" id="markdown-toc-AnchorIDGettingStartedGuides">Getting started guides</a>
        </li>
        
    
    
    
        
        <li>
            <a href="#AnchorIDDataVisualization" id="markdown-toc-AnchorIDDataVisualization">Data visualization</a>
        </li>
        
    
    
    
        
        <li>
            <a href="#AnchorIDConnectYourDevice" id="markdown-toc-AnchorIDConnectYourDevice">Connect your device</a>
        </li>
        
    
    
    
        
        <li>
            <a href="#AnchorIDDataProcessing" id="markdown-toc-AnchorIDDataProcessing">Data processing & actions</a>
        </li>
        
    
    
    
        
        <li>
            <a href="#AnchorIDDataAnalytics" id="markdown-toc-AnchorIDDataAnalytics">IoT Data analytics</a>
        </li>
        
    
    
    
        
        <li>
            <a href="#AnchorIDAdvancedFeatures" id="markdown-toc-AnchorIDAdvancedFeatures">Advanced features</a>
        </li>
        
    
    
    
        
        <li>
            <a href="#AnchorIDOAuth" id="markdown-toc-AnchorIDOAuth">OAuth 2.0</a>
        </li>
        
    
    
    
        
        <li>
            <a href="#AnchorIDContribution" id="markdown-toc-AnchorIDContribution">Contribution and Development</a>
        </li>
        
    
    
</ul>

<div class="guides">
    <div class="filter-panel">
        <div id="searchGuideBox">
            <input type="text" id="searchGuideInput" placeholder="Find a guide...">
            <button class="searchButton"></button>
        </div>
    </div>
    


<h1 style="font-size: 28px; transform: translateY(40px); margin-bottom: 0;">Getting started guides</h1>


<li class="guide-container">
    <a href="">
        <div class="guide-text">
            <p class="guide-title">
                
            </p>
            <p class="guide-subtitle">
                
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<div class="guides-block" id="AnchorIDGettingStartedGuides">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <p class="guides-subtitle">
                These guides provide quick overview of main SENTIENT features. Designed to be completed in 15-30 minutes.
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="/docs/getting-started-guides/helloworld/">
        <div class="guide-text">
            <p class="guide-title">
                Hello world
            </p>
            <p class="guide-subtitle">
                Learn how to collect data from IoT devices using MQTT, HTTP, or CoAP and visualize it on a simple dashboard.
            </p>
            <p class="guide-keywords">
                mqtt http coap visualization helloworld
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/dashboards/">
        <div class="guide-text">
            <p class="guide-title">
                Working with IoT dashboards
            </p>
            <p class="guide-subtitle">
                Learn how to perform basic operations over Dashboards.
            </p>
            <p class="guide-keywords">
                dashboards
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/re-getting-started/">
        <div class="guide-text">
            <p class="guide-title">
                Getting started with Rule Engine
            </p>
            <p class="guide-subtitle">
                Learn about SENTIENT rule engine and typical use cases you can implement. Review Hello World example and learn how-to enable filtering of incoming telemetry messages.
            </p>
            <p class="guide-keywords">
                device management attributes
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


    </ul>
</div>


<div class="guides-block" id="AnchorIDDataVisualization">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <h2>
                Data visualization
            </h2>
            
            <p class="guides-subtitle">
                These guides contain instructions how to configure complex SENTIENT dashboards.
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="https://youtu.be/BNY-kd320sE">
        <div class="guide-text">
            <p class="guide-title">
                Key concepts for working with the main functions of SENTIENT
            </p>
            <p class="guide-subtitle">
                In this intro video, we kick off a tutorial series on SENTIENT. Together, we'll explore key features and build a step-by-step smart dashboard to collect, visualize, and monitor data from office-integrated IoT devices.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="https://youtu.be/65SoFceFDBE">
        <div class="guide-text">
            <p class="guide-title">
                Practical Lesson 1. Adding an entity and visualizing it on the Dashboard
            </p>
            <p class="guide-subtitle">
                We will create your first dashboard in SENTIENT. Add Office A as an asset, define its contact information as attributes, and visualize it using an Information card widget.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="https://youtu.be/fijOV0Gxu0k">
        <div class="guide-text">
            <p class="guide-title">
                Practical Lesson 2. Adding devices and visualizing their telemetry on the Dashboard
            </p>
            <p class="guide-subtitle">
                Time to connect our devices! In this video, we'll add three devices, link them to Office A, simulate telemetry data using the Rule Engine, and display it on the dashboard.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="https://youtu.be/X26jgF5nX5g">
        <div class="guide-text">
            <p class="guide-title">
                Practical Lesson 3. Time window in SENTIENT
            </p>
            <p class="guide-subtitle">
                Learn what a Time window feature is in SENTIENT and how to set time intervals for working with telemetry data.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="https://youtu.be/FzjpjvoPRok">
        <div class="guide-text">
            <p class="guide-title">
                Practical Lesson 4. Visualizing device locations with Image Map widget
            </p>
            <p class="guide-subtitle">
                Learn how to create an Image Map widget to display device locations directly on the office floor plan.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="https://youtu.be/MuOB13aH--U">
        <div class="guide-text">
            <p class="guide-title">
                Practical Lesson 5. Part 1. States & Multi-Level Dashboard Hierarchy
            </p>
            <p class="guide-subtitle">
                Mastering states in SENTIENT! In this tutorial, we will create separate states for each sensor, configure actions to navigate between them, and set up the air sensor state to monitor temperature, humidity, and CO₂ levels in the office.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="https://youtu.be/QZ4z_aaub6I">
        <div class="guide-text">
            <p class="guide-title">
                Practical Lesson 5. Part 2. Configuring States for Energy & Water Monitoring
            </p>
            <p class="guide-subtitle">
                Expanding our dashboard with more states! In this tutorial, we will configure states for monitoring power and water consumption.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="https://youtu.be/2k5DUCOpdfk">
        <div class="guide-text">
            <p class="guide-title">
                Practical Lesson 6. Sharing Your Dashboard with Customer
            </p>
            <p class="guide-subtitle">
                Time to share dashboard data with your customers. In this guide, we’ll add customers, configure their permissions for dashboard data.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
        </div>
    </a>
</li>


    </ul>
</div>


<div class="guides-block" id="AnchorIDConnectYourDevice">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <h2>
                Connect your device
            </h2>
            
            <p class="guides-subtitle">
                Learn how to connect devices based on your connectivity technology or solution.
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="/docs/reference/http-api/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices using SENTIENT HTTP API
            </p>
            <p class="guide-subtitle">
                Learn how to connect your devices using HTTP protocol and SENTIENT built-in payload format.
            </p>
            <p class="guide-keywords">
                http connect
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/reference/mqtt-api/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices using SENTIENT MQTT API
            </p>
            <p class="guide-subtitle">
                Learn how to connect your devices using MQTT protocol and SENTIENT built-in payload format.
            </p>
            <p class="guide-keywords">
                mqtt connect
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/reference/mqtt-sparkplug-api/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices using  SENTIENT MQTT Sparkplug API
            </p>
            <p class="guide-subtitle">
                Learn how to connect your devices using MQTT Sparkplug protocol and SENTIENT built-in payload format.
            </p>
            <p class="guide-keywords">
                sparkplug connect
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/reference/lwm2m-api/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices using SENTIENT LwM2M API
            </p>
            <p class="guide-subtitle">
                Learn how to connect your devices using LwM2M protocol and SENTIENT built-in payload format.
            </p>
            <p class="guide-keywords">
                lwm2m connect
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/reference/coap-api/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices using SENTIENT CoAP API
            </p>
            <p class="guide-subtitle">
                Learn how to connect your devices using CoAP protocol and SENTIENT built-in payload format.
            </p>
            <p class="guide-keywords">
                coap connect
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/iot-gateway/getting-started/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices through SENTIENT IoT Gateway
            </p>
            <p class="guide-subtitle">
                Learn how to deploy IoT Gateway in your local network and route messages from your devices to the cloud.
            </p>
            <p class="guide-keywords">
                gateway connect
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/">
        <div class="guide-text">
            <p class="guide-title">
                SENTIENT Integrations basics
            </p>
            <p class="guide-subtitle">
                Learn about SENTIENT Integrations feature and how you can use it to connect devices and apps that use custom payload formats.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/#platform-integrations-vs-iot-gateway">
        <div class="guide-text">
            <p class="guide-title">
                SENTIENT Integrations vs IoT Gateway
            </p>
            <p class="guide-subtitle">
                Learn the differences between the Platform Integrations and IoT Gateway.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/http/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices with custom payload using SENTIENT HTTP Integration
            </p>
            <p class="guide-subtitle">
                Convert existing protocols and payload formats to SENTIENT message format.
            </p>
            <p class="guide-keywords">
                http connect
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/mqtt/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices with custom payload using SENTIENT MQTT Integration.
            </p>
            <p class="guide-subtitle">
                Connect to external brokers and consume MQTT data stream
            </p>
            <p class="guide-keywords">
                mqtt connect
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/kafka/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices with custom payload using SENTIENT Kafka Integration.
            </p>
            <p class="guide-subtitle">
                Connect to external brokers and consume Kafka data stream
            </p>
            <p class="guide-keywords">
                kafka connect
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/sigfox/">
        <div class="guide-text">
            <p class="guide-title">
                Connect SigFox devices using TB PE Integration
            </p>
            <p class="guide-subtitle">
                Learn how to route messages from Sigfox backend to SENTIENT and decode binary device payloads.
            </p>
            <p class="guide-keywords">
                sigfox connect
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/ttn/">
        <div class="guide-text">
            <p class="guide-title">
                Connect LoRaWAN devices using TheThingsStack
            </p>
            <p class="guide-subtitle">
                Learn how to route messages from TheThingsStack backend to SENTIENT and vise-versa.
            </p>
            <p class="guide-keywords">
                ttn connect
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/opc-ua/">
        <div class="guide-text">
            <p class="guide-title">
                Connect OPC-UA servers to SENTIENT
            </p>
            <p class="guide-subtitle">
                Learn how to connect OPC-UA devices to SENTIENT.
            </p>
            <p class="guide-keywords">
                opcua connect
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/thingpark/">
        <div class="guide-text">
            <p class="guide-title">
                Connect LoRaWAN devices using Actility ThingPark
            </p>
            <p class="guide-subtitle">
                Learn how to route messages from ThingPark to SENTIENT and vise-versa.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/aws-iot/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices through AWS IoT
            </p>
            <p class="guide-subtitle">
                Learn how to connect to AWS IoT broker, transform the incoming messages and generate the downlinks using SENTIENT.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/aws-kinesis/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices through AWS Kinesis
            </p>
            <p class="guide-subtitle">
                Learn how to connect to AWS Kinesis stream, transform the incoming messages and generate the downlinks using SENTIENT.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/ibm-watson-iot/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices through IBM Watson IoT
            </p>
            <p class="guide-subtitle">
                Learn how to connect to IBM Watson IoT broker, transform the incoming messages and generate the downlinks using SENTIENT.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/azure-event-hub/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices through Azure Event Hub
            </p>
            <p class="guide-subtitle">
                Learn how to connect to Azure Event Hub, transform the incoming messages and generate the downlinks using SENTIENT.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/azure-iot-hub/">
        <div class="guide-text">
            <p class="guide-title">
                Connect devices through Azure IoT Hub
            </p>
            <p class="guide-subtitle">
                Learn how to connect to Azure IoT Hub and transform the incoming messages using SENTIENT.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/tcp/">
        <div class="guide-text">
            <p class="guide-title">
                Devices uses TCP protocol
            </p>
            <p class="guide-subtitle">
                How to connect to SENTIENT TCP-server, transform the incoming messages and generate the downlinks using SENTIENT.
            </p>
            <p class="guide-keywords">
                Connect TCP devices
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/udp/">
        <div class="guide-text">
            <p class="guide-title">
                Devices uses UDP protocol
            </p>
            <p class="guide-subtitle">
                How to connect to SENTIENT UDP-server, transform the incoming messages and generate the downlinks using SENTIENT.
            </p>
            <p class="guide-keywords">
                Connect UDP devices
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/samples/tektelic/">
        <div class="guide-text">
            <p class="guide-title">
                Connect Tektelic LoRaWAN sensors using TEKTELIC KONA Core Network Server
            </p>
            <p class="guide-subtitle">
                Learn how to route messages from TEKTELIC KONA Core Network Server to SENTIENT.
            </p>
            <p class="guide-keywords">
                Tektelic connect
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/tuya/">
        <div class="guide-text">
            <p class="guide-title">
                Connect smart devices through Tuya Smart
            </p>
            <p class="guide-subtitle">
                Learn how to connect smart devices using Tuya Smart to SENTIENT.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/samples/sia-connect/">
        <div class="guide-text">
            <p class="guide-title">
                Connect OPC-UA devices through SIA Connect
            </p>
            <p class="guide-subtitle">
                Learn how to connect OPC-UA devices using the SIA Connect to the SENTIENT.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


    </ul>
</div>


<div class="guides-block" id="AnchorIDDataProcessing">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <h2>
                Data processing & actions
            </h2>
            
            <p class="guides-subtitle">
                Learn how to process data in SENTIENT.
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="/docs/tutorials/validate-incoming-telemetry/">
        <div class="guide-text">
            <p class="guide-title">
                Validate incoming telemetry
            </p>
            <p class="guide-subtitle">
                Learn how to configure Rule Engine to discard invalid telemetry readings based on JavaScript filter function.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/tutorials/telemetry-delta-calculation/">
        <div class="guide-text">
            <p class="guide-title">
                Telemetry delta calculation
            </p>
            <p class="guide-subtitle">
                Learn how to calculate telemetry delta readings using the Calculated fields feature.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/tutorials/function-based-on-telemetry-from-two-devices/">
        <div class="guide-text">
            <p class="guide-title">
                Data function based on telemetry from 2 devices
            </p>
            <p class="guide-subtitle">
                Learn how to generate a new telemetry value based on telemetry readings from multiple devices using the Calculated fields feature.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/transform-telemetry-using-previous-record/">
        <div class="guide-text">
            <p class="guide-title">
                Transform telemetry using previous record
            </p>
            <p class="guide-subtitle">
                Learn how to configure Rule Engine to calculate “delta” of the counter readings based on current and previous reading.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/tutorials/create-clear-alarms/">
        <div class="guide-text">
            <p class="guide-title">
                Create & clear alarms
            </p>
            <p class="guide-subtitle">
                Learn how to configure alarm rules to trigger and clear alarms based on incoming device data.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/create-clear-alarms-with-details/">
        <div class="guide-text">
            <p class="guide-title">
                Working with Alarm details
            </p>
            <p class="guide-subtitle">
                Learn how to configure Alarm Details function in Alarm nodes and how to add an Alarm widget to the dashboard.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/tutorials/send-email/">
        <div class="guide-text">
            <p class="guide-title">
                Send email on alarm
            </p>
            <p class="guide-subtitle">
                Learn how to send an email notification when a new alarm is created.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/send-email-to-customer/">
        <div class="guide-text">
            <p class="guide-title">
                Send email to customer
            </p>
            <p class="guide-subtitle">
                Learn how to configure Rule Engine to send email to the customer of the assigned device.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/integration-with-telegram-bot/">
        <div class="guide-text">
            <p class="guide-title">
                Notifications and Alarms on your smartphone using Telegram Bot
            </p>
            <p class="guide-subtitle">
                Learn how to configure Rule Engine to send notification using Telegram Bot when new alarm is created.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/create-inactivity-alarm/">
        <div class="guide-text">
            <p class="guide-title">
                Create alarm when the device is offline
            </p>
            <p class="guide-subtitle">
                Learn how to create an alarm when the device is offline for a certain period of time using RuleEngine.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/check-relation-tutorial/">
        <div class="guide-text">
            <p class="guide-title">
                Check relation between Entities
            </p>
            <p class="guide-subtitle">
                Learn how the Check Relation node can be used to check the relation between Entities.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/rpc-request-tutorial/">
        <div class="guide-text">
            <p class="guide-title">
                RPC Request to related Device
            </p>
            <p class="guide-subtitle">
                Learn how to send a remote request call to a Related Device using Rule Engine.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/get-weather-using-rest-api-call/">
        <div class="guide-text">
            <p class="guide-title">
                Using REST API to get weather data
            </p>
            <p class="guide-subtitle">
                Learn how to use REST API to get weather data in a specified location.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/add-devices-to-group/">
        <div class="guide-text">
            <p class="guide-title">
                Add & remove devices to group dynamically
            </p>
            <p class="guide-subtitle">
                Learn how to how to dynamically add & remove device from the device group based on incoming data from device.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/integrations/send-data-external-mqtt-brokers/">
        <div class="guide-text">
            <p class="guide-title">
                Send data to external MQTT brokers
            </p>
            <p class="guide-subtitle">
                Connect to external brokers and send MQTT data stream
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-5/tutorials/queues-for-synchronization/">
        <div class="guide-text">
            <p class="guide-title">
                Using queues for synchronization
            </p>
            <p class="guide-subtitle">
                Learn how to use Rule Engine 2.5 queues for message processing synchronization.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-5/tutorials/queues-for-message-reprocessing/">
        <div class="guide-text">
            <p class="guide-title">
                Using queues for message reprocessing
            </p>
            <p class="guide-subtitle">
                Learn how to use Rule Engine 2.5 queues for message reprocessing in case of failure or timeout.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


    </ul>
</div>


<div class="guides-block" id="AnchorIDDataAnalytics">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <h2>
                IoT Data analytics
            </h2>
            
            <p class="guides-subtitle">
                Learn how to use rule engine to perform basic analytics tasks.
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/aggregate-incoming-data-stream/">
        <div class="guide-text">
            <p class="guide-title">
                Aggregate incoming data stream
            </p>
            <p class="guide-subtitle">
                Calculate total water consumption in the building based on readings from multiple water meters within a building.
            </p>
            <p class="guide-keywords">
                aggregation water meter analytics rule engine
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/rule-engine-2-0/tutorials/aggregate-latest-data/">
        <div class="guide-text">
            <p class="guide-title">
                Aggregate latest telemetry values periodically
            </p>
            <p class="guide-subtitle">
                Calculate average temperature in the warehouse based on readings from multiple temperature sensors.
            </p>
            <p class="guide-keywords">
                average temperature analytics rule engine
            </p>
        </div>
        <div class="guide-icons">
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/sentient-analytics/prediction/">
        <div class="guide-text">
            <p class="guide-title">
                Predict timeseries
            </p>
            <p class="guide-subtitle">
                Build prediction model based on vibration of water pump
            </p>
            <p class="guide-keywords">
                analytics forecast prediction
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


    </ul>
</div>


<div class="guides-block" id="AnchorIDAdvancedFeatures">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <h2>
                Advanced features
            </h2>
            
            <p class="guides-subtitle">
                Learn about advanced SENTIENT features
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="/docs/user-guide/device-connectivity-status/">
        <div class="guide-text">
            <p class="guide-title">
                Connectivity status
            </p>
            <p class="guide-subtitle">
                Learn how to track connectivity status of the devices: connected, disconnected, active, inactive
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/audit-log/">
        <div class="guide-text">
            <p class="guide-title">
                Audit log
            </p>
            <p class="guide-subtitle">
                Learn how to track user actions in order to keep audit log.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/api-limits/">
        <div class="guide-text">
            <p class="guide-title">
                API limits
            </p>
            <p class="guide-subtitle">
                Learn how to control API usage, by limiting number of requests from single host during single time unit (Minutes, Hours, etc.)
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/white-labeling/">
        <div class="guide-text">
            <p class="guide-title">
                White-labeling
            </p>
            <p class="guide-subtitle">
                Learn how to configure your company or product logo and color scheme in 2 minutes with zero coding efforts.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/groups/">
        <div class="guide-text">
            <p class="guide-title">
                Device and Asset groups
            </p>
            <p class="guide-subtitle">
                Learn how to work with entity groups and perform bulk operations
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/scheduler/">
        <div class="guide-text">
            <p class="guide-title">
                Scheduler
            </p>
            <p class="guide-subtitle">
                Learn how to schedule various types of events and trigger actions.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/reporting/">
        <div class="guide-text">
            <p class="guide-title">
                Reporting
            </p>
            <p class="guide-subtitle">
                Learn how to schedule and generate reports based on existing dashboards.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            <span class="video"></span>
            
            
            <span class="pe"></span>
            
        </div>
    </a>
</li>


    </ul>
</div>


<div class="guides-block" id="AnchorIDOAuth">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <h2>
                OAuth 2.0
            </h2>
            
            <p class="guides-subtitle">
                Learn how to step-by-step setup OAuth with different providers.
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="/docs/user-guide/oauth-2-support/#login-with-google">
        <div class="guide-text">
            <p class="guide-title">
                Google OAuth example
            </p>
            <p class="guide-subtitle">
                Learn how to step-by-step setup OAuth with Google.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/oauth-2-support/#login-with-auth0">
        <div class="guide-text">
            <p class="guide-title">
                OAuth0 OAuth example
            </p>
            <p class="guide-subtitle">
                Learn how to step-by-step setup OAuth with OAuth0.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/oauth-2-support/#login-with-okta">
        <div class="guide-text">
            <p class="guide-title">
                OAuth0 Okta example
            </p>
            <p class="guide-subtitle">
                Learn how to step-by-step setup OAuth with Okta.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/oauth-2-support/#login-with-keycloak">
        <div class="guide-text">
            <p class="guide-title">
                OAuth0 Keycloak example
            </p>
            <p class="guide-subtitle">
                Learn how to step-by-step setup OAuth with Keycloak.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/oauth-2-support/#login-with-azure">
        <div class="guide-text">
            <p class="guide-title">
                OAuth0 Azure Active Directory example
            </p>
            <p class="guide-subtitle">
                Learn how to step-by-step setup OAuth with Azure Active Directory.
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


    </ul>
</div>


<div class="guides-block" id="AnchorIDContribution">
    <div class="guides-title-panel">
        <div class="guides-text">
            
            <h2>
                Contribution and Development
            </h2>
            
            <p class="guides-subtitle">
                Learn how to contribute to Sentient, customize & develop custom widgets and rule nodes
            </p>
        </div>
    </div>
    <ul class="guides-list">
        


<li class="guide-container">
    <a href="/docs/user-guide/contribution/how-to-contribute/">
        <div class="guide-text">
            <p class="guide-title">
                How to Contribute
            </p>
            <p class="guide-subtitle">
                Learn how to contribute to Sentient
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/contribution/how-to-contribute-your-device-integration-guide/">
        <div class="guide-text">
            <p class="guide-title">
                How to contribute your device integration guide
            </p>
            <p class="guide-subtitle">
                Learn how to contribute to Sentient
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/contribution/rule-node-development/">
        <div class="guide-text">
            <p class="guide-title">
                Rule Node Development Guide
            </p>
            <p class="guide-subtitle">
                Learn how to customize and create custom rule nodes
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


<li class="guide-container">
    <a href="/docs/user-guide/contribution/widgets-development/">
        <div class="guide-text">
            <p class="guide-title">
                Widgets Development Guide
            </p>
            <p class="guide-subtitle">
                Learn how to customize and create custom widgets
            </p>
            <p class="guide-keywords">
                
            </p>
        </div>
        <div class="guide-icons">
            
            
        </div>
    </a>
</li>


    </ul>
</div>


</div>
