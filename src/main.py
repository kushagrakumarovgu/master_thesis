from openai_inference import generate_inference
from examples import sample_review


if __name__ == "__main__":

    output = generate_inference(sample_review)
    print(output)
