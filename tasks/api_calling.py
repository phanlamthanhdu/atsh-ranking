import requests

def fetch_data_from_api(url: str, params: dict = None, headers: dict = None) -> dict:
    """
    Fetch data from a given API endpoint.

    Args:
        url (str): The API endpoint URL.
        params (dict, optional): Query parameters to include in the request.
        headers (dict, optional): Headers to include in the request.

    Returns:
        dict: The JSON response from the API if the request is successful.
        None: If the request fails.
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from {url}:\n{e}")
        return None