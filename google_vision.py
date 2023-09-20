"Google Vision api Class"
import base64
import requests


class GoogleVision:
    """
    requests google vision api more easy in python
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.request_endpoint = "https://vision.googleapis.com/v1/images:annotate"
        self.request_url = self.request_endpoint + "?" + "key=" + self.api_key

    def __get_features(
        self, feature_type: str, max_results: int = 10, model: str = None
    ):
        features = {
            "type": feature_type.upper(),
            "maxResults": max_results,
            "model": model.upper(),
        }
        return [features]

    def __get_image_object(self, img_source: str or bytes):
        if isinstance(img_source, bytes):
            return {"content": base64.b64encode(img_source).decode("utf-8")}
        return {"source": {"imageUri": img_source}}

    def request_api(
        self,
        img_source: str or bytes,
        feature_type: str = "WEB_DETECTION",
        max_result: int = 10,
        time_out: int = 10,
    ):
        """
        Args:
            img_source (str or bytes, require): using image uri or image bytes.
            feature_type (str, optional): type of feature, Defaults to "WEB_DETECTION".
            max_result (int, optional): count of results, Defaults to 10.
            time_out (int, optional): second of request, Defaults to 10.

        Returns:
            response : result of api reqeusts
        """
        data = {
            "requests": [
                {
                    "image": self.__get_image_object(img_source=img_source),
                    "features": self.__get_features(
                        feature_type=feature_type, max_results=max_result, model=None
                    ),
                },
            ]
        }
        return requests.post(timeout=time_out, url=self.request_url, json=data)
