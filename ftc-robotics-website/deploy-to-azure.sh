#!/bin/bash

# Azure deployment script for BotBuilders Hub
# Make sure you're logged in to Azure CLI first: az login

echo "Starting deployment to Azure..."

# Variables
RESOURCE_GROUP="botbuilders-hub-rg"
APP_SERVICE_PLAN="botbuilders-hub-plan"
WEB_APP_NAME="botbuilders-hub"
LOCATION="eastus"

# Create resource group
echo "Creating resource group..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create App Service plan (Free tier)
echo "Creating App Service plan..."
az appservice plan create --name $APP_SERVICE_PLAN --resource-group $RESOURCE_GROUP --sku F1 --is-linux

# Create web app
echo "Creating web app..."
az webapp create --resource-group $RESOURCE_GROUP --plan $APP_SERVICE_PLAN --name $WEB_APP_NAME --runtime "PYTHON|3.11"

# Configure startup command
echo "Configuring startup command..."
az webapp config set --resource-group $RESOURCE_GROUP --name $WEB_APP_NAME --startup-file "startup.sh"

# Deploy from local git
echo "Setting up deployment..."
az webapp deployment source config-local-git --name $WEB_APP_NAME --resource-group $RESOURCE_GROUP

echo "Deployment setup complete!"
echo "Your app will be available at: https://$WEB_APP_NAME.azurewebsites.net"
echo ""
echo "To deploy your code:"
echo "1. Add the Azure remote: git remote add azure <deployment-url>"
echo "2. Push your code: git push azure main"
