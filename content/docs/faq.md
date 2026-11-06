+++
title = "Frequently Asked Questions"
description = "SENTIENT FAQ"

[extra]
status = "imported"
checked = ""
source = "docs/faq.md"
+++
<style>
.tb-faq-wrapper { padding: 20px 15px 80px; max-width: 1200px; margin: 0 auto; }
.tb-faq-wrapper h1 { text-align: center; font-size: 36px; font-weight: 500; line-height: 48px; margin-bottom: 48px; color: #212529; }
.tb-faq-sections { display: flex; gap: 40px; }
@media (max-width: 1200px) { .tb-faq-sections { flex-direction: column; } }
.tb-faq-tabs { display: flex; flex-direction: column; align-items: flex-start; padding: 8px; width: fit-content; margin-bottom: 24px; }
@media (max-width: 690px) { .tb-faq-tabs { width: 100%; } }
.tb-faq-tab { width: 100%; font-size: 24px; font-weight: 500; line-height: 36px; padding: 24px 32px; border: 1.5px solid transparent; border-radius: 24px; cursor: pointer; color: #757575; }
.tb-faq-tab:hover { color: #757575; }
.tb-faq-tab.active { color: #000000DE; border-bottom: 1.5px solid #E6F0FC; background: #e8f4f4; }
.tb-faq-answers { flex: 1.5; }
.tb-faq-category { display: none; }
.tb-faq-category.active { display: block; }
.tb-faq-question { border-bottom: 1.5px solid rgba(62,154,248,0.12); margin-bottom: 7px; }
.tb-faq-question-title { 
    font-size: 18px; 
    font-weight: 500; 
    line-height: 30px; 
    color: #212121; 
    padding: 22px 37px 22px 7px; 
    cursor: pointer; 
    position: relative; 
    margin: 0;
    display: block;
}
.tb-faq-question-title:hover { color: rgba(33, 33, 33, 0.78); }
.tb-faq-question-title:after { 
    font-family: "Font Awesome 5 Free"; 
    font-weight: 900; 
    color: rgba(0,0,0,0.38); 
    content: "\f078"; 
    position: absolute; 
    right: 8px; 
    top: 22px; 
    transition: transform 0.3s; 
}
.tb-faq-question.open .tb-faq-question-title:after { transform: rotate(180deg); }
.tb-faq-answer { 
    display: none; 
    padding: 5px 50px 25px 10px; 
    margin: 0 10px 10px; 
    font-size: 14px; 
    line-height: 24px; 
}
.tb-faq-question.open .tb-faq-answer { display: block; }
.tb-faq-answer p, .tb-faq-answer li { font-size: 14px; color: #3D3D3D; line-height: 24px; }
.tb-faq-answer a { color: #187074; text-decoration: none; }
.tb-faq-answer a:hover { text-decoration: underline; }
.tb-faq-answer ul { margin: 20px 0; padding-left: 30px; list-style: disc; }
.tb-faq-answer li { margin-bottom: .75em; }
.tb-faq-hidden { display: none; }
.tb-faq-load-more { 
    border-bottom: 1.5px solid rgba(62,154,248,0.12);
    overflow: visible;
    margin-bottom: 7px;
    position: relative;
}
.tb-faq-load-more .title { 
    font-size: 18px;
    font-weight: 500;
    line-height: 30px;
    color: #187074;
    padding: 22px 37px 22px 7px;
    margin: 0;
    cursor: pointer;
    transition: none;
}
.tb-faq-load-more .title:hover { 
    color: #1e5fb8;
}
.tb-faq-load-more .title:after {
    color: #187074;
    content: "+";
    position: absolute;
    right: 8px;
    top: 22px;
    font-size: 20px;
    font-weight: 300;
    line-height: 1;
}
</style>

<script>
function toggleTbFaq(element) {
    var question = element.closest('.tb-faq-question');
    question.classList.toggle('open');
}

function switchTbFaqTab(tabId) {
    // Remove active from all tabs
    var tabs = document.querySelectorAll('.tb-faq-tab');
    tabs.forEach(function(tab) {
        tab.classList.remove('active');
    });
    
    // Remove active from all categories
    var categories = document.querySelectorAll('.tb-faq-category');
    categories.forEach(function(cat) {
        cat.classList.remove('active');
    });
    
    // Add active to clicked tab
    event.target.classList.add('active');
    
    // Add active to corresponding category
    var category = document.getElementById('tb-faq-cat-' + tabId);
    if (category) category.classList.add('active');
    
    // Reset load more button for the new category
    resetLoadMore(tabId);
}

function loadMoreTbFaq(loadMoreDiv) {
    var category = loadMoreDiv.closest('.tb-faq-category');
    var hiddenQuestions = category.querySelectorAll('.tb-faq-question.tb-faq-hidden');
    
    // Show all hidden questions
    hiddenQuestions.forEach(function(question) {
        question.classList.remove('tb-faq-hidden');
    });
    
    // Hide the load more div
    loadMoreDiv.style.display = 'none';
}

function resetLoadMore(categoryId) {
    var category = document.getElementById('tb-faq-cat-' + categoryId);
    var loadMoreDiv = category.querySelector('.tb-faq-load-more');
    
    if (loadMoreDiv) {
        var hiddenQuestions = category.querySelectorAll('.tb-faq-question.tb-faq-hidden');
        if (hiddenQuestions.length > 0) {
            loadMoreDiv.style.display = 'block';
        }
    }
}
</script>

<h2>Open Source IoT Platform</h2>

<div class="tb-faq-wrapper">
    <div class="tb-faq-sections">
        <div class="tb-faq-tabs">
            <div class="tb-faq-tab active" onclick="switchTbFaqTab('general')">General</div>
            
            <div class="tb-faq-tab" onclick="switchTbFaqTab('ai')">AI Capabilities</div>
            <div class="tb-faq-tab" onclick="switchTbFaqTab('deployment')">Deployments & Limits</div>
            <div class="tb-faq-tab" onclick="switchTbFaqTab('security')">Security & Compliance</div>
            <div class="tb-faq-tab" onclick="switchTbFaqTab('support')">Support & Assistance</div>
        </div>
        <div class="tb-faq-answers">
            <div id="tb-faq-cat-general" class="tb-faq-category active">
                <div class="tb-faq-question">
                    
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">What is SENTIENT?</div>
                    
                    <div class="tb-faq-answer">
                        <p>SENTIENT is an IoT platform for <b>data collection, processing, visualization, and device management</b>. It enables you to accelerate development and lower costs by providing out-of-the-box components and APIs while maintaining full control over your solution and data.</p>
                        
                        <p>SENTIENT (CE) is a <b>free, open-source IoT platform</b> for collecting, storing, and analyzing data from IoT devices. It is designed for developers and organizations that want full control over their own IoT infrastructure and source code without any licensing fees.</p>
                        <p>Learn more about the platform's architecture in our <a href="/docs/getting-started-guides/what-is-sentient/" target="_blank">What is SENTIENT?</a> guide, or jump straight to the <a href="/docs/getting-started-guides/helloworld/" target="_blank">Getting Started Guide</a> to build your first project.</p>
                       
                    </div>
                </div>
                <div class="tb-faq-question">
                    
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Is SENTIENT free?</div>
                    
                    <div class="tb-faq-answer">
                        
                        <p>Yes, it <b>is completely free</b>, with no licensing fees or hidden costs.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">What's the difference between Community and Professional Edition?</div>
                    <div class="tb-faq-answer">
                        <p><b>Community Edition (CE)</b> is a free, open-source platform suitable for development, testing, and production use without licensing costs. It includes essential features for IoT device management, data collection, visualization, and rule processing.</p>
                        <p><b>Professional Edition (PE)</b> includes all CE features and offers advanced capabilities such as <a href="/docs/pe/user-guide/white-labeling/" target="_blank">white-labeling</a>, <a href="/docs/pe/user-guide/rbac/" target="_blank">role-based access control (RBAC)</a>, <a href="/docs/user-guide/integrations/" target="_blank">platform integrations</a>, <a href="/docs/pe/solution-templates/overview/" target="_blank">solution templates</a>, <a href="/docs/pe/user-guide/scheduler/" target="_blank">scheduler</a>, and enterprise support.</p>
                        <p>See the <a href="/products/sentient-pe/" target="_blank">PE product page</a> for a detailed <b>feature comparison table</b>.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">How do I get started with SENTIENT?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Install SENTIENT locally by following our <a href="/docs/user-guide/install/installation-options/" target="_blank">installation guide</a>.</p>
                        
                        <p>To connect your first device and build dashboards, explore the <a href="/docs/getting-started-guides/helloworld/" target="_blank">Getting Started Guide</a>.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Are there API rate limits?</div>
                    <div class="tb-faq-answer">
                        
                        <p>SENTIENT does not have built-in API rate limits; however, system performance and request handling are subject to the limitations of the infrastructure on which it is hosted.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Are there device limits?</div>
                    <div class="tb-faq-answer">
                        
                        <p>No, the Community Edition does not impose programmatic device limits. The number of devices you can connect is only limited by your server's hardware resources.</p>
                        
                        
                        <p>The SENTIENT platform is designed to be <b>horizontally scalable</b>. By utilizing a <a href="https://en.wikipedia.org/wiki/Consistent_hashing" target="_blank">consistent-hashing</a> load balancing algorithm between cluster nodes, the system ensures high availability and performance. Actual capacity depends on your specific usage scenarios and data throughput requirements.</p>
                        <p>For instance, even a cluster of commodity hardware can support <a href="/docs/reference/iot-platform-deployment-scenarios/#1-million-smart-meters-tco" target="_blank">several million</a> devices connected via MQTT.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">How to connect my device?</div>
                    <div class="tb-faq-answer">
                        <p>SENTIENT provides <a href="/docs/reference/mqtt-api" target="_blank">MQTT</a>, <a href="/docs/reference/coap-api" target="_blank">CoAP</a>, <a href="/docs/reference/http-api" target="_blank">HTTP</a>, and <a href="/docs/reference/lwm2m-api" target="_blank">LwM2M</a> protocols support. <b>Existing</b> devices may be connected to the platform using <b><a href="/docs/iot-gateway/what-is-iot-gateway/" target="_blank">SENTIENT IoT Gateway</a></b>. You can find more information on the <a href="/docs/reference/protocols/" target="_blank">connectivity</a> page.</p>
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Do I need to use an SDK?</div>
                    <div class="tb-faq-answer">
                        <p>No, many IoT devices cannot afford the overhead of embedding a third-party SDK. SENTIENT provides a simple API over common IoT protocols, allowing you to choose any client-side library you prefer or use your own. Some useful references include:</p>
                        <ul>
                            <li><a href="https://github.com/mqtt/mqtt.github.io/wiki/libraries" target="_blank">List of MQTT client-side libraries</a></li>
                            <li><a href="https://libcoap.net/" target="_blank">C-implementation for CoAP</a></li>
                        </ul>
                    </div>
                </div>
                
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Where can I host SENTIENT?</div>
                    <div class="tb-faq-answer">
                        <p>You can host SENTIENT in the cloud, on-premises, or locally on your laptop, PC, or even a Raspberry Pi. We recommend getting started with a Docker installation:</p>
                        <ul>
                            <li><a href="/docs/user-guide/install/docker/" target="_blank">Linux & macOS</a></li>
                            <li><a href="/docs/user-guide/install/docker-windows/" target="_blank">Windows</a></li>
                        </ul>
                        <p>You can also take a look at the <a href="/docs/user-guide/install/cluster-setup/" target="_blank">cluster setup</a> guide.</p>
                    </div>
                </div>
                
                
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I use Community Edition for commercial projects?</div>
                    <div class="tb-faq-answer">
                        <p>Yes. CE is licensed under <a href="https://github.com/sentient/sentient/blob/master/LICENSE" target="_blank">Apache 2.0</a>, allowing commercial use without restrictions. You can build, sell, and deploy commercial products on CE.</p>
                    </div>
                </div>
                
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I migrate from CE to PE?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, you can migrate from SENTIENT to Professional Edition <b>without losing telemetry data and/or configurations</b>. The upgrade process preserves your existing setup, ensuring a seamless transition.</p>
                        <p>However, please note that <b>any custom modifications</b> made directly to the source code of the Community Edition <b>will be removed</b> during the upgrade process.</p>
                        <p>See the <a href="/docs/pe/user-guide/install/upgrade-instructions/upgrade-from-ce/" target="_blank">SENTIENT instructions for upgrading from Community Edition</a>. Back up your data before starting.</p>
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">How can I check which version of SENTIENT I’m currently using?</div>
                    <div class="tb-faq-answer">
                        
                        <p>The easiest way is to log in as SysAdmin. On the home page, you will find a widget in the bottom-left corner of the screen showing the current platform version and whether an upgrade is available.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I integrate with third-party systems?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes, you can integrate SENTIENT with third-party systems through REST APIs or Rule Engine.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support white-labeling?</div>
                    <div class="tb-faq-answer">
                        
                        <p>No, white-labeling is available only in the Professional Edition.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I replace the default SENTIENT logo in the menu?</div>
                    <div class="tb-faq-answer">
                        
                        <p>The Community Edition does not include a built-in white-labeling feature. However, it is technically possible to replace the default SENTIENT logo by modifying the source code and rebuilding the platform. This requires development expertise and familiarity with SENTIENT’s codebase. Please note that such changes will need to be reapplied after each upgrade of the platform.</p>
                        <p>If you need a more streamlined and configurable option, we recommend considering the Professional Edition. With Professional Edition, you can effortlessly upload your own logo and favicon, customize login and system pages, adjust colors and branding palettes, and even tailor <a href="/docs/pe/user-guide/mail-templates/" target="_blank">email templates</a>, <a href="/docs/pe/user-guide/custom-translation/" target="_blank">translations</a>, and <a href="/docs/pe/user-guide/custom-menu/" target="_blank">custom menus</a> - all directly from the user interface, without touching the code. This empowers your organization to deliver a fully branded, professional-grade experience to your customers and tenants in just a few clicks.</p>
                        <p>More details: <a href="/docs/pe/user-guide/white-labeling/#customize-sentient-web-interface" target="_blank">PE White-Labeling Guide</a>.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I try Professional Edition before purchasing?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, use the <b>Free plan</b>. This includes access to all PE features for evaluation, including add-ons - Edge computing and SENTIENT ANALYTICS.</p>
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Where can I find the source code?</div>
                    <div class="tb-faq-answer">
                        
                        <p>The source code is available on <a href="https://github.com/sentient/sentient" target="_blank">GitHub</a>. You can fork, modify, and contribute to the project under the <a href="https://github.com/sentient/sentient/blob/master/LICENSE" target="_blank">Apache 2.0 license</a>. It is free for both personal and commercial usage, and you can deploy it anywhere.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I contribute to SENTIENT?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes! Pull requests and contributions are welcome on <a href="https://github.com/sentient/sentient/" target="_blank">GitHub</a>.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-load-more" onclick="loadMoreTbFaq(this)">
                    <div class="title">Load more FAQ</div>
                </div>
            </div>
            
            <div id="tb-faq-cat-ai" class="tb-faq-category">
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support AI integration?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, SENTIENT includes an <a href="/docs/user-guide/rule-engine-2-0/nodes/external/ai-request/" target="_blank">AI Request node</a> in the Rule Engine that allows integration with AI services like OpenAI, Azure OpenAI, and custom AI endpoints.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I use AI for predictive maintenance?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, SENTIENT includes built-in AI integration capabilities. You can use the <a href="/docs/user-guide/rule-engine-2-0/nodes/external/ai-request/" target="_blank">AI Request node</a> to send telemetry data to machine learning models for predictive analytics, anomaly detection, and maintenance scheduling.</p>
                        <p>See the predictive maintenance example for implementation details.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Which AI providers are supported?</div>
                    <div class="tb-faq-answer">
                        <p>SENTIENT supports a variety of AI providers, including, but not limited to, OpenAI, Azure OpenAI, and custom API endpoints. Check the <a href="/docs/samples/analytics/ai-models/" target="_blank">AI models</a> page for more details.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I train custom ML models with SENTIENT data?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, export historical telemetry via <a href="/docs/api/" target="_blank">REST API</a> or <a href="/docs/pe/user-guide/csv-xls-data-export/" target="_blank">data export features (PE)</a> to train models externally. Deploy trained models as API endpoints and integrate them using the <a href="/docs/user-guide/rule-engine-2-0/nodes/external/ai-request/" target="_blank">AI Request node</a>.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Are there examples of AI use cases?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, see documentation for examples including <a href="/docs/samples/analytics/ai-predictive-maintenance/" target="_blank">anomaly detection</a>, and <a href="/docs/samples/analytics/ai-models/" target="_blank">natural language processing</a>.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Do I need a separate AI subscription?</div>
                    <div class="tb-faq-answer">
                        <p>SENTIENT integration is included, but you need subscriptions to external AI services (OpenAI, Azure, etc.) if using those providers. Custom AI endpoints are entirely under your control.</p>
                    </div>
                </div>
            </div>
            <div id="tb-faq-cat-deployment" class="tb-faq-category">
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Where can I install SENTIENT?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Community Edition can be installed on:</p>
                        <ul>
                        <li><b>On-premise</b> servers or virtual machines. Docker and Kubernetes deployments are supported.</li>
                        <li><b>Cloud platforms:</b> AWS, Microsoft Azure, DigitalOcean, Google Cloud Platform.</li>
                        </ul>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support clustering?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, clustering is supported in all deployment options.</p>
                        
                        <p>See <a href="/docs/user-guide/install/cluster-setup/" target="_blank">cluster setup guide</a> for configuration details.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">What are the hardware requirements?</div>
                    <div class="tb-faq-answer">
                        <p><b>Minimum:</b> 2 CPU cores, 4GB RAM for testing.</p>
                        <p><b>Recommended for production:</b> 8+ CPU cores, 16GB+ RAM. Requirements scale with device count and message volume.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">How many devices can SENTIENT handle?</div>
                    <div class="tb-faq-answer">
                    
                        <p>There are <b>no programmatic software limits</b> on the number of devices in the Community Edition. The capacity of your system depends entirely on your hardware resources, database configuration, and deployment architecture (standalone vs. cluster).</p>
                        <p>A single modern server can typically handle tens of thousands of devices, while <b>clustered deployments</b> can scale to support millions of concurrent connections.</p>
                    
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Where does SENTIENT store data?</div>
                    <div class="tb-faq-answer">
                        <p>SENTIENT supports two database approaches:</p>
                        <ul>
                        <li><b>Pure SQL</b>: PostgreSQL database which is default and recommended for development and production environments with a reasonable load (< 5000 msg/sec).</li>
                        <li><b>Hybrid database</b>: PostgreSQL + Cassandra for 1M+ devices in production or high data ingestion rate (> 5000 msg/sec). </li>
                        </ul>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support multi-tenancy?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes, the SENTIENT supports multi-tenancy out of the box.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support OTA (Over-the-Air) firmware updates?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, SENTIENT supports OTA (Over-the-Air) firmware updates.</p>
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Do you charge for API requests?</div>
                    <div class="tb-faq-answer">
                        
                        <p>No. Community Edition has no charges or limits on API requests. However, performance depends on your server capacity and infrastructure.</p>
                        
                    </div>
                </div>
                
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Is there a mobile app for SENTIENT?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes. SENTIENT <a href="/products/mobile/" target="_blank">Mobile Application</a> is free and open-source (Apache 2.0 license). It's available for iOS and Android and works with SENTIENT Server.</p>
                        
                    </div>
                </div>
                
                <div class="tb-faq-load-more" onclick="loadMoreTbFaq(this)">
                    <div class="title">Load more FAQ</div>
                </div>
            </div>
            <div id="tb-faq-cat-security" class="tb-faq-category">
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Is my SENTIENT instance secure?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes, but security depends on your deployment setup and infrastructure.</p>
                        
                        <p>SENTIENT provides device authentication, encrypted communication (SSL/TLS), role-based access control, and audit logging.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support encryption?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes, the Community Edition includes transport encryption (TLS/SSL).</p>
                        <p>For data-at-rest encryption, configure database-level encryption. See <a href="/docs/user-guide/ui/security-settings/" target="_blank">security documentation</a> for setup instructions.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support SSO/OAuth?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes, the Community Edition includes SSO (Single Sign-On) and OAuth functionality.</p>
                        <p>See <a href="/docs/user-guide/ui/security-settings/" target="_blank">security documentation</a> for setup instructions.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I store SENTIENT data in my preferred region?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Yes, you have full control over where your data is stored.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">How are devices authenticated?</div>
                    <div class="tb-faq-answer">
                        <p>SENTIENT supports multiple authentication methods: access tokens, X.509 certificates, and username/password. Each device receives unique credentials. See <a href="/docs/user-guide/device-credentials/" target="_blank">device authentication options</a> available.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Does SENTIENT support role-based access control (RBAC)?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Community Edition supports a <b>straight-forward security model</b> with three main roles: System administrator, Tenant administrator, and Customer user. A system administrator is able to manage tenants, while a tenant administrator manages devices, dashboards, customers, and other entities that belong to a particular tenant. Customer user is able to view dashboards and control devices that are assigned to a specific customer.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Is SENTIENT compliant with regulations (GDPR, etc.)?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Compliance depends on your hosting environment and data security practices.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I integrate with external authentication providers?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, SENTIENT supports OAuth2, LDAP, and SAML integration.</p>
                    </div>
                </div>
                <div class="tb-faq-question tb-faq-hidden">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Are there audit logs?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, SENTIENT logs user actions.</p>
                    </div>
                </div>
                <div class="tb-faq-load-more" onclick="loadMoreTbFaq(this)">
                    <div class="title">Load more FAQ</div>
                </div>
            </div>
            <div id="tb-faq-cat-support" class="tb-faq-category">
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">What support is available for SENTIENT?</div>
                    <div class="tb-faq-answer">
                        
                        <p>The SENTIENT team does not provide dedicated support for Community Edition users. Support is community-driven through <a href="https://github.com/sentient/sentient" target="_blank">GitHub</a> (report issues, contribute), <a href="https://stackoverflow.com/questions/tagged/sentient" target="_blank">Stack Overflow</a> (developer questions), <a href="/docs/" target="_blank">Documentation</a> (guides and tutorials), <a href="https://www.youtube.com/sentient" target="_blank">Youtube channel</a> (tutorials).</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Do you offer professional services?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, SENTIENT offers consulting, <a href="/services/development-services/" target="_blank">custom development</a>, <a href="/services/trainings/" target="_blank">learning resources</a>, and deployment assistance. <a href="/docs/contact-us/" target="_blank">Contact us</a> to discuss your requirements.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">How do I report a bug?</div>
                    <div class="tb-faq-answer">
                        
                        <p>Report bugs on <a href="https://github.com/sentient/sentient/issues" target="_blank">GitHub Issues</a>. Include detailed reproduction steps, logs, and system information. Community members and maintainers will investigate.</p>
                        
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Are there training resources?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, comprehensive documentation, video tutorials, and sample projects are available. Professional services include custom training programs. See <a href="/services/trainings/" target="_blank">learning resources</a> for more.</p>
                    </div>
                </div>
                <div class="tb-faq-question">
                    <div class="tb-faq-question-title" onclick="toggleTbFaq(this)">Can I get help with deployment?</div>
                    <div class="tb-faq-answer">
                        <p>Yes, professional services include deployment assistance, architecture review, and production setup. <a href="/docs/contact-us/" target="_blank">Contact us</a> to discuss your deployment needs.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
