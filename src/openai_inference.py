from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from helpers import gpt_model
from prompts import human_template
from data_classes import ModelOutput

model = ChatOpenAI(
    model=gpt_model,
    temperature=0.1, # Not given the paper
    max_tokens=1000, # Not given in the paper 
    model_kwargs={
        "top_p": 1, # Not given in the paper
        "frequency_penalty": 0.0, # Not given in the paper
        "presence_penalty": 0.0, # Not given in the paper
    },
)

def generate_inference(review: str):

    pydantic_parser = PydanticOutputParser(pydantic_object=ModelOutput)

    format_instructions = pydantic_parser.get_format_instructions()

    prompt = PromptTemplate(
        template=human_template,
        input_variables=["review"],
        partial_variables={"format_instructions": format_instructions},
    )

    chain = prompt | model | pydantic_parser
    #print(f"{chain=}")

    model_output = chain.invoke({"review": review})
    #print(f"{model_output=}")

    return model_output
