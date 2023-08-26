import os
import replicate

def describe_image(file_path, token):
    replicate_client = replicate.Client(api_token=token)
    output = replicate_client.run(
        "daanelson/minigpt-4:b96a2f33cc8e4b0aa23eacfce731b9c41a7d9466d9ed4e167375587b54db9423",
        input={"image": open(os.path.dirname(__file__) +  "\\" + file_path, "rb"),
            "prompt": "what is this image, explain to me in detail?"}
    )
    return output