from urllib.parse import urlparse
import re


def extract_basic_features(url):
    """
    Extract basic URL-based features.
    More features will be added in the next steps.
    """

    parsed = urlparse(url)

    hostname = parsed.netloc

    features = {
        "length_url": len(url),
        "length_hostname": len(hostname),
        "nb_dots": url.count("."),
        "nb_hyphens": url.count("-"),
        "nb_slash": url.count("/"),
        "nb_qm": url.count("?"),
        "ip": 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", hostname) else 0
    }

    return features