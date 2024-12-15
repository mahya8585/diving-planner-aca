# diving-planner-aca


SET RESOURCE_GROUP="album-containerapps"
SET LOCATION="canadacentral"
SET ENVIRONMENT="env-album-containerapps"
SET API_NAME="album-api"
SET GITHUB_USERNAME="mahya8585"
SET ACR_NAME="acaalbums"$GITHUB_USERNAME

https://github.com/mahya8585/containerapps-albumapi-python.git

az containerapp up --name %API_NAME% --resource-group %RESOURCE_GROUP% --location %LOCATION% --environment %ENVIRONMENT% --context-path ./src --repo https://github.com/mahya8585/containerapps-albumap-python

