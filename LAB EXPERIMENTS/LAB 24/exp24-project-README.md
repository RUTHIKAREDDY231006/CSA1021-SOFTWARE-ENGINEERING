# flask-cicd

Flask app with a GitHub Actions pipeline: test → build-and-push → deploy. Add these **repository secrets**: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `HEROKU_API_KEY`, `HEROKU_APP_NAME` (the manual notes Heroku needs a verified account; AWS App Runner or Render are alternatives). Never commit secrets.
