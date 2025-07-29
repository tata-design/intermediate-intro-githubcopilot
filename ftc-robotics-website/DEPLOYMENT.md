# Deployment Guide for BotBuilders Hub

## Option 1: Streamlit Community Cloud (FREE & EASY)

Streamlit Community Cloud is perfect for your FTC Robotics website and it's completely free!

### Steps:

1. **Push your code to GitHub** (if not already done)
   - Make sure your repository is public or you have a GitHub Pro account
   - Your `app.py` file should be in the root of your repository

2. **Go to Streamlit Community Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

3. **Deploy your app**
   - Click "New app"
   - Select your repository: `intermediate-intro-githubcopilot`
   - Set the main file path: `ftc-robotics-website/app.py`
   - Click "Deploy!"

4. **Your app will be live at**: `https://[your-app-name].streamlit.app`

### Advantages:
- ✅ Completely free
- ✅ Easy setup (5 minutes)
- ✅ Automatic HTTPS
- ✅ Custom domain support
- ✅ Automatic redeployment on git push

## Option 2: Azure App Service

### Prerequisites:
- Active Azure subscription
- Azure CLI installed and logged in

### Steps:

1. **Run the deployment script**:
   ```bash
   cd ftc-robotics-website
   ./deploy-to-azure.sh
   ```

2. **Set up git deployment**:
   ```bash
   # Get the deployment URL from Azure
   az webapp deployment list-publishing-credentials --name botbuilders-hub --resource-group botbuilders-hub-rg
   
   # Add Azure as a remote
   git remote add azure <deployment-url>
   
   # Deploy
   git push azure main
   ```

3. **Your app will be live at**: `https://botbuilders-hub.azurewebsites.net`

### Azure Pricing:
- Free tier: F1 (limited resources, good for testing)
- Basic tier: B1 ($13/month, better performance)

## Option 3: Other Cloud Platforms

### Heroku
- Free tier discontinued, but affordable paid options
- Easy deployment with git

### Railway
- Free tier available
- Simple deployment process

### Render
- Free tier with limitations
- Good for static sites and simple apps

## Recommendation

For your FTC Robotics educational website, I recommend starting with **Streamlit Community Cloud** because:

1. It's completely free
2. Perfect for Streamlit applications
3. Easy to set up and maintain
4. Professional-looking URLs
5. Great for educational projects

You can always migrate to Azure later if you need more advanced features or higher performance.
