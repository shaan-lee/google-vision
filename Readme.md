# This repo will do
- this Class will make easy to use google vision api

# Using example
```
vision = GoogleVision(api_key = [your_key])

response = vision.request_api(image_source = [your_image_url], feature_type = "WEB_DETECTION")

data = response.content
```