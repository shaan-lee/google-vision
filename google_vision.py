"Google Vision api Class"
import requests


class GoogleVision:
    """
    requests google vision api more easy in python
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.request_endpoint = "https://vision.googleapis.com/v1/images:annotate"
        self.request_url = self.request_endpoint + "?" + "key=" + self.api_key

    def get_features(self, feature_type: str, max_results: int = 10, model: str = None):
        """
        Args:
            feature_type (str): type of feature [TYPE_UNSPECIFIED,FACE_DETECTION,LANDMARK_DETECTION,LOGO_DETECTION,LABEL_DETECTION,TEXT_DETECTION,DOCUMENT_TEXT_DETECTION,SAFE_SEARCH_DETECTION,IMAGE_PROPERTIES,CROP_HINTS,WEB_DETECTION,PRODUCT_SEARCH,OBJECT_LOCALIZATION]
            max_results (int, optional): result max count, Defaults to 10.
            model (str, optional): using model name, Defaults to None.

        Returns:
            list : contains features dictionary
        """
        features = {"type": feature_type, "maxResults": max_results, "model": model}
        return [features]

    def get_image_object(self, img_source: str = "", content: bytes = b""):
        """
        Args:
            img_source (str, optional): using image uri, Defaults to "".
            content (bytes, optional): using image bytes, Defaults to b"".

        Returns:
            dictionary : contains decoded content, image uri
        """
        image = {
            "content": content.decode("base64"),
            "source": {"imageUri": img_source},
        }
        return image

    def request_api(
        self,
        img_source: str = "",
        content: bytes = b"",
        feature_type: str = "WEB_DETECTION",
    ):
        """
        Args:
            img_source (str, optional): using image uri, Defaults to "".
            content (bytes, optional): using image bytes, Defaults to b"".
            feature_tyep (str, optional): type of feature, Defaults to "WEB_DETECTION".

        Returns:
            response : result of api reqeusts
        """
        data = {
            "requests": [
                {
                    "image": self.get_image_object(
                        img_source=img_source, content=content
                    ),
                    "features": self.get_features(
                        feature_type=feature_type, max_results=0, model=None
                    ),
                },
            ]
        }
        return requests.post(timeout=10, url=self.request_url, json=data)
