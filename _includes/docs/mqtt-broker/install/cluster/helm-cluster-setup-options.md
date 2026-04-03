{% if (docsPrefix == "pe/") %}

<div class="installation-options">
    <div class="install-options-header">
       <div class="install-options-hero">
          <div class="container">
            <div class="install-options-hero-content">
                <h1>Kubernetes environment options for ST-RMQTT PE cluster setup using Helm</h1>
                <div class="install-options-description">
                    <p>The core ST-RMQTT PE installation process using Helm is consistent across Kubernetes environments. However, the full installation guide—including steps for configuring the Kubernetes cluster—varies depending on the platform. To proceed, please select your Kubernetes environment below. You’ll then be guided through the complete ST-RMQTT PE installation tailored to your chosen platform, including environment-specific Kubernetes setup and other relevant configurations.</p>
                </div>
            </div>
            <div class="deployment-container one-line-deployment-container">
                <div class="deployment-div">
                    {% include installation-options-cards.liquid installationOptions="installation-options-pe-mqtt-broker-helm" active=true %}
                </div>
            </div>
          </div>
       </div>
    </div>
</div>

{% else %}

<div class="installation-options">
    <div class="install-options-header">
       <div class="install-options-hero">
          <div class="container">
            <div class="install-options-hero-content">
                <h1>Kubernetes environment options for ST-RMQTT cluster setup using Helm</h1>
                <div class="install-options-description">
                    <p>The core ST-RMQTT installation process using Helm is consistent across Kubernetes environments. However, the full installation guide—including steps for configuring the Kubernetes cluster—varies depending on the platform. To proceed, please select your Kubernetes environment below. You’ll then be guided through the complete ST-RMQTT installation tailored to your chosen platform, including environment-specific Kubernetes setup and other relevant configurations.</p>
                </div>
            </div>
            <div class="deployment-container one-line-deployment-container">
                <div class="deployment-div">
                    {% include installation-options-cards.liquid installationOptions="installation-options-mqtt-broker-helm" active=true %}
                </div>
            </div>
          </div>
       </div>
    </div>
</div>

{% endif %}
